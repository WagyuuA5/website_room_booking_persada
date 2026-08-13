namespace booking_room.Services;

public class LoadingStateService
{
    public bool IsLoading { get; private set; }

    public event Action? OnChange;

    public void SetLoading(bool isLoading)
    {
        if (IsLoading != isLoading)
        {
            IsLoading = isLoading;
            NotifyStateChanged();
        }
    }

    private void NotifyStateChanged() => OnChange?.Invoke();
}
