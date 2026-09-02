using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Components;
using booking_room.Components.Shared;

namespace booking_room.Services
{
    public class ModalService : IModalService
    {
        private readonly List<ModalInstance> _stack = new();

        public event Action? OnChange;
        public IReadOnlyList<ModalInstance> Stack => _stack.AsReadOnly();

        public Task<ModalResult> ShowAsync<TComponent>(IDictionary<string, object>? parameters = null) where TComponent : IComponent
        {
            return ShowAsync(typeof(TComponent), parameters);
        }

        public Task<ModalResult> ShowAsync(string componentKey, IDictionary<string, object>? parameters = null)
        {
            var componentType = ResolveComponentType(componentKey);
            return ShowAsync(componentType, parameters);
        }

        public Task<ModalResult> ShowAsync(Type componentType, IDictionary<string, object>? parameters = null)
        {
            var instance = new ModalInstance
            {
                ComponentType = componentType,
                Parameters = parameters
            };

            _stack.Add(instance);
            OnChange?.Invoke();
            return instance.TaskSource.Task;
        }

        public Task CloseTopAsync(ModalResult? result = null)
        {
            if (_stack.Count > 0)
            {
                var top = _stack[^1];
                _stack.RemoveAt(_stack.Count - 1);
                top.TaskSource.TrySetResult(result ?? ModalResult.Cancel());
                OnChange?.Invoke();
            }
            return Task.CompletedTask;
        }

        public Task CloseAllAsync()
        {
            if (_stack.Count > 0)
            {
                var list = _stack.ToList();
                _stack.Clear();
                foreach (var item in list)
                {
                    item.TaskSource.TrySetResult(ModalResult.Cancel());
                }
                OnChange?.Invoke();
            }
            return Task.CompletedTask;
        }

        public void Close(ModalResult? result = null)
        {
            _ = CloseTopAsync(result);
        }

        private static Type ResolveComponentType(string key)
        {
            return key.ToLowerInvariant() switch
            {
                "checkincountdowncard" or "checkincountdownmodal" or "countdownmodal" or "checkin" => typeof(CheckInCountdownCard),
                "roomdetailsmodal" or "roomdetail" or "roomdetails" or "roomdetailspopup" => typeof(RoomDetailsModal),
                "chartdetailmodal" or "analyticsdetailpopup" or "analytics" => typeof(ChartDetailModal),
                "cancelconfirmationmodal" or "confirmcancelmodal" or "cancelbooking" => typeof(CancelConfirmationModal),
                "cancelrequestmodal" or "cancelrequest" => typeof(CancelRequestModal),
                "checkinsuccessmodal" or "checkinsuccess" or "success" => typeof(CheckInSuccessModal),
                "availableroomsmodal" or "roomavailable" or "availablerooms" => typeof(AvailableRoomsModal),
                "pendingapprovalsmodal" or "pendingapproval" or "pendingapprovals" => typeof(PendingApprovalsModal),
                "confirmbookingmodal" or "quickbook" or "confirmbooking" => typeof(ConfirmBookingModal),
                "incidentdetailmodal" or "systemalert" or "serveralert" => typeof(IncidentDetailModal),
                "requestmoretimemodal" or "requestmoretime" => typeof(RequestMoreTimeModal),
                "bookingautoreleasedmodal" or "autoreleased" => typeof(BookingAutoReleasedModal),
                "reportbugmodal" or "reportbug" => typeof(ReportBugModal),
                _ => typeof(CheckInCountdownCard)
            };
        }
    }
}
