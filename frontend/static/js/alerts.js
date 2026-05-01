document.addEventListener('DOMContentLoaded', () => {
    loadAlertsFeed();
    setInterval(loadAlertsFeed, 60000);
});

async function loadAlertsFeed() {
    const res = await fetch('/api/alerts');
    const alerts = await res.json();
    const container = document.getElementById('alerts-feed');
    if (!container) return;
    container.innerHTML = alerts.map(a => `
        <div class="card alert-${a.severity}">
            <div style="display:flex; justify-content:space-between;">
                <strong>${a.title}</strong>
                <span style="color:#94a3b8; font-size:0.8rem;">${new Date(a.created_at).toLocaleString()}</span>
            </div>
            <p style="margin-top:0.5rem; color:#cbd5e1;">${a.description}</p>
            <span style="font-size:0.75rem; color:#64748b;">${a.country_code} | ${a.alert_type} | ${a.severity}</span>
        </div>
    `).join('');
}
