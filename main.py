import streamlit as st
from streamlit_option_menu import option_menu


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

    pages = {
        "Donations": access_donations,
        "Barcode Scanner": receive_barcodes,
        "Dataset": view_dataset,
    }
    st.write(menu)
    pages["Donations"]

    st.write(pages[menu])


def access_donations():
    st.title("Donations Received Today:")


def receive_barcodes():
    st.text_input("Enter barcode:")


def view_dataset():
    st.title("Woolworths Dataset:")


if __name__ == "__main__":
    main()
