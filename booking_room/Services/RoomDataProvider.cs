using booking_room.Components.Models;

namespace booking_room.Services;

public static class RoomDataProvider
{
    private static readonly List<RoomItem> _rooms = new()
    {
        new("1", "Executive Boardroom A", 16, "Ruang rapat eksekutif premium dengan fasilitas konferensi video 4K dan internet serat optik kecepatan tinggi untuk pertemuan penting.", "available", new List<string>{"Proyektor", "AC", "Konferensi Video", "WiFi"}, "3", "https://images.unsplash.com/photo-1497366216548-37526070297c?auto=format&fit=crop&w=800&q=80"),
        new("2", "Collaborative Space B", 8, "Ruang kerja kolaboratif dengan tempat duduk modular dan papan tulis luas untuk sesi perancangan ide dan diskusi tim.", "booked", new List<string>{"Papan Tulis", "AC", "WiFi", "Sofa"}, "2", "https://images.unsplash.com/photo-1524758631624-e2822e304c36?auto=format&fit=crop&w=800&q=80"),
        new("3", "Presentation Hall", 50, "Aula berkapasitas besar cocok untuk rapat divisi akbar atau presentasi klien dengan sistem peredam akustik modern.", "available", new List<string>{"Proyektor", "AC", "Sistem Audio", "WiFi"}, "1", "https://images.unsplash.com/photo-1431540015160-0295aaa24f7f?auto=format&fit=crop&w=800&q=80"),
        new("4", "Delta Studio", 10, "Studio kedap suara dengan sistem audio profesional, ideal untuk lokakarya, podcast, dan siaran langsung persada.", "available", new List<string>{"Sistem Audio", "Proyektor", "AC", "WiFi"}, "1", "https://images.unsplash.com/photo-1505373877841-8d25f7d46678?auto=format&fit=crop&w=800&q=80"),
        new("5", "Executive Suite", 20, "Suite rapat mewah di lantai atas dengan panorama kota Jakarta dan fasilitas lounge eksklusif.", "available", new List<string>{"Konferensi Video", "TV LED", "AC", "WiFi", "Aksesibilitas"}, "5", "https://images.unsplash.com/photo-1462826303086-329426d1aef5?auto=format&fit=crop&w=800&q=80"),
        new("6", "Focus Room Alpha", 4, "Ruang kerja tenang kedap suara untuk panggilan konferensi penting dan wawancara daring satu lawan satu.", "available", new List<string>{"AC", "WiFi", "Papan Tulis"}, "3", "https://images.unsplash.com/photo-1497215842964-222b430dc094?auto=format&fit=crop&w=800&q=80"),
        new("7", "Training Room B", 30, "Ruang pelatihan interaktif dilengkapi meja berderet dan layar ganda untuk sesi edukasi karyawan.", "booked", new List<string>{"Proyektor", "Papan Tulis", "Sistem Audio", "AC", "WiFi"}, "2", "https://images.unsplash.com/photo-1524758631624-e2822e304c36?auto=format&fit=crop&w=800&q=80"),
        new("8", "Huddle Space C", 6, "Ruang kolaborasi kompak dengan TV interaktif dan konektivitas kilat untuk sesi sinkronisasi tim lincah.", "available", new List<string>{"Smart TV", "AC", "WiFi", "Papan Tulis"}, "1", "https://images.unsplash.com/photo-1497366811353-6870744d04b2?auto=format&fit=crop&w=800&q=80"),
        new("9", "Conference Hall", 50, "Aula konferensi utama representatif dengan tata suara panggung mutakhir, proyektor ganda, dan ruang leluasa.", "available", new List<string>{"Proyektor", "Sound System", "AC", "WiFi", "Podium"}, "1", "https://images.unsplash.com/photo-1431540015160-0295aaa24f7f?auto=format&fit=crop&w=800&q=80"),
        new("10", "Innovation Lab", 15, "Laboratorium inovasi dan riset dengan perangkat teknologi modern, meja modular fleksibel, dan layar interaktif.", "available", new List<string>{"Smart TV", "Whiteboard", "Proyektor", "AC", "WiFi"}, "3", "https://images.unsplash.com/photo-1497366754888-5a456d4b3447?auto=format&fit=crop&w=800&q=80"),
        new("11", "Gamma Lounge", 8, "Ruang santai dengan sofa empuk dan fasilitas kopi.", "available", new List<string>{"Sofa", "Kopi", "WiFi", "AC"}, "1", "https://images.unsplash.com/photo-1497366216548-37526070297c?auto=format&fit=crop&w=800&q=80"),
        new("12", "Theta Creative Space", 12, "Area kreatif dengan sofa modular dan papan tulis lebar.", "available", new List<string>{"Sofa", "Papan Tulis", "WiFi", "AC"}, "2", "https://images.unsplash.com/photo-1524758631624-e2822e304c36?auto=format&fit=crop&w=800&q=80")
    };

    public static IReadOnlyList<RoomItem> GetRooms() => _rooms.AsReadOnly();

    public static RoomItem? GetRoomById(string id) => _rooms.FirstOrDefault(r => r.Id == id);

    public static string GetRoomPhoto(string? photoUrl, string roomIdOrName = "")
    {
        if (!string.IsNullOrEmpty(photoUrl)) return photoUrl;
        var r = _rooms.FirstOrDefault(x => x.Id == roomIdOrName || x.Name.Equals(roomIdOrName, StringComparison.OrdinalIgnoreCase));
        if (r != null && !string.IsNullOrEmpty(r.PhotoUrl)) return r.PhotoUrl;
        return "https://images.unsplash.com/photo-1497366216548-37526070297c?auto=format&fit=crop&w=800&q=80";
    }
}
