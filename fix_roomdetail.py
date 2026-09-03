import os

path = 'booking_room/Components/Shared/RoomDetailsModal.razor'
new_content = """@namespace booking_room.Components.Shared
@using booking_room.Components.Models

<AppModal Visible="@Visible" VisibleChanged="HandleVisibleChanged" Size="xl" ShowHeader="false" ShowFooter="false" NoPadding="true">
    <BodyContent>
        <div class="room-detail-layout">
            <!-- Kiri: Media -->
            <div class="detail-media-col">
                <div class="detail-photo-wrap">
                    <img src="@Room?.PhotoUrl" alt="@Room?.Name" class="detail-photo" />
                    <div class="room-status-badge @GetStatusBadgeClass(Room?.Status)">
                        <div class="status-dot"></div>
                        @GetStatusText(Room?.Status)
                    </div>
                </div>
                
                <!-- Peta Lokasi / Denah -->
                <div class="detail-map-panel">
                    <span class="map-label">Lantai @Room?.Floor, Sayap Utama, Persada HQ</span>
                    <div class="map-placeholder">
                        <svg width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="var(--color-neutral-400)" stroke-width="1.5">
                            <rect x="3" y="3" width="18" height="18" rx="2" ry="2"></rect>
                            <path d="M3 9h18M9 21V9"></path>
                        </svg>
                        <p>Denah lantai belum tersedia</p>
                    </div>
                </div>
            </div>

            <!-- Kanan: Info -->
            <div class="detail-info-col">
                <div class="info-content-scroll">
                    <h2 class="detail-title">@Room?.Name</h2>
                    <div class="detail-location">
                        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"></path><circle cx="12" cy="10" r="3"></circle></svg>
                        <span>Lantai @Room?.Floor, Sayap Utama, Persada HQ</span>
                    </div>
                    
                    <p class="detail-desc">@Room?.Description</p>
                    
                    <label class="section-label">FASILITAS TERMASUK</label>
                    <div class="amenities-grid">
                        @if (Room?.Amenities != null)
                        {
                            @foreach(var am in Room.Amenities)
                            {
                                <div class="amenity-item">
                                    <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"></polyline></svg>
                                    <span>@am</span>
                                </div>
                            }
                        }
                    </div>
                </div>
                
                <div class="detail-footer">
                    <button class="btn-secondary" @onclick="Close">Batal</button>
                    <button class="btn-primary" @onclick="Book">
                        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="4" width="18" height="18" rx="2" ry="2"></rect><line x1="16" y1="2" x2="16" y2="6"></line><line x1="8" y1="2" x2="8" y2="6"></line><line x1="3" y1="10" x2="21" y2="10"></line></svg>
                        Pesan Sekarang
                    </button>
                </div>
            </div>
        </div>
    </BodyContent>
</AppModal>

<style>
    .room-detail-layout {
        display: flex;
        min-height: 500px;
        background: var(--color-white, #FFFFFF);
    }
    body.dark-mode .room-detail-layout { background: var(--color-neutral-900, #1D1D1F); }

    .detail-media-col {
        width: 45%;
        display: flex;
        flex-direction: column;
        border-right: 1px solid var(--color-neutral-200, #E8E8ED);
    }
    body.dark-mode .detail-media-col { border-color: rgba(255,255,255,0.1); }

    .detail-photo-wrap {
        position: relative;
        height: 300px;
    }
    .detail-photo {
        width: 100%;
        height: 100%;
        object-fit: cover;
        border-top-left-radius: var(--radius-lg, 22px);
    }
    .room-status-badge {
        position: absolute;
        top: 16px;
        left: 16px;
        padding: 6px 12px;
        border-radius: var(--radius-full, 999px);
        font-size: var(--fs-xs, 12px);
        font-weight: var(--fw-semibold, 600);
        display: flex;
        align-items: center;
        gap: 6px;
        background: rgba(255, 255, 255, 0.95);
        backdrop-filter: blur(4px);
        color: var(--color-navy, #0F172A);
        box-shadow: 0 2px 8px rgba(0,0,0,0.1);
    }
    body.dark-mode .room-status-badge {
        background: rgba(30, 30, 30, 0.95);
        color: var(--color-white, #FFFFFF);
    }
    .status-dot { width: 8px; height: 8px; border-radius: 50%; }
    .badge-available .status-dot { background: var(--color-success, #34D399); }
    .badge-booked .status-dot { background: var(--color-warning, #F59E0B); }
    .badge-unavailable .status-dot { background: var(--color-danger, #EF4444); }

    .detail-map-panel {
        padding: 20px;
        flex: 1;
        display: flex;
        flex-direction: column;
        gap: 8px;
    }
    .map-label {
        font-size: var(--fs-xs, 12px);
        font-weight: var(--fw-semibold, 600);
        color: var(--color-neutral-600, #6E6E73);
    }
    .map-placeholder {
        flex: 1;
        background: var(--color-neutral-100, #F5F5F7);
        border: 1px dashed var(--color-neutral-200, #E8E8ED);
        border-radius: var(--radius-md, 14px);
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        gap: 8px;
        color: var(--color-neutral-400, #86868B);
        font-size: var(--fs-sm, 14px);
    }
    body.dark-mode .map-placeholder {
        background: rgba(255,255,255,0.05);
        border-color: rgba(255,255,255,0.1);
    }

    .detail-info-col {
        width: 55%;
        display: flex;
        flex-direction: column;
    }
    .info-content-scroll {
        padding: 32px;
        flex: 1;
        overflow-y: auto;
    }
    .detail-title {
        font-size: var(--fs-h1, 32px);
        line-height: var(--lh-h1, 40px);
        font-weight: var(--fw-bold, 700);
        color: var(--color-navy, #0F172A);
        margin: 0 0 8px 0;
    }
    body.dark-mode .detail-title { color: var(--color-white, #FFFFFF); }

    .detail-location {
        display: flex;
        align-items: center;
        gap: 6px;
        font-size: var(--fs-sm, 14px);
        font-weight: var(--fw-semibold, 600);
        color: var(--color-neutral-600, #6E6E73);
        margin-bottom: 20px;
    }
    .detail-desc {
        font-size: var(--fs-body, 16px);
        line-height: var(--lh-body, 24px);
        color: var(--color-neutral-600, #6E6E73);
        margin: 0 0 24px 0;
    }
    .section-label {
        font-size: var(--fs-xs, 12px);
        font-weight: var(--fw-semibold, 600);
        color: var(--color-neutral-600, #6E6E73);
        letter-spacing: 0.04em;
        margin-bottom: 12px;
        display: block;
    }

    .amenities-grid {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 12px;
    }
    .amenity-item {
        display: flex;
        align-items: center;
        gap: 8px;
        font-size: var(--fs-sm, 14px);
        color: var(--color-navy, #0F172A);
    }
    body.dark-mode .amenity-item { color: var(--color-white, #FFFFFF); }
    .amenity-item svg { color: var(--color-primary, #F5A623); }

    .detail-footer {
        padding: 20px 32px;
        border-top: 1px solid var(--color-neutral-200, #E8E8ED);
        display: flex;
        justify-content: flex-end;
        gap: 12px;
    }
    body.dark-mode .detail-footer { border-color: rgba(255,255,255,0.1); }

    .btn-secondary {
        height: 44px;
        padding: 0 24px;
        border-radius: var(--radius-full, 999px);
        background: transparent;
        border: 1px solid var(--color-neutral-400, #86868B);
        color: var(--color-neutral-900, #1D1D1F);
        font-weight: var(--fw-semibold, 600);
        cursor: pointer;
        transition: var(--motion-fast);
    }
    body.dark-mode .btn-secondary { color: var(--color-white, #FFFFFF); }
    .btn-secondary:hover { background: var(--color-neutral-100, #F5F5F7); }
    body.dark-mode .btn-secondary:hover { background: rgba(255,255,255,0.1); }

    .btn-primary {
        height: 44px;
        padding: 0 24px;
        border-radius: var(--radius-full, 999px);
        background: var(--color-primary, #F5A623);
        border: none;
        color: var(--color-navy, #0F172A);
        font-weight: var(--fw-bold, 700);
        display: flex;
        align-items: center;
        gap: 8px;
        cursor: pointer;
        transition: var(--motion-fast);
    }
    .btn-primary:hover {
        background: var(--color-primary-dark, #D98E12);
        transform: scale(0.98);
    }

    @@media (max-width: 768px) {
        .room-detail-layout { flex-direction: column; }
        .detail-media-col, .detail-info-col { width: 100%; border-right: none; }
        .detail-photo { border-top-right-radius: var(--radius-lg, 22px); }
        .info-content-scroll { padding: 20px; }
        .detail-footer { padding: 16px 20px; }
    }
</style>

@code {
    [Parameter] public bool Visible { get; set; }
    [Parameter] public EventCallback<bool> VisibleChanged { get; set; }
    [Parameter] public RoomItem? Room { get; set; }
    [Parameter] public EventCallback OnClose { get; set; }
    [Parameter] public EventCallback OnBook { get; set; }

    private async Task HandleVisibleChanged(bool value)
    {
        Visible = value;
        if (VisibleChanged.HasDelegate)
            await VisibleChanged.InvokeAsync(value);
    }

    private async Task Close()
    {
        await HandleVisibleChanged(false);
        if (OnClose.HasDelegate)
            await OnClose.InvokeAsync();
    }

    private async Task Book()
    {
        await HandleVisibleChanged(false);
        if (OnBook.HasDelegate)
            await OnBook.InvokeAsync();
    }

    private string GetStatusBadgeClass(string? status) => status switch {
        "available" => "badge-available",
        "booked" => "badge-booked",
        _ => "badge-unavailable"
    };
    
    private string GetStatusText(string? status) => status switch {
        "available" => "Tersedia Sekarang",
        "booked" => "Dipesan",
        _ => "Tidak Tersedia"
    };
}
"""
with open(path, 'w', encoding='utf-8') as f:
    f.write(new_content)
print("RoomDetailsModal.razor updated.")
