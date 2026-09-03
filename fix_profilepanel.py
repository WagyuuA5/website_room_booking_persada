import os
import re

path = 'booking_room/Components/Shared/ProfilePanel.razor'
with open(path, 'r', encoding='utf-8') as f: content = f.read()

replacement = """                <!-- Action Section -->
                <div class="glass-actions">
                    <button class="btn-edit-profile-pill" @onclick="HandleEditProfile" type="button">
                        Edit Profil
                    </button>
                    <button class="btn-logout-link" @onclick="HandleLogout" type="button">
                        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M9 21H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h4"></path><polyline points="16 17 21 12 16 7"></polyline><line x1="21" y1="12" x2="9" y2="12"></line></svg>
                        Keluar
                    </button>
                </div>"""

content = re.sub(r'<!-- Action Section -->.*?</div>', replacement, content, flags=re.DOTALL)

code_addition = """    private void HandleLogout()
    {
        // Simple logout logic
        Navigation.NavigateTo("/", forceLoad: true);
    }
}"""
content = content.replace('}', code_addition)

with open(path, 'w', encoding='utf-8') as f: f.write(content)
print("Added logout link to ProfilePanel")
