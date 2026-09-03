using Microsoft.Extensions.FileProviders;
using booking_room.Components;

var builder = WebApplication.CreateBuilder(args);

// Add services to the container.
builder.Services.AddRazorComponents()
    .AddInteractiveServerComponents();

builder.Services.AddSingleton<IFileProvider>(sp =>
    sp.GetRequiredService<IWebHostEnvironment>().WebRootFileProvider);
builder.Services.AddScoped<booking_room.Services.NotificationState>();
builder.Services.AddScoped<booking_room.Services.INotificationService, booking_room.Services.NotificationService>();
builder.Services.AddScoped<booking_room.Services.LoadingStateService>();
builder.Services.AddScoped<booking_room.Services.DataExportService>();
builder.Services.AddScoped<booking_room.Services.ModalStateService>();
builder.Services.AddScoped<booking_room.Services.IModalService, booking_room.Services.ModalService>();
builder.Services.AddScoped<booking_room.Services.IToastService, booking_room.Services.ToastService>();

var app = builder.Build();

// Configure the HTTP request pipeline.
if (!app.Environment.IsDevelopment())
{
    app.UseExceptionHandler("/Error", createScopeForErrors: true);
    // The default HSTS value is 30 days. You may want to change this for production scenarios, see https://aka.ms/aspnetcore-hsts.
    app.UseHsts();
}
app.UseStatusCodePagesWithReExecute("/not-found", createScopeForStatusCodePages: true);
if (!app.Environment.IsDevelopment())
{
    app.UseHttpsRedirection();
}

app.UseAntiforgery();

app.MapStaticAssets();
app.MapRazorComponents<App>()
    .AddInteractiveServerRenderMode();

app.Run();

