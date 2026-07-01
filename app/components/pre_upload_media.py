import streamlit as st
import time
import pathlib as ptl

def pre_upload_media():
  preview_media = None
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

  st.write(
            """
        <div class="header-upload">
          <p>
            Choose Your Image to Analyze
          <p>
        </div>
      """, unsafe_allow_html=True
        )

  if 'uploaded_media' in st.session_state:
    try:
      _, _, _, c4med, _, _, _ = st.columns(7)
      if ptl.Path(st.session_state['uploaded_media'].name).suffix in ['.jpg', '.jpeg', '.png']:
        st.session_state['thumbnail'] = st.session_state['uploaded_media']
        c4med.image(st.session_state['uploaded_media'], use_container_width=True)
      elif ptl.Path(st.session_state['uploaded_media'].name).suffix in ['.mp4', '.mkv']:
        st.session_state['thumbnail'] = 'https://courses.nestjs.com/no-preview-video.876718d4.jpeg'
        c4med.image('https://courses.nestjs.com/no-preview-video.876718d4.jpeg', use_container_width=True)
      else:
        raise ValueError("Invalid file format")
    except Exception as e:
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
      if isinstance(e, ValueError):
        st.error(e)
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
    

  _, _, _, c4but, _, _, _ = st.columns(7)

  def process_media():
    st.session_state.processing_media = True
    
    
  if 'uploaded_media' in st.session_state and st.session_state['uploaded_media'] is not None:
    c4but.button("Analyze", use_container_width=True, on_click=process_media)
  
  st.file_uploader(
      "format: *.jpg, *.jpeg, *.png, *.mp4, *.mkv",
      type=["png", "jpg", "jpeg", 'mp4', 'mkv'],
      accept_multiple_files=False,
      key="uploaded_media"
  )