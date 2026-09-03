import os
import re

path = 'booking_room/Components/Pages/User/Beranda.razor'
with open(path, 'r', encoding='utf-8') as f: content = f.read()

content = content.replace('<!-- UI-10 Modal Menunggu Persetujuan -->', '<!-- UI-10 Modal Menunggu Persetujuan -->\n<ScheduleDetailModal Visible="_isScheduleDetailOpen" VisibleChanged="v => _isScheduleDetailOpen = v" />')

content = content.replace('<div class="upcoming-item-row">', '<div class="upcoming-item-row" @onclick="() => _isScheduleDetailOpen = true">')

code_add = """    private bool _isCheckInSuccessOpen;
    private bool _isScheduleDetailOpen;"""
    
content = content.replace('private bool _isCheckInSuccessOpen;', code_add)

with open(path, 'w', encoding='utf-8') as f: f.write(content)
print("Wired ScheduleDetailModal in Beranda")
