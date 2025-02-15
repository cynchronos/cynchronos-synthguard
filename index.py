import streamlit as st
from streamlit_option_menu import option_menu
from app.home import home
from app.deepfake_analyzer import deepfake_analyzer
from app.settings import settings

st.set_page_config(page_title="Cynchronos SynthGuard", layout="wide")


# sidebar menu
def main():
    with st.sidebar:
        sidebar = option_menu(
            "Cynchronos SynthGuard",
            ["Home", "DeepFake Analyzer", "Settings"],
            icons=["house", "vignette", "gear"],
            menu_icon="opencollective",
            default_index=0,
            key="sidebar",
            styles={
                "menu-title": {"font-weight": "bold"},
                "menu-icon": {"color": "#f22929"},
            },
        )

    if sidebar == "Home":
        home()
    elif sidebar == "DeepFake Analyzer":
        deepfake_analyzer()
    elif sidebar == "Settings":
        settings()


if __name__ == "__main__":
    main()
