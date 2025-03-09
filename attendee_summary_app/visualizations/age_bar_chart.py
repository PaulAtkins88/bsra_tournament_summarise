import plotly.express as px

def create_age_bar_chart(summary):
    fig = px.bar(
        summary["age_df"],
        x="Age Group",
        y="Count",
        title="Age Distribution",
    )
    return fig