import os

path = 'booking_room/Components/Pages/SettingsPage.razor'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

# Make sure dark mode toggles and localization settings are there.
new_content = """@page "/settings"
@using booking_room.Components.Shared

<PageTitle>Pengaturan — Persada Booking Ruangan</PageTitle>

<div class="content-fade-in settings-page-wrapper">
    <div class="settings-header">
        <h1>Pengaturan Akun</h1>
        <p>Kelola preferensi, keamanan, dan integrasi personal Anda.</p>
    </div>

    <div class="settings-layout">
        <!-- Sidebar Navigation -->
        <div class="settings-sidebar">
            <button class="settings-nav-item @(activeTab == "preferences" ? "active" : "")" @onclick='() => activeTab = "preferences"'>Preferensi Tampilan</button>
            <button class="settings-nav-item @(activeTab == "security" ? "active" : "")" @onclick='() => activeTab = "security"'>Keamanan Akun</button>
            <button class="settings-nav-item @(activeTab == "integrations" ? "active" : "")" @onclick='() => activeTab = "integrations"'>Integrasi Personal</button>
        </div>

        <!-- Main Content Panel -->
        <div class="settings-main-panel">
            @if (activeTab == "preferences")
            {
                <div class="settings-section">
                    <h2>Tema Tampilan</h2>
                    <div class="settings-card">
                        <div class="setting-row">
                            <div>
                                <h4>Mode Gelap (Dark Mode)</h4>
                                <p>Gunakan tampilan gelap untuk mengurangi ketegangan mata.</p>
                            </div>
                            <button class="btn-toggle @(_isDarkMode ? "active" : "")" @onclick="ToggleDarkMode">
                                <div class="toggle-knob"></div>
                            </button>
                        </div>
                    </div>
                </div>
                <div class="settings-section" style="margin-top: 24px;">
                    <h2>Bahasa & Regional</h2>
                    <div class="settings-card">
                        <div class="setting-row">
                            <div>
                                <h4>Bahasa Aplikasi</h4>
                                <p>Sistem ini hanya mendukung Bahasa Indonesia (baku).</p>
                            </div>
                            <span class="badge-locked">ID (Indonesia)</span>
                        </div>
                        <div class="setting-row">
                            <div>
                                <h4>Format Tanggal & Waktu</h4>
                                <p>Sistem menggunakan format 24-jam (mis. 12 Mei 2024, 09:00 - 11:30).</p>
                            </div>
                            <span class="badge-locked">WIB / 24-jam</span>
                        </div>
                    </div>
                </div>
            }
            else if (activeTab == "security")
            {
                <div class="settings-section">
                    <h2>Keamanan Akun</h2>
                    <div class="settings-card">
                        <div class="setting-row">
                            <div>
                                <h4>Ubah Kata Sandi</h4>
                                <p>Perbarui kata sandi Anda secara berkala.</p>
                            </div>
                            <button class="btn-secondary" @onclick="() => isChangePasswordModalOpen = true">Ubah</button>
                        </div>
                    </div>
                </div>
            }
            else if (activeTab == "integrations")
            {
                <div class="settings-section">
                    <h2>Integrasi Aplikasi</h2>
                    <div class="settings-card">
                        <div class="setting-row">
                            <div>
                                <h4>Tautkan Kalender (Outlook / Google)</h4>
                                <p>Sinkronisasi jadwal rapat Anda dengan kalender eksternal.</p>
                            </div>
                            <button class="btn-secondary">Hubungkan</button>
                        </div>
                    </div>
                </div>
            }
        </div>
    </div>
</div>

<ChangePasswordModal Visible="isChangePasswordModalOpen" VisibleChanged="v => isChangePasswordModalOpen = v" />

<style>
    .settings-page-wrapper {
        max-width: 1200px;
        margin: 0 auto;
        padding: 24px;
        display: flex;
        flex-direction: column;
        gap: 24px;
    }
    .settings-header h1 {
        font-size: var(--fs-h1, 32px);
        font-weight: var(--fw-bold, 700);
        margin: 0 0 8px 0;
    }
    .settings-header p {
        color: var(--color-neutral-600);
        margin: 0;
    }
    
    .settings-layout {
        display: flex;
        gap: 32px;
    }
    
    .settings-sidebar {
        width: 240px;
        display: flex;
        flex-direction: column;
        gap: 8px;
    }
    .settings-nav-item {
        padding: 12px 16px;
        text-align: left;
        background: transparent;
        border: none;
        border-radius: var(--radius-sm, 8px);
        font-weight: var(--fw-semibold, 600);
        color: var(--color-neutral-600);
        cursor: pointer;
    }
    .settings-nav-item.active {
        background: var(--color-neutral-200);
        color: var(--color-navy);
    }
    body.dark-mode .settings-nav-item.active {
        background: rgba(255,255,255,0.1);
        color: var(--color-white);
    }
    
    .settings-main-panel {
        flex: 1;
    }
    
    .settings-section h2 {
        font-size: var(--fs-h3, 20px);
        font-weight: var(--fw-bold, 700);
        margin: 0 0 16px 0;
    }
    
    .settings-card {
        background: var(--color-white);
        border: 1px solid var(--color-neutral-200);
        border-radius: var(--radius-md, 14px);
        overflow: hidden;
    }
    body.dark-mode .settings-card {
        background: var(--color-neutral-900);
        border-color: rgba(255,255,255,0.1);
    }
    
    .setting-row {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 16px 20px;
        border-bottom: 1px solid var(--color-neutral-200);
    }
    body.dark-mode .setting-row { border-color: rgba(255,255,255,0.1); }
    .setting-row:last-child { border-bottom: none; }
    
    .setting-row h4 { margin: 0 0 4px 0; font-weight: var(--fw-semibold, 600); }
    .setting-row p { margin: 0; font-size: 12px; color: var(--color-neutral-600); }
    
    .btn-toggle {
        width: 44px;
        height: 24px;
        border-radius: 12px;
        background: var(--color-neutral-400);
        border: none;
        position: relative;
        cursor: pointer;
        transition: background 0.3s;
    }
    .btn-toggle.active { background: var(--color-primary); }
    .toggle-knob {
        width: 20px;
        height: 20px;
        background: var(--color-white);
        border-radius: 50%;
        position: absolute;
        top: 2px;
        left: 2px;
        transition: transform 0.3s;
    }
    .btn-toggle.active .toggle-knob {
        transform: translateX(20px);
    }

    .badge-locked {
        padding: 6px 12px;
        background: var(--color-neutral-100);
        color: var(--color-neutral-600);
        border-radius: var(--radius-full);
        font-size: 12px;
        font-weight: 600;
    }
    body.dark-mode .badge-locked {
        background: rgba(255,255,255,0.05);
    }
</style>

@code {
    private string activeTab = "preferences";
    private bool _isDarkMode = false;
    private bool isChangePasswordModalOpen = false;

    private void ToggleDarkMode()
    {
        _isDarkMode = !_isDarkMode;
        // Logic to toggle dark mode class on body is handled globally or via JS interop in a real app
    }
}
"""
with open(path, 'w', encoding='utf-8') as f:
    f.write(new_content)
print("SettingsPage.razor updated.")
