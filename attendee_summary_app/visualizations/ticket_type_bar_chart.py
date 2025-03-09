import plotly.express as px


def create_ticket_type_bar_chart(summary):
    fig = px.bar(
        summary["ticket_type_df"],
        x="Ticket Type",
        y="Count",
        title="Ticket Type Distribution",
    )
    return fig
