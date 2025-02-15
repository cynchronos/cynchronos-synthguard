import streamlit as st
from streamlit_option_menu import option_menu
from app.home import home
from app.deepfake_analyzer import deepfake_analyzer
from app.about import about

st.set_page_config(page_title="Cynchronos SynthGuard", layout="wide")


# sidebar menu
def main():
    with st.sidebar:
        sidebar = option_menu(
            "Cynchronos SynthGuard",
            ["Home", "DeepFake Analyzer", "About"],
            icons=["house", "vignette", "info-circle"],
            menu_icon="opencollective",
            default_index=0,
            key="sidebar",
            styles={
                "menu-title": {"font-weight": "bold"},
                "menu-icon": {"color": "#f22929"},
            },
        )

    if sidebar == "Home":
        page = st.navigation([st.Page(home)])
        page.run()
    elif sidebar == "DeepFake Analyzer":
        page = st.navigation([st.Page(deepfake_analyzer)])
        page.run()
    elif sidebar == "About":
        page = st.navigation([st.Page(about)])
        page.run()


if __name__ == "__main__":
    main()
