import plotly.express as px


def create_registration_timeline(summary):
    fig = px.line(
        summary["registration_df"],
        x="Date",
        y="Count",
        title="Registration Timeline",
    )
    return fig
