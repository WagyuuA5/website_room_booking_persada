import os

path = 'booking_room/Components/Shared/RoomUtilizationChart.razor'
markup = """@namespace booking_room.Components.Shared
@inject IJSRuntime JS
@implements IAsyncDisposable

<div class="utilization-card">
    <div class="utilization-header">
        <div class="utilization-title-col">
            <h3>Analitik Utilisasi Ruangan</h3>
            <span class="sub">5 Ruangan Paling Sering Dipesan</span>
        </div>
        <div class="utilization-tabs">
            <button class="@(Period == "Minggu" ? "active" : "")" @onclick='() => ChangePeriod("Minggu")'>Minggu</button>
            <button class="@(Period == "Bulan" ? "active" : "")" @onclick='() => ChangePeriod("Bulan")'>Bulan</button>
            <button class="@(Period == "Tahun" ? "active" : "")" @onclick='() => ChangePeriod("Tahun")'>Tahun</button>
        </div>
    </div>

    @if (_isLoading)
    {
        <div class="skeleton-chart" style="height: 250px; border-radius: var(--radius-md);"></div>
    }
    else
    {
        <div class="chart-container @(_animateIn ? "animate-chart-in" : "")">
            @foreach (var item in Data)
            {
                <div class="chart-row" @onclick="() => OpenDetail(item)">
                    <span class="chart-label">@item.Name</span>
                    <div class="chart-bar-wrap">
                        <div class="chart-bar" style="width: @(item.Percentage)%; transition-delay: @(item.Index * 80)ms;">
                            <span class="chart-value">@item.Hours jam</span>
                        </div>
                    </div>
                </div>
            }
        </div>
    }
</div>

@code {
    private string Period = "Bulan";
    private bool _isLoading = false;
    private bool _animateIn = false;
    private List<ChartItem> Data = new();

    public class ChartItem {
        public int Index { get; set; }
        public string Name { get; set; } = "";
        public int Hours { get; set; }
        public double Percentage { get; set; }
    }

    protected override void OnInitialized()
    {
        LoadData(Period);
        _animateIn = true;
    }

    private async Task ChangePeriod(string newPeriod)
    {
        if (Period == newPeriod) return;
        Period = newPeriod;
        _isLoading = true;
        await Task.Delay(300); // Simulate network
        LoadData(Period);
        _isLoading = false;
        _animateIn = false;
        StateHasChanged();
        await Task.Delay(50);
        _animateIn = true;
    }

    private void LoadData(string period)
    {
        int multiplier = period == "Minggu" ? 1 : period == "Bulan" ? 4 : 48;
        Data = new List<ChartItem>
        {
            new() { Index=0, Name="Boardroom A", Hours = 20 * multiplier, Percentage = 85 },
            new() { Index=1, Name="Meeting Room 1", Hours = 15 * multiplier, Percentage = 65 },
            new() { Index=2, Name="Training Center", Hours = 10 * multiplier, Percentage = 45 },
            new() { Index=3, Name="Huddle Space C", Hours = 8 * multiplier, Percentage = 35 },
            new() { Index=4, Name="Focus Room B", Hours = 5 * multiplier, Percentage = 20 }
        };
    }

    private void OpenDetail(ChartItem item)
    {
        // Open modal detail for item
    }

    public async ValueTask DisposeAsync()
    {
    }
}
"""
with open(path, 'w', encoding='utf-8') as f: f.write(markup)

css = """
/* DASH-02: Room Utilization Chart */
.utilization-card {
    background: var(--color-white, #FFFFFF);
    border: 1px solid var(--color-neutral-200, #E8E8ED);
    border-radius: var(--radius-md, 14px);
    padding: 24px;
    box-shadow: 0 4px 16px rgba(0,0,0,0.02);
}
body.dark-mode .utilization-card {
    background: var(--color-neutral-900, #1D1D1F);
    border-color: rgba(255,255,255,0.1);
}
.utilization-header {
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
    margin-bottom: 24px;
}
.utilization-title-col h3 {
    margin: 0;
    font-size: var(--fs-h2, 24px);
    font-weight: var(--fw-bold, 700);
    color: var(--color-navy);
}
body.dark-mode .utilization-title-col h3 { color: var(--color-white); }
.utilization-title-col .sub {
    font-size: var(--fs-sm, 14px);
    color: var(--color-neutral-600);
}
.utilization-tabs {
    display: flex;
    background: var(--color-neutral-100);
    border-radius: var(--radius-sm, 8px);
    padding: 4px;
}
body.dark-mode .utilization-tabs { background: rgba(255,255,255,0.1); }
.utilization-tabs button {
    background: transparent;
    border: none;
    padding: 6px 12px;
    border-radius: var(--radius-sm, 8px);
    font-size: var(--fs-sm, 14px);
    font-weight: var(--fw-semibold, 600);
    color: var(--color-neutral-600);
    cursor: pointer;
    transition: var(--motion-fast);
}
body.dark-mode .utilization-tabs button { color: var(--color-neutral-400); }
.utilization-tabs button.active {
    background: var(--color-white);
    color: var(--color-navy);
    box-shadow: 0 1px 3px rgba(0,0,0,0.1);
}
body.dark-mode .utilization-tabs button.active {
    background: var(--color-neutral-600);
    color: var(--color-white);
}

.chart-container {
    display: flex;
    flex-direction: column;
    gap: 16px;
}
.chart-row {
    display: flex;
    align-items: center;
    gap: 16px;
    cursor: pointer;
}
.chart-row:hover .chart-bar {
    filter: brightness(1.05);
}
.chart-label {
    width: 140px;
    font-size: var(--fs-sm, 14px);
    font-weight: var(--fw-semibold, 600);
    color: var(--color-navy);
    text-align: right;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
}
body.dark-mode .chart-label { color: var(--color-white); }
.chart-bar-wrap {
    flex: 1;
    background: var(--color-neutral-100);
    border-radius: var(--radius-full);
    height: 32px;
}
body.dark-mode .chart-bar-wrap { background: rgba(255,255,255,0.05); }
.chart-bar {
    height: 100%;
    border-radius: var(--radius-full);
    background: linear-gradient(90deg, var(--color-navy), var(--color-info));
    display: flex;
    align-items: center;
    justify-content: flex-end;
    padding-right: 12px;
    width: 0; /* start width 0 for animation */
    transition: width var(--motion-chart, 900ms) ease-out;
}
.animate-chart-in .chart-bar {
    /* The width will be updated via inline style, so just triggering transition */
}
.chart-value {
    color: var(--color-white);
    font-size: var(--fs-xs, 12px);
    font-weight: var(--fw-bold, 700);
}
"""
path = 'booking_room/wwwroot/app.css'
with open(path, 'a', encoding='utf-8') as f: f.write(css)

print("Created RoomUtilizationChart")
