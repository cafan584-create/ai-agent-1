async function loadChart(canvasId, countryCode) {
    const res = await fetch(`/api/health-scores/${countryCode}`);
    const data = await res.json();
    if (!data.length) return;

    const ctx = document.getElementById(canvasId).getContext('2d');
    new Chart(ctx, {
        type: 'line',
        data: {
            labels: data.map(d => new Date(d.calculated_at).toLocaleDateString()).reverse(),
            datasets: [{
                label: 'Health Score',
                data: data.map(d => d.overall_score).reverse(),
                borderColor: '#38bdf8',
                backgroundColor: 'rgba(56,189,248,0.1)',
                fill: true,
            }]
        },
        options: {
            responsive: true,
            scales: { y: { min: 0, max: 100, ticks: { color: '#94a3b8' } }, x: { ticks: { color: '#94a3b8' } } },
            plugins: { legend: { labels: { color: '#e2e8f0' } } }
        }
    });
}
