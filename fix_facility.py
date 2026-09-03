import os

path = 'booking_room/Components/Shared/FacilityRequestView.razor'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

# Add detail popup
new_modal = """
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
                <div>
                    <label style="font-size: 12px; color: #6B7280;">Catatan</label>
                    <div>Tambahan kursi, proyektor, dan konsumsi.</div>
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
    content = content.replace("</style>", "</style>\n" + new_modal)
    content = content.replace("@code {", """@code {
    private bool _isDetailOpen;
    private dynamic _selectedRequest;

    private void ViewDetail(dynamic req)
    {
        _selectedRequest = req;
        _isDetailOpen = true;
    }
""")
    # Add onclick to the row
    content = content.replace('class="facility-row"', 'class="facility-row" @onclick="() => ViewDetail(req)" style="cursor: pointer;"')

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)
print("FacilityRequestView.razor updated.")
