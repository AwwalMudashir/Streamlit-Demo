import streamlit as st
import table
import chart
import form

st.title("My First App")
# st.write("Hello World")

# st.image("s-logo.png",caption="Streamlit Logo")
# st.video("https://www.youtube.com/watch?v=pBX3m5r28ug&t=3491s")
# st.code("console.log('hello world')",language="javascript")

# st.header("Demo App")
# st.subheader("Introduction")
st.text("Hope you're liking streamlit ?")
# st.markdown("**Bold Text** and *italic text* using markdown")

import pandas as pd

def show():
    st.subheader("File Upload")

    uploaded_file = st.file_uploader("Upload a csv file", type="csv")

    if uploaded_file:
        df = pd.read_csv(uploaded_file)
        st.dataframe(df)

st.sidebar.title("Navigation")
page = st.sidebar.selectbox("Page",["Home","Table","Chart","Form"])

st.sidebar.info("Copyright Services 2025")


# Navigation simulation

if page == "Home":
    show()
elif page == "Table":
    table.show()
elif page == "Chart":
    chart.show()
elif page == "Form":
    form.show()
else:
    st.error("Error 404: Page Not Found")










