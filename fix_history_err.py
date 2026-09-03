import os
import re

path = 'booking_room/Components/Pages/History.razor'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

# I injected @code twice or injected fields twice. Let's fix.
# Let's clean the extra variables.
# First, see if there are two @code blocks.
parts = content.split("@code {")
if len(parts) > 2:
    # Remove the first one that I injected.
    pass

# A better way is to restore History.razor from git, then inject correctly.
