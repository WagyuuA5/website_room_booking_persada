namespace booking_room.Services;

public static class FacilityIconMapper
{
    private static readonly Dictionary<string, string[]> KeywordMap = new(StringComparer.OrdinalIgnoreCase)
    {
        ["speaker"] = new[] { "sound", "speaker", "suara", "sound system", "audio", "toa" },
        ["projector"] = new[] { "proyektor", "projector", "infocus" },
        ["mic"] = new[] { "mic", "mikrofon", "microphone", "clip on" },
        ["chair"] = new[] { "kursi", "chair", "extra chair", "kursi tambahan", "seat" },
        ["table"] = new[] { "meja", "table", "desk", "meja rapat" },
        ["ac"] = new[] { "ac", "pendingin", "air conditioner", "kipas", "ventilasi" },
        ["tv"] = new[] { "tv", "layar", "screen", "monitor", "display", "smart tv" },
        ["cable"] = new[] { "kabel", "cable", "hdmi", "adaptor", "adapter", "converter", "colokan", "vga" },
        ["whiteboard"] = new[] { "whiteboard", "papan tulis", "flipchart", "spidol", "marker" },
        ["camera"] = new[] { "kamera", "camera", "webcam", "video" },
        ["wifi"] = new[] { "wifi", "internet", "lan", "hotspot" },
        ["catering"] = new[] { "kopi", "coffee", "catering", "makanan", "snack", "teh", "konsumsi", "minum", "air" },
        ["printer"] = new[] { "printer", "cetak", "fotokopi", "scanner" }
    };

    public static string GetIconType(string query)
    {
        if (string.IsNullOrWhiteSpace(query)) return "default";

        var clean = query.Trim().ToLowerInvariant();

        foreach (var (iconType, keywords) in KeywordMap)
        {
            foreach (var kw in keywords)
            {
                if (clean.Contains(kw, StringComparison.OrdinalIgnoreCase) || kw.Contains(clean, StringComparison.OrdinalIgnoreCase))
                {
                    return iconType;
                }
            }
        }

        return "default";
    }

