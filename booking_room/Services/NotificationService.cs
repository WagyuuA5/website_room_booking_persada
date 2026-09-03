using System;
using System.Collections.Generic;
using System.Linq;

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
            SourceName = "Sistem",
            Title = "Pengingat: Rapat Tim Eksekutif",
            Description = "Rapat di Executive Boardroom A dimulai dalam 15 menit.",
            Timestamp = DateTime.Now.AddMinutes(-2),
            IsRead = false,
            Category = "Reminder",
            IconType = "clock",
            ActionType = NotificationActionType.NavigateToRoute,
            RoutePath = "/status?bookingId=1",
            ReferenceId = "1",
            ModalComponentKey = "CheckInCountdownCard",
            ActionParameters = new Dictionary<string, object>
            {
                { "RoomName", "Executive Boardroom A" },
                { "TimeSlot", "09:00 - 12:00" },
                { "Location", "Lantai 42, Sayap Utara" },
                { "Capacity", 15 }
            }
        });

        _notifications.Add(new NotificationItem
        {
            SourceName = "Budi Santoso",
            Title = "Undangan Rapat",
            Description = "Budi Santoso telah mengundang Anda ke sesi evaluasi kinerja teknis.",
            Timestamp = DateTime.Now.AddMinutes(-5),
            IsRead = false,
            Category = "Invitation",
            IconType = "avatar",
            AvatarUrl = "https://ui-avatars.com/api/?name=Budi+Santoso&background=f59e0b&color=fff",
            ActionType = NotificationActionType.NavigateToRoute,
            RoutePath = "/status?bookingId=4",
            ReferenceId = "4",
            ModalComponentKey = "CheckInCountdownCard",
            ActionParameters = new Dictionary<string, object>
            {
                { "RoomName", "Focus Room Alpha" },
                { "Location", "Lantai 3, Sayap Barat" }
            }
        });

        _notifications.Add(new NotificationItem
        {
            SourceName = "Admin Sistem",
            Title = "Persetujuan Tertunda",
            Description = "Anda memiliki permintaan pemesanan yang menunggu persetujuan.",
            Timestamp = DateTime.Now.AddMinutes(-12),
            IsRead = false,
            Category = "System",
            IconType = "calendar",
            ActionType = NotificationActionType.NavigateToRoute,
            RoutePath = "/status?filter=Menunggu+Persetujuan",
            ReferenceId = "pending"
        });

        _notifications.Add(new NotificationItem
        {
            SourceName = "Sistem Keamanan",
            Title = "Pembaruan Kata Sandi Berhasil",
            Description = "Keamanan akun Anda adalah prioritas kami. Kata sandi telah diperbarui melalui cloud.",
            Timestamp = DateTime.Now.AddMinutes(-15),
            IsRead = true,
            Category = "Security",
            IconType = "shield",
            ActionType = NotificationActionType.NavigateToRoute,
            RoutePath = "/pengaturan",
            ReferenceId = "security"
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
            AvatarUrl = "https://ui-avatars.com/api/?name=Siti+Aminah&background=10b981&color=fff",
            ActionType = NotificationActionType.NavigateToRoute,
            RoutePath = "/riwayat",
            ReferenceId = "report"
        });

        _notifications.Add(new NotificationItem
        {
            SourceName = "Peringatan Server",
            Title = "Beban Lalu Lintas Tinggi",
            Description = "Lonjakan penggunaan terdeteksi di klaster Asia Tenggara. Tim TI sedang memantau situasi.",
            Timestamp = DateTime.Now.AddHours(-2),
            IsRead = true,
            Category = "System",
            IconType = "warning",
            ActionType = NotificationActionType.OpenModal,
            ModalComponentKey = "IncidentDetailModal",
            ActionParameters = new Dictionary<string, object>
            {
                { "Title", "Beban Lalu Lintas Tinggi" },
                { "Description", "Lonjakan penggunaan terdeteksi di klaster Asia Tenggara. Tim TI sedang memantau situasi." },
                { "Category", "Peringatan Server" }
            }
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
