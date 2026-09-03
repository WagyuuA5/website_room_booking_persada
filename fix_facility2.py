import os
import re

path = 'booking_room/Components/Shared/FacilityRequestView.razor'
with open(path, 'r', encoding='utf-8') as f: content = f.read()

# I will remove the injected AppModal completely
bad_modal_pattern = r'<AppModal Visible="@\(_selectedReq != null\)".*?</AppModal>'
content = re.sub(bad_modal_pattern, '', content, flags=re.DOTALL)

with open(path, 'w', encoding='utf-8') as f: f.write(content)
print("Removed bad modal from FacilityRequestView")
