import { useEffect, useState } from "react";

import atlasApi from "../api/atlasApi";

import TopEntities from "../components/TopEntities";
import ExecutiveBrief from "../components/ExecutiveBrief";
import InsightList from "../components/InsightList";
import "../styles/dashboard.css";

import StatsBar from "../components/StatsBar";

function Dashboard() {

    const [dashboard, setDashboard] = useState(null);

    const [loading, setLoading] = useState(true);

    useEffect(() => {

        async function loadDashboard() {

            try {

                const response = await atlasApi.get(
                    "/dashboard/"
                );

                setDashboard(
                    response.data
                );

            }

            catch (error) {

                console.error(error);

            }

            finally {

                setLoading(false);

            }

        }

        loadDashboard();

    }, []);

    if (loading) {

        return <h2>Loading Atlas...</h2>;

    }

    if (!dashboard) {

        return <h2>Unable to load dashboard.</h2>;

    }

    return (

        <div className="dashboard">
    
            <h1>Atlas Dashboard</h1>

            <p className="subtitle">
                Executive Intelligence Overview
            </p>

            <StatsBar dashboard={dashboard} />
    
            <div className="dashboard-grid">
    
                <div className="left-column">
    
                    <TopEntities
                        entities={dashboard.top_entities}
                    />
    
                </div>
    
                <div className="right-column">
    
                    <ExecutiveBrief
                        brief={dashboard.executive_brief}
                    />
    
                    <InsightList
                        insights={dashboard.insights}
                    />
    
                </div>
    
            </div>
    
        </div>
    
    );
}

export default Dashboard;