# Checklist QA Terpusat — Sistem Manajemen Ruangan & Pemesanan PT PERSADA

Dokumen ini menggabungkan seluruh standar kontrol kualitas (QA) dari seri `V1` sampai `V21` dan revisi sisi Pengguna (`V1`–`V2`), yang wajib diperiksa sebelum melakukan *merge* Pull Request (PR) ke branch utama.

---

## 1. Audit Routing & Struktur Komponen (Kritis V2)
- [ ] **Tidak ada duplikasi `@page` directive**: Setiap string rute (misal `"/boarding"`, `"/beranda"`, `"/dashboard"`, `"/bookings"`) dideklarasikan secara unik di satu komponen saja.
  - Perintah verifikasi: `grep -rn "@page" Components/Pages`
- [ ] **Pemisahan rute Admin vs Pengguna**:
  - Pengguna: Beranda dialihkan ke `/beranda`.
  - Admin: Dashboard dialihkan ke `/dashboard`.
  - Mengakses `/dashboard` sebagai Pengguna secara otomatis melakukan *redirect* ke `/beranda`.
- [ ] **Alur First-time User (Onboarding)**:
  - Tersedia di `Components/Pages/User/Boarding.razor` (3 slide, foto aset, tombol Lewati, Lanjut, dan Mulai Sekarang).
  - Menggunakan flag `localStorage` (`persada-onboarding-seen` / `hasSeenBoarding`).

---

## 2. Audit Dependency Injection (DI) & Resiliensi Circuit (Kritis V1)
- [ ] **Seluruh Service Ter-inject Wajib Terdaftar di `Program.cs`**:
  - `ModalStateService` (Scoped)
  - `NotificationState` (Scoped)
  - `INotificationService` / `NotificationService` (Scoped)
  - `LoadingStateService` (Scoped)
  - `DataExportService` (Scoped)
- [ ] **Pencegahan Circuit Crash**:
  - `<ErrorBoundary>` terpasang di `MainLayout.razor` membungkus `@Body` dengan UI fallback kustom berdesain PERSADA.
  - Banner `#blazor-error-ui` di-restyle mengikuti token `--card-bg`, `--shadow-md`, dan `--accent-amber`.

---

## 3. Audit Desain & Token Konsistensi (V11–V21)
- [ ] **Design Tokens**: Menggunakan variabel CSS yang konsisten (`--persada-navy-900`, `--persada-yellow-500`, `--persada-accent-blue`, `--persada-success-green`, dll).
- [ ] **Status Badges**:
  - Disetujui / Selesai / Berlangsung: Hijau (`#F0FDF4`, `#166534`)
  - Menunggu Persetujuan: Kuning / Amber (`#FEF3C7`, `#D97706`)
  - Ditolak / Dibatalkan: Merah (`#FEF2F2`, `#EF4444`)
- [ ] **Dark Mode**: Seluruh card, modal, sidebar, tabel, dan form mendukung toggle dark mode secara halus.
- [ ] **Bahasa**: 100% Bahasa Indonesia baku di seluruh antarmuka (User & Admin).

---

## 4. Audit Komponen Reusable & Interaktivitas (V13–V15, V20)
- [ ] **AppModal & ModalOverlayBlur**: Seluruh popup modal menggunakan modal reusable dan terhubung ke `ModalStateService`.
- [ ] **DataGrid**: Fungsi pencarian, penyaringan (filter), pemilahan rentang tanggal, dan ekspor CSV/JSON berfungsi tanpa error console.
- [ ] **Chart & Analitik**: Komponen chart (ApexCharts) memuat data dinamis sesuai periode (Minggu, Bulan, Tahun) dan mendukung legend chip toggle / drilldown.
- [ ] **Avatar Pengguna**: Inisial deterministik berdasar nama pengguna.

---

## 5. Checklist Verifikasi Kompilasi & Build
- [ ] `dotnet build` menghasilkan **0 Error** dan **0 Warning**.
- [ ] Jalankan navigasi lengkap:
  1. `Boarding` (`/boarding`) → `Login` (`/login`)
  2. `Beranda` (`/beranda`)
  3. `Pemesanan` (`/bookings` atau `/pemesanan`)
  4. `Status` (`/status`)
  5. `Riwayat` (`/history`)
  6. `Pengaturan` (`/pengaturan`)
