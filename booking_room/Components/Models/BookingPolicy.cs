namespace booking_room.Components.Models;

/// <summary>
/// Single source of truth for booking statuses.
/// String values are strictly mapped here, eliminating fragile string-matching across components.
/// </summary>
public enum BookingStatus
{
    Pending,
    Approved,
    Rejected,
    Canceled,
    Completed,
    Reserved,
    Maintenance,
    Unknown
}

/// <summary>
/// Centralized SOP Policy for booking actions across the entire application.
/// Strictly enforces that cancellation and modification are ONLY allowed for BookingStatus.Pending ("Menunggu Persetujuan").
/// </summary>
public static class BookingPolicy
{
    /// <summary>
    /// Parses any known string representation (English or Indonesian) into the strongly-typed BookingStatus enum.
    /// </summary>
    public static BookingStatus ParseStatus(string? status)
    {
        if (string.IsNullOrWhiteSpace(status)) return BookingStatus.Unknown;
        var s = status.Trim().ToLowerInvariant();
        return s switch
        {
            "pending" or "menunggu" or "menunggu persetujuan" => BookingStatus.Pending,
            "approved" or "disetujui" or "mybooking" => BookingStatus.Approved,
            "rejected" or "ditolak" => BookingStatus.Rejected,
            "canceled" or "cancelled" or "dibatalkan" => BookingStatus.Canceled,
            "completed" or "selesai" => BookingStatus.Completed,
            "reserved" or "dipesan" => BookingStatus.Reserved,
            "maintenance" or "pemeliharaan" or "perawatan" => BookingStatus.Maintenance,
            _ => BookingStatus.Unknown
        };
    }

    /// <summary>
    /// Checks if a booking with the given status enum can be canceled.
    /// Strictly BookingStatus.Pending ("Menunggu Persetujuan").
    /// </summary>
    public static bool CanCancelBooking(BookingStatus status) => status == BookingStatus.Pending;
    public static bool CanCancelBooking(string? status) => CanCancelBooking(ParseStatus(status));

    /// <summary>
    /// Checks if a booking with the given status enum can be modified / rescheduled.
    /// Strictly BookingStatus.Pending ("Menunggu Persetujuan").
    /// </summary>
    public static bool CanModifyBooking(BookingStatus status) => status == BookingStatus.Pending;
    public static bool CanModifyBooking(string? status) => CanModifyBooking(ParseStatus(status));

    /// <summary>
    /// Checks if the informative "Lihat Jadwal Ruangan" button can be shown.
    /// Informative and read-only; hidden for pending approval (Menunggu Persetujuan) status.
    /// </summary>
    public static bool CanViewRoomSchedule(BookingStatus status) => status != BookingStatus.Pending;
    public static bool CanViewRoomSchedule(string? status) => CanViewRoomSchedule(ParseStatus(status));

    /// <summary>
    /// Returns the Indonesian user-facing label for a status.
    /// </summary>
    public static string GetStatusDisplayLabel(BookingStatus status) => status switch
    {
        BookingStatus.Pending => "Menunggu Persetujuan",
        BookingStatus.Approved => "Disetujui",
        BookingStatus.Rejected => "Ditolak",
        BookingStatus.Canceled => "Dibatalkan",
        BookingStatus.Completed => "Selesai",
        BookingStatus.Reserved => "Dipesan",
        BookingStatus.Maintenance => "Perawatan",
        _ => "Tidak Diketahui"
    };

    public static string GetStatusDisplayLabel(string? status) => GetStatusDisplayLabel(ParseStatus(status));
}
