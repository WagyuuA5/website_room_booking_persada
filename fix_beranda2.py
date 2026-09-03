import os

path = 'booking_room/Components/Pages/User/Beranda.razor'
with open(path, 'r', encoding='utf-8') as f: content = f.read()

start_idx = content.find('<div class="hero-quick-actions">')
end_idx = content.find('<div class="dashboard-main-columns">')

if start_idx != -1 and end_idx != -1:
    hero_replacement = """<div class="hero-quick-actions">
                <button class="btn-hero-action primary" @onclick='() => Navigation.NavigateTo("/bookings")'>
                    <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                        <rect x="3" y="4" width="18" height="18" rx="2"></rect>
                        <line x1="16" y1="2" x2="16" y2="6"></line>
                        <line x1="8" y1="2" x2="8" y2="6"></line>
                        <line x1="3" y1="10" x2="21" y2="10"></line>
                    </svg>
                    <span>Pesan Ruangan</span>
                </button>
                <button class="btn-hero-action secondary" @onclick='() => Navigation.NavigateTo("/status")'>
                    <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                        <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path>
                        <polyline points="14 2 14 8 20 8"></polyline>
                        <line x1="16" y1="13" x2="8" y2="13"></line>
                        <line x1="16" y1="17" x2="8" y2="17"></line>
                        <polyline points="10 9 9 9 8 9"></polyline>
                    </svg>
                    <span>Status Saya</span>
                </button>
            </div>
        </div>

        <div class="summary-cards-row">
            <!-- DASH-01: Ruangan Tersedia -->
            <div class="summary-card" @onclick="() => _isAvailableRoomsOpen = true">
                <div class="card-icon-wrap bg-green-light">
                    <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"></path></svg>
                </div>
                <div class="card-text-col">
                    <span class="card-label">RUANGAN TERSEDIA</span>
                    <div class="card-value-row">
                        <span class="value-large">8</span>
                        <span class="value-total">/ 20</span>
                    </div>
                </div>
            </div>

            <!-- UI-08: Menunggu Persetujuan -->
            <div class="summary-card interactive" @onclick="() => _isPendingOpen = true">
                <div class="card-icon-wrap bg-amber-light">
                    <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><circle cx="12" cy="14" r="3"></circle></svg>
                </div>
                <div class="card-text-col">
                    <span class="card-label">MENUNGGU PERSETUJUAN</span>
                    <span class="value-large">3</span>
                    <span class="card-desc">Permintaan pemesanan menunggu tindakan</span>
                </div>
                <svg class="chevron-icon" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="9 18 15 12 9 6"></polyline></svg>
            </div>

            <!-- UI-07: Tersedia Berikutnya -->
            <div class="summary-card dark-accent" @onclick="() => _isAvailableRoomsOpen = true">
                <div class="card-top-row">
                    <div class="card-icon-wrap bg-green-accent">
                        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"></polygon></svg>
                    </div>
                    <span class="pill-badge green-pill">TERSEDIA DALAM 45 MENIT</span>
                </div>
                <div class="card-text-col mt-2">
                    <span class="card-label">Tersedia Berikutnya</span>
                    <span class="value-large text-white">Delta Boardroom</span>
                    <span class="card-desc text-gray">Kapasitas: 20</span>
                </div>
                <button class="btn-primary btn-sm mt-3" style="width: 100%; border-radius: 999px;">Pesan Instan</button>
            </div>
        </div>

        """
    content = content[:start_idx] + hero_replacement + content[end_idx:]
    with open(path, 'w', encoding='utf-8') as f: f.write(content)
    print("Updated Beranda.razor")
else:
    print("Could not find start or end index.")
