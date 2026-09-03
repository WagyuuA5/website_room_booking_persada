import os

path = 'booking_room/Components/Pages/Status.razor'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace top injects
old_injects = """@inject NavigationManager Navigation"""
new_injects = """@inject NavigationManager Navigation
@implements IDisposable"""
content = content.replace(old_injects, new_injects)

# Replace @code and LoadData
old_code_start = """@code {
    private string _searchQuery = "";"""
new_code_start = """@code {
    private bool _disposed;
    private System.Threading.CancellationTokenSource? _cts;
    
    private string _searchQuery = "";"""
content = content.replace(old_code_start, new_code_start)

old_init = """    protected override void OnInitialized()
    {
        LoadData();
    }

    private void LoadData()
    {
        _allBookings = BookingDataStore.AllBookings.ToList();

        if (selectedBooking == null && _allBookings.Count > 0)
        {
            selectedBooking = _allBookings[0];
        }
    }"""
new_init = """    protected override async Task OnInitializedAsync()
    {
        _cts = new System.Threading.CancellationTokenSource();
        try {
            await LoadDataAsync(_cts.Token);
        } catch (TaskCanceledException) {}
    }

    private async Task LoadDataAsync(System.Threading.CancellationToken token)
    {
        // Add fake delay to simulate async api
        await Task.Delay(200, token);
        _allBookings = BookingDataStore.AllBookings.ToList();

        if (selectedBooking == null && _allBookings.Count > 0)
        {
            selectedBooking = _allBookings[0];
        }
        
        if (!_disposed) {
            try { InvokeAsync(StateHasChanged); } catch {}
        }
    }
    
    private void LoadData() { } // Fallback for RefreshData if it calls LoadData() synchronously, wait, let's also update RefreshData"""
content = content.replace(old_init, new_init)

old_refresh = """    private void RefreshData()
    {
        LoadData();
        ToastService.Success("Data Diperbarui", "Status pemesanan berhasil disinkronkan.");
    }"""
new_refresh = """    private async Task RefreshData()
    {
        if (_cts != null) {
            _cts.Cancel();
            _cts.Dispose();
        }
        _cts = new System.Threading.CancellationTokenSource();
        try {
            await LoadDataAsync(_cts.Token);
            ToastService.Success("Data Diperbarui", "Status pemesanan berhasil disinkronkan.");
        } catch (TaskCanceledException) {}
    }"""
content = content.replace(old_refresh, new_refresh)
content = content.replace('@onclick="RefreshData"', '@onclick="RefreshData"')

# Add dispose method
if "public void Dispose()" not in content:
    content = content.rsplit("}", 1)[0] + """
    public void Dispose()
    {
        _disposed = true;
        if (_cts != null)
        {
            _cts.Cancel();
            _cts.Dispose();
            _cts = null;
        }
    }
}
"""

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)
print("Status.razor fixed.")
