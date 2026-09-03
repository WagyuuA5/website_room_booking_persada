import os

path = 'booking_room/Components/Pages/User/Beranda.razor'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

# Add available / pending modals to the end of the file
modals = """
<!-- UI-09 Modal Tersedia -->
<AvailableRoomsModal Visible="_isAvailableRoomsOpen" VisibleChanged="v => _isAvailableRoomsOpen = v" />
<!-- UI-10 Modal Menunggu Persetujuan -->
<PendingApprovalsModal Visible="_isPendingOpen" VisibleChanged="v => _isPendingOpen = v" />
"""

if "<AvailableRoomsModal" not in content:
    content = content.replace("</style>", "</style>\n" + modals)

if "private bool _isAvailableRoomsOpen;" not in content:
    content = content.replace("@code {", """@code {
    private bool _isAvailableRoomsOpen;
    private bool _isPendingOpen;
""")

# Look for stat cards grid to insert UI-07 and UI-08
# Actually, I can just append them after the hero card.
if "card-tersedia-berikutnya" not in content:
    new_cards = """
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 16px; margin-top: 24px;">
            <div class="stat-highlight-card card-tersedia-berikutnya" @onclick="() => _isAvailableRoomsOpen = true" style="cursor:pointer; background: var(--color-white); border: 1px solid var(--color-neutral-200); border-radius: var(--radius-md); padding: 20px;">
                <h4 style="margin:0 0 8px 0; color: var(--color-navy); font-weight:700;">Tersedia Berikutnya</h4>
                <p style="margin:0; font-size:14px; color: var(--color-neutral-600);">Lihat ruangan yang bisa langsung dipesan sekarang.</p>
            </div>
            <div class="stat-highlight-card card-menunggu-persetujuan" @onclick="() => _isPendingOpen = true" style="cursor:pointer; background: var(--color-white); border: 1px solid var(--color-neutral-200); border-radius: var(--radius-md); padding: 20px;">
                <h4 style="margin:0 0 8px 0; color: var(--color-warning); font-weight:700;">Menunggu Persetujuan</h4>
                <p style="margin:0; font-size:14px; color: var(--color-neutral-600);">2 reservasi Anda sedang menunggu konfirmasi admin.</p>
            </div>
        </div>
"""
    content = content.replace('</button>\n            </div>\n        </div>', '</button>\n            </div>\n        </div>' + new_cards)

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)
print("Beranda.razor updated for UI-07, UI-08, UI-09, UI-10.")
