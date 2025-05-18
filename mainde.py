# main.py

import os
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout, BatchNormalization

# ----- Dataset folder path -----
dataset_path = "./datasetde"  # tman specify your dataset path here (folder containing 'normal' and 'cataract')

# Raise error if path doesn't exist
if not os.path.exists(dataset_path):
    raise Exception(f"Dataset path '{dataset_path}' does not exist.")

# ----- Encoder setup -----
encoder = OneHotEncoder()
encoder.fit([[0], [1]])  # 0 -> strabismus, 1 -> Normal

# ----- Preparing data and labels -----
data = []
labels = []

# --- Load Cataract images
for r, d, f in os.walk(os.path.join(dataset_path, 'dryeye')):  # tman
    for file in f:
        if file.endswith('.jpg') or file.endswith('.png'):
            path = os.path.join(r, file)
            img = Image.open(path).resize((128, 128))
            img = np.array(img)
            if img.shape == (128, 128, 3):
                data.append(img)
                labels.append(encoder.transform([[0]]).toarray())

# --- Load Normal images
for r, d, f in os.walk(os.path.join(dataset_path, 'normal')):  # tman
    for file in f:
        if file.endswith('.jpg') or file.endswith('.png'):
            path = os.path.join(r, file)
            img = Image.open(path).resize((128, 128))
            img = np.array(img)
            if img.shape == (128, 128, 3):
                data.append(img)
                labels.append(encoder.transform([[1]]).toarray())

# ----- Prepare dataset -----
data = np.array(data)
labels = np.array(labels)
labels = labels.reshape(-1, 2)  # (flatten label array)

print(f"Total Images: {len(data)}")

# ----- Split data -----
x_train, x_test, y_train, y_test = train_test_split(data, labels, test_size=0.2, random_state=42)

# ----- Build model -----
model = Sequential()

model.add(Conv2D(32, (3, 3), padding='same', activation='relu', input_shape=(128, 128, 3)))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(BatchNormalization())

model.add(Conv2D(64, (3, 3), padding='same', activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(BatchNormalization())

model.add(Flatten())
model.add(Dense(128, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(2, activation='softmax'))

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# ----- Train model -----
history = model.fit(x_train, y_train, epochs=20, batch_size=32, validation_data=(x_test, y_test))


model.save('dryeye_model.h5')  # tman
print("✅ dryeye_model.h5")

# ----- Plot accuracy chart -----
plt.plot(history.history['accuracy'], label='Training Accuracy')
plt.plot(history.history['val_accuracy'], label='Validation Accuracy')
plt.legend()
plt.show()

# ----- Save model -----
model.save('dryeye_model.h5')
