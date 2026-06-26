document.addEventListener('DOMContentLoaded', () => {
  // --- Brain & Robot Audio Logic ---
  // The user clicked from the navbar, so browsers typically allow this cross-page autoplay.
  // Play exactly 1 second after load (which equates to ~1 sec after click depending on load time)
  const brainAudio = new Audio('assets/videos/brain-voice.mp3');
  const robotAudio = new Audio('assets/videos/robot-voice.mp3');

  setTimeout(() => {
    // Play both audio files
    const p1 = brainAudio.play();
    const p2 = robotAudio.play();
    
    Promise.all([p1, p2]).catch(err => {
      console.log("Audio play blocked on portfolio:", err);
      
      // Fallback: unlock on next interaction if blocked
      const unlockAudio = () => {
        brainAudio.play().catch(e => {});
        robotAudio.play().catch(e => {});
        ['mousemove', 'click', 'scroll', 'touchstart', 'keydown'].forEach(evt => {
          window.removeEventListener(evt, unlockAudio);
        });
      };
      ['mousemove', 'click', 'scroll', 'touchstart', 'keydown'].forEach(evt => {
        window.addEventListener(evt, unlockAudio);
      });
    });
  }, 1000);
  // -------------------------

  // --- SCROLL LOCK LOGIC FOR INTRO ---
  const originalOverflow = document.body.style.overflow;
  document.body.style.overflow = 'hidden';
  // -----------------------------------

  // Only run if we are on the portfolio page with the portfolio-verse
  const verse = document.getElementById('portfolio-verse');
  if (!verse) return;

  const brainContainer = document.querySelector('.verse-brain');
  const heroCard = document.querySelector('.verse-hero-card');

  if (heroCard) {
    // Make card container invisible initially
    gsap.set(heroCard, { opacity: 0, autoAlpha: 0 });
    gsap.set('.verse-hero-card > *', { opacity: 0, y: 30 });

    // Sequence: Fade in the card glass background first, then stagger text
    const introTl = gsap.timeline({ delay: 5 });
    
    introTl.to(heroCard, {
      opacity: 1,
      autoAlpha: 1,
      duration: 1,
      ease: "power2.inOut",
      boxShadow: "0 40px 100px rgba(0, 0, 0, 0.8), 0 0 40px rgba(0, 191, 255, 0.4), inset 0 0 0 1px rgba(255,255,255,0.05)"
    })
    .to('.verse-hero-card > *', {
      opacity: 1,
      y: 0,
      duration: 1,
      stagger: 0.2,
      ease: "power3.out",
      textShadow: "0 0 10px rgba(255, 255, 255, 0.3)"
    }, "-=0.5")
    .call(() => {
      // Unlock scroll once the intro animation finishes
      document.body.style.overflow = originalOverflow;
      
      // Fade out the hero card automatically before starting slideshow
      gsap.to(heroCard, {
        opacity: 0,
        autoAlpha: 0,
        scale: 1.1,
        duration: 1,
        ease: "power2.inOut",
        delay: 2, // Hold it for 2 seconds after text finishes
        onComplete: initInteractiveSlideshow
      });
      
      // Optional: blur background after intro
      if (brainContainer) {
        gsap.to(brainContainer, { filter: 'blur(20px) brightness(0.4)', duration: 1, delay: 2 });
      }
    });
  } else {
    document.body.style.overflow = originalOverflow;
    initInteractiveSlideshow();
  }

  function initInteractiveSlideshow() {
    const cards = document.querySelectorAll('.verse-card');
    const controlsContainer = document.querySelector('.verse-slider-controls');
    const projectsContainer = document.querySelector('.verse-projects');
    
    if (!cards.length) return;

    let currentIndex = 0;
    let autoPlayTimer;
    const slideDuration = 4000; // 4 seconds per slide
    let isTransitioning = false;

    // Initialize cards offscreen left, preserving the -50%, -50% centering translation!
    gsap.set(cards, { 
      opacity: 0, 
      autoAlpha: 0, 
      xPercent: -50, 
      yPercent: -50, 
      x: '-10vw', 
      scale: 0.95, 
      zIndex: 10 
    });

    // Generate pagination dots
    cards.forEach((_, index) => {
      const dot = document.createElement('div');
      dot.classList.add('verse-dot');
      if (index === 0) dot.classList.add('active');
      
      // Click event for manual control
      dot.addEventListener('click', () => {
        if (currentIndex !== index && !isTransitioning) {
          goToSlide(index);
          resetAutoPlay();
        }
      });
      controlsContainer.appendChild(dot);
    });

    const dots = document.querySelectorAll('.verse-dot');

    function updateDots(index) {
      dots.forEach(d => d.classList.remove('active'));
      dots[index].classList.add('active');
    }

    function goToSlide(newIndex) {
      if (isTransitioning || newIndex === currentIndex) return;
      isTransitioning = true;
      
      const currentCard = cards[currentIndex];
      const nextCard = cards[newIndex];
      
      // Determine direction based on index
      // If jumping forward, next comes from left. If backwards, next comes from right.
      // But standard left-to-right flow implies exiting right, entering left.
      // Let's keep it consistent: always exit to right (10vw), enter from left (-10vw).
      
      gsap.set(currentCard, { zIndex: 10 });
      gsap.set(nextCard, { zIndex: 20, x: '-10vw', opacity: 0, autoAlpha: 0, scale: 0.95 });

      // Animate current out to right
      gsap.to(currentCard, {
        opacity: 0,
        autoAlpha: 0,
        x: '10vw',
        scale: 0.95,
        duration: 1,
        ease: "power2.in"
      });

      // Animate next in from left
      gsap.to(nextCard, {
        opacity: 1,
        autoAlpha: 1,
        x: '0vw',
        scale: 1,
        duration: 1,
        ease: "power2.out",
        onComplete: () => {
          isTransitioning = false;
        }
      });

      currentIndex = newIndex;
      updateDots(currentIndex);
    }

    function nextSlide() {
      const newIndex = (currentIndex + 1) % cards.length;
      goToSlide(newIndex);
    }

    function startAutoPlay() {
      stopAutoPlay();
      autoPlayTimer = setInterval(nextSlide, slideDuration);
    }

    function stopAutoPlay() {
      if (autoPlayTimer) clearInterval(autoPlayTimer);
    }

    function resetAutoPlay() {
      stopAutoPlay();
      startAutoPlay();
    }

    // Hover to pause logic
    if (projectsContainer) {
      projectsContainer.addEventListener('mouseenter', stopAutoPlay);
      projectsContainer.addEventListener('mouseleave', startAutoPlay);
    }

    // Show first slide immediately
    gsap.to(cards[0], {
      opacity: 1,
      autoAlpha: 1,
      x: '0vw',
      scale: 1,
      duration: 1.5,
      ease: "power2.out"
    });

    startAutoPlay();
  }
});
