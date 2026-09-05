namespace booking_room.Services;

public class CalendarEventItem
{
    public string Id { get; set; } = Guid.NewGuid().ToString();
    public string RoomId { get; set; } = "1";
    public string RoomName { get; set; } = "Executive Boardroom A";
    public string ActivityTitle { get; set; } = "Rapat Koordinasi Mingguan";
    public string BookerName { get; set; } = "Anggoro Ravi";
    public string Division { get; set; } = "Teknologi Informasi";
    public string Status { get; set; } = "MyBooking"; // MyBooking, Reserved, Pending, Maintenance
    public bool IsRecurring { get; set; } = false;
    public string RecurrenceType { get; set; } = "None"; // None, Daily, Weekly
    public DayOfWeek RecurrenceDay { get; set; } = DayOfWeek.Tuesday;
    public DateTime? RecurrenceEndDate { get; set; }
    public HashSet<DateTime> CancelledInstances { get; set; } = new();
    public DateTime SpecificDate { get; set; }
    public TimeSpan StartTime { get; set; } = new(9, 0, 0);
    public TimeSpan EndTime { get; set; } = new(11, 0, 0);
    public List<string> Attendees { get; set; } = new();
    public bool IsStarred { get; set; } = false;
    public string AdditionalFacilities { get; set; } = "";
    public string FacilityRequestId { get; set; } = "";
}

public interface ICalendarBookingService
{
    IReadOnlyList<CalendarEventItem> GetAllEvents();
    List<CalendarEventItem> GetEventsForDateRange(DateTime startOfWeek, DateTime endOfWeek);
    void CancelInstance(string eventId, DateTime date);
    void AddEvent(CalendarEventItem ev);
    event Action? OnChange;
}

public class CalendarBookingService : ICalendarBookingService
{
    private readonly List<CalendarEventItem> _events = new();
    public event Action? OnChange;

