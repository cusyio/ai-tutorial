Praktische Einführung: Lineare Regression
=========================================

Was ist Lineare Regression?
---------------------------

* Die **Lineare Regression** ist eines der grundlegendsten Modelle des maschinellen Lernens.
* Sie wird verwendet, um eine abhängige Variable (Zielvariable) anhand einer oder mehrerer unabhängiger Variablen vorherzusagen.
* Bei der linearen Regression ist die Voraussetzung, dass das `Skalenniveau <https://datatab.de/tutorial/skalenniveau>`_ der abhängigen Variable `intervallskaliert <https://de.statista.com/statistik/lexikon/definition/71/intervallskaliert/#:~:text=Eine%20Skala%20ist%20intervallskaliert%2C%20wenn,den%20Werten%205%20und%206.>`_ ist, sowie eine Normalverteilung vorliegt. 
* Ist die abhängige Variable kategorisch, wird eine logistische Regression verwendet.

* Die Gleichung einer einfachen linearen Regression lautet:

  .. math::
     y = wX + b

  wobei:

  - `y` die Zielvariable ist,

  - `X` die unabhängige Variable,

  - `w` die Steigung der Geraden (Gewicht) und

  - `b` der Achsenabschnitt (Bias).


Interpretabilität von Linearen Regressions-Modellen
----------------------------------------------------

Wie viele Modelle müssen für die Lineare Regression einige Voraussetzungen in den Daten erfüllt sein, 
damit die Ergebnisse der Regressionsanalyse interpretiert werden können. 

* Linearität: 
    Es muss ein linearer Zusammenhang zwischen der abhängigen und den unabhängigen Variablen bestehen.
* Homoskedastizität: 
    Die Residuen müssen eine konstante Varianz haben.
* Normalität: 
    Normalverteilte Fehlerkomponente
* Keine Multikollinearität: 
    Keine hohe Korrelation zwischen den unabhängigen Variablen
* Keine Autokorrelation: 
    Die Fehlerkomponente sollte keine Autokorrelation aufweisen.

.. seealso::
   * `datalab-tutorial <https://datatab.de/tutorial/lineare-regression>`_

Beispiel mit scikit-learn
-------------------------

Schritte zur Implementierung eines ML-Modells
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. **Daten laden und vorbereiten**

   * Import von Bibliotheken und Laden eines Datensatzes.
   * Untersuchung der Datenverteilung, Korrelationen und möglicher Ausreißer.
   * Aufteilung der Daten in Trainings- und Testsets.

2. **Datenvorbereitung**

   * Umwandlung kategorischer Merkmale (One-Hot-Encoding).
   * Normalisierung und Skalierung numerischer Merkmale.
   * Aufteilung in Trainings- und Testdaten.

3. **Modell erstellen und trainieren**

   * Ein Lineares Regressionsmodell aus `scikit-learn` erstellen und trainieren.
   * Verwendung von Metriken zur Bewertung der Modellgüte (z.B. MSE, R²).

4. **Modell evaluieren und Interpretation**

   * Bewertung der Modellperformance auf dem Testdatensatz.
   * Interpretation der wichtigsten Einflussgrößen.