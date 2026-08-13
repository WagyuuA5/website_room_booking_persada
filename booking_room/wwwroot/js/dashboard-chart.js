let analyticsChart = null;

window.initAnalyticsChart = function (canvasId, labels, datasets) {
    const canvas = document.getElementById(canvasId);
    if (!canvas) return;

    const ctx = canvas.getContext('2d');
    const chartHeight = canvas.parentElement.clientHeight || 400;

    const enriched = datasets.map((ds, index) => {
        const gradient = ctx.createLinearGradient(0, 0, 0, chartHeight);
        const baseColor = ds.borderColor || '#3b82f6';
        gradient.addColorStop(0, baseColor + '40');
        gradient.addColorStop(1, baseColor + '00');

        return {
            label: ds.label,
            data: ds.data,
            borderColor: baseColor,
            backgroundColor: gradient,
            fill: true,
            tension: 0.4,
            pointRadius: 3,
            pointHoverRadius: 6,
            pointBackgroundColor: baseColor,
            pointBorderColor: '#ffffff',
            pointBorderWidth: 2,
            borderWidth: 2.5
        };
    });

    if (analyticsChart) {
        analyticsChart.destroy();
    }

    analyticsChart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: labels,
            datasets: enriched
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            interaction: {
                mode: 'index',
                intersect: false
            },
            plugins: {
                legend: {
                    position: 'top',
                    align: 'end',
                    labels: {
                        usePointStyle: true,
                        pointStyle: 'circle',
                        padding: 20,
                        font: {
                            size: 12,
                            family: "'Segoe UI', 'Helvetica Neue', Helvetica, Arial, sans-serif"
                        },
                        color: '#64748b'
                    }
                },
                tooltip: {
                    backgroundColor: 'rgba(15, 31, 61, 0.95)',
                    titleFont: {
                        size: 13,
                        weight: '600',
                        family: "'Segoe UI', 'Helvetica Neue', Helvetica, Arial, sans-serif"
                    },
                    bodyFont: {
                        size: 12,
                        family: "'Segoe UI', 'Helvetica Neue', Helvetica, Arial, sans-serif"
                    },
                    padding: 12,
                    cornerRadius: 8,
                    displayColors: true,
                    boxPadding: 4
                },
                zoom: {
                    pan: {
                        enabled: true,
                        mode: 'x',
                        threshold: 5
                    },
                    zoom: {
                        wheel: {
                            enabled: true,
                            speed: 0.05
                        },
                        pinch: {
                            enabled: true
                        },
                        mode: 'x'
                    }
                }
            },
            scales: {
                x: {
                    grid: {
                        display: false,
                        drawBorder: false
                    },
                    ticks: {
                        font: {
                            size: 11,
                            family: "'Segoe UI', 'Helvetica Neue', Helvetica, Arial, sans-serif"
                        },
                        color: '#94a3b8'
                    }
                },
                y: {
                    grid: {
                        color: '#f1f5f9',
                        drawBorder: false
                    },
                    ticks: {
                        font: {
                            size: 11,
                            family: "'Segoe UI', 'Helvetica Neue', Helvetica, Arial, sans-serif"
                        },
                        color: '#94a3b8'
                    }
                }
            },
            animation: {
                duration: 350,
                easing: 'easeInOutQuart'
            }
        }
    });
};

window.updateAnalyticsChart = function (labels, datasets) {
    if (!analyticsChart) return;

    const canvas = document.getElementById(analyticsChart.canvas.id);
    if (!canvas) return;

    const ctx = canvas.getContext('2d');
    const chartHeight = canvas.parentElement.clientHeight || 400;

    const enriched = datasets.map((ds) => {
        const gradient = ctx.createLinearGradient(0, 0, 0, chartHeight);
        const baseColor = ds.borderColor || '#3b82f6';
        gradient.addColorStop(0, baseColor + '40');
        gradient.addColorStop(1, baseColor + '00');

        return {
            label: ds.label,
            data: ds.data,
            borderColor: baseColor,
            backgroundColor: gradient,
            fill: true,
            tension: 0.4,
            pointRadius: 3,
            pointHoverRadius: 6,
            pointBackgroundColor: baseColor,
            pointBorderColor: '#ffffff',
            pointBorderWidth: 2,
            borderWidth: 2.5
        };
    });

    analyticsChart.data.labels = labels;
    analyticsChart.data.datasets = enriched;
    analyticsChart.update('default');
};
