namespace booking_room.Components.Models;

public record RoomSummary(string Name, int Available, int Total);
public record NextAvailableRoom(string RoomName, int AvailableInMinutes, int Capacity, bool IsAvailableNow);
public record RoomUtilization(string RoomName, int HoursUsed);
public record AnalyticsData(string Period, List<RoomUtilization> Rooms);
public record ChartDataset(string Label, double[] Data, string BorderColor);
public record ChartData(string[] Labels, ChartDataset[] Datasets);

public record RoomDetail(string RoomName, string Floor, int Capacity, string Status, string StatusClass, string Facilities);
public record PendingApprovalItem(string RoomName, string RequestedBy, string Date, string TimeSlot, string Purpose, string Priority);
public record RoomItem(string Id, string Name, int Capacity, string Description, string Status, List<string> Amenities, string Floor, string PhotoUrl = "");
public record UpcomingBookingItem(string Id, string Category, string IconType, string AccentColor, string RoomName, string Location, string Date, string TimeSlot);

public record TodayScheduleItem(string RoomName, string TimeSlot, string Title, string Status, string StatusLabel, string AccentColor);
public record ActivityFeedItem(string IconType, string Description, string Timestamp, string AccentColor);
public record MetricTrend(string Label, string Value, string TrendPercent, bool IsUp, string Description);
public record CurrentRoomInfo(string RoomName, string TimeSlot, int RemainingMinutes, string Location);

public static class DashboardData
{
    public static RoomSummary AvailableRooms => new("Total Ruangan", 8, 20);
    public static int PendingApprovals = 3;

    public static List<NextAvailableRoom> NextAvailableRooms =>
    [
        new("Delta Boardroom", 45, 12, false),
        new("Boardroom A", 90, 20, false),
        new("Meeting Room 1", 120, 8, false),
        new("Training Center", 180, 30, false)
    ];

    public static List<TodayScheduleItem> TodaySchedule { get; } = new()
    {
        new("Executive Boardroom A", "09:00 - 11:00", "Rapat Strategi Q3", "sedang-berlangsung", "Berlangsung", "#10B981"),
        new("Huddle Space C", "13:30 - 15:00", "Sesi Brainstorming UI/UX", "akan-datang", "Akan Datang", "#3B82F6"),
        new("Training Center", "15:00 - 17:00", "Workshop Tim", "akan-datang", "Akan Datang", "#F59E0B"),
    };

    public static void AddTodayScheduleItem(TodayScheduleItem item)
    {
        TodaySchedule.Add(item);
    }

    public static List<ActivityFeedItem> RecentActivities =>
    [
        new("approval", "Budi menyetujui booking Executive Suite A", "5 menit lalu", "#10B981"),
        new("cancel", "Booking Training Ruangan B dibatalkan oleh sistem (no-show)", "12 menit lalu", "#EF4444"),
        new("alert", "Ruangan Delta Boardroom akan dilepas otomatis dalam 5 menit", "18 menit lalu", "#F59E0B"),
        new("booking", "Siti Rahayu membuat booking baru di Conference Hall", "32 menit lalu", "#3B82F6"),
        new("checkin", "Ahmad Fauzi check-in ke Meeting Room 1", "1 jam lalu", "#10B981"),
    ];

    public static List<MetricTrend> MetricTrends =>
    [
        new("Utilisasi Ruangan", "62%", "↑8%", true, "dari minggu lalu"),
        new("Rata-rata Durasi", "1.5 jam", "↑12%", true, "dari minggu lalu"),
        new("Tingkat No-Show", "8%", "↓3%", false, "dari minggu lalu"),
    ];

    public static CurrentRoomInfo? ActiveCheckIn => null;

    public static Dictionary<string, List<string>> RoleWidgetPriority => new()
    {
        ["Admin"] = new() { "PendingApproval", "Analytics", "TodaySchedule", "QuickBook", "ActivityFeed", "CurrentRoom", "Trends" },
        ["Employee"] = new() { "TodaySchedule", "QuickBook", "ActivityFeed", "CurrentRoom", "Trends" },
    };

    public static string CurrentUserRole => "Admin";

