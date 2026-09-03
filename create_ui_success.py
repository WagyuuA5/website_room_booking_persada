import os

path = 'booking_room/Components/Shared/CheckInSuccessModal.razor'
markup = """@namespace booking_room.Components.Shared

<AppModal Visible="@Visible" VisibleChanged="HandleVisibleChanged" Size="sm" ShowHeader="false" ShowFooter="false">
    <BodyContent>
        <div class="modal-body-pad text-center checkin-success-modal">
            <div class="success-icon-large">
                <svg width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"></polyline></svg>
            </div>
            
            <h2 class="success-title">Check-in Berhasil</h2>
            <p class="success-sub">pukul @DateTime.Now.ToString("HH:mm")</p>

            <button class="btn-primary" style="width: 100%; margin-top: 24px;" @onclick="Close">
                Tutup
            </button>
        </div>
    </BodyContent>
</AppModal>

@code {
    [Parameter] public bool Visible { get; set; }
    [Parameter] public EventCallback<bool> VisibleChanged { get; set; }

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
/* DASH-03d: CheckIn Success Modal */
.checkin-success-modal {
    background: var(--color-navy);
    color: var(--color-white);
    border-radius: var(--radius-lg);
    margin: -24px; /* override AppModal default padding if necessary */
    padding: 32px 24px;
}
.success-icon-large {
    width: 80px;
    height: 80px;
    background: rgba(52, 211, 153, 0.15);
    color: var(--color-success);
    border-radius: 50%;
    display: inline-flex;
    align-items: center;
    justify-content: center;
    margin-bottom: 24px;
}
.success-title {
    font-size: var(--fs-h2, 24px);
    font-weight: var(--fw-bold, 700);
    margin: 0 0 8px 0;
}
.success-sub {
    font-size: var(--fs-base, 16px);
    color: var(--color-neutral-400);
    margin: 0;
}
"""
path = 'booking_room/wwwroot/app.css'
with open(path, 'a', encoding='utf-8') as f: f.write(css)

print("Created CheckInSuccessModal")
