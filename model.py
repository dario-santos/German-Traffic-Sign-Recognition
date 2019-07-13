# Dados:
# Treino: 39209
# Teste: 12631

import tensorflow as tf

# 1 - Carregar os dados
train_path = './GTSRB/Training'
validate_path = './GTSRB/Test'

train_datagen = tf.keras.preprocessing.image.ImageDataGenerator(rotation_range=40, 
                                                                zoom_range=0.2, 
                                                                width_shift_range=0.2, 
                                                                height_shift_range=0.2,
                                                                shear_range=0.2, 
                                                                rescale=1./255)

validate_datagen = tf.keras.preprocessing.image.ImageDataGenerator(rescale=1./255)


# 2 - Processar os dados
train_generator = train_datagen.flow_from_directory(train_path, 
                                  target_size=(30, 30), 
                                  batch_size=76,
                                  class_mode='categorical')

validation_generator = validate_datagen.flow_from_directory(validate_path, 
                                     target_size=(30, 30), 
                                     batch_size=76,
                                     class_mode='categorical')


# 3 - Construir o modelo
model = tf.keras.models.Sequential([
    tf.keras.layers.Conv2D(32, (3, 3), activation='relu',input_shape=(30, 30, 3)),
    tf.keras.layers.MaxPool2D((2, 2)),
    tf.keras.layers.Conv2D(64, (3, 3), activation='relu'),
    tf.keras.layers.MaxPool2D((3, 3)),
    tf.keras.layers.Conv2D(64, (3, 3), activation='relu'),
    tf.keras.layers.MaxPool2D((2, 2)),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(512, activation='relu'),
    tf.keras.layers.Dense(43, activation='softmax')
])


# 4 - Compilar o modelo
model.compile(optimizer='RMSprop',
              loss='categorical_crossentropy',
              metrics=['acc'])


# 5 - Treinar e Validar o modelo
history = model.fit_generator(train_generator, steps_per_epoch=512, epochs=20)

# 6 - Testar o modelo
