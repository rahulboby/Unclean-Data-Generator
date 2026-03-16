import streamlit as st
import data_downloader as downloader
import generator

st.title("Download Unclean Data to test your Agents")

num_records = st.number_input(
    "Number of records to generate (Min 200)",
    min_value=1,
    value=200,
    step=1
)

if st.button("Generate Data"):
    data = generator.get_data(num_rows=int(num_records))
    st.dataframe(data)
    downloader.add_download_buttons(data, "Download Unclean Data")