from keras.models import load_model,model_from_json
import numpy as np
import tensorflow as tf
import cv2
def mask(test_image):
    json_file = open('../model.json', 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    loaded_model = tf.keras.models.model_from_json(loaded_model_json)
    loaded_model.load_weights("../model.h5")
    # print("Loaded model from disk")
    # test_image = cv2.imread("../test.jpg",1)
    test_image = cv2.resize(test_image, (64, 64)) 
    test_image = np.expand_dims(test_image,axis=0)
    result = list(loaded_model.predict(test_image)[0])
    print(result)
    if result[1] > result[0]:
        return "Not Masked"
    else:
        return "Masked"