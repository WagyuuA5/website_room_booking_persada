import os

path = 'booking_room/Components/Shared/AppModal.razor'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

# Add Subtitle and IconContent
if "[Parameter] public string? Subtitle" not in content:
    content = content.replace("[Parameter] public string Title { get; set; } = string.Empty;", """[Parameter] public string? Title { get; set; } = string.Empty;
    [Parameter] public string? Subtitle { get; set; }
    [Parameter] public Microsoft.AspNetCore.Components.RenderFragment? IconContent { get; set; }""")

# Replace modal header rendering
old_header = """<div class="modal-default-header">
                            <h3 id="modal-title-heading" class="modal-heading-text">@Title</h3>
                        </div>"""

new_header = """<div class="modal-default-header" style="display: flex; align-items: center; gap: 12px;">
                            @if (IconContent != null)
                            {
                                <div class="modal-header-icon">
                                    @IconContent
                                </div>
                            }
                            <div>
                                @if (!string.IsNullOrEmpty(Title))
                                {
                                    <h3 id="modal-title-heading" class="modal-heading-text" style="margin: 0; font-size: 1.25rem; font-weight: 700;">@Title</h3>
                                }
                                @if (!string.IsNullOrEmpty(Subtitle))
                                {
                                    <p class="modal-subtitle-text" style="margin: 4px 0 0 0; font-size: 0.875rem; color: var(--color-neutral-600, #6B7280);">@Subtitle</p>
                                }
                            </div>
                        </div>"""
content = content.replace(old_header, new_header)

# Standardize Backdrop (DS-04)
# Currently: background-color: rgba(15, 23, 42, 0.65); backdrop-filter: blur(8px);
old_backdrop = """background-color: rgba(15, 23, 42, 0.65);
        backdrop-filter: blur(8px);
        -webkit-backdrop-filter: blur(8px);"""
new_backdrop = """background: rgba(15, 23, 42, 0.45);
        backdrop-filter: blur(5px);
        -webkit-backdrop-filter: blur(5px);"""
content = content.replace(old_backdrop, new_backdrop)

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)
print("AppModal.razor updated.")
