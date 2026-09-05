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

    public static RoomAmenity Create(string name) => name?.ToLowerInvariant() switch
    {
        "proyektor" or "projector" => new RoomAmenity(name ?? "", "icons/icon_projector.svg"),
        "ac" => new RoomAmenity(name ?? "", "icons/icon_ac.svg"),
        "wifi" => new RoomAmenity(name ?? "", "icons/icon_wifi.svg"),
        "konferensi video" or "video conference" or "video conf" => new RoomAmenity(name ?? "", "icons/icon_video_conf.svg"),
        "papan tulis" or "whiteboard" => new RoomAmenity(name ?? "", "icons/icon_whiteboard.svg"),
        "sistem audio" or "audio system" => new RoomAmenity(name ?? "", "icons/icon_audio.svg"),
        "aksesibilitas" or "accessibility" => new RoomAmenity(name ?? "", "icons/icon_accessibility.svg"),
        "tv" or "tv led" => new RoomAmenity(name ?? "", "icons/icon_tv.svg"),
        _ => new RoomAmenity(name ?? "", "icons/icon_check_circle.svg")
    };
}

public class Room
{
    public string Id { get; set; } = "";
    public string Name { get; set; } = "";
    public List<RoomAmenity> Amenities { get; set; } = new();
}
