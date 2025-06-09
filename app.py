import streamlit as st
st.set_page_config(
    page_title="Streamlit App",
    page_icon="✨",
    layout="centered",
    initial_sidebar_state="collapsed",
)

st.markdown(
    """
    <style>
    .main-title {
        font-size: 50px;
        color: #4CAF50;
        text-align: center;
        font-weight: bold;
        margin-top: 20px;
        margin-bottom: 40px;
        font-family: Arial, sans-serif;
        text-shadow: 2px 2px 4px #888888;
    }
    </style>
    <h1 class="main-title">✨ Welcome to My Streamlit App! ✨</h1>
    """,
    unsafe_allow_html=True,
)
name = st.text_input("Enter your name:")
age = st.slider("Select your age:", 1, 100, 25)
if st.button("Submit"):
    if name.strip():
        st.success(f"Hello, {name}. You are {age} years old! 🎉")
    else:
        st.warning("Please enter your name before submitting!")
