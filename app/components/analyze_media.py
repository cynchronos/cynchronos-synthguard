import streamlit as st
import streamlit_ext as ste
import pathlib as ptl
import random
import string
import numpy as np
import os
import tempfile
from app.utils.media_processing import processing_image, processing_video

@st.cache_data
def media_cache(input):
  return input


def analyze_media():
    uploaded_media = media_cache(st.session_state.uploaded_media)
    temp_dir = "media-temp"
    os.makedirs(temp_dir, exist_ok=True)
    output_temp_path = None

    # save temp files
    input_name = ''.join(random.choices(string.ascii_lowercase, k=12))
    file_name = uploaded_media.name.split(".")[0]
    file_ext = uploaded_media.name.split(".")[-1]
    input_temp_path = os.path.join(temp_dir, f"{input_name}.{file_ext}")
    if file_ext in ['jpg', 'jpeg', 'png']:
        output_temp_path = os.path.join(temp_dir, f"{input_name}-result.{file_ext}")
    elif file_ext in ['mp4', 'mkv']:
        output_temp_path = os.path.join(temp_dir, f"{input_name}-result.mp4")
    else:
        st.error("Invalid file format")
        return

    with open(input_temp_path, "wb") as f:
        f.write(uploaded_media.getvalue())

    st.markdown(
        """
                <style>
                  .analysis-result {
                      display:flex;
                      flex-direction:column;
                      align-items: center;
                      padding-bottom: 3rem;
                    }
                  
                  .analysis-result p {
                    font-size:36px;
                    font-weight: bold;
                  }
                  
                  .result-filename {
                    display:flex;
                    flex-direction:column;
                    align-items: center;
                    padding-bottom: 1rem;
                  }
                  
                  .result-filename p {
                    font-size: 24px;
                  }
                  
                  .analysis-bar {
                    display:flex;
                    flex-direction:row;
                    justify-content: center;
                    gap: 5rem;
                    }
                    
                  .bar-info {
                    font-size: 24px;
                  }
                    
                  .bar-info:first-child {
                    display:flex;
                    flex-direction:column;
                    align-items: center;
                    color: #f22929;
                  }
                  
                  .bar-info:nth-child(2) {
                    display:flex;
                    flex-direction:column;
                    align-items: center;
                    color: #f2f229;
                  }
                  
                  .bar-info:last-child {
                    display:flex;
                    flex-direction:column;
                    align-items: center;
                    color: #29f229;
                  }
                  
                  .download-analysis p {
                    font-size: 16px;
                  }
                  
                  .prob-res {
                    display:flex;
                    flex-direction:column;
                    align-items: center;
                    padding-top: 1rem;
                    padding-bottom: 2rem;
                  }
                  
                  .prob-res p {
                    font-size: 24px;
                  }
                </style>
                """,
        unsafe_allow_html=True,
    )

    st.write(
        """
        <div class="analysis-result">
          <p>Analysis Result</p>
        </div>
                 """,
        unsafe_allow_html=True,
    )

    c1, c2 = st.columns(2)
    c1.image(
        st.session_state.thumbnail,
        use_container_width=True,
    )
    with c2:
        filename = uploaded_media.name
        st.write(
            f"""
                 <div className="result-filename">
                   <p>File Name: {filename}</p>
                  </div>
                 """,
            unsafe_allow_html=True,
        )
        
        if file_ext in ['jpg', 'jpeg', 'png']:
          absolute_fake, almost_fake, real = processing_image(input_temp_path, output_path=output_temp_path)
        elif file_ext in ['mp4', 'mkv']:
          absolute_fake, almost_fake, real = processing_video(input_temp_path, output_path=output_temp_path)
        else:
          st.error("Invalid file format")
          return
        
        total = absolute_fake + almost_fake + real
        
        if ptl.Path(uploaded_media.name).suffix in ['.mp4', '.mkv']:
          len_pred = len(total)
          absolute_fake_percent = round((len(absolute_fake) / len_pred) * 100)
          almost_fake_percent = round((len(almost_fake) / len_pred) * 100)
          real_percent = round((len(real) / len_pred) * 100)
          
          st.write(f"""
                  <div className="analysis-bar">
                      <div className="bar-info">
                        <p>Absolute Fake:</p>
                        <p>{absolute_fake_percent}%</p>
                      </div>
                      <div className="bar-info">
                        <p>Almost Fake:</p>
                        <p>{almost_fake_percent}%</p>
                    </div>
                    <div className="bar-info">
                      <p>Real</p>
                      <p>{real_percent}%</p>
                    </div>
                  """, unsafe_allow_html=True)
        else:
          real_probability = total
          st.write(
            f"""
              <div className="prob-res">
                <p>Real Probability:</p>
                <p>{real_probability:.2f}</p>
              </div>
              """,
              unsafe_allow_html=True,
          )
        if os.path.exists(output_temp_path) and ptl.Path(output_temp_path).suffix in ['.mp4', '.mkv']:
            with open(output_temp_path, "rb") as f:
                output_bytes = f.read()
            _, cdown2, _ = st.columns(3)
            with cdown2:
              st.write(
                  """
                  <div className="download-analysis">
                    <p>Download Analysis Result: </p>
                  </div>
                  """,
                  unsafe_allow_html=True,
              )
              ste.download_button(
                  label="Download",
                  data=output_bytes,
                  file_name=f"{file_name}-result.mp4",
                  mime="video/mp4",
              )
            
