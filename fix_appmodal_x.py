import os
import re

path = 'booking_room/Components/Shared/AppModal.razor'
with open(path, 'r', encoding='utf-8') as f: content = f.read()

# Remove the close button X completely
content = re.sub(
    r'@if\s*\(ShowCloseButton\)\s*\{\s*<button[^>]*>\s*<svg[^>]*>.*?</svg>\s*</button>\s*\}', 
    '', 
    content, flags=re.DOTALL
)

with open(path, 'w', encoding='utf-8') as f: f.write(content)
print("Removed X icon from AppModal")
