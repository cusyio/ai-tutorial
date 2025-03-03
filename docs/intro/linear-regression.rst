Praktische Einführung: Lineare Regression
=========================================

Was ist Lineare Regression?
---------------------------

- Die **Lineare Regression** ist eines der grundlegendsten Modelle des maschinellen Lernens.

- Sie wird verwendet, um eine abhängige Variable (Zielvariable) anhand einer oder mehrerer unabhängiger Variablen vorherzusagen.

- Die Gleichung einer einfachen linearen Regression lautet:

  .. math::
     y = wX + b

  wobei:

  - `y` die Zielvariable ist,

  - `X` die unabhängige Variable,

  - `w` die Steigung der Geraden (Gewicht) und

  - `b` der Achsenabschnitt (Bias).

Beispiel mit scikit-learn
-------------------------

Schritte zur Implementierung eines ML-Modells
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. **Daten laden und vorbereiten**

   - Import von Bibliotheken und Laden eines Datensatzes.

   - Aufteilung der Daten in Trainings- und Testsets.

2. **Modell erstellen und trainieren**

   - Ein Lineares Regressionsmodell aus `scikit-learn` erstellen und trainieren.

3. **Modell evaluieren**

   - Vorhersagen treffen und mit Metriken wie dem mittleren quadratischen Fehler (MSE) bewerten.

Code
~~~~

.. code-block:: python
   :linenos:

   import numpy as np
   import matplotlib.pyplot as plt
   from sklearn.model_selection import train_test_split
   from sklearn.linear_model import LinearRegression
   from sklearn.metrics import mean_squared_error

   # Beispiel-Datensatz erstellen
   np.random.seed(42)
   X = 2 * np.random.rand(100, 1)
   y = 4 + 3 * X + np.random.randn(100, 1)

   # Aufteilung in Trainings- und Testdaten
   X_train, X_test, y_train, y_test = train_test_split(
       X, y, test_size=0.2, random_state=42
   )

   # Modell erstellen und trainieren
   model = LinearRegression()
   model.fit(X_train, y_train)

   # Vorhersagen treffen
   y_pred = model.predict(X_test)

   # Modellbewertung
   mse = mean_squared_error(y_test, y_pred)
   print(f"Mittlerer quadratischer Fehler (MSE): {mse}")

   # Visualisierung
   plt.scatter(X_test, y_test, color="blue", label="Tatsächliche Werte")
   plt.plot(X_test, y_pred, color="red", linewidth=2, label="Vorhersagen")
   plt.legend()
   plt.xlabel("X")
   plt.ylabel("y")
   plt.title("Lineare Regression mit scikit-learn")
   plt.show()

Zeilen 8–10
    Wir generieren synthetische Daten mit einer linearen Beziehung und fügen
    zufällige Schwankungen hinzu.
Zeilen 13–15
    Wir teilen die Daten in **Trainings- und Testsets**, um eine objektive
    Modellbewertung zu ermöglichen.
Zeilen 18–19
    Mit `LinearRegression().fit()` trainieren wir unser Modell.
Zeilen 25–26
    Wir verwenden `mean_squared_error()`, um die Modellgenauigkeit zu messen.
Zeilen 29–35
    Schließlich visualisieren wir die tatsächlichen und vorhergesagten Werte, um
    die Modellleistung zu interpretieren.
