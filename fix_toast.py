import os

path = 'booking_room/Services/ToastService.cs'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

# Fix the timer thread issue in ToastService
content = content.replace("var timer = new System.Threading.Timer(state =>", """var timer = new System.Threading.Timer(state =>
            {
                if (state is string toastId)
                {
                    Remove(toastId);
                }
            }, toast.Id, durationMs, System.Threading.Timeout.Infinite);""")

# Wait, looking at the code, it's ALREADY doing that.
# Let's check what I need to change.
# "Tanggung jawab marshalling ke UI thread ada di komponen consumer, bukan di service."
# If so, maybe I just don't need to change ToastService.cs if it already does `OnChange?.Invoke();`.
# But BUG-03 says "Ganti koleksi toast (list biasa) di ToastService menjadi ConcurrentDictionary<string, ToastMessage>".
# It is ALREADY ConcurrentDictionary! Let's check if the prompt is outdated compared to the current file, or if I am missing something.
