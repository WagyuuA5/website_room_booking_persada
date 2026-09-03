window.modalHelper = {
    lockBodyScroll: function () {
        const body = document.body;
        if (body) {
            body.style.overflow = 'hidden';
        }
    },
    unlockBodyScroll: function () {
        const body = document.body;
        if (body) {
            body.style.removeProperty('overflow');
        }
    }
};

window.popoverHelper = {
    _handlers: new Map(),
    registerScrollClose: function (id, dotNetHelper) {
        if (window.popoverHelper._handlers.has(id)) {
            window.popoverHelper.unregisterScrollClose(id);
        }
        const handler = function (e) {
            // Ignore scroll inside popover-card itself (e.g. notification list)
            if (e.target && typeof e.target.closest === 'function' && e.target.closest('.popover-card')) {
                return;
            }
            try {
                dotNetHelper.invokeMethodAsync('OnWindowScrolled');
            } catch (err) { }
        };
        window.addEventListener('scroll', handler, { passive: true, capture: true });
        window.popoverHelper._handlers.set(id, handler);
    },
    unregisterScrollClose: function (id) {
        if (window.popoverHelper._handlers.has(id)) {
            const handler = window.popoverHelper._handlers.get(id);
            window.removeEventListener('scroll', handler, { capture: true });
            window.popoverHelper._handlers.delete(id);
        }
    }
};
window.registerEscapeKey = function (dotNetHelper) {
    window.addEventListener('keydown', function (e) {
        if (e.key === 'Escape' || e.key === 'Esc') {
            dotNetHelper.invokeMethodAsync('OnEscapePressed');
        }
    });
};

window.initDragScroll = function (elementId) {
    const slider = document.getElementById(elementId);
    if (!slider || slider.dataset.dragScrollInit) return;
    slider.dataset.dragScrollInit = "true";

    let isDown = false;
    let startX;
    let scrollLeft;
    let hasMoved = false;

    slider.addEventListener('mousedown', (e) => {
        // Only trigger on left mouse click
        if (e.button !== 0) return;
        isDown = true;
        hasMoved = false;
        slider.classList.add('grabbing');
        startX = e.pageX - slider.offsetLeft;
        scrollLeft = slider.scrollLeft;
    });

    slider.addEventListener('mouseleave', () => {
        isDown = false;
        slider.classList.remove('grabbing');
    });

    slider.addEventListener('mouseup', () => {
        isDown = false;
        slider.classList.remove('grabbing');
    });

    slider.addEventListener('mousemove', (e) => {
        if (!isDown) return;
        const x = e.pageX - slider.offsetLeft;
        const walk = (x - startX) * 1.5;
        if (Math.abs(walk) > 4) {
            hasMoved = true;
            e.preventDefault();
        }
        slider.scrollLeft = scrollLeft - walk;
    });

    slider.addEventListener('click', (e) => {
        if (hasMoved) {
            e.stopPropagation();
            e.preventDefault();
            hasMoved = false;
        }
    }, true);
};

