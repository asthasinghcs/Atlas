import "../styles/insight-list.css";

function InsightList({ insights }) {

    return (

        <section className="insight-list">

            <h2>Insights</h2>

            <ul>

                {

                    insights.map(

                        (insight, index) => (

                            <li key={index}>

                                {insight}

                            </li>

                        )

                    )

                }

            </ul>

        </section>

    );

}

export default InsightList;