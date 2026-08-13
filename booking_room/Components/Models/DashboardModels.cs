namespace booking_room.Components.Models;

public record RoomSummary(string Name, int Available, int Total);
public record NextAvailableRoom(string RoomName, int AvailableInMinutes, int Capacity, bool IsAvailableNow);
public record RoomUtilization(string RoomName, int HoursUsed);
public record AnalyticsData(string Period, List<RoomUtilization> Rooms);

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
}
