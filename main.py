import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(
    page_title="Woolworths Project",
    page_icon="🤖",
    layout="wide"
)

title = "Woolworths Project"
title = st.markdown(
    f"<h1 style='text-align: center;'>{title}</h1>", unsafe_allow_html=True
)

menu = option_menu(
    menu_title=None,
    options=["Donations", "Barcode Scanner", "Dataset"],
    icons=["clipboard-data", "upc-scan", "database"],  # https://icons.getbootstrap.com/
    menu_icon="menu-up",
    default_index=1,
    orientation="horizontal",
    styles=None,
)

def access_donations():
    st.title("Donations Received Today:")

def receive_barcodes():
    st.text_input("Enter barcode:")

def view_dataset():
    st.title("Woolworths Dataset:")
pages = {
    "Donations": access_donations,
    "Barcode Scanner": receive_barcodes,
    "Dataset": view_dataset
}

pages[menu]()