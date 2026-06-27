import { useEffect, useState } from "react";

import atlasApi from "../../api/atlasApi";

import TopEntities from "../../components/dashboard/TopEntities/TopEntities";
import ExecutiveBrief from "../../components/dashboard/ExecutiveBrief/ExecutiveBrief";
import InsightList from "../../components/dashboard/InsightList/InsightList";
import StatsBar from "../../components/dashboard/StatsBar/StatsBar";

import "./Dashboard.css";

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

                console.error("Dashboard request failed");
            
                console.error(error);
            
                console.error(error.response);
            
                console.error(error.response?.data);
            
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
    
            <section className="hero-section">
    
                <ExecutiveBrief
                    brief={dashboard.executive_brief}
                />
    
            </section>
    
            <section className="metrics-section">
    
                <StatsBar dashboard={dashboard} />
    
            </section>
    
            <section className="intelligence-grid">
    
                <div className="entities-column">
    
                    <TopEntities
                        entities={dashboard.top_entities}
                    />
    
                </div>
    
                <div className="signals-column">
    
                    <InsightList
                        insights={dashboard.insights}
                    />
    
                </div>
    
            </section>
    
            <section className="activity-section">
    
                <div className="placeholder-panel">
    
                    Knowledge Activity
    
                </div>
    
            </section>
    
        </div>
    
    );
}

export default Dashboard;