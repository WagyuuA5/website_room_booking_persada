param(
    [switch]$Run = $false
)

Write-Host "Mengecek proses booking_room yang masih berjalan..." -ForegroundColor Cyan
Get-Process booking_room, booking_room.exe -ErrorAction SilentlyContinue | Stop-Process -Force
Start-Sleep -Seconds 1

Write-Host "Menjalankan dotnet build..." -ForegroundColor Yellow
dotnet build

if ($LASTEXITCODE -eq 0 -and $Run) {
    Write-Host "Build sukses, menjalankan aplikasi..." -ForegroundColor Green
    dotnet run
}
