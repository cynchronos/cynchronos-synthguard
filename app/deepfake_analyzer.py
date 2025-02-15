import streamlit as st


def deepfake_analyzer():
    container = st.container(border=True)

    st.markdown("""
                <style>
                  .header-upload {
                      display:flex;
                      flex-direction:column;
                      align-items: center;
                      font-size:32px;
                    }

                  .stFileUploader {
                    width: 50% !important;
                    margin:auto;
                  }

                  .upload-icon {
                      display: flex;
                      justify-content: center;
                      padding-bottom: 1em;
                  }
                  
                </style>
                """, unsafe_allow_html=True
                )

    with container:
        st.write(
            """
        <div class="header-upload">
          <p>
            Choose Your Image to Analyze
          <p>
        </div>
      """, unsafe_allow_html=True
        )

        if 'uploaded_image' in st.session_state:
          try:
            _, _, _, c4, _, _, _ = st.columns(7)
            c4.image(st.session_state['uploaded_image'])
          except:
            st.write(
            """
            <div class="upload-icon">
              <svg xmlns="http://www.w3.org/2000/svg" width="64" height="64" fill="currentColor" class="bi bi-image" viewBox="0 0 16 16">
                <path d="M6.002 5.5a1.5 1.5 0 1 1-3 0 1.5 1.5 0 0 1 3 0"/>
                <path d="M2.002 1a2 2 0 0 0-2 2v10a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V3a2 2 0 0 0-2-2zm12 1a1 1 0 0 1 1 1v6.5l-3.777-1.947a.5.5 0 0 0-.577.093l-3.71 3.71-2.66-1.772a.5.5 0 0 0-.63.062L1.002 12V3a1 1 0 0 1 1-1z"/>
              </svg>
            </div>
          """, unsafe_allow_html=True
        )
        else:
          st.write(
            """
            <div class="upload-icon">
              <svg xmlns="http://www.w3.org/2000/svg" width="64" height="64" fill="currentColor" class="bi bi-image" viewBox="0 0 16 16">
                <path d="M6.002 5.5a1.5 1.5 0 1 1-3 0 1.5 1.5 0 0 1 3 0"/>
                <path d="M2.002 1a2 2 0 0 0-2 2v10a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V3a2 2 0 0 0-2-2zm12 1a1 1 0 0 1 1 1v6.5l-3.777-1.947a.5.5 0 0 0-.577.093l-3.71 3.71-2.66-1.772a.5.5 0 0 0-.63.062L1.002 12V3a1 1 0 0 1 1-1z"/>
              </svg>
            </div>
          """, unsafe_allow_html=True
        )

        _, _, _, c4, _, _, _ = st.columns(7)

        def process_image():
            if st.session_state['uploaded_image'] is not None:
              c4.button("Analyze", use_container_width=True)

        st.file_uploader(
            "format: *.jpg, *.jpeg, *.png",
            type=["png", "jpg", "jpeg"],
            accept_multiple_files=False,
            on_change=process_image,
            key="uploaded_image"
        )


if __name__ == "__main__":
    deepfake_analyzer()
