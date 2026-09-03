namespace booking_room.Components.Models;

public class RoomAmenity
{
    public string Name { get; set; } = "";
    public string IconSvgPath { get; set; } = "";

    public RoomAmenity() { }

    public RoomAmenity(string name, string iconSvgPath)
    {
        Name = name;
        IconSvgPath = iconSvgPath;
    }

    public static RoomAmenity Create(string name)
    {
        var norm = name?.Trim().ToLowerInvariant() ?? "";
        var icon = norm switch
        {
            "proyektor" or "projector" or "layar" => "assets/icons/projector.svg",
            "konferensi video" or "video conf" or "video conference" or "kamera video" => "assets/icons/video-conference.svg",
            "papan tulis" or "whiteboard" => "assets/icons/whiteboard.svg",
            "sistem audio" or "audio system" or "speaker" => "assets/icons/audio-system.svg",
            "ac" or "pendingin ruangan" => "assets/icons/ac.svg",
            "wifi" or "wifi kecepatan tinggi" => "assets/icons/wifi.svg",
            "tv led" or "tv" or "monitor" => "assets/icons/tv.svg",
            "aksesibilitas" or "kursi roda" => "assets/icons/accessibility.svg",
            _ => "assets/icons/check.svg"
        };
        return new RoomAmenity(name ?? "", icon);
    }
}

public class Room
{
    public string Id { get; set; } = "";
    public string Name { get; set; } = "";
    public List<RoomAmenity> Amenities { get; set; } = new();
}
