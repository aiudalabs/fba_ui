import streamlit as st
from st_aggrid import AgGrid
from st_aggrid.grid_options_builder import GridOptionsBuilder
from PIL import Image

import requests
import json

import pandas as pd


def make_hyperlink(value):
    return '=HYPERLINK("%s")' % (value)


st.title("👋 Search For Competitive Products")

with st.sidebar:
    st.caption("Data from Amazon using https://rainforestapi.com/ API")
    # st.image(Image.open("pages/a.png"))


# set up the request parameters
params = {
    "api_key": "2758604B50A746EBA972BC894472FD83",
    "domain": "amazon.com",
    "type": "bestsellers",
}

# make the http GET request to Rainforest API
api_result = requests.get("https://api.rainforestapi.com/categories", params)


bestsellers_categories = pd.DataFrame.from_dict(api_result.json().get("categories"))
bestsellers_categories = bestsellers_categories[["id", "name", "link"]]

# bestsellers_categories["link"] = bestsellers_categories["link"].apply(make_hyperlink)
gd = GridOptionsBuilder.from_dataframe(bestsellers_categories)
gd.configure_selection(selection_mode="multiple", use_checkbox=True)

gridOptions = gd.build()

AgGrid(
    bestsellers_categories.sort_values("name"), gridOptions=gridOptions, width="100%"
)
