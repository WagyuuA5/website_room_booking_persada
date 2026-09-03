import os

path = 'booking_room/Components/Shared/ConfirmBookingModal.razor'
with open(path, 'r', encoding='utf-8') as f: content = f.read()

# Make conflict dynamic
conflict_markup = """
            <!-- Selected Participants -->
            <div class="participants-chips">
                @foreach(var p in _participants)
                {
                    <div class="participant-chip">
                        <div class="chip-avatar">@p.Substring(0,1)</div>
                        <span>@p</span>
                        <button type="button" class="btn-remove-chip" @onclick="() => RemoveParticipant(p)">×</button>
                    </div>
                }
            </div>
            
            @if (_hasConflict)
            {
                <div class="conflict-alert animate-fade-in">
                    <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M10.29 3.86L1.82 18a2 2 0 0 0 1.71 3h16.94a2 2 0 0 0 1.71-3L13.71 3.86a2 2 0 0 0-3.42 0z"></path><line x1="12" y1="9" x2="12" y2="13"></line><line x1="12" y1="17" x2="12.01" y2="17"></line></svg>
                    <span>⚠ Ada potensi bentrok jadwal</span>
                </div>
            }
"""

# Replace old markup
import re
content = re.sub(r'<!-- Selected Participants -->.*?</div>\s*<div class="conflict-alert"[^>]*>.*?</div>', conflict_markup, content, flags=re.DOTALL)

# Add _hasConflict to @code
code_addition = """
    private bool _hasConflict = false;
    private async Task AddParticipant(string name)
    {
        if(!string.IsNullOrWhiteSpace(name) && !_participants.Contains(name))
        {
            _participants.Add(name);
            _inviteInput = "";
            
            // Simulate conflict check
            _hasConflict = false;
            await Task.Delay(300);
            if (name.ToLower().Contains("budi") || name.ToLower().Contains("conflict"))
            {
                _hasConflict = true;
            }
        }
    }
    
    private void RemoveParticipant(string name)
    {
        _participants.Remove(name);
        _hasConflict = false;
    }
"""
content = re.sub(r'private void AddParticipant.*?\}', code_addition, content, flags=re.DOTALL)

with open(path, 'w', encoding='utf-8') as f: f.write(content)
print("Updated ConfirmBookingModal with dynamic conflict check")