    public CalendarBookingService()
    {
        // Reference Monday for current test anchor (31 Aug 2026 or dynamic current week)
        var baseMonday = DateTime.Today.AddDays(-(int)DateTime.Today.DayOfWeek + (int)DayOfWeek.Monday);
        if (DateTime.Today.DayOfWeek == DayOfWeek.Sunday) baseMonday = baseMonday.AddDays(-7);

        // 1. Weekly recurring "Boardroom Alpha" / Executive Boardroom A (Booking Saya) - Every Tuesday 09:00 - 11:00
        _events.Add(new CalendarEventItem
        {
            Id = "EV-101",
            RoomId = "1",
            RoomName = "Executive Boardroom A",
            ActivityTitle = "Rapat Perencanaan Strategis Q3 & Evaluasi",
            BookerName = "Anggoro Ravi",
            Division = "Teknologi Informasi",
            Status = "MyBooking",
            IsRecurring = true,
            RecurrenceType = "Weekly",
            RecurrenceDay = DayOfWeek.Tuesday,
            RecurrenceEndDate = baseMonday.AddMonths(3),
            SpecificDate = baseMonday.AddDays(1), // Tuesday
            StartTime = new TimeSpan(9, 0, 0),
            EndTime = new TimeSpan(11, 0, 0),
            Attendees = new List<string> { "Budi Santoso", "Siti Rahayu", "Dewi Lestari", "Rian Hidayat" },
            IsStarred = true,
            AdditionalFacilities = "Proyektor 4K, Catering Kopi (15 pax), Unit AV Eksternal",
            FacilityRequestId = "FR-101"
        });

        // 2. Weekly recurring "Focus Room B" (Booking Saya) - Every Thursday 14:00 - 16:00
        _events.Add(new CalendarEventItem
        {
            Id = "EV-102",
            RoomId = "6",
            RoomName = "Focus Room Alpha",
            ActivityTitle = "Wawancara Kandidat Senior Frontend Engineer",
            BookerName = "Anggoro Ravi",
            Division = "Teknologi Informasi",
            Status = "MyBooking",
            IsRecurring = true,
            RecurrenceType = "Weekly",
            RecurrenceDay = DayOfWeek.Thursday,
            RecurrenceEndDate = baseMonday.AddMonths(2),
            SpecificDate = baseMonday.AddDays(3), // Thursday
            StartTime = new TimeSpan(14, 0, 0),
            EndTime = new TimeSpan(16, 0, 0),
            Attendees = new List<string> { "HR Talent Acquisition", "Kandidat Pelamar" },
            IsStarred = true,
            AdditionalFacilities = "Webcam HD & Mic Eksternal"
        });

        // 3. Reserved by another division - Collaborative Space B - Monday 10:00 - 12:00
        _events.Add(new CalendarEventItem
        {
            Id = "EV-103",
            RoomId = "2",
            RoomName = "Collaborative Space B",
            ActivityTitle = "Sprint Planning Divisi Marketing",
            BookerName = "Rina Marlina",
            Division = "Pemasaran & Komunikasi",
            Status = "Reserved",
            IsRecurring = false,
            SpecificDate = baseMonday, // Monday
            StartTime = new TimeSpan(10, 0, 0),
            EndTime = new TimeSpan(12, 0, 0),
            Attendees = new List<string> { "Tim Pemasaran (6 org)" },
            IsStarred = false
        });

        // 4. Pending Approval - Presentation Hall - Wednesday 13:00 - 15:30
        _events.Add(new CalendarEventItem
        {
            Id = "EV-104",
            RoomId = "3",
            RoomName = "Presentation Hall",
            ActivityTitle = "Sosialisasi Benefit & Asuransi Karyawan",
            BookerName = "Ahmad Zaki",
            Division = "Sumber Daya Manusia (SDM)",
            Status = "Pending",
            IsRecurring = false,
            SpecificDate = baseMonday.AddDays(2), // Wednesday
            StartTime = new TimeSpan(13, 0, 0),
            EndTime = new TimeSpan(15, 30, 0),
            Attendees = new List<string> { "Seluruh Karyawan Baru (35 org)" },
            IsStarred = false,
            AdditionalFacilities = "Sound System, 2 Mic Wireless, Layar Proyektor Utama"
        });

        // 5. Maintenance - Delta Studio - Friday 08:30 - 11:30
        _events.Add(new CalendarEventItem
        {
            Id = "EV-105",
            RoomId = "4",
            RoomName = "Delta Studio",
            ActivityTitle = "Pemeliharaan Rutin Panel Akustik & Mixer Audio",
            BookerName = "Divisi Sarana & Prasarana",
            Division = "Umum & Pengadaan",
            Status = "Maintenance",
            IsRecurring = false,
            SpecificDate = baseMonday.AddDays(4), // Friday
            StartTime = new TimeSpan(8, 30, 0),
            EndTime = new TimeSpan(11, 30, 0),
            Attendees = new List<string> { "Teknisi Vendor Audio" },
            IsStarred = false
        });

        // 6. Another Reserved - Executive Suite - Wednesday 09:00 - 11:00
        _events.Add(new CalendarEventItem
        {
            Id = "EV-106",
            RoomId = "5",
            RoomName = "Executive Suite",
            ActivityTitle = "Kunjungan Mitra Korporasi FinTech",
            BookerName = "Direktur Operasional",
            Division = "Direksi & Komisaris",
            Status = "Reserved",
            IsRecurring = false,
            SpecificDate = baseMonday.AddDays(2),
            StartTime = new TimeSpan(9, 0, 0),
            EndTime = new TimeSpan(11, 0, 0),
            Attendees = new List<string> { "Delegasi Bank Mitra (5 org)" },
            IsStarred = false
        });
    }

    public IReadOnlyList<CalendarEventItem> GetAllEvents() => _events.AsReadOnly();

