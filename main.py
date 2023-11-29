import streamlit as st
import pandas as pd

st.title('Data Visualization')

st.file_uploader('Choose a csv file', type=(['.csv'])

if data_file is not None:
  df = pd_read_csv(data_file)
  st.dataframe(df)
