import streamlit as st
from pathlib import Path

# ---------------------------------------------------------
# Page Config
# ---------------------------------------------------------
st.set_page_config(
    page_title="Projects | Bruce Zhang",
    page_icon="📁",
    layout="wide"
)

# ---------------------------------------------------------
# CSS for clean card layout
# ---------------------------------------------------------
card_css = """
<style>
.project-card {
    background-color: #ffffff;
    padding: 20px;
    border-radius: 12px;
    margin-bottom: 20px;
    box-shadow: 0 2px 8px rgba(0,0,0,0.08);
}
.project-title {
    font-size: 22px;
    font-weight: 600;
    margin-bottom: 6px;
}
.project-desc {
    font-size: 16px;
    color: #555;
    margin-bottom: 10px;
}
.tech-badge {
    display: inline-block;       /* 关键：改成横向排列 */
    padding: 4px 10px;
    border-radius: 8px;
    background-color: #eef1f5;
    margin-right: 6px;
    margin-bottom: 6px;
    font-size: 13px;
}
</style>
"""

st.markdown(card_css, unsafe_allow_html=True)

st.title("📁 Projects")
st.write("Here is a curated selection of my work across LLM evaluation, geospatial modeling, and ML research.")

# ---------------------------------------------------------
# Helper to render a project card
# ---------------------------------------------------------
def project_card(title, desc, tech_list=None, links=None):
    st.markdown("<div class='project-card'>", unsafe_allow_html=True)

    st.markdown(f"<div class='project-title'>{title}</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='project-desc'>{desc}</div>", unsafe_allow_html=True)

    # Tech badges
    # Tech badges (inline)
    if tech_list:
        badges_html = " ".join(
            [f"<span class='tech-badge'>{t}</span>" for t in tech_list]
        )
        st.markdown(badges_html, unsafe_allow_html=True)


    # External links
    if links:
        cols = st.columns(len(links))
        for i, (label, url) in enumerate(links.items()):
            with cols[i]:
                st.link_button(label, url)

    st.markdown("</div>", unsafe_allow_html=True)


# ---------------------------------------------------------
# Example Projects
# ---------------------------------------------------------
project_card(
    title="MathLabs Benchmark System",
    desc="An evaluation pipeline for student-vs-master LLM performance on math MCQ tasks, "
         "featuring diagram generation, automated scoring, confidence intervals, and dataset management.",
    tech_list=["Python", "Streamlit", "MongoDB", "Plotly", "LLMs"],
    links={
        "GitHub": "https://github.com/yourrepo",
        "Live Demo": "https://yourstreamlitlink",
    }
)

project_card(
    title="POI Inference from Staypoints",
    desc="Indirect inference of activity types and POI categories from spatiotemporal staypoints using "
         "LLMs, geospatial heuristics, and sequence alignment (SAM).",
    tech_list=["Python", "GeoPandas", "LLMs", "Trajectory Modeling"],
    links={
        "GitHub": "https://github.com/yourrepo",
    }
)

project_card(
    title="Data Engineering Pipeline for Geospatial Data",
    desc="A distributed ETL pipeline for cleaning, enriching, and normalizing multi-week location datasets "
         "with MySQL + GeoJSON + zoning integration.",
    tech_list=["SQL", "MariaDB", "Airflow (optional)", "Pandas"],
    links={
        "Report": "https://example.com",
    }
)

# ---------------------------------------------------------
# Tableau Section
# ---------------------------------------------------------
st.markdown("---")
st.subheader("📊 Tableau Visualizations")

st.write("Below is an embedded Tableau workbook showcasing one of my interactive dashboards.")

tableau_url = "https://public.tableau.com/views/YourWorkbookName/YourSheetName?:embed=y&:showVizHome=no"

# Streamlit supports raw HTML iframe embedding:
st.components.v1.html(
    f"""
    <iframe 
        src="{tableau_url}" 
        width="100%" 
        height="900px" 
        style="border: none;">
    </iframe>
    """,
    height=900,
)