    public List<CalendarEventItem> GetEventsForDateRange(DateTime startOfWeek, DateTime endOfWeek)
    {
        var result = new List<CalendarEventItem>();

        foreach (var ev in _events)
        {
            if (ev.IsRecurring)
            {
                if (ev.RecurrenceType == "Weekly")
                {
                    // Find the date in this week that matches RecurrenceDay
                    int diff = ((int)ev.RecurrenceDay - (int)startOfWeek.DayOfWeek + 7) % 7;
                    var occurrenceDate = startOfWeek.Date.AddDays(diff);

                    if (occurrenceDate >= startOfWeek.Date && occurrenceDate <= endOfWeek.Date)
                    {
                        if (ev.RecurrenceEndDate == null || occurrenceDate <= ev.RecurrenceEndDate.Value.Date)
                        {
                            if (!ev.CancelledInstances.Contains(occurrenceDate))
                            {
                                result.Add(new CalendarEventItem
                                {
                                    Id = ev.Id,
                                    RoomId = ev.RoomId,
                                    RoomName = ev.RoomName,
                                    ActivityTitle = ev.ActivityTitle,
                                    BookerName = ev.BookerName,
                                    Division = ev.Division,
                                    Status = ev.Status,
                                    IsRecurring = true,
                                    RecurrenceType = ev.RecurrenceType,
                                    RecurrenceDay = ev.RecurrenceDay,
                                    RecurrenceEndDate = ev.RecurrenceEndDate,
                                    SpecificDate = occurrenceDate,
                                    StartTime = ev.StartTime,
                                    EndTime = ev.EndTime,
                                    Attendees = ev.Attendees,
                                    IsStarred = ev.IsStarred,
                                    AdditionalFacilities = ev.AdditionalFacilities,
                                    FacilityRequestId = ev.FacilityRequestId
                                });
                            }
                        }
                    }
                }
                else if (ev.RecurrenceType == "Daily")
                {
                    // Monday to Friday
                    for (int i = 0; i < 5; i++)
                    {
                        var curDate = startOfWeek.Date.AddDays(i);
                        if (ev.RecurrenceEndDate == null || curDate <= ev.RecurrenceEndDate.Value.Date)
                        {
                            if (!ev.CancelledInstances.Contains(curDate))
                            {
                                result.Add(new CalendarEventItem
                                {
                                    Id = ev.Id,
                                    RoomId = ev.RoomId,
                                    RoomName = ev.RoomName,
                                    ActivityTitle = ev.ActivityTitle,
                                    BookerName = ev.BookerName,
                                    Division = ev.Division,
                                    Status = ev.Status,
                                    IsRecurring = true,
                                    RecurrenceType = ev.RecurrenceType,
                                    SpecificDate = curDate,
                                    StartTime = ev.StartTime,
                                    EndTime = ev.EndTime,
                                    Attendees = ev.Attendees,
                                    IsStarred = ev.IsStarred,
                                    AdditionalFacilities = ev.AdditionalFacilities
                                });
                            }
                        }
                    }
                }
            }
            else
            {
                if (ev.SpecificDate.Date >= startOfWeek.Date && ev.SpecificDate.Date <= endOfWeek.Date)
                {
                    if (!ev.CancelledInstances.Contains(ev.SpecificDate.Date))
                    {
                        result.Add(ev);
                    }
                }
            }
        }

        return result;
    }

    public void CancelInstance(string eventId, DateTime date)
    {
        var ev = _events.FirstOrDefault(e => e.Id == eventId);
        if (ev != null)
        {
            if (ev.IsRecurring)
            {
                ev.CancelledInstances.Add(date.Date);
            }
            else
            {
                _events.Remove(ev);
            }
            OnChange?.Invoke();
        }
    }

    public void AddEvent(CalendarEventItem ev)
    {
        _events.Add(ev);
        OnChange?.Invoke();
    }
}
