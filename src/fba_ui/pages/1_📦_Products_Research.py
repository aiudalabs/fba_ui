import streamlit as st
from st_aggrid import AgGrid
from st_aggrid.grid_options_builder import GridOptionsBuilder
from PIL import Image

import requests
import json

import pandas as pd

import keepa

# enter real access key here
accesskey = "75pbng069l13ht8qbtt9pmnubdbp2eu3m5d6aih13r9rd41kagu43q9euvfis0gm"
api = keepa.Keepa(accesskey)


@st.cache_data
def get_best_sellers_by_category(category_id):
    # set up the request parameters
    params = {
        "api_key": "2758604B50A746EBA972BC894472FD83",
        "type": "bestsellers",
        "amazon_domain": "amazon.com",
        "category_id": category_id,
        "max_page": 2,
    }

    # make the http GET request to Rainforest API
    api_result = requests.get("https://api.rainforestapi.com/request", params)
    products = pd.DataFrame.from_dict(api_result.json().get("bestsellers"))

    return products


# make the http GET request to Rainforest API
@st.cache_data
def get_bestsellers_categories():
    api_result = requests.get(
        "https://api.rainforestapi.com/categories",
        params,
    )

    return api_result


def make_hyperlink(value):
    return '=HYPERLINK("%s")' % (value)


def get_price(row):
    try:
        return row.price["value"]
    except:
        return 0


def get_category(row):
    try:
        return row.current_category["id"]
    except:
        return None


st.title("👋 Products Research")

with st.sidebar:
    st.caption("Data from Amazon using https://rainforestapi.com/ API")
    # st.image(Image.open("pages/a.png"))

# set up the request parameters
params = {
    "api_key": "2758604B50A746EBA972BC894472FD83",
    "domain": "amazon.com",
    "type": "bestsellers",
}


api_result = get_bestsellers_categories()


bestsellers_categories = pd.DataFrame.from_dict(api_result.json().get("categories"))
bestsellers_categories = bestsellers_categories[["id", "name", "link"]]
bestsellers_categories = bestsellers_categories.sort_values("name")

options = st.multiselect(
    "Select Bestsellers Categories",
    bestsellers_categories.sort_values("name")["name"].values.tolist(),
    ["Patio, Lawn & Garden"],
)


selected_df = bestsellers_categories[bestsellers_categories["name"].isin(options)]

if selected_df.shape[0] > 0:
    selected_df = selected_df[["id", "name", "link"]]

    st.subheader("Selected Categories")
    st.write(selected_df)

    st.header("Add Filters")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.subheader("Price")
        min_price = st.number_input("Min Price", value=15)
        max_price = st.number_input("Max Price", value=30)

    with col2:
        st.subheader("Rating")
        min_rating = st.number_input(
            "Min Rating", value=0.0, min_value=0.0, max_value=3.0, format="%f", step=0.5
        )
        max_rating = st.number_input(
            "Max Rating", value=5.0, min_value=3.0, max_value=5.0, format="%f", step=0.5
        )

    with col3:
        st.subheader("Bought in past month")
        bought_past_month = st.number_input(
            "Bought Past Month", value=1000, min_value=100, max_value=50000
        )

    if st.button("Find Products", type="primary"):
        st.subheader("Products List")

        products = pd.DataFrame()
        for category_id in selected_df["id"].tolist():
            products = pd.concat([products, get_best_sellers_by_category(category_id)])

        products["price"] = products.apply(lambda row: get_price(row), axis=1)
        products["current_category"] = products.apply(
            lambda row: get_category(row), axis=1
        )

        products = products[
            (products.price >= min_price)
            & (products.price <= max_price)
            & (products.rating <= max_rating)
        ]

        products["selected"] = False

        edited_df = st.data_editor(
            products[
                [
                    "rank",
                    "position",
                    "title",
                    "asin",
                    "link",
                    "rating",
                    "ratings_total",
                    "price",
                    "current_category",
                    "selected",
                ]
            ],
            column_config={"link": st.column_config.LinkColumn("Amazon Link")},
            hide_index=True,
            disabled=[
                "rank",
                "position",
                "title",
                "asin",
                "link",
                "rating",
                "ratings_total",
                "price",
                "current_category",
            ],
        )

        # asins = products.head(3)["asin"].tolist()
        # keepa_products = api.query(asins, offers=20)

        # st.subheader("Products Details")

        # st.write(keepa_products)
