import "./ExecutiveBrief.css";

function ExecutiveBrief({ brief }) {

    return (

        <section className="executive-brief">

            <div className="brief-header">

                <span className="brief-label">
                    Executive Intelligence Brief
                </span>

                <span className="brief-status">
                    Live
                </span>

            </div>

            <p className="brief-content">

                {brief}

            </p>

        </section>

    );

}

export default ExecutiveBrief;