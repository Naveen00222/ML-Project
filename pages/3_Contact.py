import streamlit as st

st.markdown("<h1>📬 Contact & Feedback</h1>", unsafe_allow_html=True)

st.markdown("""
We’d love to hear your thoughts and feedback about **Futuristic Health AI**.

If you’re a researcher, healthcare professional, or student interested in collaboration — get in touch!
""")

name = st.text_input("Your Name")
email = st.text_input("Email Address")
message = st.text_area("Message")

if st.button("Send Message"):
    if name and email and message:
        st.success("✅ Thank you for reaching out! We’ll get back to you soon.")
    else:
        st.error("⚠️ Please fill all fields before submitting.")