    public static string GetSvgIcon(string iconType)
    {
        return iconType switch
        {
            "speaker" => "<svg width=\"20\" height=\"20\" viewBox=\"0 0 24 24\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2\" stroke-linecap=\"round\" stroke-linejoin=\"round\"><polygon points=\"11 5 6 9 2 9 2 15 6 15 11 19 11 5\"></polygon><path d=\"M15.54 8.46a5 5 0 0 1 0 7.07\"></path><path d=\"M19.07 4.93a10 10 0 0 1 0 14.14\"></path></svg>",
            "projector" => "<svg width=\"20\" height=\"20\" viewBox=\"0 0 24 24\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2\" stroke-linecap=\"round\" stroke-linejoin=\"round\"><rect x=\"2\" y=\"7\" width=\"20\" height=\"10\" rx=\"2\"></rect><circle cx=\"17\" cy=\"12\" r=\"2\"></circle><line x1=\"6\" y1=\"11\" x2=\"6.01\" y2=\"11\"></line><line x1=\"10\" y1=\"11\" x2=\"10.01\" y2=\"11\"></line><line x1=\"6\" y1=\"17\" x2=\"6\" y2=\"19\"></line><line x1=\"18\" y1=\"17\" x2=\"18\" y2=\"19\"></line></svg>",
            "mic" => "<svg width=\"20\" height=\"20\" viewBox=\"0 0 24 24\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2\" stroke-linecap=\"round\" stroke-linejoin=\"round\"><path d=\"M12 1a3 3 0 0 0-3 3v8a3 3 0 0 0 6 0V4a3 3 0 0 0-3-3z\"></path><path d=\"M19 10v2a7 7 0 0 1-14 0v-2\"></path><line x1=\"12\" y1=\"19\" x2=\"12\" y2=\"23\"></line><line x1=\"8\" y1=\"23\" x2=\"16\" y2=\"23\"></line></svg>",
            "chair" => "<svg width=\"20\" height=\"20\" viewBox=\"0 0 24 24\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2\" stroke-linecap=\"round\" stroke-linejoin=\"round\"><path d=\"M6 19v2M18 19v2M6 12h12M6 4h12v8H6zM4 15h16v4H4z\"/></svg>",
            "table" => "<svg width=\"20\" height=\"20\" viewBox=\"0 0 24 24\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2\" stroke-linecap=\"round\" stroke-linejoin=\"round\"><rect x=\"3\" y=\"6\" width=\"18\" height=\"4\" rx=\"1\"/><line x1=\"5\" y1=\"10\" x2=\"5\" y2=\"20\"/><line x1=\"19\" y1=\"10\" x2=\"19\" y2=\"20\"/><line x1=\"2\" y1=\"14\" x2=\"22\" y2=\"14\"/></svg>",
            "ac" => "<svg width=\"20\" height=\"20\" viewBox=\"0 0 24 24\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2\" stroke-linecap=\"round\" stroke-linejoin=\"round\"><rect x=\"2\" y=\"4\" width=\"20\" height=\"8\" rx=\"2\"></rect><line x1=\"6\" y1=\"16\" x2=\"6.01\" y2=\"16\"></line><line x1=\"10\" y1=\"18\" x2=\"10.01\" y2=\"18\"></line><line x1=\"14\" y1=\"18\" x2=\"14.01\" y2=\"18\"></line><line x1=\"18\" y1=\"16\" x2=\"18.01\" y2=\"16\"></line></svg>",
            "tv" => "<svg width=\"20\" height=\"20\" viewBox=\"0 0 24 24\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2\" stroke-linecap=\"round\" stroke-linejoin=\"round\"><rect x=\"2\" y=\"7\" width=\"20\" height=\"14\" rx=\"2\" ry=\"2\"></rect><polyline points=\"17 2 12 7 7 2\"></polyline></svg>",
            "cable" => "<svg width=\"20\" height=\"20\" viewBox=\"0 0 24 24\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2\" stroke-linecap=\"round\" stroke-linejoin=\"round\"><path d=\"M4 11h16M7 7v4M17 7v4M12 11v8M8 19h8\"/></svg>",
            "whiteboard" => "<svg width=\"20\" height=\"20\" viewBox=\"0 0 24 24\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2\" stroke-linecap=\"round\" stroke-linejoin=\"round\"><rect x=\"3\" y=\"3\" width=\"18\" height=\"12\" rx=\"2\"></rect><line x1=\"8\" y1=\"21\" x2=\"12\" y2=\"15\"></line><line x1=\"16\" y1=\"21\" x2=\"12\" y2=\"15\"></line></svg>",
            "camera" => "<svg width=\"20\" height=\"20\" viewBox=\"0 0 24 24\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2\" stroke-linecap=\"round\" stroke-linejoin=\"round\"><path d=\"M23 7l-7 5 7 5V7z\"></path><rect x=\"1\" y=\"5\" width=\"15\" height=\"14\" rx=\"2\" ry=\"2\"></rect></svg>",
            "wifi" => "<svg width=\"20\" height=\"20\" viewBox=\"0 0 24 24\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2\" stroke-linecap=\"round\" stroke-linejoin=\"round\"><path d=\"M5 12.55a11 11 0 0 1 14.08 0\"></path><path d=\"M1.42 9a16 16 0 0 1 21.16 0\"></path><path d=\"M8.53 16.11a6 6 0 0 1 6.95 0\"></path><line x1=\"12\" y1=\"20\" x2=\"12.01\" y2=\"20\"></line></svg>",
            "catering" => "<svg width=\"20\" height=\"20\" viewBox=\"0 0 24 24\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2\" stroke-linecap=\"round\" stroke-linejoin=\"round\"><path d=\"M18 8h1a4 4 0 0 1 0 8h-1\"></path><path d=\"M2 8h16v9a4 4 0 0 1-4 4H6a4 4 0 0 1-4-4V8z\"></path><line x1=\"6\" y1=\"1\" x2=\"6\" y2=\"4\"></line><line x1=\"10\" y1=\"1\" x2=\"10\" y2=\"4\"></line><line x1=\"14\" y1=\"1\" x2=\"14\" y2=\"4\"></line></svg>",
            "printer" => "<svg width=\"20\" height=\"20\" viewBox=\"0 0 24 24\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2\" stroke-linecap=\"round\" stroke-linejoin=\"round\"><polyline points=\"6 9 6 2 18 2 18 9\"></polyline><path d=\"M6 18H4a2 2 0 0 1-2-2v-5a2 2 0 0 1 2-2h16a2 2 0 0 1 2 2v5a2 2 0 0 1-2 2h-2\"></path><rect x=\"6\" y=\"14\" width=\"12\" height=\"8\"></rect></svg>",
            _ => "<svg width=\"20\" height=\"20\" viewBox=\"0 0 24 24\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2\" stroke-linecap=\"round\" stroke-linejoin=\"round\"><path d=\"M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z\"></path><polyline points=\"3.27 6.96 12 12.01 20.73 6.96\"></polyline><line x1=\"12\" y1=\"22.08\" x2=\"12\" y2=\"12\"></line></svg>"
        };
    }

    public static string GetFacilityIcon(string facilityName)
    {
        var type = GetIconType(facilityName);
        return GetSvgIcon(type);
    }
}
