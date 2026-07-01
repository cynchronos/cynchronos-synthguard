# Cynchronos SynthGuard

Cynchronos SynthGuard is an advanced, enterprise-grade deepfake detection and analysis platform. Designed with a robust modular architecture, the system leverages computer vision and deep learning models to identify synthetic media manipulation in both static images and video sequences.

## Core Architecture & Technologies

The platform integrates several industry-standard technologies to ensure high accuracy and performance:

*   **Framework:** Streamlit (for high-throughput, interactive web application deployment).
*   **Computer Vision:** OpenCV (utilizing Haar Cascade classifiers for rapid, initial Region of Interest (ROI) extraction and facial detection).
*   **Deep Learning Engine:** TensorFlow/Keras. The core inference engine is based on the MesoNet architecture, specifically optimized for mesoscopic properties of images to detect deepfake artifacts.
*   **Data Processing:** NumPy for high-performance matrix operations and tensor manipulations.

## Key Features

*   **Multi-Modal Analysis:** Native support for both image formats (JPEG, JPG, PNG) and video formats (MP4, MKV).
*   **Frame-by-Frame Video Processing:** Implements a sequential frame extraction pipeline. Each frame undergoes facial localization, bounding box expansion, and individual deepfake inference.
*   **Confidence Scoring:** Provides granular classification outputs. For images, it returns a continuous probability score. For videos, it aggregates frame-level predictions into discrete categories: Absolute Fake, Almost Fake, and Real.
*   **Visual Overlays:** Automatically generates and overlays bounding boxes and probability metrics onto the processed video, outputting a downloadable artifact for further forensic review.

## System Prerequisites

Ensure the deployment environment meets the following specifications:

*   Python 3.8 or higher.
*   Sufficient computational resources for TensorFlow execution.

## Installation

1.  Clone the repository to your local environment.
2.  Navigate to the project root directory.
3.  Establish an isolated Python virtual environment:
    ```bash
    python -m venv virtualenv
    source virtualenv/bin/activate  # On Windows, use `virtualenv\Scripts\activate`
    ```
4.  Install the required dependencies via the provided package list:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

Initiate the application server using Streamlit:

```bash
streamlit run index.py
```

Upon successful initialization, the application will be accessible via the defined local network port. Navigate through the sidebar menu to access the DeepFake Analyzer module, upload target media, and initiate the inference pipeline.

## Project Structure

*   `index.py`: The application entry point and routing controller.
*   `app/`: Contains the core application logic.
    *   `components/`: Modular UI components and the main analysis pipeline execution handler.
    *   `utils/`: Core processing scripts, including media manipulation and model inference functions.
*   `modules/`: Stores serialized model weights and pre-trained classifiers.
    *   `haarcascade_frontalface_default.xml`: Pre-trained classifier for facial ROI extraction.
    *   `mesonet-v1-face.keras`: Serialized MesoNet model weights.
    *   `mesonet-v1-wide.keras`: Serialized MesoNet model weights (wide variant).
*   `media-temp/`: Ephemeral storage directory for processing uploaded files and generating output artifacts.

## Model Configuration & Hosting

The inference engine relies on a pre-trained MesoNet model. The input pipeline standardizes all extracted facial ROIs to a normalized tensor of dimensions (256, 256, 3) before feeding them into the network. The decision boundary is established based on a thresholding mechanism to classify the media's authenticity.

The pre-trained AI models and serialized weights are hosted on Hugging Face. You can access and download the models from the following repository:
*   [Model Repository](https://huggingface.co/cynchronos/SynthGuard-MesoNet-1.0)

Ensure the downloaded weights are placed within the `modules/` directory prior to initialization.

## License

Please refer to the `LICENSE` file located in the root directory for distribution and usage rights.
