namespace booking_room.Services;

public record RequestedFacilityItem(string Name, int Quantity, string Note, string IconType);

public class FacilityRequestItem
{
    public string Id { get; set; } = Guid.NewGuid().ToString();
    public string RoomId { get; set; } = "1";
    public string RoomName { get; set; } = "Executive Boardroom A";
    public string RoomPhotoUrl { get; set; } = "/images/poto 1.jpg";
    public string BookerName { get; set; } = "Anggoro Ravi";
    public string Division { get; set; } = "Teknologi Informasi";
    public DateTime BookingDate { get; set; } = DateTime.Today.AddDays(2);
    public string BookingTime { get; set; } = "09:00 - 11:00 WIB";
    public DateTime RequestedAt { get; set; } = DateTime.Now.AddHours(-3);
    public string Status { get; set; } = "Sedang Disiapkan"; // Sedang Disiapkan, Menunggu, Siap
    public DateTime StatusUpdatedAt { get; set; } = DateTime.Now.AddMinutes(-30);
    public List<RequestedFacilityItem> Items { get; set; } = new();
    public string Notes { get; set; } = string.Empty;
}

public interface IFacilityRequestService
{
    IReadOnlyList<FacilityRequestItem> GetRequests();
    FacilityRequestItem? GetRequestById(string id);
    void AddRequest(FacilityRequestItem request);
    event Action? OnChange;
}

public class FacilityRequestService : IFacilityRequestService
{
    private readonly List<FacilityRequestItem> _requests = new()
    {
        new FacilityRequestItem
        {
            Id = "FR-101",
            RoomId = "1",
            RoomName = "Executive Boardroom A",
            RoomPhotoUrl = "/images/poto 1.jpg",
            BookerName = "Anggoro Ravi",
            Division = "Teknologi Informasi",
            BookingDate = DateTime.Today.AddDays(1),
            BookingTime = "09:00 - 11:00 WIB",
            RequestedAt = DateTime.Now.AddHours(-4),
            Status = "Sedang Disiapkan",
            StatusUpdatedAt = DateTime.Now.AddHours(-1),
            Items = new List<RequestedFacilityItem>
            {
                new("Proyektor 4K", 1, "Siapkan kabel HDMI panjang", "projector"),
                new("Catering Kopi & Snack", 12, "Coffee break jam 10:00", "catering"),
                new("Unit AV Eksternal", 1, "Testing mic sebelum rapat", "speaker")
            },
            Notes = "Rapat koordinasi dewan direksi kuartal 4, harap dipastikan tepat waktu."
        },
        new FacilityRequestItem
        {
            Id = "FR-102",
            RoomId = "2",
            RoomName = "Collaborative Space B",
            RoomPhotoUrl = "/images/poto 2.jpg",
            BookerName = "Siti Rahayu",
            Division = "Operasional",
            BookingDate = DateTime.Today.AddDays(3),
            BookingTime = "13:30 - 15:30 WIB",
            RequestedAt = DateTime.Now.AddDays(-1),
            Status = "Menunggu",
            StatusUpdatedAt = DateTime.Now.AddDays(-1),
            Items = new List<RequestedFacilityItem>
            {
                new("Kursi Tambahan", 4, "Susun melingkar di sudut", "chair"),
                new("Papan Tulis Flipchart", 2, "Lengkap dengan spidol warna", "whiteboard")
            },
            Notes = "Sesi brainstorming tim operasional cabang baru."
        },
        new FacilityRequestItem
        {
            Id = "FR-103",
            RoomId = "3",
            RoomName = "Presentation Hall",
            RoomPhotoUrl = "/images/poto 3.png",
            BookerName = "Budi Santoso",
            Division = "Sumber Daya Manusia (SDM)",
            BookingDate = DateTime.Today.AddDays(5),
            BookingTime = "10:00 - 12:00 WIB",
            RequestedAt = DateTime.Now.AddDays(-2),
            Status = "Siap",
            StatusUpdatedAt = DateTime.Now.AddHours(-2),
            Items = new List<RequestedFacilityItem>
            {
                new("Microphone Wireless", 4, "Baterai cadangan tersedia", "mic"),
                new("Sound System Podium", 1, "Preset suara vokal jernih", "speaker")
            },
            Notes = "Townhall bulanan seluruh karyawan divisi SDM."
        }
    };

    public event Action? OnChange;

    public IReadOnlyList<FacilityRequestItem> GetRequests() => _requests.OrderByDescending(r => r.RequestedAt).ToList().AsReadOnly();

    public FacilityRequestItem? GetRequestById(string id) => _requests.FirstOrDefault(r => r.Id == id);

    public void AddRequest(FacilityRequestItem request)
    {
        _requests.Insert(0, request);
        OnChange?.Invoke();
    }
}
