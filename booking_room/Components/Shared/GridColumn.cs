using Microsoft.AspNetCore.Components;
using System;

namespace booking_room.Components.Shared
{
    public class GridColumn<TItem>
    {
        public string Title { get; set; } = "";
        public string PropertyName { get; set; } = "";
        public Func<TItem, object>? ValueFunc { get; set; }
        public RenderFragment<TItem>? CellTemplate { get; set; }
        public bool Sortable { get; set; } = true;
        public string Align { get; set; } = "left";
    }
}
