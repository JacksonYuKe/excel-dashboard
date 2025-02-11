import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Set title
st.title("📊 Excel Data Visualization Dashboard")

# Upload Excel file
uploaded_file = st.file_uploader("Upload Excel file", type=["xlsx", "xls"])

if uploaded_file is not None:
    df = pd.read_excel(uploaded_file)
    st.write("Data Preview:", df.head())

    # Select columns
    columns = df.columns.tolist()
    x_axis = st.selectbox("Select X-axis", columns)
    y_axis = st.selectbox("Select Y-axis", columns)

    # Generate line chart
    if st.button("Generate Line Chart"):
        fig, ax = plt.subplots()
        ax.plot(df[x_axis], df[y_axis], marker="o", linestyle="-")
        ax.set_xlabel(x_axis)
        ax.set_ylabel(y_axis)
        ax.set_title(f"{y_axis} vs {x_axis}")
        st.pyplot(fig)
