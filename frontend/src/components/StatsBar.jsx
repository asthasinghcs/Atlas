import "../styles/stats-bar.css";

function StatsBar({ dashboard }) {

    if (!dashboard || !dashboard.stats) {
        return null;
    }

    const stats = dashboard.stats;

    return (
        <div className="stats-bar">

            <div className="stat-card">
                <h3>Entities</h3>
                <p>{stats.entities}</p>
            </div>

            <div className="stat-card">
                <h3>Relationships</h3>
                <p>{stats.relationships}</p>
            </div>

            <div className="stat-card">
                <h3>Documents</h3>
                <p>{stats.documents}</p>
            </div>

            <div className="stat-card">
                <h3>Avg Influence</h3>
                <p>{stats.average_influence}</p>
            </div>

        </div>
    );
}

export default StatsBar;