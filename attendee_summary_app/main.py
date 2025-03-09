import pandas as pd
import streamlit as st
from utils.data_loader import load_data
from utils.summaries import summarize_attendees
from visualizations.age_bar_chart import create_age_bar_chart
from visualizations.registration_timeline import create_registration_timeline
from visualizations.section_pie_chart import create_section_pie_chart
from visualizations.ticket_type_bar_chart import create_ticket_type_bar_chart

# Streamlit web app
st.set_page_config(page_title="Attendee Summary App")

st.title("Attendee Summary App")

uploaded_file = st.file_uploader("Upload CSV file", type="csv")

if uploaded_file is not None:
    df = load_data(uploaded_file)
    summary = summarize_attendees(df)

    st.markdown(
        f"""
        <div class="card p-3">
            <h5 class="card-title">Summary Report</h5>
            <p>Total Attendees: {summary['total_attendees']}</p>
            <p>Total Paid: {summary['total_paid']:.2f}</p>
        </div>
        <br>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class="card p-3">
            <h5 class="card-title">Players per Section</h5>
            <ul class="list-group list-group-flush">
        """,
        unsafe_allow_html=True,
    )
    for section, count in summary['section_data'].items():
        st.markdown(f"<li class='list-group-item'>{section}: {count}</li>", unsafe_allow_html=True)
    st.markdown("</ul></div><br>", unsafe_allow_html=True)

    st.markdown(
        f"""
        <div class="card p-3">
            <h5 class="card-title">Juniors/Adults and Age</h5>
            <p>Juniors: {summary['junior_count']}</p>
            <p>Adults: {summary['adult_count']}</p>
            <p>Average Age: {summary['average_age']:.1f}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown('<div class="chart-row">', unsafe_allow_html=True)
    st.markdown('<div class="chart-container">', unsafe_allow_html=True)
    st.plotly_chart(create_section_pie_chart(summary))
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="chart-container">', unsafe_allow_html=True)
    st.plotly_chart(create_age_bar_chart(summary))
    st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="chart-row">', unsafe_allow_html=True)
    st.markdown('<div class="chart-container">', unsafe_allow_html=True)
    st.plotly_chart(create_ticket_type_bar_chart(summary))
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="chart-container">', unsafe_allow_html=True)
    st.plotly_chart(create_registration_timeline(summary))
    st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)