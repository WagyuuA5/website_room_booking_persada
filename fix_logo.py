import os

path = 'booking_room/Components/Layout/NavMenu.razor.css'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

# Make the logo smaller (DS-12)
if ".navbar-brand-logo" in content:
    content = content.replace("width: 86.883px;", "width: 32px;")
    content = content.replace("height: 48px;", "height: 32px; object-fit: contain;")
else:
    content += "\n.navbar-brand-logo { width: 32px !important; height: 32px !important; object-fit: contain; }"

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)
print("NavMenu.razor.css updated.")
