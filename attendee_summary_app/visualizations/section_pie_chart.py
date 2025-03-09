import plotly.express as px

def create_section_pie_chart(summary):
    fig = px.pie(
        names=list(summary['section_data'].keys()),
        values=[int(v.split()[0]) for v in summary['section_data'].values()],
        title="Section Distribution",
    )
    return fig