import os

path = 'booking_room/Components/Shared/FacilityRequestView.razor'
with open(path, 'r', encoding='utf-8') as f: content = f.read()

content = content.replace("FacilityRequestItem", "FacilityRequest")
with open(path, 'w', encoding='utf-8') as f: f.write(content)
print("Fixed FacilityRequest type.")
