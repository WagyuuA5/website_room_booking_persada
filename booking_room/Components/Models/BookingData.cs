namespace booking_room.Components.Models;

public record BookingItem(
    string Id,
    string RequestId,
    string RoomName,
    string Floor,
    string Status, // "pending", "approved", "rejected", "completed"
    string Date,
    string TimeSlot,
    string Duration,
    int Attendees,
    int Capacity,
    string RequestedBy,
    string RequestedByTitle,
    string Purpose,
    string PhotoUrl
);

public record UserProfileData(
    string FullName,
    string Email,
    string Phone,
    string JobTitle,
    string Department,
    string OfficeLocation,
    string LastLogin,
    string Initials
)
{
    public string PhotoUrl { get; set; } = string.Empty;

    public string Name => FullName;
    public string Title => JobTitle;
    public int TotalBookings => 24;
    public int CanceledBookings => 3;
    public string MostBookedRoom => "Executive Boardroom A";
};

public static class BookingDataStore
{
    public static List<BookingItem> AllBookings => new()
    {
        new("1", "REQ-8942-BR", "Executive Boardroom A", "Lantai 42, Sayap Utara",
            "pending", "27 Agustus 2026", "09:00 - 12:00", "3 Jam",
            12, 15, "Sarah Jenkins", "VP Operasional",
            "Rapat evaluasi eksekutif kuartalan bersama seluruh kepala departemen untuk membahas strategi Q4 dan alokasi anggaran.",
            "https://images.unsplash.com/photo-1497366216548-37526070297c?auto=format&fit=crop&w=800&q=80"),

        new("2", "REQ-7731-MR", "Training Room B", "Lantai 2, Sayap Timur",
            "approved", "28 Agustus 2026", "13:00 - 16:00", "3 Jam",
            25, 30, "Ahmad Fauzi", "Manajer Pelatihan",
            "Workshop orientasi karyawan baru — penilaian keterampilan teknis dan kegiatan membangun tim.",
            "https://images.unsplash.com/photo-1524758631624-e2822e304c36?auto=format&fit=crop&w=800&q=80"),

        new("3", "REQ-6650-HS", "Huddle Space C", "Lantai 1, Sayap Selatan",
            "rejected", "26 Agustus 2026", "10:00 - 11:00", "1 Jam",
            4, 6, "Nadia Pradipta", "Desainer Produk",
            "Review singkat design sprint bersama tim UX — sesi umpan balik prototipe aplikasi mobile baru.",
            "https://images.unsplash.com/photo-1497366811353-6870744d04b2?auto=format&fit=crop&w=800&q=80"),

        new("4", "REQ-5521-FC", "Focus Room Alpha", "Lantai 3, Sayap Barat",
            "completed", "25 Agustus 2026", "14:00 - 15:30", "1 Jam 30 Menit",
            3, 4, "Budi Santoso", "Lead Engineer",
            "Sesi tatap muka evaluasi kinerja dan perencanaan pengembangan karier.",
            "https://images.unsplash.com/photo-1497215842964-222b430dc094?auto=format&fit=crop&w=800&q=80"),

        new("5", "REQ-4410-CR", "Conference Hall", "Lantai 1, Gedung Utama",
            "approved", "29 Agustus 2026", "09:00 - 17:00", "8 Jam",
            45, 50, "Rina Wulandari", "Koordinator Acara",
            "Town hall tahunan perusahaan dengan presentasi keynote dan showcase departemen.",
            "https://images.unsplash.com/photo-1431540015160-0295aaa24f7f?auto=format&fit=crop&w=800&q=80"),

        new("6", "REQ-3309-IL", "Innovation Lab", "Lantai 3, Sayap Utara",
            "pending", "1 September 2026", "10:00 - 12:00", "2 Jam",
            10, 15, "Dimas Prasetyo", "Manajer R&D",
            "Sesi brainstorming inovasi produk — mengeksplorasi kemungkinan integrasi AI baru.",
            "https://images.unsplash.com/photo-1497366754888-5a456d4b3447?auto=format&fit=crop&w=800&q=80"),

        new("7", "REQ-2200-ES", "Executive Suite", "Lantai 5, Lantai Puncak",
            "completed", "24 Agustus 2026", "11:00 - 12:30", "1 Jam 30 Menit",
            8, 10, "Alex Mercer", "CTO",
            "Rapat dewan direksi — presentasi hasil keuangan Q3 dan perencanaan strategis.",
            "https://images.unsplash.com/photo-1462826303086-329426d1aef5?auto=format&fit=crop&w=800&q=80"),
    };

    private static UserProfileData _currentUser = new(
        "Wahyu Ravi",
        "whyuravi.2008@gmail.com",
        "+62 897 5678 98",
        "System Admin",
        "IT Dept",
        "Kantor Pusat - Lantai 3",
        "Hari ini, 08:30",
        "WR"
    );

    public static UserProfileData CurrentUser
    {
        get => _currentUser;
        set => _currentUser = value;
    }

    public static string GetStatusLabel(string status) => status switch
    {
        "pending" => "Menunggu",
        "approved" => "Disetujui",
        "rejected" => "Ditolak",
        "completed" => "Selesai",
        _ => status
    };

    public static string GetStatusBadgeClass(string status) => status switch
    {
        "pending" => "badge-pending",
        "approved" => "badge-approved",
        "rejected" => "badge-rejected",
        "completed" => "badge-completed",
        _ => ""
    };
}
