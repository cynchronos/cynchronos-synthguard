import streamlit as st
from app.components.pre_upload_media import pre_upload_media
from app.components.analyze_media import analyze_media


def deepfake_analyzer():
    container = st.container(border=True)

    with container:
        if (
            "uploaded_media" in st.session_state
            and st.session_state.uploaded_media is not None
            and "processing_media" in st.session_state
            and st.session_state.processing_media == True
        ):
            analyze_media()
        else:
            st.session_state.processing_media = False
            pre_upload_media()


if __name__ == "__main__":
    deepfake_analyzer()
