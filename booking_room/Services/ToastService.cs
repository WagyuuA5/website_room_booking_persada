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
    private readonly List<ToastMessage> _toasts = new();
    public event Action? OnChange;

    public IReadOnlyList<ToastMessage> ActiveToasts => _toasts.AsReadOnly();

    public void Show(string title, string message = "", ToastType type = ToastType.Info, int durationMs = 4000)
    {
        var toast = new ToastMessage
        {
            Title = title,
            Message = message,
            Type = type,
            DurationMs = durationMs
        };

        _toasts.Add(toast);
        NotifyStateChanged();

        var timer = new System.Threading.Timer(_ =>
        {
            Remove(toast.Id);
        }, null, durationMs, System.Threading.Timeout.Infinite);
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
        var item = _toasts.FirstOrDefault(t => t.Id == id);
        if (item != null)
        {
            _toasts.Remove(item);
            NotifyStateChanged();
        }
    }

    private void NotifyStateChanged() => OnChange?.Invoke();
}
