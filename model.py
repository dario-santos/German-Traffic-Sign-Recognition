# Dados:
# Train samples    : 37919
# Validation samples :  1290

from tensorflow import keras
from tensorflow.keras import layers


# 1 - Load and process the data
train_path = './GTSRB/Training'
validate_path = './GTSRB/Validation'

train_datagen = keras.preprocessing.image.ImageDataGenerator(rescale=1./255)

validate_datagen = keras.preprocessing.image.ImageDataGenerator(rescale=1./255)

train_generator = train_datagen.flow_from_directory(train_path, 
                                  target_size=(64, 64), 
                                  batch_size=74,
                                  class_mode='categorical')

validation_generator = validate_datagen.flow_from_directory(validate_path, 
                                     target_size=(64, 64), 
                                     batch_size=40,
                                     class_mode='categorical')


# 2 - Build the model
model = keras.models.Sequential([
    layers.Conv2D(32, (3, 3), activation='relu',input_shape=(64, 64, 3)),
    layers.Conv2D(32, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.MaxPooling2D((3, 3)),
    layers.Dropout(0.3),
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),
    layers.Dropout(0.3),
    layers.Flatten(),
    layers.Dense(512, activation='relu'),
    layers.Dropout(0.5),
    layers.Dense(43, activation='softmax')
])


# 3 - Compile the model
model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['acc'])


# 4 - Train and evaluate the model
history = model.fit_generator(
    train_generator,
    steps_per_epoch=512,
    epochs=8,
    validation_data=validation_generator, 
    validation_steps=32)

model.save('gtsrb_model.h5')

# 5 - Analyze the data
import matplotlib.pyplot as plt


acc = history.history['acc']
val_acc = history.history['val_acc']
loss = history.history['loss']
val_loss = history.history['val_loss']

epochs = range(1, len(acc) + 1)

plt.plot(epochs, acc, 'bo', label='Training acc')
plt.plot(epochs, val_acc, 'b', label='Validation acc')
plt.title('Training and validation accuracy')
plt.legend()

plt.figure()

plt.plot(epochs, loss, 'bo', label='Training loss')
plt.plot(epochs, val_loss, 'b', label='Validation loss')
plt.title('Training and validation loss')
plt.legend()

plt.show()