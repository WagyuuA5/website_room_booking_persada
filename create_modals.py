import os

path1 = 'booking_room/Components/Shared/AvailableRoomsModal.razor'
with open(path1, 'w', encoding='utf-8') as f:
    f.write("""@namespace booking_room.Components.Shared
<AppModal Visible="@Visible" VisibleChanged="HandleVisibleChanged" Title="Ruangan Tersedia Saat Ini" Size="md">
    <BodyContent>
        <div style="display:flex; flex-direction:column; gap:12px;">
            <div style="padding:16px; border:1px solid var(--color-neutral-200); border-radius:var(--radius-sm);">
                <h4 style="margin:0 0 4px 0;">Ruang Meeting A</h4>
                <p style="margin:0; font-size:12px; color:var(--color-neutral-600);">Kapasitas 8 orang • Lantai 2</p>
                <button class="btn-primary" style="margin-top:12px; font-size:12px; padding:6px 12px; border:none; border-radius:4px; background:var(--color-primary); color:var(--color-navy); cursor:pointer;">Pesan Instan</button>
            </div>
            <div style="padding:16px; border:1px solid var(--color-neutral-200); border-radius:var(--radius-sm);">
                <h4 style="margin:0 0 4px 0;">Ruang Diskusi C</h4>
                <p style="margin:0; font-size:12px; color:var(--color-neutral-600);">Kapasitas 4 orang • Lantai 3</p>
                <button class="btn-primary" style="margin-top:12px; font-size:12px; padding:6px 12px; border:none; border-radius:4px; background:var(--color-primary); color:var(--color-navy); cursor:pointer;">Pesan Instan</button>
            </div>
        </div>
    </BodyContent>
    <FooterContent>
        <button class="btn-secondary" @onclick="Close" style="padding:8px 16px; background:transparent; border:1px solid var(--color-neutral-400); border-radius:var(--radius-full); cursor:pointer;">Tutup</button>
    </FooterContent>
</AppModal>

@code {
    [Parameter] public bool Visible { get; set; }
    [Parameter] public EventCallback<bool> VisibleChanged { get; set; }
    private async Task HandleVisibleChanged(bool value) { Visible = value; await VisibleChanged.InvokeAsync(value); }
    private async Task Close() { await HandleVisibleChanged(false); }
}
""")

path2 = 'booking_room/Components/Shared/PendingApprovalsModal.razor'
with open(path2, 'w', encoding='utf-8') as f:
    f.write("""@namespace booking_room.Components.Shared
<AppModal Visible="@Visible" VisibleChanged="HandleVisibleChanged" Title="Menunggu Persetujuan" Size="md">
    <BodyContent>
        <div style="display:flex; flex-direction:column; gap:12px;">
            <div style="padding:16px; border:1px solid var(--color-warning); border-radius:var(--radius-sm); background:#FFFBEB;">
                <h4 style="margin:0 0 4px 0; color:var(--color-warning);">Auditorium Utama</h4>
                <p style="margin:0; font-size:12px; color:var(--color-neutral-600);">25 Okt 2026 • 09:00 - 12:00</p>
            </div>
        </div>
    </BodyContent>
    <FooterContent>
        <button class="btn-secondary" @onclick="Close" style="padding:8px 16px; background:transparent; border:1px solid var(--color-neutral-400); border-radius:var(--radius-full); cursor:pointer;">Tutup</button>
    </FooterContent>
</AppModal>

@code {
    [Parameter] public bool Visible { get; set; }
    [Parameter] public EventCallback<bool> VisibleChanged { get; set; }
    private async Task HandleVisibleChanged(bool value) { Visible = value; await VisibleChanged.InvokeAsync(value); }
    private async Task Close() { await HandleVisibleChanged(false); }
}
""")
print("Created AvailableRoomsModal and PendingApprovalsModal.")
