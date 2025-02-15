import streamlit as st


def about():
    with st.container():
        st.write(
            """
              <div style="display: flex; justify-content:center;">
                <div style="display: flex; align-items: center;">
                  <svg xmlns="http://www.w3.org/2000/svg" width="70" height="70" fill="#f22929" class="bi bi-opencollective" viewBox="0 0 16 16">
                    <path fill-opacity=".4" d="M12.995 8.195c0 .937-.312 1.912-.78 2.693l1.99 1.99c.976-1.327 1.6-2.966 1.6-4.683 0-1.795-.624-3.434-1.561-4.76l-2.068 2.028c.468.781.78 1.679.78 2.732z"/>
                    <path d="M8 13.151a4.995 4.995 0 1 1 0-9.99c1.015 0 1.951.273 2.732.82l1.95-2.03a7.805 7.805 0 1 0 .04 12.449l-1.951-2.03a5.07 5.07 0 0 1-2.732.781z"/>
                  </svg>
                  <h1 style="margin-left: 20px;">SynthGuard</h1> 
                </div>  
              </div>
      """, unsafe_allow_html=True
        )

    with st.container():
        st.write(
            """
              <div style="padding-top:50px; font-size:20px; white-space: wrap; text-indent: 50px; text-align:justify;">
                <p>
                  Cynchronos SynthGuard is a cutting-edge website platform designed to distinguish between DeepFake images and real images with unparalleled accuracy. Built on the robust foundation of Streamlit for seamless user interaction and powered by advanced Neural Network technology, this platform leverages the innovative MesoNet (Meso Network) architecture as its core AI engine. The model has been trained on a pre-trained dataset of 10,000 images and is designed for future fine-tuning to enhance its capabilities. This state-of-the-art model is specifically tailored to detect subtle artifacts and inconsistencies often found in manipulated images, ensuring reliable and precise results.
                </p>
                <p>
                  This website committed to empowering users with the tools to combat digital misinformation and protect the integrity of visual content. Whether you're a journalist verifying the authenticity of an image, a business  safeguarding its digital assets, or an individual curious about the origins of a photo, our platform provides an intuitive and user-friendly experience. With a focus on transparency, accuracy, and innovation, Cynchronos SynthGuard is your trusted partner in the fight against DeepFake technology.
                </p>    
              </div>      
            """, unsafe_allow_html=True)


if __name__ == "__main__":
    about()
