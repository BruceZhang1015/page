import streamlit as st

# ---------------------------------------------------------
# Page Config
# ---------------------------------------------------------
st.set_page_config(
    page_title="Contact | Bruce Zhang",
    page_icon="✉️",
    layout="wide"
)

# ---------------------------------------------------------
# CSS Styling
# ---------------------------------------------------------
contact_css = """
<style>
.contact-card {
    background-color: #ffffff;
    padding: 28px;
    border-radius: 16px;
    box-shadow: 0 2px 10px rgba(0,0,0,0.08);
    max-width: 520px;
    margin-left: auto;
    margin-right: auto;
}
.contact-title {
    font-size: 28px;
    font-weight: 600;
    text-align: center;
    margin-bottom: 12px;
}
.contact-item {
    font-size: 17px;
    margin-bottom: 10px;
}
.label {
    font-weight: 600;
}
</style>
"""
st.markdown(contact_css, unsafe_allow_html=True)

# ---------------------------------------------------------
# Content
# ---------------------------------------------------------
st.markdown("<div class='contact-card'>", unsafe_allow_html=True)

st.markdown("<div class='contact-title'>Get In Touch</div>", unsafe_allow_html=True)

st.write(
    """
Please feel free to reach out for any questions or collaboration/job opportunities!
"""
)

# ---------------------------------------------------------
# Contact Information
# ---------------------------------------------------------
st.markdown("<div class='contact-item'><span class='label'>Email:</span> yz8063@nyu.edu</div>", unsafe_allow_html=True)
st.markdown("<div class='contact-item'><span class='label'>LinkedIn:</span> <a href='https://www.linkedin.com/in/bruce-zhang-6a873421a/' target='_blank'>linkedin.com/in/bruce-zhang-6a873421a/</a></div>", unsafe_allow_html=True)
st.markdown("<div class='contact-item'><span class='label'>GitHub:</span> <a href='https://github.com/BruceZhang1015' target='_blank'>github.com/BruceZhang1015</a></div>", unsafe_allow_html=True)

st.write("")
st.write("")

# ---------------------------------------------------------
# Buttons
# ---------------------------------------------------------
col2, col3 = st.columns(2)


with col2:
    st.link_button("LinkedIn", "https://www.linkedin.com/in/bruce-zhang-6a873421a/")
with col3:
    st.link_button("GitHub", "https://github.com/BruceZhang1015")

st.markdown("</div>", unsafe_allow_html=True)


# ---------------------------------------------------------
# Optional: Contact Form (Message)
# ---------------------------------------------------------
st.write("")
st.subheader("Send Me a Message")

with st.form("contact_form"):
    name = st.text_input("Your Name")
    email = st.text_input("Your Email")
    message = st.text_area("Message")

    submitted = st.form_submit_button("Send")
    if submitted:
        st.success("Thanks for reaching out! I’ll get back to you shortly.")
