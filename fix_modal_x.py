import os

path = 'booking_room/Components/Shared/AppModal.razor'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace standard close button with text "Tutup" if it exists
if "ShowCloseButton" in content:
    old_close = """<button class="modal-close-btn" @onclick="CloseModal" aria-label="Tutup">
                                <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                                    <line x1="18" y1="6" x2="6" y2="18"></line>
                                    <line x1="6" y1="6" x2="18" y2="18"></line>
                                </svg>
                            </button>"""
    new_close = """<button class="modal-close-text-btn" @onclick="CloseModal" aria-label="Tutup">Tutup</button>"""
    if old_close in content:
        content = content.replace(old_close, new_close)
    else:
        # Broad replacement
        content = content.replace('<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">\n                                    <line x1="18" y1="6" x2="6" y2="18"></line>\n                                    <line x1="6" y1="6" x2="18" y2="18"></line>\n                                </svg>', 'Tutup')
    
with open(path, 'w', encoding='utf-8') as f:
    f.write(content)
print("AppModal.razor X replaced.")
