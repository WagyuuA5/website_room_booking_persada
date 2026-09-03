import os

path = 'booking_room/Components/Pages/User/Beranda.razor'
with open(path, 'r', encoding='utf-8') as f: content = f.read()

# Let's replace everything after `</NotificationBanner>` or `<div class="hero-welcome-card">` up to `<!-- Right Col -->` or similar.
# Wait, I'll just write a whole new Beranda.razor to be safe and perfectly match DASH-01, DASH-02, DASH-03, DASH-04.
