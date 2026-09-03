import os

path = 'booking_room/Components/Shared/ScheduleDetailModal.razor'
markup = """@namespace booking_room.Components.Shared

<AppModal Visible="@Visible" VisibleChanged="HandleVisibleChanged" Size="md" ShowHeader="false" ShowFooter="false" NoPadding="true">
    <BodyContent>
        <div class="schedule-detail-header">
            <img src="https://images.unsplash.com/photo-1497366754888-5a456d4b3447?auto=format&fit=crop&w=600&q=80" alt="Room" class="schedule-img" />
            <div class="schedule-overlay">
                <span class="badge-status-green">Disetujui</span>
            </div>
        </div>
        <div class="modal-body-pad">
            <h2 class="schedule-title">@RoomName</h2>
            <div class="schedule-meta-list">
                <div class="meta-item">
                    <span class="meta-label">Pemesan</span>
                    <span class="meta-val">Andi Wijaya</span>
                </div>
                <div class="meta-item">
                    <span class="meta-label">Waktu</span>
                    <span class="meta-val">@Date, @Time</span>
                </div>
                <div class="meta-item">
                    <span class="meta-label">Fasilitas</span>
                    <span class="meta-val">AC, Proyektor, WiFi</span>
                </div>
                <div class="meta-item">
                    <span class="meta-label">Keperluan</span>
                    <span class="meta-val">Meeting Sinkronisasi Mingguan Tim IT</span>
                </div>
            </div>
        </div>
        <div class="modal-footer-2btn">
            <div style="flex: 1;"></div>
            <button class="btn-outline-pill" style="width: auto; padding: 0 32px;" @onclick="Close">Tutup</button>
        </div>
    </BodyContent>
</AppModal>

@code {
    [Parameter] public bool Visible { get; set; }
    [Parameter] public EventCallback<bool> VisibleChanged { get; set; }
    [Parameter] public string RoomName { get; set; } = "Executive Boardroom A";
    [Parameter] public string Date { get; set; } = "12 Okt 2023";
    [Parameter] public string Time { get; set; } = "10:00 - 11:30";

    private async Task HandleVisibleChanged(bool val)
    {
        Visible = val;
        await VisibleChanged.InvokeAsync(val);
    }

    private async Task Close()
    {
        await HandleVisibleChanged(false);
    }
}
"""
with open(path, 'w', encoding='utf-8') as f: f.write(markup)

css = """
/* UI-03: Schedule Detail Modal */
.schedule-detail-header {
    position: relative;
    height: 180px;
}
.schedule-img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    border-radius: var(--radius-lg, 22px) var(--radius-lg, 22px) 0 0;
}
.schedule-overlay {
    position: absolute;
    top: 16px;
    right: 16px;
}
.badge-status-green {
    background: var(--color-success);
    color: var(--color-white);
    padding: 6px 12px;
    border-radius: var(--radius-full);
    font-size: var(--fs-xs, 12px);
    font-weight: var(--fw-bold, 700);
}
.schedule-title {
    margin: 0 0 20px 0;
    font-size: var(--fs-h2, 24px);
    font-weight: var(--fw-bold, 700);
    color: var(--color-navy);
}
body.dark-mode .schedule-title { color: var(--color-white); }
.schedule-meta-list {
    display: flex;
    flex-direction: column;
    gap: 16px;
}
.meta-item {
    display: flex;
    flex-direction: column;
    gap: 4px;
}
.meta-item .meta-label {
    font-size: var(--fs-xs, 12px);
    font-weight: var(--fw-semibold, 600);
    color: var(--color-neutral-600);
    text-transform: uppercase;
    letter-spacing: 0.05em;
}
.meta-item .meta-val {
    font-size: var(--fs-base, 16px);
    color: var(--color-neutral-900);
}
body.dark-mode .meta-item .meta-val { color: var(--color-white); }
"""
path = 'booking_room/wwwroot/app.css'
with open(path, 'a', encoding='utf-8') as f: f.write(css)

print("Created ScheduleDetailModal")
