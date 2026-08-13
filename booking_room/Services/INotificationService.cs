namespace booking_room.Services;

public class NotificationItem
{
    public string Id { get; set; } = Guid.NewGuid().ToString();
    public string SourceName { get; set; } = string.Empty;
    public string Title { get; set; } = string.Empty;
    public string Description { get; set; } = string.Empty;
    public DateTime Timestamp { get; set; }
    public bool IsRead { get; set; }
    public string Category { get; set; } = "System"; // "Reminder", "Security", "Report", "System"
    public string IconType { get; set; } = string.Empty;
    public string? AvatarUrl { get; set; }
}

public interface INotificationService
{
    IReadOnlyList<NotificationItem> Notifications { get; }
    int UnreadCount { get; }
    event Action? OnChange;

    void MarkAsRead(string id);
    void MarkAllAsRead();
}
