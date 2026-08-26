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
