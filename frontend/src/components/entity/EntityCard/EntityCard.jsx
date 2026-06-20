import "./EntityCard.css";

function EntityCard({ entity }) {

    return (

        <div className="entity-card">

            <h3>{entity.entity}</h3>

            <p>Type: {entity.entity_type}</p>

            <p>Influence: {entity.influence_score}</p>

            <p>Mentions: {entity.mentions}</p>

            <p>Relationships: {entity.relationship_strength}</p>

        </div>

    );

}

export default EntityCard;