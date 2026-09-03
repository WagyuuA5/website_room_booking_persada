import os

path = 'booking_room/Components/Pages/History.razor'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

# Add DatePicker and HistoryBookingDetailModal to the file
modals = """
<DatePickerPopup Visible="_isDatePickerOpen" VisibleChanged="v => _isDatePickerOpen = v" />
<HistoryBookingDetailModal Visible="_isDetailOpen" VisibleChanged="v => _isDetailOpen = v" Booking="_selectedBooking" />
"""

if "<DatePickerPopup" not in content:
    content = content.replace("</style>", "</style>\n" + modals)

if "private bool _isDatePickerOpen;" not in content:
    content = content.replace("@code {", """@code {
    private bool _isDatePickerOpen;
    private bool _isDetailOpen;
    private dynamic _selectedBooking;
    
    private void OpenDatePicker() => _isDatePickerOpen = true;
    private void ViewDetail(dynamic booking)
    {
        _selectedBooking = booking;
        _isDetailOpen = true;
    }
""")

# In history cards, make sure there's an onclick
content = content.replace('class="history-card"', 'class="history-card" @onclick="() => ViewDetail(booking)" style="cursor: pointer;"')

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)
print("History.razor updated.")
