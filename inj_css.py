import os

css = """
/* UI-16: Invitation Modal */
.invitation-header {
    background: var(--color-navy, #0F172A);
    color: var(--color-white, #FFFFFF);
    padding: 16px 20px;
    display: flex;
    align-items: center;
    gap: 12px;
}
.invitation-header h2 {
    margin: 0;
    font-size: var(--fs-h3, 20px);
    font-weight: var(--fw-bold, 700);
}
.invitation-body {
    padding: 24px;
}
.meeting-title {
    font-size: var(--fs-h2, 24px);
    font-weight: var(--fw-bold, 700);
    margin: 0 0 12px 0;
    color: var(--color-navy, #0F172A);
}
body.dark-mode .meeting-title { color: var(--color-white, #FFFFFF); }
.inviter-row {
    display: flex;
    align-items: center;
    gap: 10px;
    margin-bottom: 24px;
    font-size: var(--fs-sm, 14px);
    color: var(--color-neutral-600, #6E6E73);
}
.inviter-avatar {
    width: 24px;
    height: 24px;
    background: var(--color-primary, #F5A623);
    color: var(--color-white, #FFFFFF);
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-weight: var(--fw-bold, 700);
    font-size: 12px;
}
.meeting-details-box {
    background: linear-gradient(135deg, var(--color-neutral-100), transparent);
    border: 1px solid var(--color-neutral-200);
    border-radius: var(--radius-md, 14px);
    padding: 16px;
    display: flex;
    flex-direction: column;
    gap: 12px;
}
body.dark-mode .meeting-details-box {
    background: linear-gradient(135deg, rgba(255,255,255,0.05), transparent);
    border-color: rgba(255,255,255,0.1);
}
.detail-row {
    display: flex;
    align-items: center;
    gap: 12px;
    font-size: var(--fs-base, 16px);
    color: var(--color-neutral-900, #1D1D1F);
}
body.dark-mode .detail-row { color: var(--color-white, #FFFFFF); }
.detail-row svg {
    color: var(--color-neutral-400);
}
.invitation-footer {
    padding: 0 24px 24px 24px;
    display: flex;
    flex-direction: column;
    gap: 12px;
}
.full-width {
    width: 100%;
    justify-content: center;
    display: flex;
    align-items: center;
    gap: 8px;
}
.secondary-actions {
    display: flex;
    gap: 12px;
    justify-content: space-between;
}
.btn-outline-pill {
    flex: 1;
    height: 40px;
    border-radius: var(--radius-full);
    border: 1px solid var(--color-neutral-400);
    background: transparent;
    color: var(--color-neutral-900);
    font-weight: var(--fw-semibold, 600);
    cursor: pointer;
    transition: var(--motion-fast);
}
body.dark-mode .btn-outline-pill { color: var(--color-white); }
.btn-outline-pill:hover { background: var(--color-neutral-100); }
body.dark-mode .btn-outline-pill:hover { background: rgba(255,255,255,0.1); }
.btn-text-muted {
    flex: 1;
    height: 40px;
    border: none;
    background: transparent;
    color: var(--color-neutral-600);
    font-weight: var(--fw-semibold, 600);
    cursor: pointer;
}
.btn-text-muted:hover { color: var(--color-danger); }

/* Common Modal Parts */
.custom-modal-header {
    display: flex;
    gap: 16px;
    padding: 24px 24px 0 24px;
}
.header-icon-wrap {
    width: 48px;
    height: 48px;
    background: var(--color-neutral-100);
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    color: var(--color-neutral-600);
}
body.dark-mode .header-icon-wrap {
    background: rgba(255,255,255,0.1);
    color: var(--color-neutral-400);
}
.header-titles {
    display: flex;
    flex-direction: column;
    justify-content: center;
}
.header-titles h3 {
    margin: 0;
    font-size: var(--fs-h3, 20px);
    font-weight: var(--fw-bold, 700);
    color: var(--color-navy, #0F172A);
}
body.dark-mode .header-titles h3 { color: var(--color-white); }
.header-titles .sub {
    font-size: var(--fs-sm, 14px);
    color: var(--color-neutral-600);
    display: flex;
    align-items: center;
    gap: 6px;
    margin-top: 4px;
}
.modal-body-pad {
    padding: 24px;
}
.info-box-amber {
    background: rgba(245, 158, 11, 0.1);
    border-radius: var(--radius-sm, 8px);
    padding: 12px 16px;
    display: flex;
    gap: 12px;
    color: var(--color-warning, #F59E0B);
    font-size: var(--fs-sm, 14px);
    line-height: var(--lh-sm, 20px);
}
.info-box-amber p { margin: 0; color: var(--color-neutral-900); }
body.dark-mode .info-box-amber p { color: var(--color-white); }
.modal-footer-2btn {
    padding: 16px 24px;
    border-top: 1px solid var(--color-neutral-200);
    display: flex;
    justify-content: space-between;
}
body.dark-mode .modal-footer-2btn { border-color: rgba(255,255,255,0.1); }
"""

path = 'booking_room/wwwroot/app.css'
with open(path, 'a', encoding='utf-8') as f: f.write(css)
print("Injected CSS")
