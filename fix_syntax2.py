import os
import re

path = 'booking_room/Components/Pages/History.razor'
with open(path, 'r', encoding='utf-8') as f: content = f.read()
# Clean up duplicate onclick
content = content.replace('class="history-card" @onclick="() => ViewDetail(item)" style="cursor: pointer;" @onclick="() => \nOpenDetail(item)"', 'class="history-card" style="cursor: pointer;" @onclick="() => OpenDetail(item)"')
content = content.replace('class="history-card" @onclick="() => ViewDetail(item)" style="cursor: pointer;" @onclick="() => OpenDetail(item)"', 'class="history-card" style="cursor: pointer;" @onclick="() => OpenDetail(item)"')
# Clean up injected ViewDetail and fields
bad_code = """@code {
    private bool _isDetailOpen;
    private dynamic? _selectedBooking;
    
    private void ViewDetail(dynamic b) {
        _selectedBooking = b;
        _isDetailOpen = true;
    }
"""
content = content.replace(bad_code, "@code {")
# Wait, let's just make _isDetailOpen tied to _selectedBooking in the template:
# <HistoryBookingDetailModal Visible="@(_selectedBooking != null)" VisibleChanged="v => { if(!v) _selectedBooking = null; }" Booking="_selectedBooking" />
content = content.replace('<HistoryBookingDetailModal Visible="_isDetailOpen" VisibleChanged="v => _isDetailOpen = v" Booking="_selectedBooking" />', '<HistoryBookingDetailModal Visible="@(_selectedBooking != null)" VisibleChanged="v => { if(!v) _selectedBooking = null; }" Booking="_selectedBooking" />')
with open(path, 'w', encoding='utf-8') as f: f.write(content)

path = 'booking_room/Components/Shared/FacilityRequestView.razor'
with open(path, 'r', encoding='utf-8') as f: content = f.read()
# Remove my injected _isDetailOpen code
bad_code2 = """@code {
    private bool _isDetailOpen;
    private FacilityRequestItem? _selectedRequest;
    
    private void ViewDetail(FacilityRequestItem req) {
        _selectedRequest = req;
        _isDetailOpen = true;
    }
"""
content = content.replace(bad_code2, "@code {")
# Is there an existing OpenDetail? 
# I will just create a basic boolean logic in HTML for FacilityRequestView.
# Actually I'll inject `private FacilityRequestItem? _selectedReq;` safely.
content = content.replace("@code {", """@code {
    private FacilityRequestItem? _selectedReq;
    private void SelectReq(FacilityRequestItem req) => _selectedReq = req;
""")
content = content.replace('class="facility-row" @onclick="() => ViewDetail(req)" style="cursor: pointer;"', 'class="facility-row" style="cursor: pointer;" @onclick="() => SelectReq(req)"')
content = content.replace('Visible="@_isDetailOpen" VisibleChanged="v => _isDetailOpen = v"', 'Visible="@(_selectedReq != null)" VisibleChanged="v => { if(!v) _selectedReq = null; }"')
content = content.replace('@_selectedRequest', '@_selectedReq')

with open(path, 'w', encoding='utf-8') as f: f.write(content)
print("Cleaned up History and Facility.")
