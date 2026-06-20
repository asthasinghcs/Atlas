import EntityCard from "../../entity/EntityCard/EntityCard";

function TopEntities({ entities }) {

    return (

        <section>

            <h2>Top Influential Entities</h2>

            {

                entities.map(

                    entity => (

                        <EntityCard

                            key={entity.entity}

                            entity={entity}

                        />

                    )

                )

            }

        </section>

    );

}

export default TopEntities;