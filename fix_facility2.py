import os

path = 'booking_room/Components/Shared/FacilityRequestView.razor'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

modals = """
<AppModal Visible="@_isDetailOpen" VisibleChanged="v => _isDetailOpen = v" Title="Detail Permintaan Fasilitas" Size="md">
    <BodyContent>
        @if(_selectedRequest != null)
        {
            <div style="display: flex; flex-direction: column; gap: 12px; padding-top: 8px;">
                <div>
                    <label style="font-size: 12px; color: #6B7280;">Nama Fasilitas</label>
                    <div style="font-weight: 600;">@_selectedRequest.FacilityName</div>
                </div>
                <div>
                    <label style="font-size: 12px; color: #6B7280;">Status</label>
                    <div style="font-weight: 600;">@_selectedRequest.Status</div>
                </div>
            </div>
        }
    </BodyContent>
    <FooterContent>
        <button class="btn-secondary" @onclick="() => _isDetailOpen = false">Tutup</button>
    </FooterContent>
</AppModal>
"""

if "_isDetailOpen" not in content:
    content = content.replace("</style>", "</style>\n" + modals)
    
    old_code = """@code {
    [Parameter] public List<FacilityRequestItem> Requests { get; set; } = new();"""
    new_code = """@code {
    private bool _isDetailOpen = false;
    private FacilityRequestItem? _selectedRequest;
    
    private void ViewDetail(FacilityRequestItem req)
    {
        _selectedRequest = req;
        _isDetailOpen = true;
    }
    
    [Parameter] public List<FacilityRequestItem> Requests { get; set; } = new();"""
    content = content.replace(old_code, new_code)
    
    content = content.replace('class="facility-row"', 'class="facility-row" @onclick="() => ViewDetail(req)" style="cursor: pointer;"')

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)
print("FacilityRequestView.razor fixed.")
