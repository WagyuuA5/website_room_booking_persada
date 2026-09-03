import os

path = 'booking_room/Components/Shared/FacilityRequestView.razor'
with open(path, 'r', encoding='utf-8') as f: content = f.read()

content = content.replace('@onclick="() => /* removed */"', '@onclick="CloseDetail"')

# Add CloseDetail method if not present
if "private void CloseDetail()" not in content:
    content = content.replace('private void OpenNewRequest()', 'private void CloseDetail() { _selectedReq = null; }\n\n    private void OpenNewRequest()')

with open(path, 'w', encoding='utf-8') as f: f.write(content)
print("Fixed FacilityRequestView.razor syntax error")
