import os

css = """
/* DASH-01 & UI-07/08: Summary Cards Row */
.summary-cards-row {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 16px;
    margin-bottom: 24px;
}
@media (max-width: 1024px) {
    .summary-cards-row { grid-template-columns: 1fr; }
}
.summary-card {
    background: var(--color-white, #FFFFFF);
    border: 1px solid var(--color-neutral-200, #E8E8ED);
    border-radius: var(--radius-md, 14px);
    padding: 20px;
    display: flex;
    flex-direction: column;
    position: relative;
    box-shadow: 0 2px 8px rgba(0,0,0,0.02);
    transition: var(--motion-fast);
}
body.dark-mode .summary-card {
    background: var(--color-neutral-900, #1D1D1F);
    border-color: rgba(255,255,255,0.1);
}
.summary-card.interactive {
    cursor: pointer;
}
.summary-card.interactive:hover {
    transform: translateY(-2px);
    box-shadow: 0 4px 12px rgba(0,0,0,0.05);
}
.card-icon-wrap {
    width: 40px;
    height: 40px;
    border-radius: 10px;
    display: flex;
    align-items: center;
    justify-content: center;
    margin-bottom: 12px;
}
.bg-green-light { background: rgba(52, 211, 153, 0.15); color: var(--color-success); }
.bg-amber-light { background: rgba(245, 158, 11, 0.15); color: var(--color-warning); }
.card-text-col {
    display: flex;
    flex-direction: column;
}
.card-label {
    font-size: var(--fs-xs, 12px);
    font-weight: var(--fw-semibold, 600);
    color: var(--color-neutral-600);
    letter-spacing: 0.04em;
    margin-bottom: 4px;
}
.card-value-row {
    display: flex;
    align-items: baseline;
    gap: 4px;
}
.value-large {
    font-size: var(--fs-h1, 32px);
    font-weight: 800;
    color: var(--color-navy);
    line-height: 1;
}
body.dark-mode .value-large { color: var(--color-white); }
.value-total {
    font-size: var(--fs-h3, 20px);
    font-weight: 800;
    color: var(--color-neutral-400);
}
.card-desc {
    font-size: var(--fs-sm, 14px);
    color: var(--color-neutral-600);
    margin-top: 4px;
}
.chevron-icon {
    position: absolute;
    bottom: 20px;
    right: 20px;
    color: var(--color-neutral-400);
}
/* UI-07 Dark Accent Card */
.summary-card.dark-accent {
    background: var(--color-navy);
    border-color: var(--color-navy);
    border-left: 4px solid var(--color-success);
}
body.dark-mode .summary-card.dark-accent {
    background: var(--color-neutral-900);
    border-color: rgba(255,255,255,0.1);
}
.summary-card.dark-accent .text-white { color: var(--color-white); }
.summary-card.dark-accent .text-gray { color: var(--color-neutral-400); }
.card-top-row {
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
}
.bg-green-accent { background: rgba(52, 211, 153, 0.2); color: var(--color-success); }
.pill-badge {
    padding: 4px 10px;
    border-radius: var(--radius-full);
    font-size: 10px;
    font-weight: 700;
    letter-spacing: 0.05em;
    text-transform: uppercase;
}
.green-pill {
    background: rgba(52, 211, 153, 0.15);
    color: var(--color-success);
}
.btn-sm { padding: 6px 12px; font-size: var(--fs-sm, 14px); height: auto; }
.mt-2 { margin-top: 8px; }
.mt-3 { margin-top: 12px; }
"""

path = 'booking_room/wwwroot/app.css'
with open(path, 'a', encoding='utf-8') as f: f.write(css)
print("Injected CSS for Dashboard Cards")
