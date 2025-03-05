Praxisbeispiel – Bildklassifikation mit CNNs
------------------------------------------------------------

**Ziel:** Einführung in Convolutional Neural Networks mit TensorFlow/Keras anhand eines Bildklassifikationsproblems.

.. note:
   Code Beispiel auch mit pytorch! als "Gegenbeispiel" zu tensorflows


**Code-Beispiel: Klassifikation des MNIST-Datensatzes (Handgeschriebene Ziffern)**

.. code-block:: python

   import tensorflow as tf
   from tensorflow.keras import layers, models
   from tensorflow.keras.datasets import mnist
   import matplotlib.pyplot as plt

   # Daten laden
   (x_train, y_train), (x_test, y_test) = mnist.load_data()
   x_train, x_test = x_train / 255.0, x_test / 255.0  # Normalisierung
   x_train = x_train[..., tf.newaxis]  # Dimension erweitern
   x_test = x_test[..., tf.newaxis]

   # Modell definieren
   model = models.Sequential(
       [
           layers.Conv2D(32, (3, 3), activation="relu", input_shape=(28, 28, 1)),
           layers.MaxPooling2D((2, 2)),
           layers.Conv2D(64, (3, 3), activation="relu"),
           layers.MaxPooling2D((2, 2)),
           layers.Conv2D(64, (3, 3), activation="relu"),
           layers.Flatten(),
           layers.Dense(64, activation="relu"),
           layers.Dense(10, activation="softmax"),
       ]
   )

   # Modell kompilieren
   model.compile(
       optimizer="adam",
       loss="sparse_categorical_crossentropy",
       metrics=["accuracy"],
   )

   # Training
   model.fit(x_train, y_train, epochs=5, validation_data=(x_test, y_test))

   # Evaluation
   test_loss, test_acc = model.evaluate(x_test, y_test)
   print(f"Testgenauigkeit: {test_acc}")

   # Beispielhafte Vorhersage
   predictions = model.predict(x_test)
   plt.imshow(x_test[0].reshape(28, 28), cmap="gray")
   plt.title(f"Vorhergesagte Klasse: {predictions[0].argmax()}")
   plt.show()
