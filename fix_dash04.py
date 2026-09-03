import os

css = """
/* DASH-04 & DS-10, DS-11: Upcoming Meetings Refinement */
.upcoming-item-row {
    display: flex;
    align-items: center;
    gap: 16px;
    padding: 14px 16px;
    background: var(--color-neutral-100, #F5F5F7);
    border: 1px solid var(--color-neutral-200, #E8E8ED);
    border-radius: var(--radius-md, 14px);
    cursor: pointer;
    transition: var(--motion-fast);
}
.upcoming-item-row:hover {
    background: var(--color-white, #FFFFFF);
    border-color: var(--color-neutral-400);
    box-shadow: 0 4px 12px rgba(0,0,0,0.05);
    transform: translateY(-2px);
}
body.dark-mode .upcoming-item-row {
    background: rgba(255,255,255,0.05);
    border-color: rgba(255,255,255,0.1);
}
body.dark-mode .upcoming-item-row:hover {
    background: rgba(255,255,255,0.08);
}
.item-time-box .time-sub {
    font-size: var(--fs-xs, 12px);
    font-weight: var(--fw-semibold, 600);
}
.item-content-box .item-title {
    font-weight: var(--fw-bold, 700);
}
"""

path = 'booking_room/wwwroot/app.css'
with open(path, 'a', encoding='utf-8') as f: f.write(css)

print("Updated upcoming-item-row CSS")
