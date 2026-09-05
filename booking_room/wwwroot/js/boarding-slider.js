/**
 * wwwroot/js/boarding-slider.js
 * Controller Animasi Swipe Onboarding PERSADA (Revisi V70)
 * - Real-time 1:1 Pointer Tracking (Touch & Mouse Drag)
 * - Modern Easing: cubic-bezier(0.22, 1, 0.36, 1) [450ms]
 * - Parallax background movement
 * - Fade + Scale transition on hero text
 * - Elastic / Rubber-band resistance at boundaries
 * - Dots live sync & seamless transition to /login
 */
window.BoardingSlider = {
    activeInstance: null,

    init: function (dotNetHelper, initialSlide) {
        if (this.activeInstance) {
            this.activeInstance.destroy();
            this.activeInstance = null;
        }

        const viewport = document.getElementById('boardingViewport');
        if (!viewport) return;

        this.activeInstance = new BoardingSliderInstance(viewport, dotNetHelper, initialSlide || 0);
    },

    destroy: function () {
        if (this.activeInstance) {
            this.activeInstance.destroy();
            this.activeInstance = null;
        }
    }
};

class BoardingSliderInstance {
    constructor(viewport, dotNetHelper, initialSlide) {
        this.viewport = viewport;
        this.dotNetHelper = dotNetHelper;
        this.currentSlide = initialSlide || 0;

        // Elements
        this.bg0 = document.getElementById('boardingBg0');
        this.bg1 = document.getElementById('boardingBg1');
        this.slide0 = document.getElementById('boardingSlide0');
        this.slide1 = document.getElementById('boardingSlide1');
        this.dot0 = document.getElementById('boardingDot0');
        this.dot1 = document.getElementById('boardingDot1');

        // Drag State
        this.isDragging = false;
        this.startX = 0;
        this.startY = 0;
        this.currentX = 0;
        this.currentY = 0;
        this.lastMoveX = 0;
        this.lastMoveTime = 0;
        this.velocityX = 0;
        this.isPointerLocked = false;
        this.isHorizDrag = false;
        this.hasDecidedDirection = false;
        this.dragOffset = 0;
        this.isCompleting = false;

        // Bindings
        this.onPointerDown = this.handlePointerDown.bind(this);
        this.onPointerMove = this.handlePointerMove.bind(this);
        this.onPointerUp = this.handlePointerUp.bind(this);
        this.onResize = this.handleResize.bind(this);

        this.viewport.addEventListener('pointerdown', this.onPointerDown);
        window.addEventListener('pointermove', this.onPointerMove);
        window.addEventListener('pointerup', this.onPointerUp);
        window.addEventListener('pointercancel', this.onPointerUp);
        window.addEventListener('resize', this.onResize);

        // Apply initial state without animation
        this.applySlideState(this.currentSlide, false);
    }

    destroy() {
        this.viewport.removeEventListener('pointerdown', this.onPointerDown);
        window.removeEventListener('pointermove', this.onPointerMove);
        window.removeEventListener('pointerup', this.onPointerUp);
        window.removeEventListener('pointercancel', this.onPointerUp);
        window.removeEventListener('resize', this.onResize);
    }

    handleResize() {
        if (!this.isDragging && !this.isCompleting) {
            this.applySlideState(this.currentSlide, false);
        }
    }

    handlePointerDown(e) {
        if (this.isCompleting) return;
        if (e.target.closest('#btnBoardingSkip') || e.target.closest('button') || e.target.closest('a')) {
            return;
        }

        this.isDragging = true;
        this.startX = e.clientX;
        this.startY = e.clientY;
        this.currentX = e.clientX;
        this.currentY = e.clientY;
        this.lastMoveX = e.clientX;
        this.lastMoveTime = performance.now();
        this.velocityX = 0;
        this.hasDecidedDirection = false;
        this.isHorizDrag = false;
        this.dragOffset = 0;

        this.removeTransitions();
    }

