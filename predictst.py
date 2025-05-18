# predict.py

import numpy as np
from PIL import Image
from tensorflow.keras.models import load_model

# ----- Load the model -----
model = load_model('strabismus_model.h5')

# ----- Function for prediction -----
def predict_image(image_path):
    img = Image.open(image_path).resize((128, 128))
    img = np.array(img)
    img = img.reshape(1, 128, 128, 3)  # reshape for prediction
    pred = model.predict(img)
    class_idx = np.argmax(pred)

    if class_idx == 0:
        confidence = pred[0][0]
        if confidence > 0.85:
            print(f" You are highly likely to have strabismus (Confidence: {confidence * 100:.2f}%). Please consult an eye specialist.")
        elif confidence > 0.6:
            print(f" You may have strabismus (Confidence: {confidence * 100:.2f}%). A medical consultation is recommended.")
        else:
            print(f" There is a slight indication of strabismus (Confidence: {confidence * 100:.2f}%). It's better to monitor and re-check.")
    else:
        confidence = pred[0][1]
        if confidence > 0.85:
            print(f" Your eye appears normal (Confidence: {confidence * 100:.2f}%).")
        elif confidence > 0.6:
            print(f" Your eye is likely normal (Confidence: {confidence * 100:.2f}%). No action needed, but stay alert.")
        else:
            print(f" Although predicted as normal (Confidence: {confidence * 100:.2f}%), uncertainty is high. Consider a check-up if symptoms exist.")


# ----- Test call -----
predict_image('./datasetst/normal/11.jpg')  # model test image path
