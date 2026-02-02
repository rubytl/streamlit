import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write("Preview of Data:")
    st.dataframe(df.head())

    metric = st.selectbox("Choose a metric:", ["test_score", "gpa_or_score"])

    total_value = df[metric].sum()
    st.write(f"**Total {metric.capitalize()}:** {total_value}")

    agg_by_region = df.groupby("origin_country")[metric].sum()
    st.write(f"**{metric.capitalize()} by Region:**")
    st.write(agg_by_region)

    chart_type = st.selectbox("Choose a chart type:", ["Bar", "Line", "Pie"])

    fig, ax = plt.subplots()
    if chart_type == "Bar":
        agg_by_region.plot(kind="bar", ax=ax, color="skyblue", edgecolor="black")
        ax.set_ylabel(metric.capitalize())
        ax.set_title(f"{metric.capitalize()} by Region")
    elif chart_type == "Line":
        agg_by_region.plot(kind="line", marker="o", ax=ax, color="green")
        ax.set_ylabel(metric.capitalize())
        ax.set_title(f"{metric.capitalize()} by Region")
    elif chart_type == "Pie":
        agg_by_region.plot(kind="pie", autopct="%1.1f%%", ax=ax)
        ax.set_ylabel(metric.capitalize())
        ax.set_title(f"{metric.capitalize()} by Region")
    st.pyplot(fig)