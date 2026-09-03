namespace booking_room.Components.Models;

public class RoomAmenity
{
    public string Name { get; set; } = "";
    public string IconSvg { get; set; } = "";
}

public class Room
{
    public string Id { get; set; } = "";
    public string Name { get; set; } = "";
    public List<RoomAmenity> Amenities { get; set; } = new();
}
