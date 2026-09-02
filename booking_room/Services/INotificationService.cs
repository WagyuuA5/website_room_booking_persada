using System;
using System.Collections.Generic;

namespace booking_room.Services;

public enum NotificationActionType
{
    None,
    NavigateToRoute,
    OpenModal
}

public class NotificationItem
{
    public string Id { get; set; } = Guid.NewGuid().ToString();
    public string SourceName { get; set; } = string.Empty;
    public string Title { get; set; } = string.Empty;
    public string Description { get; set; } = string.Empty;
    public DateTime Timestamp { get; set; } = DateTime.Now;
    public bool IsRead { get; set; }
    public string Category { get; set; } = "System"; // "Reminder", "Invitation", "Security", "Report", "System"
    public string IconType { get; set; } = string.Empty;
    public string? AvatarUrl { get; set; }

    public NotificationActionType ActionType { get; set; } = NotificationActionType.None;
    public string? RoutePath { get; set; }
    public string? ModalComponentKey { get; set; }
    public Dictionary<string, object>? ActionParameters { get; set; }
}

public interface INotificationService
{
    IReadOnlyList<NotificationItem> Notifications { get; }
    int UnreadCount { get; }
    event Action? OnChange;

    void MarkAsRead(string id);
    void MarkAllAsRead();
}
