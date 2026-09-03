import os

path = 'booking_room/Components/Pages/History.razor'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

modals = """
<DatePickerPopup Visible="_isDatePickerOpen" VisibleChanged="v => _isDatePickerOpen = v" />
<HistoryBookingDetailModal Visible="_isDetailOpen" VisibleChanged="v => _isDetailOpen = v" Booking="_selectedBooking" />
"""

if "<DatePickerPopup" not in content:
    content = content.replace("</style>", "</style>\n" + modals)

if "private bool _isDatePickerOpen;" not in content:
    # Safely inject inside @code {
    old_code = """@code {
    private string _searchQuery = "";"""
    new_code = """@code {
    private bool _isDatePickerOpen = false;
    private bool _isDetailOpen = false;
    private dynamic? _selectedBooking;
    
    private void OpenDatePicker() => _isDatePickerOpen = true;
    private void ViewDetail(dynamic booking)
    {
        _selectedBooking = booking;
        _isDetailOpen = true;
    }
    
    private string _searchQuery = "";"""
    content = content.replace(old_code, new_code)
    
    # Also add the onclick to history cards
    content = content.replace('class="history-card"', 'class="history-card" @onclick="() => ViewDetail(booking)" style="cursor: pointer;"')
    
    # And fix any 'OpenDatePicker' usage if it was inline
    content = content.replace('@onclick="() => {}"', '@onclick="OpenDatePicker"')

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)
print("History.razor fixed.")
