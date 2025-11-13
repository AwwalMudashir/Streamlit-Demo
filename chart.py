import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

def show():
    st.subheader("Matplotlib")

    x = np.linspace(0, 10, 20)
    y = np.sin(x)

    fig, ax = plt.subplots()
    ax.plot(x, y)
    st.pyplot(fig)