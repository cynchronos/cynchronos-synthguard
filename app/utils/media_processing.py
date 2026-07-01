import tensorflow as tf
import numpy as np
import cv2
from app.utils.models import mesonet
import streamlit as st
import stqdm

haar_cascade = cv2.CascadeClassifier('./modules/haarcascade_frontalface_default.xml')
# mtcnn_detector = MTCNN()
def detect_roi(input, ex, ey, ew, eh):
  try:
        face_data = haar_cascade.detectMultiScale(input, scaleFactor=1.1, minNeighbors=5)

        if face_data is not None:
          for (x,y,w,h) in face_data:

            # expand bounding box
            x = x - (w * ex)
            y = y - (h * ey)
            w = w + (w * ew)
            h = h + (h * eh)

            x = max(int(x), 0)
            y = max(int(y), 0)
            w = min(int(w), input.shape[1] - x)
            h = min(int(h), input.shape[0] - y)

            crop_image = input[y:y+h, x:x+w]

            return crop_image, (x,y,w,h)
          else:
            return None, None
  except Exception as e:
    print(f'Error: {e}')

# def mtcnn_roi(input, ex, ey, ew, eh):
#   try:
#     face_data = mtcnn_detector.detect_faces(input)

#     if face_data is not None:
#       crop_image = input

#       for i, face in enumerate(face_data):
#         box = face['box']
#         x,y,w,h = box

#         # expand bounding box
#         x,y,w,h = x-ex, y-ey, w+ew, h+eh
#         crop_image = input[y:y+h, x:x+w]

#         return crop_image , (x, y, w, h)
#       else:
#         return None
#   except Exception as e:
#     print(f'Error: {e}')

def get_video_thumbnail(input):
  try:
    cap = cv2.VideoCapture(input)
    if not cap.isOpened():
      print(f'Error: cannot open video {input}')
      return

    ret, frame = cap.read()
    if not ret:
      print(f'Error: cannot read frame from video {input}')
      return

    return frame
  except Exception as e:
    print(f'Error: {e}')

def processing_image(image, output_path):
  try:
    image_data = cv2.imread(image)
    crop_image, bbox = detect_roi(image_data, 0.1, 0.2, 0.3, 0.3)

    resized_image = cv2.resize(crop_image, (256, 256))
    normalized_image = resized_image / 255.0
    resized_image = np.expand_dims(normalized_image, axis=0)

    # Deepfake engine
    prediction = mesonet.predict(resized_image)
    prediction = prediction[0][0]

    return 0, 0, prediction
  except Exception as e:
    print(f'Error: {e}')

def processing_video(video, output_path):
  try:
    # get the frame
    cap = cv2.VideoCapture(video)
    if not cap.isOpened():
      print(f'Error: cannot open video {video}')
      return

    # create output video
    codec = cv2.VideoWriter.fourcc(*'mp4v')
    fps_output = cap.get(cv2.CAP_PROP_FPS)
    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    frame_size_output = (frame_width, frame_height)
    total_frame= int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    output = cv2.VideoWriter(output_path, codec, fps_output, frameSize=frame_size_output)
    progress_bar = stqdm.stqdm(total=total_frame, desc='Processing video')
    frame_count = 0
    absolute_fake = []
    almost_fake = []
    real = []

    # scrap frame
    while True:
      ret, frame = cap.read()
      if not ret:
        break

      crop_face, bbox = detect_roi(frame, 0.3, 0.4, 0.5, 0.65)

      processed_frame = frame
      if crop_face is not None:
        processed_frame  = crop_face
        x,y,w,h = bbox

        # write rect
        cv2.rectangle(frame, (int(x),int(y)), (int(x+w), int(y+h)), (0,255,0), 2)
      # frame process
      resized_frame = cv2.resize(processed_frame, (256, 256))
      normalized_frame = resized_frame / 255
      resized_frame = np.expand_dims(normalized_frame, axis=0)

      # Deepfake engine
      prediction = mesonet.predict(resized_frame)
      prediction = prediction[0][0]

      # Write predict text
      proba = f'Real: {prediction:.2f}'
      color_overlay  = (255,255,255)
      
      if prediction > 0.6 :
        real.append(prediction)
        color_overlay = (0,255,0)
      elif prediction <= 0.6 and prediction >= 0.3 :
        almost_fake.append(prediction)
        color_overlay = (0,255,255)
      else:
        absolute_fake.append(prediction)
        color_overlay = (0,0,255)

      cv2.putText(frame, proba, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, color_overlay, 1, cv2.LINE_AA)
      output.write(frame)
      progress_bar.update(1)
      frame_count += 1

    progress_bar.close()
    # clean
    cap.release()
    output.release()
  
    return absolute_fake, almost_fake, real
  except Exception as e:
    print(f'Error: {e}')