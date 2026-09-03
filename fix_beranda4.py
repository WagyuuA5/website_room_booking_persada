import os

path = 'booking_room/Components/Pages/User/Beranda.razor'
with open(path, 'r', encoding='utf-8') as f: content = f.read()

# Add CheckInSuccessModal to the top
content = content.replace('<!-- UI-10 Modal Menunggu Persetujuan -->', '<!-- UI-10 Modal Menunggu Persetujuan -->\n<CheckInSuccessModal Visible="_isCheckInSuccessOpen" VisibleChanged="v => _isCheckInSuccessOpen = v" />')

# Add to code
code_addition = """    private bool _isCheckInSuccessOpen;

    private async Task HandleCheckInClick()
    {
        var parameters = new Dictionary<string, object>
        {
            { "RoomName", "Executive Boardroom A" },
            { "TimeSlot", "09:00 - 11:00" },
            { "Location", "Lantai 3, Sayap Utara" },
            { "Capacity", 15 },
            { "OnConfirm", EventCallback.Factory.Create(this, async () => {
                await ModalService.CloseTopAsync(ModalResult.Ok());
                _isCheckInSuccessOpen = true;
                StateHasChanged();
            })}
        };
        await ModalService.ShowAsync<CheckInCountdownCard>(parameters);
    }"""
    
import re
content = re.sub(r'private async Task HandleCheckInClick\(\)\s*\{.*?\}', code_addition, content, flags=re.DOTALL)

with open(path, 'w', encoding='utf-8') as f: f.write(content)
print("Updated Beranda.razor CheckIn flow")
