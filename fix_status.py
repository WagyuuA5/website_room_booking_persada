import os
import re

path = 'booking_room/Components/Pages/Status.razor'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

# Add implements IDisposable
if "@implements IDisposable" not in content:
    content = content.replace("@inject NavigationManager Navigation", "@inject NavigationManager Navigation\n@implements IDisposable")

# Update @code block
if "private bool _disposed;" not in content:
    code_idx = content.find("@code {")
    if code_idx != -1:
        new_code_start = """@code {
    private bool _disposed;
    private System.Threading.CancellationTokenSource? _cts;"""
        content = content[:code_idx] + content[code_idx:].replace("@code {", new_code_start, 1)

# Modify LoadData to be async and use CancellationToken
if "private async Task LoadDataAsync" not in content:
    content = content.replace("private void LoadData()", "private async Task LoadDataAsync(System.Threading.CancellationToken token = default)")
    content = content.replace("protected override void OnInitialized()", "protected override async Task OnInitializedAsync()")
    content = content.replace("LoadData();", "await LoadDataAsync(_cts?.Token ?? default);")
    content = content.replace("_allBookings = BookingDataStore.AllBookings.ToList();", """
        // Simulasi fetch data async
        await Task.Delay(200, token);
        _allBookings = BookingDataStore.AllBookings.ToList();""")

# Implement Dispose
if "public void Dispose()" not in content:
    dispose_method = """
    public void Dispose()
    {
        _disposed = true;
        _cts?.Cancel();
        _cts?.Dispose();
    }
}"""
    content = content.replace("}\n", dispose_method + "\n", 1)  # Only replace the last brace roughly, wait, better use rfind
    content = content.rsplit("}", 1)[0] + dispose_method

# Also add the instantiation of _cts in OnInitializedAsync
content = content.replace("protected override async Task OnInitializedAsync()\n    {\n        await LoadDataAsync(_cts?.Token ?? default);\n    }", """protected override async Task OnInitializedAsync()
    {
        _cts = new System.Threading.CancellationTokenSource();
        try {
            await LoadDataAsync(_cts.Token);
        } catch (TaskCanceledException) { }
    }""")

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)
print("Status.razor updated for BUG-01.")
