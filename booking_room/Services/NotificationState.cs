using System;
using System.Timers;

namespace booking_room.Services
{
    public class NotificationState : IDisposable
    {
        private System.Timers.Timer? _timer;
        
        // This would typically come from a database, hardcoded for now based on user's upcoming booking
        public DateTime? NextBookingTime { get; set; } = DateTime.Now.AddMinutes(16); // Start > 15 mins
        
        public event Action? OnChange;

        public NotificationState()
        {
            _timer = new System.Timers.Timer(1000); // Check every second
            _timer.Elapsed += (s, e) => NotifyStateChanged();
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

                // Window check-in active (e.g. from 0 to 15 mins after booking time)
                // Assuming check-in window is active once the booking time is reached
                if (remaining <= TimeSpan.Zero && remaining > TimeSpan.FromMinutes(-15))
                {
                    return BannerType.ActionRequired;
                }
                
                // 15 - 1 minute before booking
                if (remaining <= TimeSpan.FromMinutes(15) && remaining > TimeSpan.Zero)
                {
                    return BannerType.Reminder;
                }

                return BannerType.None;
            }
        }

        public void DismissBanner()
        {
            NextBookingTime = null; // Clear booking to hide banner
            NotifyStateChanged();
        }

        private void NotifyStateChanged() => OnChange?.Invoke();

        public void Dispose()
        {
            _timer?.Dispose();
        }
    }
}
