import os
import re

path = 'booking_room/Components/Pages/User/Beranda.razor'
with open(path, 'r', encoding='utf-8') as f: content = f.read()

# I will find "private async Task HandleCheckInClick()" and replace it up to the end of the file or up to the last "}"
code_addition = """    private async Task HandleCheckInClick()
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
    }
}"""
content = re.sub(r'private async Task HandleCheckInClick\(\).*?\}\s*$', code_addition, content, flags=re.DOTALL)

with open(path, 'w', encoding='utf-8') as f: f.write(content)
print("Fixed Beranda.razor syntax error")
