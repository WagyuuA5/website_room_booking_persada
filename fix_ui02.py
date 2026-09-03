import os

path = 'booking_room/Components/Shared/RoomDetailsModal.razor'
with open(path, 'r', encoding='utf-8') as f: content = f.read()

content = content.replace('background: var(--color-white, #FFFFFF);', '')
content = content.replace('body.dark-mode .room-detail-layout { background: var(--color-neutral-900, #1D1D1F); }', '')

with open(path, 'w', encoding='utf-8') as f: f.write(content)
print("Removed double background from RoomDetailsModal")
