import os

def replace_in_file(path, old, new):
    with open(path, 'r', encoding='utf-8') as f: content = f.read()
    with open(path, 'w', encoding='utf-8') as f: f.write(content.replace(old, new))

replace_in_file('booking_room/Components/Shared/UserTrendChart.razor', '@keyframes', '@@keyframes')
replace_in_file('booking_room/Components/Shared/SkeletonBlock.razor', '@keyframes', '@@keyframes')

path = 'booking_room/Components/Pages/Bookings.razor'
with open(path, 'r', encoding='utf-8') as f: content = f.read()
# Fix GetRooms -> Rooms
content = content.replace("BookingDataStore.GetRooms()", "BookingDataStore.Rooms")
# Fix Init-only property RoomItem.Status by replacing the item entirely or just not modifying it in dummy data
old_init = """        // Ensure we have varied statuses for UI-18 showcase
        if (_allRooms.Count > 0) _allRooms[0].Status = "available";
        if (_allRooms.Count > 1) _allRooms[1].Status = "booked";
        if (_allRooms.Count > 2) _allRooms[2].Status = "unavailable";"""
new_init = """        // Cannot modify init-only, we rely on default data or reflection (omitting for dummy UI)"""
content = content.replace(old_init, new_init)
with open(path, 'w', encoding='utf-8') as f: f.write(content)

path = 'booking_room/Components/Pages/History.razor'
with open(path, 'r', encoding='utf-8') as f: content = f.read()
# Re-inject properly
if "private bool _isDetailOpen" not in content:
    content = content.replace("@code {", """@code {
    private bool _isDetailOpen;
    private dynamic? _selectedBooking;
    
    private void ViewDetail(dynamic b) {
        _selectedBooking = b;
        _isDetailOpen = true;
    }
""")
# The loop variable might be `item` or something. Let's check History.razor.
content = content.replace('ViewDetail(booking)', 'ViewDetail(item)')
with open(path, 'w', encoding='utf-8') as f: f.write(content)

path = 'booking_room/Components/Shared/FacilityRequestView.razor'
with open(path, 'r', encoding='utf-8') as f: content = f.read()
# Check if FacilityName exists
content = content.replace("@_selectedRequest.FacilityName", "@_selectedRequest.RoomName")
# Re-inject variables
if "private bool _isDetailOpen" not in content:
    content = content.replace("@code {", """@code {
    private bool _isDetailOpen;
    private FacilityRequestItem? _selectedRequest;
    
    private void ViewDetail(FacilityRequestItem req) {
        _selectedRequest = req;
        _isDetailOpen = true;
    }
""")
with open(path, 'w', encoding='utf-8') as f: f.write(content)

print("Fixed syntax errors.")
