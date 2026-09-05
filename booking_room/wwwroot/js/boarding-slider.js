/**
 * wwwroot/js/boarding-slider.js
 * Controller Animasi Onboarding PERSADA (Revisi V72)
 * - Dual Zone Tap (Gaya Instagram / WhatsApp Stories):
 *   * Tap KANAN (clientX >= width / 2): Maju ke slide berikutnya / ke /login di slide terakhir
 *   * Tap KIRI (clientX < width / 2): Mundur ke slide sebelumnya / tetap diam di slide 0
 * - Visual Feedback: Ripple koordinat & zone flash halus (~200ms)
 * - Stories Progress Bar di bagian atas layar: real-time & multi-slide state sync
 * - Desktop Directional Cursor: Cues visual panah kiri/kanan pada non-touch devices
 * - Real-time 1:1 Pointer Tracking (Swipe / Touch Drag) tetap berdampingan
 * - Modern Easing: cubic-bezier(0.22, 1, 0.36, 1) [450ms]
 * - Parallax background movement (~25%)
 * - Fade + Scale transition on hero text
 * - Elastic boundary resistance & bounce
 * - Full synchronization with Blazor state
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

    goToSlide: function (slideIndex) {
        if (this.activeInstance) {
            this.activeInstance.goToSlide(slideIndex);
        }
    },

    destroy: function () {
        if (this.activeInstance) {
            this.activeInstance.destroy();
            this.activeInstance = null;
        }
    }
};

class BoardingSliderInstance {
    static RIGHT_CURSOR = "url(\"data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='28' height='28' viewBox='0 0 28 28' fill='none'%3E%3Ccircle cx='14' cy='14' r='12' fill='rgba(0,0,0,0.45)' stroke='rgba(255,255,255,0.8)' stroke-width='1.5'/%3E%3Cpath d='M12 9l5 5-5 5' stroke='white' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'/%3E%3C/svg%3E\") 14 14, e-resize";
    static LEFT_CURSOR = "url(\"data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='28' height='28' viewBox='0 0 28 28' fill='none'%3E%3Ccircle cx='14' cy='14' r='12' fill='rgba(0,0,0,0.45)' stroke='rgba(255,255,255,0.8)' stroke-width='1.5'/%3E%3Cpath d='M16 9l-5 5 5 5' stroke='white' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'/%3E%3C/svg%3E\") 14 14, w-resize";

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
        this.rippleContainer = document.getElementById('boardingRippleContainer');
        this.flashLeft = document.getElementById('zoneFlashLeft');
        this.flashRight = document.getElementById('zoneFlashRight');

        // Pointer / Drag State
        this.isPointerDown = false;
        this.isDragging = false;
        this.startX = 0;
        this.startY = 0;
        this.startTime = 0;
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
        this.onHoverMove = this.handleHoverMove.bind(this);

        this.viewport.addEventListener('pointerdown', this.onPointerDown);
        this.viewport.addEventListener('pointermove', this.onHoverMove);
        window.addEventListener('pointermove', this.onPointerMove);
        window.addEventListener('pointerup', this.onPointerUp);
        window.addEventListener('pointercancel', this.onPointerUp);
        window.addEventListener('resize', this.onResize);

        // Apply initial state
        this.applySlideState(this.currentSlide, false);
    }

    destroy() {
        this.viewport.removeEventListener('pointerdown', this.onPointerDown);
        this.viewport.removeEventListener('pointermove', this.onHoverMove);
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

    handleHoverMove(e) {
        if (this.isDragging || this.isCompleting) return;
        if (e.pointerType === 'touch') return;

        const width = this.viewport.clientWidth || window.innerWidth;
        if (e.clientX >= width / 2) {
            this.viewport.style.cursor = BoardingSliderInstance.RIGHT_CURSOR;
        } else {
            this.viewport.style.cursor = this.currentSlide === 0 ? 'default' : BoardingSliderInstance.LEFT_CURSOR;
        }
    }

    handlePointerDown(e) {
        if (this.isCompleting) return;
        if (e.target.closest('#btnBoardingSkip') || e.target.closest('button') || e.target.closest('a')) {
            return;
        }

        this.isPointerDown = true;
        this.isDragging = false;
        this.startX = e.clientX;
        this.startY = e.clientY;
        this.startTime = performance.now();
        this.currentX = e.clientX;
        this.currentY = e.clientY;
        this.lastMoveX = e.clientX;
        this.lastMoveTime = this.startTime;
        this.velocityX = 0;
        this.hasDecidedDirection = false;
        this.isHorizDrag = false;
        this.dragOffset = 0;
    }

    handlePointerMove(e) {
        if (!this.isPointerDown || this.isCompleting) return;

        this.currentX = e.clientX;
        this.currentY = e.clientY;
        const deltaX = this.currentX - this.startX;
        const deltaY = this.currentY - this.startY;

        if (!this.hasDecidedDirection) {
            if (Math.abs(deltaX) > 8 || Math.abs(deltaY) > 8) {
                this.hasDecidedDirection = true;
                if (Math.abs(deltaX) >= Math.abs(deltaY)) {
                    this.isHorizDrag = true;
                    this.isDragging = true;
                    this.viewport.style.cursor = 'grabbing';
                    this.removeTransitions();
                    try {
                        this.viewport.setPointerCapture(e.pointerId);
                        this.isPointerLocked = true;
                    } catch (_) {}
                } else {
                    this.isHorizDrag = false;
                    this.isPointerDown = false;
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
            effectiveDeltaX = deltaX * 0.28;
        } else if (this.currentSlide === 1 && deltaX < 0) {
            effectiveDeltaX = deltaX * 0.65;
        }

        this.dragOffset = effectiveDeltaX;
        this.renderDrag(effectiveDeltaX);
    }

    renderDrag(deltaX) {
        const width = this.viewport.clientWidth || window.innerWidth;
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

        // Background Parallax (~25% speed of foreground)
        if (this.bg0) {
            const bgTx0 = -progress * 25;
            const bgOp0 = Math.max(0, Math.min(1, 1 - progress));
            this.bg0.style.transform = 'translate3d(' + bgTx0 + '%, 0, 0)';
            this.bg0.style.opacity = bgOp0;
        }
        if (this.bg1) {
            const bgTx1 = (1 - progress) * 25;
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
        if (!this.isPointerDown || this.isCompleting) {
            this.isPointerDown = false;
            this.isDragging = false;
            return;
        }

        const duration = performance.now() - this.startTime;
        const totalDistance = Math.hypot(e.clientX - this.startX, e.clientY - this.startY);

        if (this.isPointerLocked) {
            try {
                this.viewport.releasePointerCapture(e.pointerId);
            } catch (_) {}
            this.isPointerLocked = false;
        }

        this.isPointerDown = false;

        // CHECK 1: TAP TO ADVANCE (Dual-Zone Instagram / WhatsApp Stories Style)
        if (!this.isDragging && totalDistance < 14 && duration < 500) {
            const width = this.viewport.clientWidth || window.innerWidth;
            const isRightSide = (e.clientX >= width / 2);

            // Visual feedback: zone flash & ripple
            this.triggerTapVisualFeedback(e.clientX, e.clientY, isRightSide);

            if (isRightSide) {
                // Tap KANAN: maju ke slide berikutnya atau ke Login jika sudah di slide terakhir
                if (this.currentSlide === 0) {
                    this.goToSlide(1);
                } else {
                    this.completeToLogin();
                }
            } else {
                // Tap KIRI: mundur ke slide sebelumnya atau tetap diam jika di slide 0
                if (this.currentSlide > 0) {
                    this.goToSlide(this.currentSlide - 1);
                } else {
                    this.triggerBoundaryBounce(0);
                }
            }
            return;
        }

        // CHECK 2: SWIPE GESTURE (Horizontal Drag)
        if (this.isHorizDrag) {
            this.isDragging = false;
            const width = this.viewport.clientWidth || window.innerWidth;
            const deltaX = this.dragOffset;
            const vx = this.velocityX;

            if (this.currentSlide === 0) {
                if (deltaX < -width * 0.16 || (deltaX < -30 && vx < -0.25)) {
                    this.goToSlide(1);
                } else {
                    this.goToSlide(0);
                }
            } else if (this.currentSlide === 1) {
                if (deltaX > width * 0.16 || (deltaX > 30 && vx > 0.25)) {
                    this.goToSlide(0);
                } else if (deltaX < -55 || (deltaX < -20 && vx < -0.25)) {
                    this.completeToLogin();
                } else {
                    this.goToSlide(1);
                }
            }
        }
    }

    triggerTapVisualFeedback(clientX, clientY, isRightSide) {
        // 1. Zone Flash
        const zoneFlash = isRightSide ? this.flashRight : this.flashLeft;
        if (zoneFlash) {
            zoneFlash.classList.add('flash');
            setTimeout(() => {
                zoneFlash.classList.remove('flash');
            }, 200);
        }

        // 2. Circular Ripple at tap coordinates
        if (this.rippleContainer) {
            const rect = this.viewport.getBoundingClientRect();
            const relX = clientX - rect.left;
            const relY = clientY - rect.top;

            const ripple = document.createElement('div');
            ripple.className = 'boarding-tap-ripple';
            ripple.style.left = relX + 'px';
            ripple.style.top = relY + 'px';
            this.rippleContainer.appendChild(ripple);

            setTimeout(() => {
                if (ripple.parentNode) {
                    ripple.parentNode.removeChild(ripple);
                }
            }, 300);
        }
    }

    triggerBoundaryBounce(slideIndex) {
        if (slideIndex === 0 && this.slide0) {
            this.slide0.style.transition = 'transform 140ms ease-out';
            this.slide0.style.transform = 'translate3d(14px, 0, 0) scale(1)';
            setTimeout(() => {
                if (this.currentSlide === 0 && this.slide0) {
                    this.slide0.style.transition = 'transform 220ms cubic-bezier(0.22, 1, 0.36, 1)';
                    this.slide0.style.transform = 'translate3d(0, 0, 0) scale(1)';
                }
            }, 140);
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
                this.slide0.classList.add('active');
                this.slide0.style.transform = 'translate3d(0, 0, 0) scale(1)';
                this.slide0.style.opacity = '1';
                this.slide0.style.pointerEvents = 'auto';
            }
            if (this.slide1) {
                this.slide1.classList.remove('active');
                this.slide1.style.transform = 'translate3d(' + width + 'px, 0, 0) scale(0.96)';
                this.slide1.style.opacity = '0';
                this.slide1.style.pointerEvents = 'none';
            }
            if (this.bg0) {
                this.bg0.classList.add('active');
                this.bg0.style.transform = 'translate3d(0, 0, 0)';
                this.bg0.style.opacity = '1';
            }
            if (this.bg1) {
                this.bg1.classList.remove('active');
                this.bg1.style.transform = 'translate3d(25%, 0, 0)';
                this.bg1.style.opacity = '0';
            }
            if (this.dot0) this.dot0.classList.add('active');
            if (this.dot1) this.dot1.classList.remove('active');
        } else {
            if (this.slide0) {
                this.slide0.classList.remove('active');
                this.slide0.style.transform = 'translate3d(-' + width + 'px, 0, 0) scale(0.96)';
                this.slide0.style.opacity = '0';
                this.slide0.style.pointerEvents = 'none';
            }
            if (this.slide1) {
                this.slide1.classList.add('active');
                this.slide1.style.transform = 'translate3d(0, 0, 0) scale(1)';
                this.slide1.style.opacity = '1';
                this.slide1.style.pointerEvents = 'auto';
            }
            if (this.bg0) {
                this.bg0.classList.remove('active');
                this.bg0.style.transform = 'translate3d(-25%, 0, 0)';
                this.bg0.style.opacity = '0';
            }
            if (this.bg1) {
                this.bg1.classList.add('active');
                this.bg1.style.transform = 'translate3d(0, 0, 0)';
                this.bg1.style.opacity = '1';
            }
            if (this.dot0) this.dot0.classList.remove('active');
            if (this.dot1) this.dot1.classList.add('active');
        }

        // Update desktop cursor according to current slide
        const currentMouseX = this.currentX || (width * 0.75);
        if (currentMouseX >= width / 2) {
            this.viewport.style.cursor = BoardingSliderInstance.RIGHT_CURSOR;
        } else {
            this.viewport.style.cursor = this.currentSlide === 0 ? 'default' : BoardingSliderInstance.LEFT_CURSOR;
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
