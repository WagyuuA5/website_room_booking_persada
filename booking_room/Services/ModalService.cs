using System;
using System.Collections.Generic;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Components;

namespace booking_room.Services
{
    public class ModalService : IModalService
    {
        public event Action? OnChange;
        public ModalInstance? ActiveModal { get; private set; }

        public Task<ModalResult> ShowAsync<TModal>(Dictionary<string, object>? parameters = null) where TModal : IComponent
        {
            return ShowAsync(typeof(TModal), parameters);
        }

        public Task<ModalResult> ShowAsync(Type componentType, Dictionary<string, object>? parameters = null)
        {
            ActiveModal = new ModalInstance
            {
                ComponentType = componentType,
                Parameters = parameters
            };

            OnChange?.Invoke();
            return ActiveModal.TaskSource.Task;
        }

        public void Close(ModalResult? result = null)
        {
            if (ActiveModal != null)
            {
                ActiveModal.TaskSource.TrySetResult(result ?? ModalResult.Cancel());
                ActiveModal = null;
                OnChange?.Invoke();
            }
        }
    }
}
