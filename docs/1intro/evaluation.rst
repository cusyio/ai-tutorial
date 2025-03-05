Evaluation von ML-Modellen
==========================

Warum ist die Modellbewertung wichtig?
--------------------------------------

* Die Evaluation von ML-Modellen stellt sicher, dass das Modell zuverlässig und
  generalisierbar ist.
* Ein gut evaluiertes Modell verhindert Overfitting und hilft, die besten
  Algorithmen und Parameter auszuwählen.

Wichtige Metriken für Klassifikationsprobleme
---------------------------------------------

Accuracy (Genauigkeit)
~~~~~~~~~~~~~~~~~~~~~~

Prozentsatz der korrekten Vorhersagen:

.. math::
   \text{Accuracy} = \frac{\text{Anzahl der korrekten Vorhersagen}}{\text{Gesamtanzahl der Vorhersagen}}

.. warning:
   Accuracy hat eine Einschränkung bei (stark) unausgewogenen Datensätzen, da
   sie hier irreführend sein kann.

Precision (Präzision)
~~~~~~~~~~~~~~~~~~~~~

Precision ist der Anteil der tatsächlich positiven Vorhersagen unter allen als
positiv klassifizierten Instanzen:

.. math::
   \text{Precision} = \frac{TP}{TP + FP}

Precision wird vor allem bevorzugt, wenn falsch-positive Fehler besonders
kritisch sind (:abbr:`z.B. (zum Beispiel)` Spam-Erkennung).

Recall (Sensitivität)
~~~~~~~~~~~~~~~~~~~~~

Recall ist der Anteil der korrekten positiven Vorhersagen unter allen
tatsächlichen positiven Fällen:

.. math::
   \text{Recall} = \frac{TP}{TP + FN}

Recall ist eine wichtige Metrik, wenn es entscheidend ist, möglichst alle
positiven Fälle zu erfassen (:abbr:`z.B. (zum Beispiel)` Krebsdiagnosen).

F1-Score
~~~~~~~~

Der F1-Score ist das harmonisches Mittel von Präzision und Recall, um ein
ausgewogenes Maß zu erhalten:

.. math::
   \text{F1-Score} = 2 \times \frac{\text{Precision} \times \text{Recall}}{\text{Precision} + \text{Recall}}

Der F1-Score ist besonders nützlich bei unausgewogenen Datensätzen (engl.:
*unbiased data sets*).

Wichtige Metriken für Regressionsprobleme
-----------------------------------------

Mean Squared Error, MSE (Mittlerer quadratischer Fehler)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Der MSE berechnet den Durchschnitt der quadrierten Fehler zwischen
vorhergesagten und tatsächlichen Werten:

.. math::
   \text{MSE} = \frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2

Somit bestraft der MSE große Fehler stärker als kleine Fehler.

Mean Absolute Error, MAE (Mittlerer absoluter Fehler)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Der MAE berechnet den Durchschnitt der absoluten Differenzen zwischen
vorhergesagten und tatsächlichen Werten:

.. math::
   \text{MAE} = \frac{1}{n} \sum_{i=1}^{n} |y_i - \hat{y}_i|

R²-Koeffizient (Bestimmtheitsmaß)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Zeigt, wie gut das Modell die Varianz der Zielvariable erklärt.
* Wertebereich: 0 (keine Erklärung) bis 1 (perfekte Erklärung).

Praktische Anwendung: Evaluierung eines Modells in Python
---------------------------------------------------------

Ein Beispiel zur Berechnung dieser Metriken mit `scikit-learn`:

.. code-block:: python
   :linenos:

   from sklearn.metrics import (
       accuracy_score,
       precision_score,
       recall_score,
       f1_score,
   )

   # Beispiel: Tatsächliche Labels und Vorhersagen
   true_labels = [1, 0, 1, 1, 0, 1, 0, 0, 1, 0]
   predicted_labels = [1, 0, 1, 0, 0, 1, 0, 1, 1, 0]

   # Berechnung der Metriken
   accuracy = accuracy_score(true_labels, predicted_labels)
   precision = precision_score(true_labels, predicted_labels)
   recall = recall_score(true_labels, predicted_labels)
   f1 = f1_score(true_labels, predicted_labels)

   print(
       f"Accuracy: {accuracy}, Precision: {precision}, Recall: {recall}, F1-Score: {f1}"
   )
   return (accuracy, precision, recall, f1)