    handlePointerMove(e) {
        if (!this.isDragging || this.isCompleting) return;

        this.currentX = e.clientX;
        this.currentY = e.clientY;
        const deltaX = this.currentX - this.startX;
        const deltaY = this.currentY - this.startY;

        if (!this.hasDecidedDirection) {
            if (Math.abs(deltaX) > 7 || Math.abs(deltaY) > 7) {
                this.hasDecidedDirection = true;
                if (Math.abs(deltaX) >= Math.abs(deltaY)) {
                    this.isHorizDrag = true;
                    try {
                        this.viewport.setPointerCapture(e.pointerId);
                        this.isPointerLocked = true;
                    } catch (_) {}
                } else {
                    this.isHorizDrag = false;
                    this.isDragging = false;
                    return;
                }
            } else {
                return;
            }
        }

        if (!this.isHorizDrag) return;

        const now = performance.now();
        const dt = now - this.lastMoveTime;
        if (dt > 0) {
            this.velocityX = (this.currentX - this.lastMoveX) / dt;
            this.lastMoveX = this.currentX;
            this.lastMoveTime = now;
        }

        // Calculate rubber-band / elastic resistance
        let effectiveDeltaX = deltaX;
        if (this.currentSlide === 0 && deltaX > 0) {
            // Elastic boundary when pulling right at first slide
            effectiveDeltaX = deltaX * 0.28;
        } else if (this.currentSlide === 1 && deltaX < 0) {
            // Progressive resistance when swiping left past slide 1
            effectiveDeltaX = deltaX * 0.65;
        }

        this.dragOffset = effectiveDeltaX;
        this.renderDrag(effectiveDeltaX);
    }

    renderDrag(deltaX) {
        const width = this.viewport.clientWidth || window.innerWidth;
        // Normalized progress: 0 (slide 0) to 1 (slide 1)
        const progress = Math.max(-0.25, Math.min(1.4, this.currentSlide - (deltaX / width)));

        // Content Slide 0
        if (this.slide0) {
            const tx0 = -progress * width;
            const scale0 = Math.max(0.94, 1 - Math.max(0, progress) * 0.05);
            const opacity0 = Math.max(0, Math.min(1, 1 - progress * 1.35));
            this.slide0.style.transform = 'translate3d(' + tx0 + 'px, 0, 0) scale(' + scale0 + ')';
            this.slide0.style.opacity = opacity0;
            this.slide0.style.pointerEvents = progress < 0.5 ? 'auto' : 'none';
        }

        // Content Slide 1
        if (this.slide1) {
            const tx1 = (1 - progress) * width;
            const p1 = 1 - progress;
            const scale1 = Math.max(0.94, 1 - Math.max(0, p1) * 0.05);
            const opacity1 = Math.max(0, Math.min(1, 1 - p1 * 1.35));
            this.slide1.style.transform = 'translate3d(' + tx1 + 'px, 0, 0) scale(' + scale1 + ')';
            this.slide1.style.opacity = opacity1;
            this.slide1.style.pointerEvents = progress >= 0.5 ? 'auto' : 'none';
        }

        // Background Parallax (moves at 25% speed of foreground)
        if (this.bg0) {
            const bgTx0 = -progress * 25; // in %
            const bgOp0 = Math.max(0, Math.min(1, 1 - progress));
            this.bg0.style.transform = 'translate3d(' + bgTx0 + '%, 0, 0)';
            this.bg0.style.opacity = bgOp0;
        }
        if (this.bg1) {
            const bgTx1 = (1 - progress) * 25; // in %
            const bgOp1 = Math.max(0, Math.min(1, progress));
            this.bg1.style.transform = 'translate3d(' + bgTx1 + '%, 0, 0)';
            this.bg1.style.opacity = bgOp1;
        }

        // Dot indicators in real-time
        if (this.dot0 && this.dot1) {
            if (progress < 0.5) {
                this.dot0.classList.add('active');
                this.dot1.classList.remove('active');
            } else {
                this.dot0.classList.remove('active');
                this.dot1.classList.add('active');
            }
        }
    }

    handlePointerUp(e) {
        if (!this.isDragging || !this.isHorizDrag || this.isCompleting) {
            this.isDragging = false;
            return;
        }

        this.isDragging = false;
        if (this.isPointerLocked) {
            try {
                this.viewport.releasePointerCapture(e.pointerId);
            } catch (_) {}
            this.isPointerLocked = false;
        }

        const width = this.viewport.clientWidth || window.innerWidth;
        const deltaX = this.dragOffset;
        const vx = this.velocityX;

        if (this.currentSlide === 0) {
            // Check if user swiped left enough to go to slide 1
            if (deltaX < -width * 0.18 || (deltaX < -35 && vx < -0.25)) {
                this.goToSlide(1);
            } else {
                // Snap back to slide 0 (rubber-band return)
                this.goToSlide(0);
            }
        } else if (this.currentSlide === 1) {
            // Check if user swiped right back to slide 0
            if (deltaX > width * 0.18 || (deltaX > 35 && vx > 0.25)) {
                this.goToSlide(0);
            } else if (deltaX < -65 || (deltaX < -25 && vx < -0.25)) {
                // User swiped left past slide 1 -> proceed to Login
                this.completeToLogin();
            } else {
                // Snap back to slide 1 (rubber-band return)
                this.goToSlide(1);
            }
        }
    }

