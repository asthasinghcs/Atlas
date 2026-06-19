def build_dashboard(
    top_entities,
    insights,
    executive_brief
):
    print("========== NEW DASHBOARD BUILDER ==========")

    return {
        "top_entities": top_entities,
        "insights": insights,
        "executive_brief": executive_brief,
        "stats": {
            "entities": 247,
            "relationships": 6913,
            "documents": 58,
            "average_influence": 218
        }
    }