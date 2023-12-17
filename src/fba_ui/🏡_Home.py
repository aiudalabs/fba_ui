import streamlit as st
from streamlit_extras.app_logo import add_logo
import pandas as pd
import numpy as np

st.set_page_config(page_title="FBA", page_icon="👋", layout="wide")


st.title("👋 Amazon FBA UI")

# st.sidebar.success("Select a functionality above.")

# add_logo("/home/nmlemus/projects/fba_ui/src/fba_ui/a.png", height=100)

st.write(" ")

st.subheader("What is Amazon FBA?")

st.markdown(
    """
        ###### Amazon FBA (Fulfillment by Amazon) is a service provided by Amazon that allows sellers to store their products in Amazon's fulfillment centers. When a customer purchases a product from a seller using FBA, Amazon takes care of the storage, packaging, and shipping of the product. Here are some key aspects of Amazon FBA:

        - Storage: Sellers send their products to Amazon's fulfillment centers, where they are stored in warehouses until sold.
        - Order Handling: When a customer places an order for a product that is fulfilled by Amazon, the order is processed by Amazon itself.
        - Shipping and Delivery: Amazon handles the packing and shipping of the product to the customer. This includes selecting the shipping method and managing returns.
        - Customer Service: Amazon also provides customer service for products sold through FBA, including handling inquiries, returns, and refunds.
        - Global Reach: FBA can help sellers reach a wider customer base, as Amazon has an extensive and efficient distribution network.
        - Costs: While FBA can save sellers time and effort, it involves certain costs, such as storage fees and fulfillment fees, which vary based on the size and weight of the products.
        - Prime Eligibility: Products fulfilled by Amazon are eligible for Amazon Prime, which can increase their visibility and appeal to Prime subscribers due to benefits like free two-day shipping.
        - Inventory Management: Amazon provides tools for sellers to manage their inventory, track sales, and understand their customers' buying habits.

        ###### FBA is popular among sellers because it simplifies the logistics of selling online, \
        especially for those who do not want to handle shipping and customer service. However, \
        it's important for sellers to consider the costs and ensure their products are a good fit for the FBA model.
    """
)
