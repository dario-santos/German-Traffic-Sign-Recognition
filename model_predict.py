import os
import csv
import numpy as np
from tensorflow import keras


folder_path = './GTSRB/Test/'
model_path = './gtsrb_model.h5'
img_width, img_height = 64, 64


# 1 - Loads the the test labels
f = open('Test.csv', mode='r')
file_reader = csv.reader(f, delimiter=';')

labels = []
for row in file_reader:
    labels.append(row[0])
f.close()


# 2 - Loads the model
model = keras.models.load_model(model_path)

model.compile(
    optimizer='adam',
    loss='categorical_crossentropy',
    metrics=['acc'])

# 3 - Predicts the images
count = 0
for img_path in os.listdir(folder_path):
    
    index = int(img_path.split('.')[0])

    img = keras.preprocessing.image.load_img(folder_path + img_path, target_size=(img_width, img_height))
    img = keras.preprocessing.image.img_to_array(img)
    img = np.expand_dims(img, axis=0)

    img_predict = model.predict_classes(img)

    if int(img_predict[0]) == int(labels[index]):
        count += 1


# 4 - Outputs the score of the model in the test data
print((count * 100) / 12629.)