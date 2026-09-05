using System.Collections.Concurrent;

namespace booking_room.Services;

public enum ToastType
{
    Success,
    Warning,
    Error,
    Info
}

public class ToastMessage
{
    public string Id { get; set; } = Guid.NewGuid().ToString();
    public string Title { get; set; } = string.Empty;
    public string Message { get; set; } = string.Empty;
    public ToastType Type { get; set; } = ToastType.Info;
    public int DurationMs { get; set; } = 4000;
    public DateTime CreatedAt { get; set; } = DateTime.Now;

    public string AccentColor => Type switch
    {
        ToastType.Success => "#10B981",
        ToastType.Warning => "#F59E0B",
        ToastType.Error => "#EF4444",
        ToastType.Info => "#3B82F6",
        _ => "#10B981"
    };

    public string BadgeText => Type switch
    {
        ToastType.Success => "BERHASIL",
        ToastType.Warning => "PERINGATAN",
        ToastType.Error => "GAGAL",
        ToastType.Info => "INFO",
        _ => "INFO"
    };
}

public interface IToastService
{
    event Action? OnChange;
    IReadOnlyList<ToastMessage> ActiveToasts { get; }
    void Show(string title, string message = "", ToastType type = ToastType.Info, int durationMs = 4000);
    void Success(string title, string message = "", int durationMs = 4000);
    void Warning(string title, string message = "", int durationMs = 4000);
    void Error(string title, string message = "", int durationMs = 4000);
    void Info(string title, string message = "", int durationMs = 4000);
    void Remove(string id);
}

public class ToastService : IToastService
{
    private readonly ConcurrentDictionary<string, ToastMessage> _toasts = new();
    private readonly ConcurrentDictionary<string, System.Threading.Timer> _timers = new();
    private const int MaxActiveToasts = 3;
    public event Action? OnChange;

    public IReadOnlyList<ToastMessage> ActiveToasts => _toasts.Values.OrderBy(t => t.CreatedAt).ToList().AsReadOnly();

    public void Show(string title, string message = "", ToastType type = ToastType.Info, int durationMs = 4000)
    {
        // Enforce deduplication to prevent identical toasts within 1.5s
        if (_toasts.Values.Any(t => t.Title == title && t.Message == message && (DateTime.Now - t.CreatedAt).TotalSeconds < 1.5))
        {
            return;
        }

        // Enforce maximum active toasts limit (remove oldest if limit exceeded)
        while (_toasts.Count >= MaxActiveToasts)
        {
            var oldest = _toasts.Values.OrderBy(t => t.CreatedAt).FirstOrDefault();
            if (oldest != null)
            {
                Remove(oldest.Id);
            }
            else
            {
                break;
            }
        }

        var toast = new ToastMessage
        {
            Title = title,
            Message = message,
            Type = type,
            DurationMs = durationMs,
            CreatedAt = DateTime.Now
        };

        if (_toasts.TryAdd(toast.Id, toast))
        {
            var timer = new System.Threading.Timer(state =>
            {
                if (state is string toastId)
                {
                    Remove(toastId);
                }
            }, toast.Id, durationMs, System.Threading.Timeout.Infinite);

            _timers.TryAdd(toast.Id, timer);
            NotifyStateChanged();
        }
    }

    public void Success(string title, string message = "", int durationMs = 4000)
        => Show(title, message, ToastType.Success, durationMs);

    public void Warning(string title, string message = "", int durationMs = 4000)
        => Show(title, message, ToastType.Warning, durationMs);

    public void Error(string title, string message = "", int durationMs = 4000)
        => Show(title, message, ToastType.Error, durationMs);

    public void Info(string title, string message = "", int durationMs = 4000)
        => Show(title, message, ToastType.Info, durationMs);

    public void Remove(string id)
    {
        if (_timers.TryRemove(id, out var timer))
        {
            try { timer.Dispose(); } catch { }
        }

        if (_toasts.TryRemove(id, out _))
        {
            NotifyStateChanged();
        }
    }

    private void NotifyStateChanged()
    {
        try
        {
            OnChange?.Invoke();
        }
        catch { }
    }
}
