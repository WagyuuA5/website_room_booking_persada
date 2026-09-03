import os

path = 'booking_room/Components/Shared/InvitationModal.razor'
markup = """@namespace booking_room.Components.Shared
@using booking_room.Components.Models
@inject booking_room.Services.ToastService Toast

<AppModal Visible="@Visible" VisibleChanged="HandleVisibleChanged" Size="md" ShowHeader="false" ShowFooter="false" NoPadding="true">
    <BodyContent>
        <div class="invitation-header">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="4" width="18" height="18" rx="2" ry="2"></rect><line x1="16" y1="2" x2="16" y2="6"></line><line x1="8" y1="2" x2="8" y2="6"></line><line x1="3" y1="10" x2="21" y2="10"></line></svg>
            <h2>Undangan</h2>
        </div>

        <div class="invitation-body">
            <h3 class="meeting-title">@MeetingTitle</h3>
            <div class="inviter-row">
                <div class="inviter-avatar">@InviterName.Substring(0,1)</div>
                <span>Diundang oleh <strong>@InviterName</strong></span>
            </div>

            <div class="meeting-details-box">
                <div class="detail-row">
                    <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="4" width="18" height="18" rx="2" ry="2"></rect><line x1="16" y1="2" x2="16" y2="6"></line><line x1="8" y1="2" x2="8" y2="6"></line><line x1="3" y1="10" x2="21" y2="10"></line></svg>
                    <span>@Date</span>
                </div>
                <div class="detail-row">
                    <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><polyline points="12 6 12 12 16 14"></polyline></svg>
                    <span>@Time</span>
                </div>
                <div class="detail-row">
                    <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"></path><polyline points="9 22 9 12 15 12 15 22"></polyline></svg>
                    <span>@RoomName</span>
                </div>
            </div>
        </div>

        <div class="invitation-footer">
            <button class="btn-primary full-width" @onclick='() => Respond("Terima")'>
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"></polyline></svg>
                Terima
            </button>
            <div class="secondary-actions">
                <button class="btn-outline-pill" @onclick='() => Respond("Mungkin")'>Mungkin</button>
                <button class="btn-text-muted" @onclick='() => Respond("Tolak")'>Tolak</button>
            </div>
        </div>
    </BodyContent>
</AppModal>

@code {
    [Parameter] public bool Visible { get; set; }
    [Parameter] public EventCallback<bool> VisibleChanged { get; set; }
    [Parameter] public string MeetingTitle { get; set; } = "Sinkronisasi Strategi Q3";
    [Parameter] public string InviterName { get; set; } = "Budi Santoso";
    [Parameter] public string Date { get; set; } = "12 Mei 2024";
    [Parameter] public string Time { get; set; } = "09:00 - 11:30";
    [Parameter] public string RoomName { get; set; } = "Alpha Boardroom";

    private async Task HandleVisibleChanged(bool val)
    {
        Visible = val;
        await VisibleChanged.InvokeAsync(val);
    }

    private async Task Respond(string response)
    {
        Toast.Show($"Anda telah merespons: {response}", "info");
        await HandleVisibleChanged(false);
    }
}
"""
with open(path, 'w', encoding='utf-8') as f: f.write(markup)
print("Created InvitationModal")
