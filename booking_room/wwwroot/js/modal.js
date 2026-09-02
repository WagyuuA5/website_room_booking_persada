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