    public static List<RoomDetail> AllRooms =>
    [
        new("Boardroom A", "Lantai 3", 20, "Tersedia", "available", "Proyektor, Papan Tulis, Konferensi Video"),
        new("Meeting Room 1", "Lantai 2", 8, "Tersedia", "available", "Layar TV, Papan Tulis"),
        new("Huddle Space C", "Lantai 1", 4, "Tersedia", "available", "Layar TV"),
        new("Focus Room B", "Lantai 2", 2, "Tersedia", "available", "Monitor"),
        new("Training Center", "Lantai 4", 30, "Tersedia", "available", "Proyektor, Sistem Audio, Podium"),
        new("Executive Suite", "Lantai 5", 10, "Tersedia", "available", "Konferensi Video, Mini Bar"),
        new("Conference Hall", "Lantai 1", 50, "Tersedia", "available", "Sistem AV Lengkap, Panggung"),
        new("Innovation Lab", "Lantai 3", 15, "Tersedia", "available", "Layar Interaktif, Printer 3D"),
        new("Delta Boardroom", "Lantai 3", 12, "Digunakan", "occupied", "Proyektor, Konferensi Video"),
        new("Alpha Room", "Lantai 2", 6, "Digunakan", "occupied", "Layar TV, Papan Tulis"),
        new("Beta Room", "Lantai 4", 8, "Digunakan", "occupied", "Proyektor"),
        new("Gamma Room", "Lantai 1", 10, "Digunakan", "occupied", "Konferensi Video, Papan Tulis"),
        new("Omega Suite", "Lantai 5", 16, "Digunakan", "occupied", "Sistem AV Lengkap"),
        new("Sigma Room", "Lantai 2", 6, "Digunakan", "occupied", "Layar TV"),
        new("Workshop A", "Lantai 4", 25, "Perawatan", "maintenance", "Sistem AV Lengkap, Peralatan Workshop"),
        new("Server Room", "Lantai 1", 4, "Perawatan", "maintenance", "Layar Monitoring"),
        new("Studio Room", "Lantai 3", 8, "Digunakan", "occupied", "Green Screen, Pencahayaan"),
        new("Library Room", "Lantai 2", 12, "Digunakan", "occupied", "Proyektor, Zona Tenang"),
        new("Zen Room", "Lantai 5", 6, "Digunakan", "occupied", "Pencahayaan Ambient"),
        new("Sky Lounge", "Lantai 5", 20, "Digunakan", "occupied", "Pemandangan Panoramik, Mini Bar")
    ];

    public static List<PendingApprovalItem> PendingApprovalItems =>
    [
        new("Boardroom A", "Budi Santoso", "14 Agustus 2026", "09:00 - 11:00", "Presentasi Klien", "Tinggi"),
        new("Training Center", "Siti Rahayu", "14 Agustus 2026", "13:00 - 16:00", "Workshop Tim", "Sedang"),
        new("Meeting Room 1", "Ahmad Fauzi", "15 Agustus 2026", "10:00 - 11:30", "Perencanaan Sprint", "Normal")
    ];

    public static List<UpcomingBookingItem> UpcomingBookings =>
    [
        new("B-101", "Ruang Rapat", "meeting", "#3b82f6", "Rapat Strategi Q3", "Executive Boardroom A (Lantai 3)", "Kamis, 27 Agustus 2026", "09:00 - 11:00"),
        new("B-102", "Area Kolaborasi", "huddle", "#10b981", "Sesi Brainstorming UI/UX", "Huddle Space C (Lantai 1)", "Kamis, 27 Agustus 2026", "13:30 - 15:00"),
        new("B-103", "Fasilitas Khusus", "training", "#f59e0b", "Orientasi Karyawan Baru", "Training Center (Lantai 4)", "Senin, 31 Agustus 2026", "09:00 - 16:00"),
        new("B-104", "Ruang Rapat", "meeting", "#3b82f6", "Sinkronisasi Tim Mingguan", "Meeting Room 1 (Lantai 2)", "Selasa, 1 September 2026", "10:00 - 11:00"),
        new("B-105", "Fokus", "focus", "#8b5cf6", "Wawancara Kandidat 1-on-1", "Focus Room B (Lantai 2)", "Rabu, 2 September 2026", "14:00 - 15:00")
    ];

