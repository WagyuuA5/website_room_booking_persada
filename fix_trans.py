import os

path = 'booking_room/Components/Shared/NotificationBanner.razor'
with open(path, 'r', encoding='utf-8') as f: content = f.read()

content = content.replace("Konfirmasi Kehadiran Sekarang", "Check-in Sekarang")

with open(path, 'w', encoding='utf-8') as f: f.write(content)
print("Updated translations in NotificationBanner")
