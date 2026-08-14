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
    // Convenience properties used by ProfilePage
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
        new("1", "REQ-8942-BR", "Executive Boardroom A", "Level 42, North Wing",
            "pending", "October 24, 2023", "09:00 - 12:00 PM", "3 Hours",
            12, 15, "Sarah Jenkins", "VP Operations",
            "Quarterly executive review meeting with all department heads to discuss Q4 strategy and budget allocation.",
            "https://images.unsplash.com/photo-1497366216548-37526070297c?auto=format&fit=crop&w=800&q=80"),

        new("2", "REQ-7731-MR", "Training Room B", "Level 2, East Wing",
            "approved", "October 25, 2023", "13:00 - 16:00 PM", "3 Hours",
            25, 30, "Ahmad Fauzi", "Training Manager",
            "New employee onboarding workshop — technical skills assessment and team building activities.",
            "https://images.unsplash.com/photo-1524758631624-e2822e304c36?auto=format&fit=crop&w=800&q=80"),

        new("3", "REQ-6650-HS", "Huddle Space C", "Level 1, South Wing",
            "rejected", "October 22, 2023", "10:00 - 11:00 AM", "1 Hour",
            4, 6, "Nadia Pradipta", "Product Designer",
            "Quick design sprint review with the UX team — feedback session on new mobile app prototype.",
            "https://images.unsplash.com/photo-1497366811353-6870744d04b2?auto=format&fit=crop&w=800&q=80"),

        new("4", "REQ-5521-FC", "Focus Room Alpha", "Level 3, West Wing",
            "completed", "October 20, 2023", "14:00 - 15:30 PM", "1.5 Hours",
            3, 4, "Budi Santoso", "Engineering Lead",
            "One-on-one performance review and career development planning session.",
            "https://images.unsplash.com/photo-1497215842964-222b430dc094?auto=format&fit=crop&w=800&q=80"),

        new("5", "REQ-4410-CR", "Conference Hall", "Level 1, Main Building",
            "approved", "October 26, 2023", "09:00 - 17:00 PM", "8 Hours",
            45, 50, "Rina Wulandari", "Event Coordinator",
            "Annual company town hall meeting with keynote presentations and department showcases.",
            "https://images.unsplash.com/photo-1431540015160-0295aaa24f7f?auto=format&fit=crop&w=800&q=80"),

        new("6", "REQ-3309-IL", "Innovation Lab", "Level 3, North Wing",
            "pending", "October 27, 2023", "10:00 - 12:00 PM", "2 Hours",
            10, 15, "Dimas Prasetyo", "R&D Manager",
            "Product innovation brainstorming session — exploring new AI integration possibilities.",
            "https://images.unsplash.com/photo-1497366754888-5a456d4b3447?auto=format&fit=crop&w=800&q=80"),

        new("7", "REQ-2200-ES", "Executive Suite", "Level 5, Top Floor",
            "completed", "October 18, 2023", "11:00 - 12:30 PM", "1.5 Hours",
            8, 10, "Alex Mercer", "CTO",
            "Board of directors meeting — Q3 financial results presentation and strategic planning.",
            "https://images.unsplash.com/photo-1462826303086-329426d1aef5?auto=format&fit=crop&w=800&q=80"),
    };

    public static UserProfileData CurrentUser => new(
        "Wahyu Ravi",
        "whyuravi.2008@gmail.com",
        "+62 897 5678 98",
        "System Admin",
        "IT Dept",
        "HQ - Floor 3",
        "Today, 08:30 AM",
        "WR"
    );

    public static string GetStatusLabel(string status) => status switch
    {
        "pending" => "Pending",
        "approved" => "Approved",
        "rejected" => "Rejected",
        "completed" => "Completed",
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
