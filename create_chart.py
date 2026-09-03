import os

path = 'booking_room/Components/Shared/UserTrendChart.razor'
new_content = """@namespace booking_room.Components.Shared
@inject IJSRuntime JSRuntime

<div class="chart-container">
    <div class="chart-header">
        <h3 class="chart-title">Tren Pemesanan Saya</h3>
        <p class="chart-subtitle">Statistik pemesanan 7 hari terakhir</p>
    </div>
    
    <div class="chart-canvas-wrapper" style="position: relative; height: 250px; width: 100%;">
        <canvas id="@_chartId"></canvas>
    </div>
</div>

<style>
    .chart-container {
        background: var(--color-white, #FFFFFF);
        border: 1px solid var(--color-neutral-200, #E8E8ED);
        border-radius: var(--radius-md, 14px);
        padding: 20px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.04);
        margin-top: 24px;
        animation: slideUpFade var(--motion-chart, 900ms ease-out) forwards;
    }
    body.dark-mode .chart-container {
        background: var(--color-neutral-900, #1D1D1F);
        border-color: rgba(255,255,255,0.1);
    }
    .chart-header { margin-bottom: 20px; }
    .chart-title {
        font-size: var(--fs-h4, 18px);
        font-weight: var(--fw-bold, 700);
        margin: 0 0 4px 0;
        color: var(--color-navy, #0F172A);
    }
    body.dark-mode .chart-title { color: var(--color-white, #FFFFFF); }
    .chart-subtitle {
        font-size: var(--fs-sm, 14px);
        color: var(--color-neutral-600, #6E6E73);
        margin: 0;
    }

    @keyframes slideUpFade {
        from { opacity: 0; transform: translateY(20px); }
        to { opacity: 1; transform: translateY(0); }
    }
</style>

@code {
    private string _chartId = "chart-" + Guid.NewGuid().ToString("N");
    
    protected override async Task OnAfterRenderAsync(bool firstRender)
    {
        if (firstRender)
        {
            // Placeholder: in a real implementation we would invoke a JS charting library (e.g. Chart.js)
            // Example:
            // await JSRuntime.InvokeVoidAsync("renderUserTrendChart", _chartId);
        }
    }
}
"""
with open(path, 'w', encoding='utf-8') as f:
    f.write(new_content)

print("UserTrendChart.razor created.")
