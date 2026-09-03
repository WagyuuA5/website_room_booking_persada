import os

css_path = 'booking_room/wwwroot/app.css'
if os.path.exists('booking_room/wwwroot/css/design-tokens.css'):
    css_path = 'booking_room/wwwroot/css/design-tokens.css'

with open(css_path, 'r', encoding='utf-8') as f:
    content = f.read()

new_tokens = """
    /* Design System Final (PERSADA + Apple Neutrals) */
    --color-primary: #F5A623;
    --color-primary-dark: #D98E12;
    --color-navy: #0F172A;
    --color-neutral-900: #1D1D1F;
    --color-neutral-600: #6E6E73;
    --color-neutral-400: #86868B;
    --color-neutral-200: #E8E8ED;
    --color-neutral-100: #F5F5F7;
    --color-white: #FFFFFF;
    
    --color-success: #34D399;
    --color-warning: #F59E0B;
    --color-danger: #EF4444;
    --color-info: #3B82F6;

    /* Typography Scale */
    --fs-h1: 32px; --lh-h1: 40px;
    --fs-h2: 24px; --lh-h2: 30px;
    --fs-h3: 20px; --lh-h3: 26px;
    --fs-h4: 18px; --lh-h4: 24px;
    --fs-body: 16px; --lh-body: 24px;
    --fs-sm: 14px; --lh-sm: 20px;
    --fs-xs: 12px; --lh-xs: 16px;
    
    --fw-regular: 400;
    --fw-medium: 500;
    --fw-semibold: 600;
    --fw-bold: 700;
    --fw-extrabold: 800;

    /* Border Radius */
    --radius-sm: 8px;
    --radius-md: 14px;
    --radius-lg: 22px;
    --radius-full: 999px;

    /* Motion */
    --motion-fast: 150ms ease-out;
    --motion-base: 250ms cubic-bezier(0.4, 0, 0.2, 1);
    --motion-slow: 400ms ease-in-out;
    --motion-chart: 900ms ease-out;
"""
if "--color-neutral-900" not in content:
    content = content.replace(":root {", ":root {\n" + new_tokens)
    with open(css_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Tokens added.")
else:
    print("Tokens already exist.")
