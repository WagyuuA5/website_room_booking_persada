namespace booking_room.Components.Models;

public record RoomSummary(string Name, int Available, int Total);
public record NextAvailableRoom(string RoomName, int AvailableInMinutes, int Capacity, bool IsAvailableNow);
public record RoomUtilization(string RoomName, int HoursUsed);
public record AnalyticsData(string Period, List<RoomUtilization> Rooms);
public record ChartDataset(string Label, double[] Data, string BorderColor);
public record ChartData(string[] Labels, ChartDataset[] Datasets);

// New models for pop-up modals
public record RoomDetail(string RoomName, string Floor, int Capacity, string Status, string StatusClass, string Facilities);
public record PendingApprovalItem(string RoomName, string RequestedBy, string Date, string TimeSlot, string Purpose, string Priority);

public static class DashboardData
{
    public static RoomSummary AvailableRooms => new("Total Ruangan", 8, 20);
    public static int PendingApprovals => 3;

    public static List<NextAvailableRoom> NextAvailableRooms =>
    [
        new("Delta Boardroom", 45, 12, false),
        new("Boardroom A", 90, 20, false),
        new("Meeting Room 1", 120, 8, false),
        new("Training Center", 180, 30, false)
    ];

    // Room details for pop-up
    public static List<RoomDetail> AllRooms =>
    [
        new("Boardroom A", "Lantai 3", 20, "Tersedia", "available", "Projector, Whiteboard, Video Conf"),
        new("Meeting Room 1", "Lantai 2", 8, "Tersedia", "available", "TV Display, Whiteboard"),
        new("Huddle Space C", "Lantai 1", 4, "Tersedia", "available", "TV Display"),
        new("Focus Room B", "Lantai 2", 2, "Tersedia", "available", "Monitor"),
        new("Training Center", "Lantai 4", 30, "Tersedia", "available", "Projector, Sound System, Podium"),
        new("Executive Suite", "Lantai 5", 10, "Tersedia", "available", "Video Conf, Mini Bar"),
        new("Conference Hall", "Lantai 1", 50, "Tersedia", "available", "Full AV System, Stage"),
        new("Innovation Lab", "Lantai 3", 15, "Tersedia", "available", "Interactive Display, 3D Printer"),
        new("Delta Boardroom", "Lantai 3", 12, "Digunakan", "occupied", "Projector, Video Conf"),
        new("Alpha Room", "Lantai 2", 6, "Digunakan", "occupied", "TV Display, Whiteboard"),
        new("Beta Room", "Lantai 4", 8, "Digunakan", "occupied", "Projector"),
        new("Gamma Room", "Lantai 1", 10, "Digunakan", "occupied", "Video Conf, Whiteboard"),
        new("Omega Suite", "Lantai 5", 16, "Digunakan", "occupied", "Full AV System"),
        new("Sigma Room", "Lantai 2", 6, "Digunakan", "occupied", "TV Display"),
        new("Workshop A", "Lantai 4", 25, "Maintenance", "maintenance", "Full AV System, Workshop Tools"),
        new("Server Room", "Lantai 1", 4, "Maintenance", "maintenance", "Monitoring Screens"),
        new("Studio Room", "Lantai 3", 8, "Digunakan", "occupied", "Green Screen, Lighting"),
        new("Library Room", "Lantai 2", 12, "Digunakan", "occupied", "Projector, Quiet Zone"),
        new("Zen Room", "Lantai 5", 6, "Digunakan", "occupied", "Ambient Lighting"),
        new("Sky Lounge", "Lantai 5", 20, "Digunakan", "occupied", "Panoramic View, Mini Bar")
    ];

    // Pending approval items for pop-up
    public static List<PendingApprovalItem> PendingApprovalItems =>
    [
        new("Boardroom A", "Budi Santoso", "14 Agustus 2026", "09:00 - 11:00", "Client Presentation", "Tinggi"),
        new("Training Center", "Siti Rahayu", "14 Agustus 2026", "13:00 - 16:00", "Team Workshop", "Sedang"),
        new("Meeting Room 1", "Ahmad Fauzi", "15 Agustus 2026", "10:00 - 11:30", "Sprint Planning", "Normal")
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
