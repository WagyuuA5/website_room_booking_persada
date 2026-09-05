/**
 * roomUsageChart.js
 * Inisialisasi dan update ApexCharts interaktif untuk analitik penggunaan ruangan.
 * Mendukung toggle Minggu/Bulan/Tahun dengan transisi animasi 350ms.
 */

let roomUsageChartInstance = null;

/**
 * Inisialisasi chart ApexCharts area (smooth) di dalam elemen dengan ID tertentu.
 * @param {string} elementId - ID dari div container
 * @param {object} data - { labels: string[], datasets: [{name, data}] }
 */
window.initRoomUsageChart = function (elementId, data) {
    // Bersihkan instance sebelumnya jika ada
    if (roomUsageChartInstance) {
        roomUsageChartInstance.destroy();
        roomUsageChartInstance = null;
    }

    const el = document.getElementById(elementId);
    if (!el) {
        console.warn('[RoomUsageChart] Element tidak ditemukan:', elementId);
        return;
    }

    // Ambil satu dataset saja (dataset pertama / Boardroom A) untuk tampilan area chart bersih
    const primaryData = data.datasets && data.datasets.length > 0
        ? data.datasets[0].data
        : [];

    const options = {
        chart: {
            type: 'area',
            height: 260,
            background: 'transparent',
            toolbar: { show: false },
            animations: {
                enabled: true,
                easing: 'easeinout',
                speed: 350,
                animateGradually: { enabled: true, delay: 80 },
                dynamicAnimation: { enabled: true, speed: 350 }
            },
            zoom: { enabled: false },
            pan: { enabled: true, type: 'x' },
            sparkline: { enabled: false }
        },
        series: [
            {
                name: 'Jam Pemakaian',
                data: primaryData
            }
        ],
        stroke: {
            curve: 'smooth',
            width: 3
        },
        fill: {
            type: 'gradient',
            gradient: {
                shadeIntensity: 1,
                opacityFrom: 0.7,
                opacityTo: 0.0,
                stops: [0, 95, 100]
            }
        },
        colors: ['#0f1f3d'],
        xaxis: {
            categories: data.labels || [],
            labels: {
                style: { colors: '#94a3b8', fontSize: '11px', fontFamily: 'Inter, sans-serif' }
            },
            axisBorder: { show: false },
            axisTicks: { show: false }
        },
        yaxis: {
            opposite: true,
            labels: {
                style: { colors: '#94a3b8', fontSize: '11px', fontFamily: 'Inter, sans-serif' },
                formatter: (val) => `${Math.round(val)} j`
            }
        },
        grid: {
            borderColor: 'rgba(255,255,255,0.06)',
            strokeDashArray: 4,
            xaxis: { lines: { show: false } },
            yaxis: { lines: { show: true } }
        },
        markers: {
            size: 0,
            hover: { size: 6, sizeOffset: 2 }
        },
        tooltip: {
            theme: 'dark',
            custom: function({series, seriesIndex, dataPointIndex, w}) {
                const date = w.globals.categoryLabels[dataPointIndex];
                const hours = series[seriesIndex][dataPointIndex];
                // Mock logic for most booked room/user based on dataPointIndex
                const rooms = ["Executive Boardroom A", "Training Center", "Meeting Room 1", "Focus Room Alpha", "Studio Webinar"];
                const users = ["Budi Santoso", "Sarah Jenkins", "Alex Mercer", "Nadia Pradipta"];
                const topRoom = rooms[dataPointIndex % rooms.length];
                const topUser = users[(dataPointIndex + 2) % users.length];
                
                return `
                    <div style="padding: 10px; background: #0f1f3d; border-radius: 8px; border: 1px solid rgba(255,255,255,0.1); box-shadow: 0 4px 12px rgba(0,0,0,0.2);">
                        <div style="font-size: 0.75rem; color: #94a3b8; margin-bottom: 4px;">${date}</div>
                        <div style="font-size: 1.1rem; font-weight: 700; color: #ffffff; margin-bottom: 8px;">${hours} Jam</div>
                        <div style="font-size: 0.75rem; color: #cbd5e1;">
                            <div style="margin-bottom: 2px;"><span style="color:#94a3b8">Terbanyak:</span> ${topRoom}</div>
                            <div><span style="color:#94a3b8">User:</span> ${topUser}</div>
                        </div>
                    </div>
                `;
            }
        },
        crosshairs: {
            show: true,
            stroke: { dashArray: 4, color: '#60a5fa', width: 1 }
        },
        dataLabels: { enabled: false },
        legend: { show: false },
        annotations: {
            yaxis: [
                {
                    y: primaryData.length > 0 ? (primaryData.reduce((a, b) => a + b, 0) / primaryData.length).toFixed(1) : 0,
                    borderColor: '#f59e0b',
                    strokeDashArray: 5,
                    label: {
                        text: 'Rata-rata',
                        style: { color: '#f59e0b', background: 'transparent', fontFamily: 'Inter, sans-serif', fontSize: '11px' }
                    }
                }
            ]
        }
    };

    roomUsageChartInstance = new ApexCharts(el, options);
    roomUsageChartInstance.render();
};

/**
 * Update data chart saat toggle Minggu/Bulan/Tahun diklik.
 * Menggunakan updateSeries agar transisi animasi tetap mulus (350ms ease).
 * @param {object} data - { labels: string[], datasets: [{name, data}] }
 */
window.updateRoomUsageChart = function (data) {
    if (!roomUsageChartInstance) return;

    const primaryData = data.datasets && data.datasets.length > 0
        ? data.datasets[0].data
        : [];

    const avg = primaryData.length > 0
        ? (primaryData.reduce((a, b) => a + b, 0) / primaryData.length).toFixed(1)
        : 0;

    // Update xaxis categories & yaxis annotations sekaligus
    roomUsageChartInstance.updateOptions({
        xaxis: { categories: data.labels || [] },
        annotations: {
            yaxis: [{
                y: parseFloat(avg),
                borderColor: '#f59e0b',
                strokeDashArray: 5,
                label: {
                    text: 'Rata-rata',
                    style: { color: '#f59e0b', background: 'transparent', fontFamily: 'Inter, sans-serif', fontSize: '11px' }
                }
            }]
        }
    }, false, true); // animate = true

    // Perbarui series data (juga dengan animasi)
    roomUsageChartInstance.updateSeries([{ name: 'Jam Pemakaian', data: primaryData }], true);
};

/**
 * Destroy chart (cleanup saat komponen Blazor di-dispose)
 */
window.destroyRoomUsageChart = function () {
    if (roomUsageChartInstance) {
        roomUsageChartInstance.destroy();
        roomUsageChartInstance = null;
    }
};
