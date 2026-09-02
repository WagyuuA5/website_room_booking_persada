/**
 * SidebarDragHandle — V6 Dynamic Island
 * Menangani gesture drag di tepi kanan sidebar untuk resize real-time.
 */

(function () {
    'use strict';

    const SIDEBAR_STORAGE_KEY = 'sidebarWidthState';
    const SNAP_THRESHOLD = 0.4;
    const MIN_WIDTH = 60;
    const MAX_EXPANDED_WIDTH = 260;

    let isDragging = false;
    let startX = 0;
    let startWidth = 0;
    let sidebar = null;
    let mainContent = null;
    let currentWidth = MAX_EXPANDED_WIDTH;
    let onSnapCallback = null;

    function getElements() {
        sidebar = document.querySelector('.sidebar');
        mainContent = document.querySelector('.main-content');
        return sidebar && mainContent;
    }

    function loadSavedState() {
        try {
            const saved = localStorage.getItem(SIDEBAR_STORAGE_KEY);
            if (saved === 'collapsed') {
                return MIN_WIDTH;
            }
        } catch (e) { }
        return MAX_EXPANDED_WIDTH;
    }

    function saveState(width) {
        try {
            const state = width < MAX_EXPANDED_WIDTH * SNAP_THRESHOLD ? 'collapsed' : 'expanded';
            localStorage.setItem(SIDEBAR_STORAGE_KEY, state);
        } catch (e) { }
    }

    function applyWidth(width, animate) {
        if (!sidebar || !mainContent) getElements();
        if (!sidebar || !mainContent) return;

        width = Math.max(MIN_WIDTH, Math.min(MAX_EXPANDED_WIDTH * 1.1, width));
        currentWidth = width;

        document.documentElement.style.setProperty('--sidebar-width', width + 'px');

        if (animate) {
            sidebar.style.transition = 'width 0.35s cubic-bezier(0.34, 1.56, 0.64, 1), min-width 0.35s cubic-bezier(0.34, 1.56, 0.64, 1)';
            mainContent.style.transition = 'margin-left 0.35s cubic-bezier(0.34, 1.56, 0.64, 1), width 0.35s cubic-bezier(0.34, 1.56, 0.64, 1)';
        } else {
            sidebar.style.transition = 'none';
            mainContent.style.transition = 'none';
        }
        sidebar.style.width = width + 'px';
        sidebar.style.minWidth = width + 'px';
        sidebar.style.transform = 'none';
        sidebar.style.overflow = 'visible';

        mainContent.style.marginLeft = width + 'px';
        mainContent.style.width = `calc(100% - ${width}px)`;
    }

    function snapToNearest(width) {
        const threshold = MAX_EXPANDED_WIDTH * SNAP_THRESHOLD;
        if (width < threshold) {
            return MIN_WIDTH;
        }
        return MAX_EXPANDED_WIDTH;
    }

    function handleStart(clientX) {
        if (!getElements()) return;
        isDragging = true;
        startX = clientX;
        startWidth = currentWidth;
        document.body.style.userSelect = 'none';
        document.body.style.webkitUserSelect = 'none';
    }

    function handleMove(clientX) {
        if (!isDragging) return;
        const deltaX = clientX - startX;
        let newWidth = startWidth + deltaX;
        newWidth = Math.max(MIN_WIDTH, Math.min(MAX_EXPANDED_WIDTH * 1.1, newWidth));
        applyWidth(newWidth, false);
    }

    function handleEnd() {
        if (!isDragging) return;
        isDragging = false;
        document.body.style.userSelect = '';
        document.body.style.webkitUserSelect = '';
        const snapped = snapToNearest(currentWidth);
        applyWidth(snapped, true);
        saveState(snapped);

        if (onSnapCallback) {
            try {
                const result = onSnapCallback(snapped, snapped === MIN_WIDTH);
                if (result && result.then) {
                    result.catch(() => { });
                }
            } catch (e) { }
        }
    }

    // Mouse events
    document.addEventListener('mousedown', function (e) {
        const handle = e.target.closest('.sidebar-drag-handle');
        if (handle) {
            e.preventDefault();
            handleStart(e.clientX);
        }
    });

    document.addEventListener('mousemove', function (e) {
        if (isDragging) {
            e.preventDefault();
            handleMove(e.clientX);
        }
    });

    document.addEventListener('mouseup', function () {
        if (isDragging) handleEnd();
    });

    // Touch events
    document.addEventListener('touchstart', function (e) {
        const handle = e.target.closest('.sidebar-drag-handle');
        if (handle && e.touches.length === 1) {
            handleStart(e.touches[0].clientX);
        }
    }, { passive: true });

    document.addEventListener('touchmove', function (e) {
        if (isDragging && e.touches.length === 1) {
            handleMove(e.touches[0].clientX);
        }
    }, { passive: true });

    document.addEventListener('touchend', function () {
        if (isDragging) handleEnd();
    });

    // Expose for Blazor interop
    window.sidebarDragInit = function () {
        if (!getElements()) return { width: MAX_EXPANDED_WIDTH, isCollapsed: false };
        currentWidth = loadSavedState();
        const isCollapsed = currentWidth < MAX_EXPANDED_WIDTH * SNAP_THRESHOLD;
        applyWidth(currentWidth, false);
        return { width: currentWidth, isCollapsed: isCollapsed };
    };

    window.sidebarDragSetCallback = function (callback) {
        onSnapCallback = callback;
    };

    window.sidebarDragGetState = function () {
        return {
            width: currentWidth,
            isCollapsed: currentWidth < MAX_EXPANDED_WIDTH * SNAP_THRESHOLD
        };
    };

    window.sidebarDragExpand = function () {
        applyWidth(MAX_EXPANDED_WIDTH, true);
        saveState(MAX_EXPANDED_WIDTH);
        if (onSnapCallback) {
            try {
                const result = onSnapCallback(MAX_EXPANDED_WIDTH, false);
                if (result && result.then) result.catch(() => { });
            } catch (e) { }
        }
    };

    // Initialize on DOM ready
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', window.sidebarDragInit);
    } else {
        window.sidebarDragInit();
    }
})();
