from typing import Callable
import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
from sqlalchemy import create_engine, engine


def create_connection_config() -> dict[str, str]:
    """Creates and returns a database connection configuration."""
    return {
        'dialect': 'postgresql',
        'username': 'postgres',
        'password': 'be_happy_and_creative',
        'host': '159.65.239.177',
        'port': '5432',
        'database': 'postgres'
    }


def create_connection_url(connection_config: dict[str, str]) -> str:
    """Creates and returns a connection URL based on the given connection configuration."""
    return (
        f"{connection_config['dialect']}://"
        f"{connection_config['username']}:{connection_config['password']}@"
        f"{connection_config['host']}:{connection_config['port']}/"
        f"{connection_config['database']}"
    )


def create_db_engine(connection_url: str) -> engine.base.Engine:
    """Creates and returns a SQLAlchemy engine based on the given connection URL."""
    return create_engine(connection_url)


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
    query = """
    SELECT *
    FROM dataset
    GROUP BY category
    ORDER BY product_code;
    """
    st.title("Woolworths Dataset:")
    fetch_data(query, engine)


if __name__ == "__main__":
    # Create a connection config
    config = create_connection_config()

    # Create a connection URL from the config
    url = create_connection_url(config)

    # Create an engine using the connection URL
    engine = create_db_engine(url)

    main()
