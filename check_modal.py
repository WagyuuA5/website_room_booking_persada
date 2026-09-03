import os

path = 'booking_room/Components/Shared/AppModal.razor'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

has_title = "[Parameter] public string Title" in content
has_subtitle = "[Parameter] public string? Subtitle" in content
has_icon = "[Parameter] public RenderFragment? IconContent" in content

print(f"Title: {has_title}, Subtitle: {has_subtitle}, IconContent: {has_icon}")
