import streamlit as st

# ---------------------------------------------------------
# Page Config
# ---------------------------------------------------------
st.set_page_config(
    page_title="Contact | Bruce Zhang",
    page_icon="✉️",
    layout="centered"
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
If you'd like to discuss research, data science, LLM evaluation,  
or potential collaboration opportunities, feel free to reach out!
"""
)

# ---------------------------------------------------------
# Contact Information
# ---------------------------------------------------------
st.markdown("<div class='contact-item'><span class='label'>Email:</span> yz8063@nyu.edu</div>", unsafe_allow_html=True)
st.markdown("<div class='contact-item'><span class='label'>LinkedIn:</span> <a href='https://www.linkedin.com/in/bruce-zhang-6a873421a/' target='_blank'>linkedin.com/in/bruce-zhang-6a873421a/</a></div>", unsafe_allow_html=True)
st.markdown("<div class='contact-item'><span class='label'>GitHub:</span> <a href='https://github.com/yourgithub' target='_blank'>github.com/yourgithub</a></div>", unsafe_allow_html=True)

st.write("")
st.write("")

# ---------------------------------------------------------
# Buttons
# ---------------------------------------------------------
col1, col2, col3 = st.columns(3)

with col1:
    st.link_button("Email", "mailto:bruce.zhang@example.com")
with col2:
    st.link_button("LinkedIn", "https://linkedin.com/in/yourprofile")
with col3:
    st.link_button("GitHub", "https://github.com/yourgithub")

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
