import tensorflow as tf
import matplotlib.pyplot as plt
from tensorflow.keras.datasets import mnist
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Flatten, Dense
from PIL import Image
import numpy as np

(X_train, y_train), (X_test, y_test) = mnist.load_data()

X_train = X_train / 255.0
X_test = X_test / 255.0

y_train = to_categorical(y_train, 10)
y_test = to_categorical(y_test, 10)

plt.figure(figsize=(12,4))
for i in range(10):
    plt.subplot(2,5,i+1)
    plt.imshow(X_train[i], cmap='gray')
    plt.title(f"Label: {int(tf.argmax(y_train[i]))}")
    plt.axis('off')

plt.suptitle("Handwritten Number Recognition", fontsize=16)
plt.show()

model = Sequential([
    Flatten(input_shape=(28,28)),
    Dense(10, activation='softmax')
])

model.compile(
    optimizer='sgd',
    loss='categorical_crossentropy',
    metrics=['accuracy']
)

model.fit(X_train, y_train, epochs=20, batch_size=32, validation_split=0.1)

test_loss, test_acc = model.evaluate(X_test, y_test)
print(f"Test accuracy: {test_acc:.4f}")

img=Image.open('test1.png').convert('L')
img=img.resize((28,28))
img_array=np.array(img)/255.0

img_array=1-img_array

img_array=img_array.reshape(1,28,28)

pred=np.argmax(model.predict(img_array))
print("Model predvidja cifru:", pred)

