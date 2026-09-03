import os

path1 = 'booking_room/Components/Shared/HistoryBookingDetailModal.razor'
with open(path1, 'w', encoding='utf-8') as f:
    f.write("""@namespace booking_room.Components.Shared
<AppModal Visible="@Visible" VisibleChanged="HandleVisibleChanged" Title="Detail Riwayat" Size="md">
    <BodyContent>
        <div style="display:flex; flex-direction:column; gap:12px;">
            <p>Informasi lengkap mengenai pemesanan sebelumnya.</p>
        </div>
    </BodyContent>
    <FooterContent>
        <button class="btn-secondary" @onclick="Close" style="padding:8px 16px; background:transparent; border:1px solid var(--color-neutral-400); border-radius:var(--radius-full); cursor:pointer;">Tutup</button>
    </FooterContent>
</AppModal>

@code {
    [Parameter] public bool Visible { get; set; }
    [Parameter] public EventCallback<bool> VisibleChanged { get; set; }
    [Parameter] public dynamic? Booking { get; set; }
    private async Task HandleVisibleChanged(bool value) { Visible = value; await VisibleChanged.InvokeAsync(value); }
    private async Task Close() { await HandleVisibleChanged(false); }
}
""")

path2 = 'booking_room/Components/Shared/DatePickerPopup.razor'
with open(path2, 'w', encoding='utf-8') as f:
    f.write("""@namespace booking_room.Components.Shared
<AppModal Visible="@Visible" VisibleChanged="HandleVisibleChanged" Title="Pilih Tanggal" Size="sm">
    <BodyContent>
        <div style="display:flex; flex-direction:column; gap:12px;">
            <input type="date" style="padding:8px; border:1px solid var(--color-neutral-200); border-radius:var(--radius-sm); width: 100%;" />
        </div>
    </BodyContent>
    <FooterContent>
        <button class="btn-primary" @onclick="Close" style="padding:8px 16px; background:var(--color-primary); color:var(--color-navy); border:none; border-radius:var(--radius-full); cursor:pointer;">Terapkan</button>
    </FooterContent>
</AppModal>

@code {
    [Parameter] public bool Visible { get; set; }
    [Parameter] public EventCallback<bool> VisibleChanged { get; set; }
    private async Task HandleVisibleChanged(bool value) { Visible = value; await VisibleChanged.InvokeAsync(value); }
    private async Task Close() { await HandleVisibleChanged(false); }
}
""")
print("Created History Modals.")
