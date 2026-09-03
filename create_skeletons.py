import os

path1 = 'booking_room/Components/Shared/SkeletonBlock.razor'
with open(path1, 'w', encoding='utf-8') as f:
    f.write("""@namespace booking_room.Components.Shared
<div class="skeleton-block" style="width: @Width; height: @Height; border-radius: @Radius;"></div>

<style>
    .skeleton-block {
        background: linear-gradient(90deg, var(--color-neutral-100, #F5F5F7) 25%, var(--color-neutral-200, #E8E8ED) 50%, var(--color-neutral-100, #F5F5F7) 75%);
        background-size: 200% 100%;
        animation: shimmer 1.5s infinite;
    }
    body.dark-mode .skeleton-block {
        background: linear-gradient(90deg, rgba(255,255,255,0.05) 25%, rgba(255,255,255,0.1) 50%, rgba(255,255,255,0.05) 75%);
        background-size: 200% 100%;
    }
    @keyframes shimmer {
        0% { background-position: 200% 0; }
        100% { background-position: -200% 0; }
    }
</style>

@code {
    [Parameter] public string Width { get; set; } = "100%";
    [Parameter] public string Height { get; set; } = "20px";
    [Parameter] public string Radius { get; set; } = "8px";
}
""")

path2 = 'booking_room/Components/Shared/SkeletonCard.razor'
with open(path2, 'w', encoding='utf-8') as f:
    f.write("""@namespace booking_room.Components.Shared
<div class="skeleton-card">
    <SkeletonBlock Height="160px" Radius="14px 14px 0 0" />
    <div style="padding: 16px;">
        <SkeletonBlock Width="70%" Height="24px" />
        <div style="margin-top: 8px;">
            <SkeletonBlock Width="100%" Height="14px" />
            <div style="margin-top: 4px;">
                <SkeletonBlock Width="60%" Height="14px" />
            </div>
        </div>
    </div>
</div>

<style>
    .skeleton-card {
        border: 1px solid var(--color-neutral-200, #E8E8ED);
        border-radius: var(--radius-md, 14px);
        background: var(--color-white, #FFFFFF);
        overflow: hidden;
    }
    body.dark-mode .skeleton-card {
        border-color: rgba(255,255,255,0.1);
        background: var(--color-neutral-900, #1D1D1F);
    }
</style>
""")

print("Created Skeletons.")
