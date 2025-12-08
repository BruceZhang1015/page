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
# Beautiful UI CSS
# ---------------------------------------------------------
card_css = """
<style>

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

/* --------- Remove Streamlit default markdown padding --------- */
.stMarkdown, .stMarkdown div {
    background-color: transparent !important;
    padding-top: 0 !important;
    padding-bottom: 0 !important;
}

/* --------- Card Container --------- */
.project-card {
    background: #ffffff;
    padding: 28px 32px;
    border-radius: 14px;
    margin: 28px 0;
    border: 1px solid #ebebeb;
    transition: all 0.15s ease;
    box-shadow: 0 2px 6px rgba(0,0,0,0.04);
}
.project-card:hover {
    box-shadow: 0 6px 18px rgba(0,0,0,0.08);
    transform: translateY(-2px);
}

/* --------- Title / Description --------- */
.project-title {
    font-size: 26px;
    font-weight: 700;
    margin-bottom: 6px;
}
.project-desc {
    font-size: 16px;
    color: #555;
    line-height: 1.5;
    margin-bottom: 14px;
}

/* --------- Tech Badge Styling --------- */
.tech-badge {
    display: inline-block;
    padding: 4px 12px;
    border-radius: 10px;
    background-color: #eef1f7;
    margin-right: 8px;
    margin-bottom: 8px;
    font-size: 13px;
    color: #445;
    border: 1px solid #dde3f0;
}

/* --------- External Button Styling --------- */
.ext-btn-container {
    margin-top: 12px;
}

.ext-button {
    padding: 8px 18px;
    border-radius: 8px;
    background-color: #fafafa;
    border: 1px solid #d0d0d0;
    cursor: pointer;
    font-size: 14px;
    margin-right: 12px;
    transition: all 0.15s;
}
.ext-button:hover {
    background-color: #f1f1f1;
    border-color: #bbb;
}
.ext-button:active {
    transform: scale(0.97);
}

</style>
"""
st.markdown(card_css, unsafe_allow_html=True)



# ---------------------------------------------------------
# Header
# ---------------------------------------------------------
st.title("📁 Projects")
st.write(
    "Here is a curated selection of my work across LLM evaluation, "
    "geospatial modeling, and ML research."
)



# ---------------------------------------------------------
# Project Card Renderer
# ---------------------------------------------------------
def project_card(title, desc, tech_list=None, links=None):
    st.markdown("<div class='project-card'>", unsafe_allow_html=True)

    # Title + description
    st.markdown(f"<div class='project-title'>{title}</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='project-desc'>{desc}</div>", unsafe_allow_html=True)

    # Tech badges
    if tech_list:
        badges_html = " ".join(
            f"<span class='tech-badge'>{t}</span>" for t in tech_list
        )
        st.markdown(badges_html, unsafe_allow_html=True)

    # External links (PRETTY BUTTONS, no Streamlit columns)
    if links:
        st.markdown("<div class='ext-btn-container'>", unsafe_allow_html=True)

        buttons_html = " ".join(
            [
                f"<a href='{url}' target='_blank'>"
                f"<button class='ext-button'>{label}</button>"
                f"</a>"
                for label, url in links.items()
            ]
        )
        st.markdown(buttons_html, unsafe_allow_html=True)

        st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)



# ---------------------------------------------------------
# Your Unmodified Projects
# ---------------------------------------------------------
project_card(
    title="MathLabs Benchmark System",
    desc="An evaluation pipeline for student-vs-master LLM performance on math MCQ tasks, "
         "featuring diagram generation, automated scoring, confidence intervals, and dataset management.",
    tech_list=["Python", "Streamlit", "MongoDB", "Plotly", "LLMs"],
    links={
        "GitHub": "https://github.com/mathlabsNYU/mathlabs",
        "Live Demo": "https://mathlabs.streamlit.app/",
    }
)

project_card(
    title="POI Inference from Staypoints",
    desc="Indirect inference of activity types and POI categories from spatiotemporal staypoints using "
         "LLMs, geospatial heuristics, and sequence alignment (SAM).",
    tech_list=["Python", "GeoPandas", "LLMs", "Trajectory Modeling"],
    links={
        "Notebook": "https://colab.research.google.com/drive/1GoaJVGJKYqYZPMR2WTfadK0FdsIfReBY?usp=sharing",
    }
)


project_card(
    title="CTR Prediction for ",
    desc="Investigates how feature selection, down-sampling, and data permutation affect the downstream utility of synthetically generated data from CTGAN in highly imbalanced classification tasks.",
    tech_list=["Python", "Pandas", "Scikit-learn", "CTGAN"],
    links={
        "GitHub": "https://github.com/BruceZhang1015/Click-Through-Rate-CTR-Prediction-and-Synthetic-Data-Usability-Investigation",
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
