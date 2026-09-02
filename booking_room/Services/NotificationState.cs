using System;
using System.Timers;

namespace booking_room.Services
{
    public class NotificationState : IDisposable
    {
        private System.Timers.Timer? _timer;
        private bool _disposed;
        
        public DateTime? NextBookingTime { get; set; } = DateTime.Now.AddMinutes(16);
        
        public event Action? OnChange;

        public NotificationState()
        {
            _timer = new System.Timers.Timer(1000);
            _timer.Elapsed += (s, e) =>
            {
                if (!_disposed)
                {
                    NotifyStateChanged();
                }
            };
            _timer.Start();
        }

        public enum BannerType
        {
            None,
            Reminder,
            ActionRequired
        }

        public BannerType CurrentBannerType
        {
            get
            {
                if (!NextBookingTime.HasValue) return BannerType.None;

                var remaining = NextBookingTime.Value - DateTime.Now;

                if (remaining <= TimeSpan.Zero && remaining > TimeSpan.FromMinutes(-15))
                {
                    return BannerType.ActionRequired;
                }
                
                if (remaining <= TimeSpan.FromMinutes(15) && remaining > TimeSpan.Zero)
                {
                    return BannerType.Reminder;
                }

                return BannerType.None;
            }
        }

        public void DismissBanner()
        {
            NextBookingTime = null;
            NotifyStateChanged();
        }

        private void NotifyStateChanged()
        {
            if (_disposed) return;
            try
            {
                OnChange?.Invoke();
            }
            catch { }
        }

        public void Dispose()
        {
            _disposed = true;
            _timer?.Dispose();
        }
    }
}