    public static AnalyticsData WeeklyData => new(
        "Minggu",
        [
            new("Boardroom A", 85),
            new("Meeting Room 1", 65),
            new("Training Center", 45),
            new("Huddle Space C", 35),
            new("Focus Room B", 20)
        ]);

    public static AnalyticsData MonthlyData => new(
        "Bulan",
        [
            new("Boardroom A", 320),
            new("Training Center", 280),
            new("Meeting Room 1", 210),
            new("Focus Room B", 150),
            new("Huddle Space C", 95)
        ]);

    public static AnalyticsData YearlyData => new(
        "Tahun",
        [
            new("Boardroom A", 1450),
            new("Training Center", 1200),
            new("Meeting Room 1", 980),
            new("Focus Room B", 650),
            new("Huddle Space C", 420)
        ]);

    public static AnalyticsData GetAnalytics(string period) => period switch
    {
        "Bulan" => MonthlyData,
        "Tahun" => YearlyData,
        _ => WeeklyData
    };

    public static ChartData GetChartData(string period)
    {
        return period switch
        {
            "Bulan" => GenerateMonthlyChartData(),
            "Tahun" => GenerateYearlyChartData(),
            _ => GenerateWeeklyChartData()
        };
    }

    private static ChartData GenerateWeeklyChartData()
    {
        var labels = new[] { "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu", "Minggu" };
        var rnd = new Random(42);
        var datasets = new[]
        {
            new ChartDataset("Boardroom A", GenerateSeries(7, 12, 18, rnd), "#0f1f3d"),
            new ChartDataset("Meeting Room 1", GenerateSeries(7, 8, 14, rnd), "#1e40af"),
            new ChartDataset("Training Center", GenerateSeries(7, 4, 10, rnd), "#3b82f6"),
            new ChartDataset("Huddle Space C", GenerateSeries(7, 2, 8, rnd), "#60a5fa"),
            new ChartDataset("Focus Room B", GenerateSeries(7, 1, 5, rnd), "#93c5fd")
        };
        return new ChartData(labels, datasets);
    }

    private static ChartData GenerateMonthlyChartData()
    {
        var labels = Enumerable.Range(1, 30).Select(i => $"{(i <= 9 ? "0" : "")}{i}").ToArray();
        var rnd = new Random(42);
        var datasets = new[]
        {
            new ChartDataset("Boardroom A", GenerateSeries(30, 8, 16, rnd), "#0f1f3d"),
            new ChartDataset("Training Center", GenerateSeries(30, 6, 14, rnd), "#1e40af"),
            new ChartDataset("Meeting Room 1", GenerateSeries(30, 4, 10, rnd), "#3b82f6"),
            new ChartDataset("Focus Room B", GenerateSeries(30, 3, 8, rnd), "#60a5fa"),
            new ChartDataset("Huddle Space C", GenerateSeries(30, 1, 5, rnd), "#93c5fd")
        };
        return new ChartData(labels, datasets);
    }

    private static ChartData GenerateYearlyChartData()
    {
        var labels = new[] { "Jan", "Feb", "Mar", "Apr", "Mei", "Jun", "Jul", "Agu", "Sep", "Okt", "Nov", "Des" };
        var rnd = new Random(42);
        var datasets = new[]
        {
            new ChartDataset("Boardroom A", GenerateSeries(12, 90, 160, rnd), "#0f1f3d"),
            new ChartDataset("Training Center", GenerateSeries(12, 70, 140, rnd), "#1e40af"),
            new ChartDataset("Meeting Room 1", GenerateSeries(12, 50, 110, rnd), "#3b82f6"),
            new ChartDataset("Focus Room B", GenerateSeries(12, 30, 80, rnd), "#60a5fa"),
            new ChartDataset("Huddle Space C", GenerateSeries(12, 15, 50, rnd), "#93c5fd")
        };
        return new ChartData(labels, datasets);
    }

    private static double[] GenerateSeries(int count, double min, double max, Random rnd)
    {
        var data = new double[count];
        for (int i = 0; i < count; i++)
        {
            data[i] = Math.Round(min + rnd.NextDouble() * (max - min), 1);
        }
        return data;
    }
}
