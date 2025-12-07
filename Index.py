import streamlit as st
from pathlib import Path
import base64




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
def get_base64(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()

avatar_base64 = get_base64(avatar_path)

st.markdown(
    f"""
    <img class='avatar' src="data:image/jpeg;base64,{avatar_base64}">
    """,
    unsafe_allow_html=True
)
# ---------------------------------------
# Main Text
# ---------------------------------------

st.markdown("<div class='header-text'>Bruce Zhang</div>", unsafe_allow_html=True)
st.markdown(
    "<div class='sub-text'>NYU MSDS · Machine Learning · Data Science · LLM Research</div>",
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
I'm a graduate student at NYU Center for Data Science estimated to graduate in May 2027, working across  
**LLM evaluation**, **geospatial analytics**, **POI inference**, and **applied ML research**. I graduated from UCLA in June 2025 with BS in Applied Math and Stats and Data Science. 

This site showcases some of my projects, dashboards, and live demos.
        """
    )

    st.markdown("</div>", unsafe_allow_html=True)

# ---------------------------------------
# Navigation Buttons (Optional)
# ---------------------------------------
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("📁 Projects"):
        st.switch_page("pages/1_Projects.py")

with col2:
    if st.button("✉️ Contact"):
        st.switch_page("pages/3_Contact.py")

with col3:
    if st.button("📄 Resume"):
        st.session_state.show_resume = not st.session_state.get("show_resume", False)



# -----------------------------------------
# Resume Viewer (toggle section)
# -----------------------------------------
if st.session_state.get("show_resume", False):

    st.markdown("### 📄 My Resume")

    # PDF path
    pdf_path = "assets/resume.pdf"   # <-- 换成你自己的路径

    # Read PDF as bytes for download + HTML embed
    with open(pdf_path, "rb") as f:
        pdf_bytes = f.read()

    # Download button
    st.download_button(
        label="Download Resume",
        data=pdf_bytes,
        file_name="Bruce_Zhang_Resume.pdf",
        mime="application/pdf",
    )

    # PDF Viewer
    base64_pdf = base64.b64encode(pdf_bytes).decode('utf-8')
    pdf_display = f"""
        <iframe 
            src="data:application/pdf;base64,{base64_pdf}" 
            width="100%" height="900px" 
            type="application/pdf">
        </iframe>
    """
    st.components.v1.html(pdf_display, height=900)
