# Techverse Studio - Development Context Guide

This document is a technical summary of the recent development sessions for the Techverse Studio project. You can provide this to any future AI agent to quickly bring them up to speed on the codebase, the specific design choices made, and the exact CSS techniques used.

## 1. The Services Section Update
- **Video Integration**: We replaced the static placeholder images in `services.html` with HTML5 `<video>` tags. There are now 9 total services in a zigzag (`reverse`) layout.
- **The "Ambient Glow" CSS Technique**: 
  - We had a significant debugging session regarding the glowing colored lights behind each video frame.
  - **The Fix**: The glow is currently applied using a `::before` pseudo-element on the `.service-visual` container. 
  - **Critical CSS Geometry**: It uses negative insets (`top: -10%; left: -10%; right: -10%; bottom: -15%;`) to ensure the glowing box is physically *larger* than the solid video player. This, combined with `filter: blur(80px)` and a completely solid `var(--glow-color)` without alpha transparency, creates the perfect massive, soft, organic ambient glow bleeding out from behind the videos.
  - **Hover Effects**: When hovering over `.service-visual`, the wrapper translates and the shadow intensifies, while the `::before` glow expands to `blur(100px)`.
- **Color Palette Coordination**: We strictly aligned the individual service colors to map to our tech-themed neon branding:
  - Blue (`rgba(0, 191, 255, 1)`)
  - Purple (`rgba(138, 46, 255, 1)`)
  - Pink (`rgba(255, 60, 247, 1)`)
  - Cyan (`rgba(0, 229, 255, 1)`)

## 2. General Design Philosophy
- **Aesthetic**: Dark mode, glassmorphism, neon accents (`var(--accent-blue)`, `var(--accent-purple)`), and futuristic tech agency vibes.
- **Micro-Interactions**: We heavily use `transform: translateY(-10px) scale(1.02)` on hover for glass cards, combined with `cubic-bezier(0.175, 0.885, 0.32, 1.275)` for an organic, bouncy feel.

---
*Note to next agent: Read this file carefully before modifying `.service-visual` or `.service-image-wrapper` to ensure you do not break the ambient glow geometry!*
