import "../styles/executive-brief.css";

function ExecutiveBrief({ brief }) {

    return (

        <section className="executive-brief">

            <h2>Executive Brief</h2>

            <p>{brief}</p>

        </section>

    );

}

export default ExecutiveBrief;