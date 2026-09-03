using booking_room.Components.Models;

namespace booking_room.Services;

public static class RoomDataProvider
{
    private static readonly List<RoomItem> _rooms = new()
    {
        new("1", "Executive Boardroom A", 16, "Ruang rapat eksekutif premium dengan fasilitas konferensi video 4K dan internet serat optik kecepatan tinggi untuk pertemuan penting.", "available", new List<string>{"Proyektor", "AC", "Konferensi Video", "WiFi"}, "3", "/images/poto 1.jpg"),
        new("2", "Collaborative Space B", 8, "Ruang kerja kolaboratif dengan tempat duduk modular dan papan tulis luas untuk sesi perancangan ide dan diskusi tim.", "booked", new List<string>{"Papan Tulis", "AC", "WiFi", "Sofa"}, "2", "/images/poto 2.jpg"),
        new("3", "Presentation Hall", 50, "Aula berkapasitas besar cocok untuk rapat divisi akbar atau presentasi klien dengan sistem peredam akustik modern.", "available", new List<string>{"Proyektor", "AC", "Sistem Audio", "WiFi"}, "1", "/images/poto 3.png"),
        new("4", "Delta Studio", 10, "Studio kedap suara dengan sistem audio profesional, ideal untuk lokakarya, podcast, dan siaran langsung persada.", "available", new List<string>{"Sistem Audio", "Proyektor", "AC", "WiFi"}, "1", "/images/poto 4.png"),
        new("5", "Executive Suite", 20, "Suite rapat mewah di lantai atas dengan panorama kota Jakarta dan fasilitas lounge eksklusif.", "available", new List<string>{"Konferensi Video", "TV LED", "AC", "WiFi", "Aksesibilitas"}, "5", "https://images.unsplash.com/photo-1497366216548-37526070297c?auto=format&fit=crop&w=800&q=80"),
        new("6", "Focus Room Alpha", 4, "Ruang kerja tenang kedap suara untuk panggilan konferensi penting dan wawancara daring satu lawan satu.", "available", new List<string>{"AC", "WiFi", "Papan Tulis"}, "3", "https://images.unsplash.com/photo-1497366811353-6870744d04b2?auto=format&fit=crop&w=800&q=80"),
        new("7", "Training Room B", 30, "Ruang pelatihan interaktif dilengkapi meja berderet dan layar ganda untuk sesi edukasi karyawan.", "booked", new List<string>{"Proyektor", "Papan Tulis", "Sistem Audio", "AC", "WiFi"}, "2", "https://images.unsplash.com/photo-1505373877841-8d25f7d46678?auto=format&fit=crop&w=800&q=80"),
        new("8", "Gamma Lounge", 8, "Ruang santai dengan sofa empuk dan fasilitas kopi.", "available", new List<string>{"Sofa", "Kopi", "WiFi", "AC"}, "1", "/images/poto 1.jpg"),
        new("9", "Theta Creative Space", 12, "Area kreatif dengan sofa modular dan papan tulis lebar.", "available", new List<string>{"Sofa", "Papan Tulis", "WiFi", "AC"}, "2", "/images/poto 2.jpg"),
        new("10", "Zeta Conference Hall", 40, "Aula konferensi dengan tata suara profesional dan AC.", "booked", new List<string>{"Sound System", "Proyektor", "AC", "WiFi"}, "1", "/images/poto 3.png")
    };

    public static IReadOnlyList<RoomItem> GetRooms() => _rooms.AsReadOnly();

    public static RoomItem? GetRoomById(string id) => _rooms.FirstOrDefault(r => r.Id == id);

    public static string GetRoomPhoto(string? photoUrl, string roomId = "")
    {
        if (!string.IsNullOrEmpty(photoUrl)) return photoUrl;
        var r = GetRoomById(roomId);
        if (r != null && !string.IsNullOrEmpty(r.PhotoUrl)) return r.PhotoUrl;
        return "/images/poto 1.jpg";
    }
}
