import streamlit as st
from streamlit_option_menu import option_menu


title = "Woolworths Project"
title = st.markdown(
    f"<h1 style='text-align: center;'>{title}</h1>", unsafe_allow_html=True
)

menu = option_menu(
    menu_title=None,
    options=["Donations", "Barcode Scanner", "Dataset"],
    icons=["suit-heart-fill", "piggy-bank", "piggy-bank"],  # https://icons.getbootstrap.com/
    menu_icon="menu-up",
    default_index=0,
    orientation="vertical",
    styles=None,
)
