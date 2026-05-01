document.addEventListener('DOMContentLoaded', () => {
    const mapEl = document.getElementById('map');
    if (!mapEl) return;
    fetch('/api/health-scores')
        .then(r => r.json())
        .then(scores => {
            const html = `<div><h3>World Map Placeholder</h3>
                <p>${scores.length} countries loaded. Integrate Chart.js or Leaflet for full map.</p>
                <div style="display:grid; grid-template-columns: repeat(5,1fr); gap:8px; margin-top:1rem;">
                    ${scores.slice(0,20).map(s => `<div style="padding:8px; background:#1e293b; border-radius:4px; text-align:center;">
                        <div style="font-size:1.2rem; font-weight:bold; color:${s.overall_score > 70 ? '#4ade80' : s.overall_score > 40 ? '#facc15' : '#f87171'}">${s.overall_score}</div>
                        <div style="font-size:0.7rem;">${s.name}</div>
                    </div>`).join('')}
                </div>
            </div>`;
            mapEl.innerHTML = html;
        })
        .catch(() => { mapEl.innerHTML = '<p>Error loading map data</p>'; });
});
