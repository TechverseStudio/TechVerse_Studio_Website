/**
 * TechVerse Studio — Main JavaScript
 */

(function () {
  'use strict';

  const WHATSAPP_NUMBER = '918788738694';
  const WHATSAPP_MESSAGE = encodeURIComponent(
    'Hi TechVerse Studio! I would like to discuss a digital project.'
  );

  /* Navbar scroll + active links */
  function initNavbar() {
    const navbar = document.querySelector('.navbar');
    const menuToggle = document.querySelector('.menu-toggle');
    const mobileMenu = document.querySelector('.mobile-menu');
    const navLinks = document.querySelectorAll('.nav-links a, .mobile-menu a');

    window.addEventListener('scroll', () => {
      navbar?.classList.toggle('scrolled', window.scrollY > 40);
      updateActiveNav();
    }, { passive: true });

    menuToggle?.addEventListener('click', () => {
      menuToggle.classList.toggle('active');
      mobileMenu?.classList.toggle('open');
      document.body.style.overflow = mobileMenu?.classList.contains('open') ? 'hidden' : '';
    });

    mobileMenu?.querySelectorAll('a').forEach((link) => {
      link.addEventListener('click', () => {
        menuToggle?.classList.remove('active');
        mobileMenu?.classList.remove('open');
        document.body.style.overflow = '';
      });
    });

    function updateActiveNav() {
      const sections = document.querySelectorAll('section[id]');
      let current = '';
      sections.forEach((section) => {
        const top = section.offsetTop - 120;
        if (window.scrollY >= top) current = section.getAttribute('id');
      });
      navLinks.forEach((link) => {
        const href = link.getAttribute('href');
        if (href?.startsWith('#')) {
          link.classList.toggle('active', href === `#${current}`);
        }
      });
    }

    const page = window.location.pathname.split('/').pop() || 'index.html';
    navLinks.forEach((link) => {
      const href = link.getAttribute('href');
      if (href && !href.startsWith('#') && href.includes(page)) {
        link.classList.add('active');
      }
    });

    navbar?.classList.toggle('scrolled', window.scrollY > 40);
  }

  /* Particle canvas */
  function initParticles() {
    const canvas = document.getElementById('particle-canvas');
    if (!canvas) return;

    const ctx = canvas.getContext('2d');
    let particles = [];
    let animationId;

    function resize() {
      canvas.width = window.innerWidth;
      canvas.height = window.innerHeight;
    }

    function createParticles() {
      const count = Math.min(80, Math.floor(window.innerWidth / 20));
      particles = [];
      for (let i = 0; i < count; i++) {
        particles.push({
          x: Math.random() * canvas.width,
          y: Math.random() * canvas.height,
          vx: (Math.random() - 0.5) * 0.4,
          vy: (Math.random() - 0.5) * 0.4,
          r: Math.random() * 2 + 0.5,
        });
      }
    }

    function draw() {
      ctx.clearRect(0, 0, canvas.width, canvas.height);

      particles.forEach((p, i) => {
        p.x += p.vx;
        p.y += p.vy;
        if (p.x < 0 || p.x > canvas.width) p.vx *= -1;
        if (p.y < 0 || p.y > canvas.height) p.vy *= -1;

        ctx.beginPath();
        ctx.arc(p.x, p.y, p.r, 0, Math.PI * 2);
        ctx.fillStyle = 'rgba(59, 130, 246, 0.5)';
        ctx.fill();

        particles.slice(i + 1).forEach((p2) => {
          const dist = Math.hypot(p.x - p2.x, p.y - p2.y);
          if (dist < 120) {
            ctx.beginPath();
            ctx.moveTo(p.x, p.y);
            ctx.lineTo(p2.x, p2.y);
            ctx.strokeStyle = `rgba(139, 92, 246, ${0.15 * (1 - dist / 120)})`;
            ctx.stroke();
          }
        });
      });

      animationId = requestAnimationFrame(draw);
    }

    resize();
    createParticles();
    draw();

    window.addEventListener('resize', () => {
      resize();
      createParticles();
    });

    if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
      cancelAnimationFrame(animationId);
      canvas.style.display = 'none';
    }
  }

  /* Animated counters */
  function initCounters() {
    const counters = document.querySelectorAll('[data-count]');
    if (!counters.length) return;

    const observer = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (!entry.isIntersecting) return;
          const el = entry.target;
          const target = parseInt(el.getAttribute('data-count'), 10);
          const suffix = el.getAttribute('data-suffix') || '';
          const duration = 2000;
          const start = performance.now();

          function update(now) {
            const progress = Math.min((now - start) / duration, 1);
            const eased = 1 - Math.pow(1 - progress, 3);
            el.textContent = Math.floor(target * eased) + suffix;
            if (progress < 1) requestAnimationFrame(update);
            else el.textContent = target + suffix;
          }

          requestAnimationFrame(update);
          observer.unobserve(el);
        });
      },
      { threshold: 0.3 }
    );

    counters.forEach((c) => observer.observe(c));
  }

  /* Scroll reveal */
  function initReveal() {
    const elements = document.querySelectorAll('.reveal');
    const observer = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) {
            entry.target.classList.add('visible');
            // Play any video inside the revealed element
            const video = entry.target.querySelector('video');
            if (video && typeof video.play === 'function') {
              video.play().catch(e => console.log("Video lazy play blocked:", e));
            }
            observer.unobserve(entry.target);
          }
        });
      },
      { threshold: 0.1, rootMargin: '0px 0px -40px 0px' }
    );
    elements.forEach((el) => observer.observe(el));
  }

  /* Portfolio filters */
  function initPortfolioFilter() {
    const filterBtns = document.querySelectorAll('.filter-btn');
    const cards = document.querySelectorAll('.portfolio-card');

    filterBtns.forEach((btn) => {
      btn.addEventListener('click', () => {
        const filter = btn.getAttribute('data-filter');
        filterBtns.forEach((b) => b.classList.remove('active'));
        btn.classList.add('active');

        cards.forEach((card) => {
          const category = card.getAttribute('data-category');
          const show = filter === 'all' || category === filter;
          card.classList.toggle('hidden', !show);
          card.style.animation = show ? 'fadeInUp 0.5s ease' : '';
        });
      });
    });
  }

  /* FAQ accordion */
  function initFAQ() {
    document.querySelectorAll('.faq-question').forEach((btn) => {
      btn.addEventListener('click', () => {
        const item = btn.closest('.faq-item');
        const wasOpen = item.classList.contains('open');
        document.querySelectorAll('.faq-item').forEach((i) => i.classList.remove('open'));
        if (!wasOpen) item.classList.add('open');
      });
    });
  }

  /* Contact form validation */
  function initContactForm() {
    const form = document.getElementById('contact-form');
    if (!form) return;

    const fields = {
      name: { required: true, min: 2 },
      email: { required: true, pattern: /^[^\s@]+@[^\s@]+\.[^\s@]+$/ },
      phone: { required: true, pattern: /^[\d\s+\-()]{10,}$/ },
      project: { required: true },
      budget: { required: true },
      message: { required: true, min: 10 },
    };

    function showError(input, message) {
      input.classList.add('error');
      const err = input.parentElement.querySelector('.form-error');
      if (err) {
        err.textContent = message;
        err.classList.add('visible');
      }
    }

    function clearError(input) {
      input.classList.remove('error');
      const err = input.parentElement.querySelector('.form-error');
      err?.classList.remove('visible');
    }

    function validateField(name, input) {
      const rules = fields[name];
      if (!rules) return true;
      const val = input.value.trim();

      if (rules.required && !val) {
        showError(input, 'This field is required.');
        return false;
      }
      if (rules.min && val.length < rules.min) {
        showError(input, `Please enter at least ${rules.min} characters.`);
        return false;
      }
      if (rules.pattern && !rules.pattern.test(val)) {
        showError(input, 'Please enter a valid value.');
        return false;
      }
      clearError(input);
      return true;
    }

    Object.keys(fields).forEach((name) => {
      const input = form.querySelector(`[name="${name}"]`);
      input?.addEventListener('blur', () => validateField(name, input));
      input?.addEventListener('input', () => {
        if (input.classList.contains('error')) validateField(name, input);
      });
    });

    form.addEventListener('submit', (e) => {
      e.preventDefault();
      let valid = true;
      Object.keys(fields).forEach((name) => {
        const input = form.querySelector(`[name="${name}"]`);
        if (input && !validateField(name, input)) valid = false;
      });

      if (!valid) return;

      const btn = form.querySelector('button[type="submit"]') || form.querySelector('.btn-primary');
      const originalText = btn.innerHTML;
      btn.innerHTML = 'Sending...';
      btn.style.opacity = '0.7';
      btn.style.pointerEvents = 'none';

      const data = new FormData(form);

      fetch('https://formsubmit.co/ajax/tvs.techverse.studio@gmail.com', {
          method: 'POST',
          headers: { 
              'Accept': 'application/json'
          },
          body: data
      })
      .then(response => response.json())
      .then(data => {
          btn.innerHTML = originalText;
          btn.style.opacity = '1';
          btn.style.pointerEvents = 'auto';
          
          const success = form.querySelector('.form-success');
          if (success) {
              success.textContent = "Thank you! Your message has been sent successfully.";
              success.classList.add('visible');
              setTimeout(() => success.classList.remove('visible'), 5000);
          }
          form.reset();
      })
      .catch(error => {
          console.error(error);
          btn.innerHTML = originalText;
          btn.style.opacity = '1';
          btn.style.pointerEvents = 'auto';
          alert("Oops! There was a problem submitting your form.");
      });
    });
  }

  /* WhatsApp */
  function initWhatsApp() {
    document.querySelectorAll('[data-whatsapp]').forEach((el) => {
      el.href = `https://wa.me/${WHATSAPP_NUMBER}?text=${WHATSAPP_MESSAGE}`;
      el.setAttribute('target', '_blank');
      el.setAttribute('rel', 'noopener noreferrer');
      });
  }

  /* Ambient Background System */
  function initAmbientSystem() {
    const container = document.createElement('div');
    container.id = 'ambient-background';
    container.style.cssText = 'position: absolute; top: 0; left: 0; width: 100%; height: 100%; pointer-events: none; z-index: 0; overflow: hidden;';
    document.body.appendChild(container);

    const shapes = [
      // Cube
      `<svg viewBox="0 0 100 100" fill="none"><polygon points="50,10 90,30 50,50 10,30" fill="rgba(138,46,255,0.4)" stroke="#8A2EFF" stroke-width="2"/><polygon points="10,30 50,50 50,90 10,70" fill="rgba(0,191,255,0.2)" stroke="#00BFFF" stroke-width="2"/><polygon points="50,50 90,30 90,70 50,90" fill="rgba(255,60,247,0.2)" stroke="#FF3CF7" stroke-width="2"/></svg>`,
      // Pyramid
      `<svg viewBox="0 0 100 100" fill="none"><polygon points="50,10 20,80 50,90" fill="rgba(0,191,255,0.3)" stroke="#00BFFF" stroke-width="2"/><polygon points="50,10 80,70 50,90" fill="rgba(138,46,255,0.3)" stroke="#8A2EFF" stroke-width="2"/></svg>`,
      // Torus
      `<svg viewBox="0 0 100 100" fill="none"><ellipse cx="50" cy="50" rx="45" ry="25" stroke="url(#neon-gradient)" stroke-width="12" fill="none" opacity="0.9"/><ellipse cx="50" cy="50" rx="35" ry="17" stroke="#00E5FF" stroke-width="2" fill="none" opacity="0.6"/></svg>`,
      // Gem
      `<svg viewBox="0 0 100 100" fill="none"><polygon points="50,10 85,35 70,80 30,80 15,35" fill="rgba(0,191,255,0.2)" stroke="#00BFFF" stroke-width="2"/><polygon points="50,10 70,45 30,45" fill="rgba(138,46,255,0.3)" stroke="#8A2EFF" stroke-width="2"/><polygon points="30,45 70,45 50,85" fill="rgba(255,60,247,0.2)" stroke="#FF3CF7" stroke-width="2"/><polygon points="15,35 30,45 30,80" fill="rgba(138,46,255,0.1)" stroke="#8A2EFF" stroke-width="2"/><polygon points="85,35 70,45 70,80" fill="rgba(138,46,255,0.1)" stroke="#8A2EFF" stroke-width="2"/></svg>`,
      // Wireframe Sphere
      `<svg viewBox="0 0 200 200" fill="none"><circle cx="100" cy="100" r="60" stroke="#8A2EFF" stroke-width="2" stroke-dasharray="4 4" fill="rgba(138,46,255,0.05)"/><ellipse cx="100" cy="100" rx="60" ry="25" stroke="#00BFFF" stroke-width="1.5"/><ellipse cx="100" cy="100" rx="25" ry="60" stroke="#00BFFF" stroke-width="1.5"/></svg>`,
      // Hexagon
      `<svg viewBox="0 0 100 100" fill="none"><polygon points="50,5 95,28 95,72 50,95 5,72 5,28" fill="rgba(255,60,247,0.1)" stroke="#FF3CF7" stroke-width="2"/><polygon points="50,15 85,35 85,65 50,85 15,65 15,35" stroke="#00BFFF" stroke-width="1" fill="none"/></svg>`,
      // Neural Node
      `<svg viewBox="0 0 100 100" fill="none"><circle cx="20" cy="50" r="5" fill="#FF3CF7"/><circle cx="50" cy="20" r="5" fill="#8A2EFF"/><circle cx="50" cy="80" r="5" fill="#8A2EFF"/><circle cx="80" cy="50" r="5" fill="#00BFFF"/><path d="M20 50 L50 20 L80 50 L50 80 Z" stroke="rgba(138,46,255,0.4)" stroke-width="2"/><path d="M20 50 L80 50 M50 20 L50 80" stroke="rgba(138,46,255,0.4)" stroke-width="2"/></svg>`,
      // Particle Cluster
      `<svg viewBox="0 0 100 100" fill="none"><circle cx="50" cy="50" r="3" fill="#00E5FF" filter="drop-shadow(0 0 8px #00E5FF)"/><circle cx="20" cy="30" r="2" fill="#FF3CF7"/><circle cx="80" cy="70" r="2" fill="#8A2EFF"/><circle cx="70" cy="20" r="1.5" fill="#00BFFF"/><circle cx="30" cy="80" r="1.5" fill="#00E5FF"/></svg>`,
      // Shard
      `<svg viewBox="0 0 100 100" fill="none"><path d="M50 10 L80 40 L50 90 L20 40 Z" fill="rgba(138,46,255,0.2)" stroke="#8A2EFF" stroke-width="2"/><path d="M50 10 L60 40 L50 90 L40 40 Z" fill="rgba(255,60,247,0.2)" stroke="#FF3CF7" stroke-width="2"/></svg>`,
      // TV Logo Fragment
      `<svg viewBox="0 0 100 100" fill="none"><path d="M20 20 L80 20 L65 40 L50 70 L35 40 Z" stroke="#00BFFF" stroke-width="2" fill="rgba(0,191,255,0.1)"/><path d="M20 30 L80 30 L65 50 L50 80 L35 50 Z" stroke="#FF3CF7" stroke-width="2" fill="none" opacity="0.5"/></svg>`
    ];

    const numObjects = 35; // Total objects to distribute
    const ambientObjects = [];

    // Distribute objects
    for (let i = 0; i < numObjects; i++) {
      const obj = document.createElement('div');
      obj.className = 'ambient-obj';
      
      // Random shape
      obj.innerHTML = shapes[Math.floor(Math.random() * shapes.length)];
      const svg = obj.querySelector('svg');
      if(svg) svg.style.width = '100%';
      if(svg) svg.style.height = '100%';

      // Determine depth layer (foreground, midground, background)
      const layerRand = Math.random();
      let depth, size, opacity, filter, animSpeed;
      
      if (layerRand < 0.3) {
        // Foreground: Large, slightly blurred, high opacity
        depth = 3;
        size = 80 + Math.random() * 80;
        opacity = 0.6 + Math.random() * 0.2; // ~70%
        filter = 'blur(4px)';
        animSpeed = 40 + Math.random() * 20; // Slower rotation
      } else if (layerRand < 0.7) {
        // Midground: Medium, normal, sharp
        depth = 2;
        size = 40 + Math.random() * 60;
        opacity = 0.65 + Math.random() * 0.15; // ~70%
        filter = 'drop-shadow(0 0 15px rgba(0,229,255,0.4))';
        animSpeed = 50 + Math.random() * 30;
      } else {
        // Background: Small, slow, sharp
        depth = 1;
        size = 15 + Math.random() * 25;
        opacity = 0.5 + Math.random() * 0.2; // ~60%
        filter = 'drop-shadow(0 0 10px rgba(255,60,247,0.5))';
        animSpeed = 60 + Math.random() * 40;
      }

      // Random positioning (0 to 100% of document height)
      const topPos = Math.random() * 100; 
      // Force some objects to sides, some to middle
      let leftPos = Math.random() * 100;
      if (Math.random() > 0.5) {
        leftPos = Math.random() < 0.5 ? Math.random() * 20 : 80 + Math.random() * 20;
      }

      const rotateStart = Math.random() * 360;
      
      // Drastically reduce parallax speed for a more professional feel
      const pSpeed = depth * 0.015 * (Math.random() > 0.5 ? 1 : -1);

      obj.style.cssText = `
        position: absolute;
        top: ${topPos}%;
        left: ${leftPos}%;
        width: ${size}px;
        height: ${size}px;
        opacity: ${opacity};
        filter: ${filter};
        transform: translate(-50%, -50%) rotate(${rotateStart}deg);
        will-change: transform;
        z-index: ${depth};
      `;

      ambientObjects.push({
        el: obj,
        parallaxSpeed: pSpeed,
        rotStart: rotateStart,
        rotSpeed: 360 / animSpeed,
        // Add slow random continuous drift velocity (pixels per second)
        vx: (Math.random() - 0.5) * 15,
        vy: (Math.random() - 0.5) * 15,
        currentX: 0,
        currentY: 0
      });

      container.appendChild(obj);
    }

    // Animation Loop
    let lastTime = performance.now();
    let scrollY = window.scrollY;
    let mouseX = 0;
    let mouseY = 0;

    document.addEventListener('mousemove', (e) => {
      mouseX = (e.clientX / window.innerWidth - 0.5) * 100;
      mouseY = (e.clientY / window.innerHeight - 0.5) * 100;
    }, {passive: true});

    document.addEventListener('scroll', () => {
      scrollY = window.scrollY;
    }, {passive: true});

    function render(time) {
      // limit dt to avoid huge jumps when switching tabs
      let dt = (time - lastTime) / 1000;
      if (dt > 0.1) dt = 0.1;
      lastTime = time;

      ambientObjects.forEach(obj => {
        // Slow continuous drift
        obj.currentX += obj.vx * dt;
        obj.currentY += obj.vy * dt;
        
        const currentRot = obj.rotStart + (time / 1000) * obj.rotSpeed;
        
        // Subtle parallax logic
        const scrollOffset = scrollY * obj.parallaxSpeed;
        const mouseOffsetX = mouseX * obj.parallaxSpeed * 2;
        const mouseOffsetY = mouseY * obj.parallaxSpeed * 2;

        obj.el.style.transform = `translate(calc(-50% + ${mouseOffsetX + obj.currentX}px), calc(-50% + ${scrollOffset + mouseOffsetY + obj.currentY}px)) rotate(${currentRot}deg)`;
      });

      requestAnimationFrame(render);
    }
    
    requestAnimationFrame(render);
  }

  /* Robot Interaction */
  function initRobotInteraction() {
    const heroVisual = document.querySelector('.hero-visual');
    const captionText = document.getElementById('robot-caption-text');
    const robotVideo = document.querySelector('.robot-video');
    if (!heroVisual || !captionText) return;

    let sequenceTimeouts = [];

    function clearSequence() {
      sequenceTimeouts.forEach(clearTimeout);
      sequenceTimeouts = [];
      heroVisual.classList.remove('is-waving');
    }

    function runSequence() {
      clearSequence();
      
      // Phase 1: Wait 3s before first message
      sequenceTimeouts.push(setTimeout(() => {
        captionText.innerHTML = "Welcome To<br>TechVerse Studio";
        heroVisual.classList.add('is-waving');
      }, 3000));

      // Phase 2: Hide first message after 3s (1.5s typing + 1.5s reading)
      sequenceTimeouts.push(setTimeout(() => {
        heroVisual.classList.remove('is-waving');
      }, 6000));

      // Phase 3: Quickly show second message (0.5s gap)
      sequenceTimeouts.push(setTimeout(() => {
        captionText.innerHTML = "Where ideas become<br>real world solutions";
        heroVisual.classList.add('is-waving');
      }, 6500));

      // Phase 4: Hide second message permanently after 3.5s (1.5s typing + 2s reading)
      sequenceTimeouts.push(setTimeout(() => {
        heroVisual.classList.remove('is-waving');
      }, 10000));
    }

    // Start the sequence exactly once on load
    runSequence();

    // Detect when the video loops back to the start
    if (robotVideo) {
      let lastTime = 0;
      robotVideo.addEventListener('timeupdate', () => {
        // If currentTime drops significantly, it means it looped back to 0
        if (robotVideo.currentTime < lastTime - 1) {
          runSequence();
        }
        lastTime = robotVideo.currentTime;
      });
    }
  }


  /* Vertical Testimonials Slideshow */
  function initTestimonials() {
    const cards = document.querySelectorAll('.testimonial-card');
    if (!cards.length) return;
    
    let currentIndex = 0;
    cards[currentIndex].classList.add('active');

    setInterval(() => {
      const currentCard = cards[currentIndex];
      currentCard.classList.remove('active');
      currentCard.classList.add('exit');

      currentIndex = (currentIndex + 1) % cards.length;
      const nextCard = cards[currentIndex];
      
      // Remove exit so it resets its transform to bottom before sliding up
      nextCard.classList.remove('exit');
      
      // Force a browser reflow so the removal of 'exit' takes effect instantly without transition
      void nextCard.offsetWidth;

      nextCard.classList.add('active');
    }, 4000); // Change testimonial every 4 seconds
  }
  /* Global Media Loader (Lazy loading & Sequential Preloader) */
  function initMediaLoader() {
    // 1. Lazy Loading for the current page
    const mediaElements = document.querySelectorAll('video[data-src], img[data-src]');
    if ('IntersectionObserver' in window) {
      const mediaObserver = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
          if (entry.isIntersecting) {
            const el = entry.target;
            el.src = el.getAttribute('data-src');
            el.removeAttribute('data-src');
            
            if (el.tagName.toLowerCase() === 'video') {
              el.load();
              el.play().catch(e => console.log("Video lazy play blocked:", e));
            }
            
            observer.unobserve(el);
          }
        });
      }, { rootMargin: '200px' });
      
      mediaElements.forEach(el => mediaObserver.observe(el));
    } else {
      mediaElements.forEach(el => {
        el.src = el.getAttribute('data-src');
        el.removeAttribute('data-src');
      });
    }

    // 2. Sequential Background Preloader
    const prefetchQueue = [
      'assets/videos/robot-new.webm',
      'assets/videos/Web-dev-video.mp4',
      'assets/videos/android-dev-video.mp4',
      'assets/videos/ai-solutions-video.mp4',
      'assets/videos/chatbots-video.mp4',
      'assets/videos/automation-video.mp4',
      'assets/videos/branding-video.mp4',
      'assets/videos/graphic-video.mp4',
      'assets/videos/animation-video.mp4',
      'assets/videos/seo-video.mp4',
      'assets/videos/portfolio-replace.mp4',
      'assets/videos/about-video.mp4',
      'assets/images/student-project-1.png',
      'assets/images/student-project-2.png',
      'assets/images/student-project-3.png',
      'assets/images/student-project-4.png',
      'assets/images/jarvis_hud.png'
    ];

    function preloadNext(index) {
      if (index >= prefetchQueue.length) return;
      
      const url = prefetchQueue[index];
      if (url.endsWith('.png') || url.endsWith('.jpg') || url.endsWith('.svg')) {
        const img = new Image();
        img.onload = img.onerror = () => preloadNext(index + 1);
        img.src = url;
      } else {
        fetch(url)
          .then(res => res.blob())
          .then(() => preloadNext(index + 1))
          .catch(() => preloadNext(index + 1));
      }
    }

    window.addEventListener('load', () => {
      setTimeout(() => {
        if ('requestIdleCallback' in window) {
          requestIdleCallback(() => preloadNext(0));
        } else {
          preloadNext(0);
        }
      }, 2000);
    });
  }

  /* Init */
  document.addEventListener('DOMContentLoaded', () => {
    initNavbar();
    initParticles();
    initCounters();
    initReveal();
    initPortfolioFilter();
    initFAQ();
    initContactForm();
    initWhatsApp();
    initAmbientSystem();
    initRobotInteraction();
    initTestimonials();
    initMediaLoader();
  });
})();