    goToSlide(targetSlide) {
        this.currentSlide = targetSlide;
        this.applySlideState(targetSlide, true);

        if (this.dotNetHelper) {
            try {
                this.dotNetHelper.invokeMethodAsync('OnSlideChanged', targetSlide);
            } catch (_) {}
        }
    }

    applySlideState(targetSlide, animate) {
        if (animate) {
            this.addTransitions();
        } else {
            this.removeTransitions();
        }

        const width = this.viewport.clientWidth || window.innerWidth;

        if (targetSlide === 0) {
            if (this.slide0) {
                this.slide0.style.transform = 'translate3d(0, 0, 0) scale(1)';
                this.slide0.style.opacity = '1';
                this.slide0.style.pointerEvents = 'auto';
            }
            if (this.slide1) {
                this.slide1.style.transform = 'translate3d(' + width + 'px, 0, 0) scale(0.96)';
                this.slide1.style.opacity = '0';
                this.slide1.style.pointerEvents = 'none';
            }
            if (this.bg0) {
                this.bg0.style.transform = 'translate3d(0, 0, 0)';
                this.bg0.style.opacity = '1';
            }
            if (this.bg1) {
                this.bg1.style.transform = 'translate3d(25%, 0, 0)';
                this.bg1.style.opacity = '0';
            }
            if (this.dot0) this.dot0.classList.add('active');
            if (this.dot1) this.dot1.classList.remove('active');
        } else {
            if (this.slide0) {
                this.slide0.style.transform = 'translate3d(-' + width + 'px, 0, 0) scale(0.96)';
                this.slide0.style.opacity = '0';
                this.slide0.style.pointerEvents = 'none';
            }
            if (this.slide1) {
                this.slide1.style.transform = 'translate3d(0, 0, 0) scale(1)';
                this.slide1.style.opacity = '1';
                this.slide1.style.pointerEvents = 'auto';
            }
            if (this.bg0) {
                this.bg0.style.transform = 'translate3d(-25%, 0, 0)';
                this.bg0.style.opacity = '0';
            }
            if (this.bg1) {
                this.bg1.style.transform = 'translate3d(0, 0, 0)';
                this.bg1.style.opacity = '1';
            }
            if (this.dot0) this.dot0.classList.remove('active');
            if (this.dot1) this.dot1.classList.add('active');
        }
    }

    addTransitions() {
        const ease = 'transform 450ms cubic-bezier(0.22, 1, 0.36, 1), opacity 450ms cubic-bezier(0.22, 1, 0.36, 1)';
        if (this.slide0) this.slide0.style.transition = ease;
        if (this.slide1) this.slide1.style.transition = ease;
        if (this.bg0) this.bg0.style.transition = ease;
        if (this.bg1) this.bg1.style.transition = ease;
    }

    removeTransitions() {
        if (this.slide0) this.slide0.style.transition = 'none';
        if (this.slide1) this.slide1.style.transition = 'none';
        if (this.bg0) this.bg0.style.transition = 'none';
        if (this.bg1) this.bg1.style.transition = 'none';
    }

    completeToLogin() {
        this.isCompleting = true;
        this.addTransitions();
        const width = this.viewport.clientWidth || window.innerWidth;
        if (this.slide1) {
            this.slide1.style.transform = 'translate3d(-' + (width * 0.85) + 'px, 0, 0) scale(0.94)';
            this.slide1.style.opacity = '0';
        }
        if (this.bg1) {
            this.bg1.style.transform = 'translate3d(-35%, 0, 0)';
            this.bg1.style.opacity = '0';
        }

        try {
            localStorage.setItem('persada-onboarding-seen', 'true');
            localStorage.setItem('hasSeenBoarding', 'true');
        } catch (_) {}

        setTimeout(() => {
            if (this.dotNetHelper) {
                try {
                    this.dotNetHelper.invokeMethodAsync('OnCompleteBoarding');
                    return;
                } catch (_) {}
            }
            window.location.href = '/login';
        }, 250);
    }
}
