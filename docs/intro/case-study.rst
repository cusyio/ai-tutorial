Fallstudie: Vorhersage von Immobilienpreisen
============================================

Ziel dieser Fallstudie
----------------------

- Anwendung der erlernten Methoden zur Vorhersage von Immobilienpreisen.

- Verwendung eines realen Datensatzes zur Modellierung.

- Umsetzung in Python mit `scikit-learn`.

Schritte zur Umsetzung
----------------------

1. **Daten laden und verstehen**

   * Nutzung eines offenen Datensatzes (:abbr:`z.B. (zum Beispiel)` `Boston
     Housing Dataset` oder `Kaggle Immobilienpreise`).
   * Untersuchung der Datenverteilung, Korrelationen und möglicher Ausreißer.

2. **Datenvorbereitung**

   * Umwandlung kategorischer Merkmale (One-Hot-Encoding).
   * Normalisierung und Skalierung numerischer Merkmale.
   * Aufteilung in Trainings- und Testdaten.

3. **Modelltraining mit Lineare Regression**

   * Trainieren eines **Linearen Regressionsmodells** mit ``scikit-learn``.
   * Verwendung von Metriken zur Bewertung der Modellgüte (:abbr:`z.B. (zum
     Beispiel)` MSE, R²).

4. **Modellbewertung und Interpretation**

   * Bewertung der Modellperformance auf dem Testdatensatz.
   * Interpretation der wichtigsten Einflussgrößen.

Code-Beispiel
-------------

.. code-block:: python
   :linenos:

   import pandas as pd
   import numpy as np
   import matplotlib.pyplot as plt
   from sklearn.model_selection import train_test_split
   from sklearn.preprocessing import StandardScaler, OneHotEncoder
   from sklearn.linear_model import LinearRegression
   from sklearn.metrics import mean_squared_error, r2_score

   # Beispieldatensatz laden (Boston Housing Dataset)
   from sklearn.datasets import load_boston

   boston = load_boston()
   df = pd.DataFrame(boston.data, columns=boston.feature_names)
   df["PRICE"] = boston.target

   # Aufteilung in Merkmale (X) und Zielvariable (y)
   X = df.drop("PRICE", axis=1)
   y = df["PRICE"]

   # Aufteilung in Trainings- und Testsets
   X_train, X_test, y_train, y_test = train_test_split(
       X, y, test_size=0.2, random_state=42
   )

   # Feature Scaling
   scaler = StandardScaler()
   X_train_scaled = scaler.fit_transform(X_train)
   X_test_scaled = scaler.transform(X_test)

   # Lineare Regression trainieren
   model = LinearRegression()
   model.fit(X_train_scaled, y_train)

   # Vorhersagen treffen
   y_pred = model.predict(X_test_scaled)

   # Modellbewertung
   mse = mean_squared_error(y_test, y_pred)
   r2 = r2_score(y_test, y_pred)
   print(f"Mittlerer quadratischer Fehler (MSE): {mse}")
   print(f"Bestimmtheitsmaß (R²): {r2}")

   # Visualisierung der Vorhersagen
   plt.scatter(y_test, y_pred, alpha=0.7)
   plt.xlabel("Tatsächliche Preise")
   plt.ylabel("Vorhergesagte Preise")
   plt.title("Tatsächliche vs. Vorhergesagte Immobilienpreise")
   plt.show()

Zeilen 12–14
    **Datensatz laden:** Wir verwenden das `Boston Housing Dataset`, das
    verschiedene Merkmale von Häusern enthält.
Zeilen 26–28
    **Datenvorverarbeitung:** Skalierung der numerischen Variablen zur besseren
    Modellleistung.
Zeilen 31–32
    **Modelltraining:** Wir verwenden eine einfache lineare Regression.
Zeilen 38–41
    **Modellbewertung:** Berechnung des mittleren quadratischen Fehlers (MSE)
    und des Bestimmtheitsmaßes (R²).
Zeilen 44–48
    **Visualisierung:** Darstellung der tatsächlichen vs. vorhergesagten Werte
    zur Überprüfung der Modellgüte.
