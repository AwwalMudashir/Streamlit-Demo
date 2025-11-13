import streamlit as st

def show():
    st.subheader("Form")

    name = st.text_input("Enter your name")

    if name.startswith("a"):
        st.image("s-logo.png", caption="Streamlit Logo")

    age = st.number_input("Enter your age", step=0.5)

    option = st.selectbox("Choose your role", ["Senior", "Mid", "Junior"])
    gender = st.radio("Gender : ", ["Male", "Female"])

    agree = st.checkbox("I accept to the terms")

    clicked = st.button("Click")

    if clicked:
        st.success("Congratulations")