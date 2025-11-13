import streamlit as st

def show():
    st.subheader("Pandas")

    import pandas as pd

    data = {"Name": ["John", "Mike", "Eleven", "Max", "Lucas", "Steve"], "Age": [20, 13, 11, 12, 12, 26]}
    df = pd.DataFrame(data)

    st.dataframe(df)
    # st.table(df)