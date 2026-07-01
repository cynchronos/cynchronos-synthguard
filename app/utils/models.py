import tensorflow as tf
from tensorflow.keras.models import load_model

with tf.device('/cpu:0'):
  mesonet = load_model('./modules/mesonet-v1-face.keras')