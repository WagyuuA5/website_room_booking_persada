namespace booking_room.Services;

public class NotificationService : INotificationService
{
    private readonly List<NotificationItem> _notifications = new();

    public IReadOnlyList<NotificationItem> Notifications => _notifications.AsReadOnly();
    public int UnreadCount => _notifications.Count(n => !n.IsRead);
    public event Action? OnChange;

    public NotificationService()
    {
        _notifications.Add(new NotificationItem
        {
            SourceName = "System",
            Title = "Pengingat: Rapat Tim Eksekutif",
            Description = "Rapat di Ruang Konferensi C dimulai dalam 15 menit.",
            Timestamp = DateTime.Now.AddMinutes(-2),
            IsRead = false,
            Category = "Reminder",
            IconType = "clock"
        });

        _notifications.Add(new NotificationItem
        {
            SourceName = "Budi Santoso",
            Title = "Undangan Rapat",
            Description = "Budi Santoso telah mengundang Anda ke sesi perencanaan Q3.",
            Timestamp = DateTime.Now.AddMinutes(-5),
            IsRead = false,
            Category = "Invitation",
            IconType = "avatar",
            AvatarUrl = "https://ui-avatars.com/api/?name=Budi+Santoso&background=f59e0b&color=fff"
        });

        _notifications.Add(new NotificationItem
        {
            SourceName = "Security System",
            Title = "Pembaruan Kata Sandi Berhasil",
            Description = "Keamanan akun Anda adalah prioritas kami. Kata sandi telah diperbarui melalui cloud.",
            Timestamp = DateTime.Now.AddMinutes(-15),
            IsRead = true,
            Category = "Security",
            IconType = "shield"
        });

        _notifications.Add(new NotificationItem
        {
            SourceName = "Siti Aminah",
            Title = "Laporan Mingguan Siap",
            Description = "Data analitik penggunaan ruangan untuk minggu kedua siap diunduh.",
            Timestamp = DateTime.Now.AddHours(-1),
            IsRead = true,
            Category = "Report",
            IconType = "avatar",
            AvatarUrl = "/images/avatar1.png" // Fallback if no image
        });

        _notifications.Add(new NotificationItem
        {
            SourceName = "Peringatan Server",
            Title = "Beban Lalu Lintas Tinggi",
            Description = "Lonjakan penggunaan terdeteksi di klaster Asia Tenggara. Tim TI sedang memantau situasi.",
            Timestamp = DateTime.Now.AddHours(-2),
            IsRead = true,
            Category = "System",
            IconType = "warning"
        });
    }

    public void MarkAsRead(string id)
    {
        var item = _notifications.FirstOrDefault(n => n.Id == id);
        if (item != null && !item.IsRead)
        {
            item.IsRead = true;
            NotifyStateChanged();
        }
    }

    public void MarkAllAsRead()
    {
        bool changed = false;
        foreach (var item in _notifications.Where(n => !n.IsRead))
        {
            item.IsRead = true;
            changed = true;
        }

        if (changed)
        {
            NotifyStateChanged();
        }
    }

    private void NotifyStateChanged() => OnChange?.Invoke();
}
