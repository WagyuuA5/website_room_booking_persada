import os

path = 'booking_room/Components/Shared/BookingAutoReleasedModal.razor'
markup = """@namespace booking_room.Components.Shared
@using booking_room.Components.Models
@inject NavigationManager Nav

<AppModal Visible="@Visible" VisibleChanged="HandleVisibleChanged" Size="md" ShowHeader="false" ShowFooter="false">
    <BodyContent>
        <div class="modal-body-pad text-center">
            <div class="warning-icon-large">
                <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M10.29 3.86L1.82 18a2 2 0 0 0 1.71 3h16.94a2 2 0 0 0 1.71-3L13.71 3.86a2 2 0 0 0-3.42 0z"></path><line x1="12" y1="9" x2="12" y2="13"></line><line x1="12" y1="17" x2="12.01" y2="17"></line></svg>
            </div>
            <span class="label-system-warning">PERINGATAN SISTEM</span>
            <h2 class="auto-release-title">Pemesanan Otomatis Dilepas</h2>
            
            <div class="badge-no-show">
                <div class="status-dot-red"></div>
                Tidak Hadir
            </div>

            <p class="auto-release-desc">
                Pemesanan Anda untuk <strong>@RoomName</strong> telah dibatalkan secara otomatis karena jendela check-in telah berakhir. Ruangan kini tersedia untuk pengguna lain.
            </p>

            <div class="key-value-box">
                <div class="kv-row">
                    <span class="kv-key">Ruangan</span>
                    <span class="kv-value">@RoomName</span>
                </div>
                <div class="kv-row">
                    <span class="kv-key">Waktu Awal</span>
                    <span class="kv-value">@Time</span>
                </div>
                <div class="kv-row">
                    <span class="kv-key">Tanggal</span>
                    <span class="kv-value">Hari ini, @Date</span>
                </div>
            </div>
        </div>

        <div class="modal-footer-2btn">
            <button class="btn-outline-pill" @onclick="GoToHistory">Lihat Riwayat</button>
            <button class="btn-primary" @onclick="NewBooking">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="12" y1="5" x2="12" y2="19"></line><line x1="5" y1="12" x2="19" y2="12"></line></svg>
                Booking Baru
            </button>
        </div>
    </BodyContent>
</AppModal>

@code {
    [Parameter] public bool Visible { get; set; }
    [Parameter] public EventCallback<bool> VisibleChanged { get; set; }
    [Parameter] public string RoomName { get; set; } = "Alpha Boardroom";
    [Parameter] public string Time { get; set; } = "09:00 - 11:30";
    [Parameter] public string Date { get; set; } = "12 Mei 2024";

    private async Task HandleVisibleChanged(bool val)
    {
        Visible = val;
        await VisibleChanged.InvokeAsync(val);
    }

    private void GoToHistory()
    {
        Nav.NavigateTo("/history");
    }

    private void NewBooking()
    {
        Nav.NavigateTo("/bookings");
    }
}
"""
with open(path, 'w', encoding='utf-8') as f: f.write(markup)

css = """
/* UI-17: Auto Released Modal */
.text-center { text-align: center; }
.warning-icon-large {
    width: 64px;
    height: 64px;
    background: rgba(239, 68, 68, 0.1);
    color: var(--color-danger, #EF4444);
    border-radius: 50%;
    display: inline-flex;
    align-items: center;
    justify-content: center;
    margin-bottom: 16px;
}
.label-system-warning {
    display: block;
    font-size: var(--fs-xs, 12px);
    font-weight: var(--fw-bold, 700);
    color: var(--color-danger, #EF4444);
    letter-spacing: 0.05em;
    margin-bottom: 8px;
}
.auto-release-title {
    margin: 0 0 16px 0;
    font-size: var(--fs-h2, 24px);
    font-weight: var(--fw-bold, 700);
    color: var(--color-navy, #0F172A);
}
body.dark-mode .auto-release-title { color: var(--color-white); }
.badge-no-show {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    background: rgba(239, 68, 68, 0.1);
    color: var(--color-danger, #EF4444);
    padding: 6px 16px;
    border-radius: var(--radius-full, 999px);
    font-size: var(--fs-sm, 14px);
    font-weight: var(--fw-semibold, 600);
    margin-bottom: 24px;
}
.status-dot-red {
    width: 8px;
    height: 8px;
    background: var(--color-danger, #EF4444);
    border-radius: 50%;
}
.auto-release-desc {
    font-size: var(--fs-base, 16px);
    color: var(--color-neutral-600, #6E6E73);
    margin-bottom: 24px;
    line-height: var(--lh-base, 24px);
}
body.dark-mode .auto-release-desc { color: var(--color-neutral-400); }
.key-value-box {
    background: var(--color-neutral-100, #F5F5F7);
    border-radius: var(--radius-md, 14px);
    padding: 16px;
    display: flex;
    flex-direction: column;
    gap: 12px;
    text-align: left;
}
body.dark-mode .key-value-box { background: rgba(255,255,255,0.05); }
.kv-row {
    display: flex;
    justify-content: space-between;
    font-size: var(--fs-sm, 14px);
}
.kv-key { color: var(--color-neutral-600); }
.kv-value { 
    color: var(--color-neutral-900);
    font-weight: var(--fw-semibold, 600);
}
body.dark-mode .kv-value { color: var(--color-white); }
"""
path = 'booking_room/wwwroot/app.css'
with open(path, 'a', encoding='utf-8') as f: f.write(css)

print("Created BookingAutoReleasedModal")
