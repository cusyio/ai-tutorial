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
