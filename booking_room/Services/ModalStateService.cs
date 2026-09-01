using System.Collections.Generic;

namespace booking_room.Services
{
    public enum ModalPriority
    {
        Normal,
        Critical
    }

    public class ModalRequest
    {
        public string Key { get; set; } = "";
        public ModalPriority Priority { get; set; } = ModalPriority.Normal;
    }

    public class ModalStateService
    {
        public event System.Action? OnChange;

        private readonly Queue<ModalRequest> _queue = new();
        public ModalRequest? ActiveModal { get; private set; }

        public void Enqueue(ModalRequest request)
        {
            if (request.Priority == ModalPriority.Critical)
            {
                var temp = new Queue<ModalRequest>();
                temp.Enqueue(request);
                while (_queue.Count > 0)
                {
                    temp.Enqueue(_queue.Dequeue());
                }
                while (temp.Count > 0)
                {
                    _queue.Enqueue(temp.Dequeue());
                }
            }
            else
            {
                _queue.Enqueue(request);
            }

            if (ActiveModal is null)
            {
                ShowNext();
            }
        }

        public void CloseActive()
        {
            ActiveModal = null;
            ShowNext();
        }

        private void ShowNext()
        {
            ActiveModal = _queue.Count > 0 ? _queue.Dequeue() : null;
            OnChange?.Invoke();
        }
    }
}
