document.addEventListener('DOMContentLoaded', () => {
    loadScores();
    loadAlerts();
});

async function loadScores() {
    const res = await fetch('/api/health-scores');
    const scores = await res.json();
    const top5 = scores.slice(0, 5);
    const bottom5 = scores.slice(-5).reverse();

    document.getElementById('top5').innerHTML = top5.map(s => `
        <div class="card"><strong>${s.name}</strong> — Score: ${s.overall_score} (${s.trend})</div>
    `).join('');

    document.getElementById('bottom5').innerHTML = bottom5.map(s => `
        <div class="card alert-medium"><strong>${s.name}</strong> — Score: ${s.overall_score} (${s.trend})</div>
    `).join('');
}

async function loadAlerts() {
    const res = await fetch('/api/alerts');
    const alerts = await res.json();
    const container = document.getElementById('alerts-list');
    if (!container) return;
    container.innerHTML = alerts.slice(0, 10).map(a => `
        <div class="card alert-${a.severity}">
            <strong>${a.title}</strong> (${a.country_code}) — ${a.description}
        </div>
    `).join('');
}
