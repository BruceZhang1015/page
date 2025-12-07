import streamlit as st
import requests
import json
import os
from pymongo import MongoClient
from datetime import datetime

# MongoDB connection (from secrets.toml)
client = MongoClient(st.secrets["MONGO_URI"])
db = client["portfolio_db"]
messages_collection = db["messages"]

RESEND_API_KEY = st.secrets["RESEND_API_KEY"]



# ---------------------------------------------------------
# Page Config
# ---------------------------------------------------------
st.set_page_config(
    page_title="Contact | Bruce Zhang",
    page_icon="✉️",
    layout="wide"
)

def send_email_notification(name, email, message):
    url = "https://api.resend.com/emails"
    headers = {
        "Authorization": f"Bearer {RESEND_API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "from": "Portfolio Contact <onboarding@resend.dev>",
        "to": ["yz8063@nyu.edu"],  # ← 你的真实 email
        "subject": f"New message from {name}",
        "html": f"""
            <p><strong>Name:</strong> {name}</p>
            <p><strong>Email:</strong> {email}</p>
            <p><strong>Message:</strong></p>
            <p>{message}</p>
        """
    }

    response = requests.post(url, headers=headers, data=json.dumps(data))
    return response


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
    # Save to MongoDB
        doc = {
            "name": name,
            "email": email,
            "message": message,
            "timestamp": datetime.utcnow()
        }
        messages_collection.insert_one(doc)

        # Send email notification
        send_email_notification(name, email, message)

        st.success("Thanks for reaching out! I’ll get back to you shortly.")

