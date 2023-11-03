from typing import Callable
import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
from sqlalchemy import create_engine, engine


def fetch_data(query: str, engine: engine.base.Engine) -> pd.DataFrame:
    """Fetches data using SQL query and returns a DataFrame."""
    with engine.connect() as connection:
        result = pd.read_sql(query, connection)
    return result


def page_setup(page_title: str, layout: str) -> None:
    st.set_page_config(page_title=page_title, page_icon="🤖", layout=layout)


def display_title(title: str) -> None:
    st.markdown(
        body=f"<h1 style='text-align: center;'>{title}</h1>", unsafe_allow_html=True
    )


def main():
    page_title = "Woolworths Project"
    page_setup(page_title=page_title, layout="wide")
    display_title(page_title)

    menu = option_menu(
        menu_title=None,
        options=["Donations", "Barcode Scanner", "Dataset"],
        icons=[
            "clipboard-data",
            "upc-scan",
            "database",
        ],  # https://icons.getbootstrap.com/
        #menu_icon="menu-up",
        default_index=1,
        orientation="horizontal",
        styles=None,
    )

    pages: dict[str, Callable] = {
        "Donations": access_donations,
        "Barcode Scanner": receive_barcodes,
        "Dataset": view_dataset,
    }
    pages[menu]()


def access_donations():
    st.title("Donations Received Today:")


def receive_barcodes():
    st.text_input("Enter barcode:")


def view_dataset():
    st.title("Woolworths Dataset:")


if __name__ == "__main__":
    main()
