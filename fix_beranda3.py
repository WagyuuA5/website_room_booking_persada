import os
import re

path = 'booking_room/Components/Pages/User/Beranda.razor'
with open(path, 'r', encoding='utf-8') as f: content = f.read()

# I will find the left column of dashboard-main-columns and place the chart there
# Wait, dashboard-main-columns has:
# <div class="dashboard-card">
#     <div class="dashboard-card-header">
#         <div>
#             <h3 class="card-title">Jadwal Pertemuan Mendatang</h3>

# Let's see the right column:
# <div class="dashboard-card">
#     <div class="dashboard-card-header">
#         <div>
#             <h3 class="card-title">Ruangan Paling Sering Dipesan</h3>

# We replace the entire right column with `<RoomUtilizationChart />`!
# Well, wait, the prompt says "Card baru di bawah baris kartu ringkasan ... Isi: horizontal bar chart".
# I'll replace the old "Ruangan Paling Sering Dipesan" with `RoomUtilizationChart`.
content = re.sub(
    r'<div class="dashboard-card">\s*<div class="dashboard-card-header">\s*<div>\s*<h3 class="card-title">Ruangan Paling Sering Dipesan</h3>.*?</div>\s*</div>\s*</div>',
    '<RoomUtilizationChart />',
    content, flags=re.DOTALL
)

with open(path, 'w', encoding='utf-8') as f: f.write(content)
print("Added RoomUtilizationChart to Beranda")
