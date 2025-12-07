import streamlit as st
from pathlib import Path

# ---------------------------------------
# Page config
# ---------------------------------------
st.set_page_config(
    page_title="Bruce Zhang | Portfolio",
    page_icon="✨",
    layout="centered"
)

# ---------------------------------------
# Basic Styling
# ---------------------------------------
# You can later move this into a CSS file
circle_image_css = """
<style>
.avatar {
    width: 140px;
    height: 140px;
    border-radius: 50%;
    object-fit: cover;
    display: block;
    margin-left: auto;
    margin-right: auto;
    box-shadow: 0 0 8px rgba(0,0,0,0.15);
}
.header-text {
    text-align: center;
    font-size: 32px;
    font-weight: 600;
    margin-top: 18px;
}
.sub-text {
    text-align: center;
    font-size: 18px;
    color: #555;
    margin-top: -5px;
}
.center-box {
    max-width: 600px;
    margin-left: auto;
    margin-right: auto;
    padding: 25px;
}
</style>
"""
st.markdown(circle_image_css, unsafe_allow_html=True)

# ---------------------------------------
# Avatar
# ---------------------------------------
avatar_path = "images/avatar.jpg"  # <<< replace with your image path

if Path(avatar_path).exists():
    st.markdown(f"<img class='avatar' src='{avatar_path}'/>", unsafe_allow_html=True)
else:
    st.warning("Please place your avatar image in images/avatar.jpg")

# ---------------------------------------
# Main Text
# ---------------------------------------

st.markdown("<div class='header-text'>Bruce Zhang</div>", unsafe_allow_html=True)
st.markdown(
    "<div class='sub-text'>NYU MSDS · Machine Learning · Data Engineering · LLM Research</div>",
    unsafe_allow_html=True
)

# ---------------------------------------
# Intro Section
# ---------------------------------------
with st.container():
    st.markdown("<div class='center-box'>", unsafe_allow_html=True)

    st.write(
        """
Hi! I'm Bruce.  
I'm a graduate student at NYU Center for Data Science, working across  
**LLM evaluation**, **geospatial analytics**, **POI inference**, and **applied ML research**.

This site showcases some of my projects, dashboards, and live demos built with Streamlit.
        """
    )

    st.markdown("</div>", unsafe_allow_html=True)

# ---------------------------------------
# Navigation Buttons (Optional)
# ---------------------------------------
col1, col2, col3 = st.columns(3)

with col1:
    st.page_link("pages/1_Projects.py", label="Projects", icon="📁")

with col2:
    st.page_link("pages/2_MathLabs.py", label="MathLabs", icon="📊")

with col3:
    st.page_link("pages/3_Contact.py", label="Contact", icon="✉️")
