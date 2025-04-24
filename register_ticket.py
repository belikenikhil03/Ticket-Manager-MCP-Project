import streamlit as st
from tools.sheet_connector import append_ticket_to_sheet

st.set_page_config(page_title="Submit a support ticket", page_icon="✔")

st.title("Submit a support ticket")

st.markdown("We will get back to you shortly with a helpful response.")

with st.form("ticket_form"):
    name = st.text_input("Full name")
    email = st.text_input("Email address")
    issue_type = st.selectbox("Issue type", ["Billing", "Technical", "Login issue", "Other"])
    message = st.text_area("Message")

    submitted = st.form_submit_button("Submit ticket")

    if submitted:
        if not name or not email or not message:
            st.error("Please fill in all the fields.")
        
        else:
            append_ticket_to_sheet(name, email, issue_type, message)
            st.success("Ticket submitted successfully!")
            