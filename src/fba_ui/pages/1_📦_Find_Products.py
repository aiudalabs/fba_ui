import streamlit as st
from PIL import Image

st.title("👋 Search For Competitive Products")

with st.sidebar:
    st.caption("Data from Amazon using https://rainforestapi.com/ API")
    st.image(Image.open("pages/a.png"))
