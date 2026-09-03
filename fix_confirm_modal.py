import os

path = 'booking_room/Components/Shared/ConfirmBookingModal.razor'
new_content = """@namespace booking_room.Components.Shared
@using booking_room.Components.Models

<AppModal Visible="@Visible" VisibleChanged="HandleVisibleChanged" Title="Konfirmasi Pemesanan" Size="lg">
    <BodyContent>
        <div class="confirm-booking-layout">
            <div class="form-section">
                <label class="form-label">RUANGAN TERPILIH</label>
                <div class="room-selector-card">
                    <img src="@Room?.PhotoUrl" alt="@Room?.Name" class="mini-thumb" />
                    <div>
                        <h4 style="margin:0 0 4px 0;">@Room?.Name</h4>
                        <p style="margin:0; font-size:12px; color:var(--color-neutral-600);">Kapasitas @Room?.Capacity org • @Room?.Floor</p>
                    </div>
                    <button class="btn-text-link" style="margin-left:auto;">GANTI RUANGAN</button>
                </div>
            </div>

            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 16px;">
                <div class="form-section">
                    <label class="form-label">JADWAL</label>
                    <input type="date" class="form-input" />
                </div>
                <div class="form-section">
                    <label class="form-label">WAKTU</label>
                    <div style="display:flex; gap:8px;">
                        <input type="time" class="form-input" style="flex:1;" />
                        <span style="align-self:center;">-</span>
                        <input type="time" class="form-input" style="flex:1;" />
                    </div>
                </div>
            </div>
            
            <div class="conflict-alert" style="display:none;">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><line x1="12" y1="8" x2="12" y2="12"></line><line x1="12" y1="16" x2="12.01" y2="16"></line></svg>
                <span>Jadwal bentrok dengan "Meeting BOD" (10:00 - 11:30)</span>
            </div>

            <div class="form-section">
                <label class="form-label">KAPASITAS PESERTA</label>
                <input type="number" class="form-input" @bind="_participants" @bind:event="oninput" style="margin-bottom:8px;" />
                <div class="progress-bar-bg">
                    <div class="progress-bar-fill @(CapacityPercentage > 100 ? "danger" : "normal")" style="width: @(Math.Min(CapacityPercentage, 100))%"></div>
                </div>
                <p style="margin:4px 0 0 0; font-size:12px; color:var(--color-neutral-600);">@_participants / @(Room?.Capacity ?? 0) Peserta</p>
            </div>
            
            <div class="form-section" style="display:flex; align-items:center; gap:12px;">
                <input type="checkbox" id="externalGuests" />
                <label for="externalGuests" style="font-size:14px; margin:0; cursor:pointer;">Undang Tamu Eksternal (Di luar Persada)</label>
            </div>
            
            <div class="form-section">
                <label class="form-label">CATATAN TAMBAHAN</label>
                <textarea class="form-input" rows="3" placeholder="Tuliskan jika butuh tambahan kursi atau konsumsi..."></textarea>
            </div>
        </div>
    </BodyContent>
    <FooterContent>
        <button class="btn-secondary" @onclick="Back">Batal</button>
        <button class="btn-primary" @onclick="Confirm">Konfirmasi Pemesanan</button>
    </FooterContent>
</AppModal>

<style>
    .confirm-booking-layout { display: flex; flex-direction: column; gap: 20px; }
    .form-section { display: flex; flex-direction: column; gap: 6px; }
    .form-label { font-size: 12px; font-weight: 600; color: var(--color-neutral-600); }
    .form-input {
        padding: 10px 12px;
        border: 1px solid var(--color-neutral-200);
        border-radius: var(--radius-sm);
        background: transparent;
        color: var(--color-navy);
        font-size: 14px;
        width: 100%;
        box-sizing: border-box;
    }
    body.dark-mode .form-input { color: var(--color-white); border-color: rgba(255,255,255,0.1); }
    .room-selector-card {
        display: flex;
        align-items: center;
        gap: 12px;
        padding: 12px;
        border: 1px solid var(--color-neutral-200);
        border-radius: var(--radius-sm);
    }
    body.dark-mode .room-selector-card { border-color: rgba(255,255,255,0.1); }
    .mini-thumb { width: 48px; height: 48px; border-radius: 8px; object-fit: cover; }
    .progress-bar-bg { height: 6px; background: var(--color-neutral-200); border-radius: 3px; overflow: hidden; }
    .progress-bar-fill { height: 100%; transition: width 0.3s; }
    .progress-bar-fill.normal { background: var(--color-primary); }
    .progress-bar-fill.danger { background: var(--color-danger); }
</style>

@code {
    [Parameter] public bool Visible { get; set; } = true;
    [Parameter] public EventCallback<bool> VisibleChanged { get; set; }
    [Parameter] public RoomItem? Room { get; set; }
    [Parameter] public EventCallback OnBack { get; set; }
    [Parameter] public EventCallback OnConfirm { get; set; }
    
    private int _participants = 4;
    private int CapacityPercentage => Room?.Capacity > 0 ? (int)((_participants / (double)Room.Capacity) * 100) : 0;

    private async Task HandleVisibleChanged(bool value) { Visible = value; await VisibleChanged.InvokeAsync(value); }
    private async Task Back() { await HandleVisibleChanged(false); if (OnBack.HasDelegate) await OnBack.InvokeAsync(); }
    private async Task Confirm() { await HandleVisibleChanged(false); if (OnConfirm.HasDelegate) await OnConfirm.InvokeAsync(); }
}
"""
with open(path, 'w', encoding='utf-8') as f:
    f.write(new_content)
print("ConfirmBookingModal.razor updated.")
