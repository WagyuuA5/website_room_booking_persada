import os

path = 'booking_room/Components/Pages/Bookings.razor'
with open(path, 'r', encoding='utf-8') as f: content = f.read()
dummy_rooms = """        _allRooms = new List<RoomItem>
        {
            new("1", "Alpha Boardroom", 12, "Lantai 3", "available", new List<string>{"Proyektor","Papan Tulis"}, "https://images.unsplash.com/photo-1497215842964-222b430dc094?auto=format&fit=crop&w=400&q=80", "Ruang meeting direksi dengan pemandangan kota."),
            new("2", "Beta Meeting", 8, "Lantai 2", "booked", new List<string>{"TV LED"}, "https://images.unsplash.com/photo-1431540015160-0295aaa24f7f?auto=format&fit=crop&w=400&q=80", "Ruang meeting standar."),
            new("3", "Gamma Discussion", 4, "Lantai 2", "unavailable", new List<string>{"Papan Tulis"}, "https://images.unsplash.com/photo-1497366754888-5a456d4b3447?auto=format&fit=crop&w=400&q=80", "Cocok untuk diskusi kelompok kecil."),
            new("4", "Delta Studio", 20, "Lantai 1", "available", new List<string>{"Audio System"}, "https://images.unsplash.com/photo-1462826303086-329426d1aef5?auto=format&fit=crop&w=400&q=80", "Ruangan kedap suara.")
        };"""
# replace the old dummy rooms
old_dummy_rooms = """        _allRooms = new List<RoomItem>
        {
            new() { Id="1", Name="Alpha Boardroom", Capacity=12, Floor="Lantai 3", Amenities=new List<string>{"Proyektor","Papan Tulis"}, PhotoUrl="https://images.unsplash.com/photo-1497215842964-222b430dc094?auto=format&fit=crop&w=400&q=80" },
            new() { Id="2", Name="Beta Meeting", Capacity=8, Floor="Lantai 2", Amenities=new List<string>{"TV LED"}, PhotoUrl="https://images.unsplash.com/photo-1431540015160-0295aaa24f7f?auto=format&fit=crop&w=400&q=80" },
            new() { Id="3", Name="Gamma Discussion", Capacity=4, Floor="Lantai 2", Amenities=new List<string>{"Papan Tulis"}, PhotoUrl="https://images.unsplash.com/photo-1497366754888-5a456d4b3447?auto=format&fit=crop&w=400&q=80" },
            new() { Id="4", Name="Delta Studio", Capacity=20, Floor="Lantai 1", Amenities=new List<string>{"Audio System"}, PhotoUrl="https://images.unsplash.com/photo-1462826303086-329426d1aef5?auto=format&fit=crop&w=400&q=80" }
        };"""
content = content.replace(old_dummy_rooms, dummy_rooms)
with open(path, 'w', encoding='utf-8') as f: f.write(content)

path = 'booking_room/Components/Shared/FacilityRequestView.razor'
with open(path, 'r', encoding='utf-8') as f: content = f.read()
content = content.replace('_isDetailOpen = false', '/* removed */')
content = content.replace('() => _isDetailOpen = false', '() => _selectedReq = null')
with open(path, 'w', encoding='utf-8') as f: f.write(content)

print("Fixed.")
