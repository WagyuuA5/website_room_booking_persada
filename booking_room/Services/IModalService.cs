using System;
using System.Collections.Generic;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Components;

namespace booking_room.Services
{
    public class ModalResult
    {
        public bool Confirmed { get; set; }
        public object? Data { get; set; }

        public static ModalResult Ok(object? data = null) => new ModalResult { Confirmed = true, Data = data };
        public static ModalResult Cancel() => new ModalResult { Confirmed = false };
    }

    public class ModalInstance
    {
        public Guid Id { get; } = Guid.NewGuid();
        public Type ComponentType { get; set; } = default!;
        public IDictionary<string, object>? Parameters { get; set; }
        public TaskCompletionSource<ModalResult> TaskSource { get; } = new(TaskCreationOptions.RunContinuationsAsynchronously);
    }

    public interface IModalService
    {
        event Action? OnChange;
        IReadOnlyList<ModalInstance> Stack { get; }
        ModalInstance? TopModal => Stack.Count > 0 ? Stack[^1] : null;
        ModalInstance? ActiveModal => TopModal;

        Task<ModalResult> ShowAsync<TComponent>(IDictionary<string, object>? parameters = null) where TComponent : IComponent;
        Task<ModalResult> ShowAsync(string componentKey, IDictionary<string, object>? parameters = null);
        Task<ModalResult> ShowAsync(Type componentType, IDictionary<string, object>? parameters = null);
        Task CloseTopAsync(ModalResult? result = null);
        Task CloseAllAsync();
        void Close(ModalResult? result = null);
    }
}
