import os

css = """
:root {
    /* DS-11: Radius System */
    --radius-sm: 8px;
    --radius-md: 14px;
    --radius-lg: 22px;
    --radius-full: 999px;

    /* DS-10: Typography */
    --fs-h1: 32px;
    --fs-h2: 24px;
    --fs-h3: 20px;
    --fs-base: 16px;
    --fs-sm: 14px;
    --fs-xs: 12px;

    --fw-regular: 400;
    --fw-medium: 500;
    --fw-semibold: 600;
    --fw-bold: 700;

    /* DS-13 & DS-14: Motion & Transitions */
    --motion-fast: 150ms ease-out;
    --motion-base: 250ms ease-out;
    --motion-slow: 400ms cubic-bezier(0.4, 0, 0.2, 1);
    --motion-chart: 900ms cubic-bezier(0.16, 1, 0.3, 1);

    /* DS-09 & DS-12: Colors (Skedda/Robin/Apple style neutral) */
    --color-neutral-100: #F5F5F7;
    --color-neutral-200: #E8E8ED;
    --color-neutral-400: #86868B;
    --color-neutral-600: #515154;
    --color-neutral-900: #1D1D1F;
    
    --color-white: #FFFFFF;
    --color-navy: #0F172A;
    --color-primary: #0A84FF;
    --color-success: #34D399;
    --color-warning: #F59E0B;
    --color-danger: #EF4444;
    --color-info: #3B82F6;
}
"""

path = 'booking_room/wwwroot/app.css'
with open(path, 'r', encoding='utf-8') as f: content = f.read()

# Prepend the variables to the top of the file
with open(path, 'w', encoding='utf-8') as f: f.write(css + '\n' + content)
print("Injected Design System Tokens into app.css")
