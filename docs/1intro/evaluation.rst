Evaluation von ML-Modellen
==========================

Warum ist die Modellbewertung wichtig?
--------------------------------------

* Die Evaluation von ML-Modellen stellt sicher, dass das Modell zuverlässig und generalisierbar ist.
* Ein gut evaluiertes Modell verhindert Overfitting und hilft, die besten Algorithmen und Parameter auszuwählen.


Wichtige Metriken und Tools für Klassifikationsprobleme
----------------------------------------------------------

Die einfachste Form der Klassifikation ist die binäre Klassifikation (binary classification) und besteht aus zwei Zuständen.

Beispiel Covid-Schnelltest: Wir wollen untersuchen, wie gut der Infektionsstatus eines Patienten durch Corona-Schnelltests wiedergespiegelt wird. 
Hier würde der Corona-Schnelltest als der Klassifikator von genau zwei Zuständen dienen: infiziert oder nicht-infiziert.

Aus diesen zwei Klassen können sich genau 4 Kombinationen ergeben, je nach dem, was das Modell vorhergesagt hat und ob das mit der Realität übereinstimmt: 

* **True Positive (TP)**: 
    Der Schnelltest klassifiziert die Person als infiziert (Positive) und ein anschließender PCR-Test bestätigt dieses Ergebnis (True prediction). Somit war der Schnelltest korrekt.
* **False Positive (FP)**: 
    Der Schnelltest klassifiziert die Person als infiziert (Positive), jedoch ergibt ein anschließender PCR-Test, dass die Person nicht infiziert ist (False prediction).
* **True Negative (TN)**: 
    Der Schnelltest klassifiziert die Person als nicht-infiziert (Negative) und die Person ist tatsächlich nicht infiziert (True prediction).
* **False Negative (FN)**: 
    Der Corona-Schnelltest klassifiziert die Person als nicht-infiziert (Negative), jedoch ist die Person infiziert und sollte somit einen positiven Schnelltest haben (False prediction).


Konfusionsmatrix / Wahrheitsmatrix (Confusion Matrix)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*siehe auch*: `confusion matrix IBM <https://www.ibm.com/de-de/topics/confusion-matrix>`_, 
`Wahrheitsmatrix <https://de.wikipedia.org/wiki/Beurteilung_eines_bin%C3%A4ren_Klassifikators#Wahrheitsmatrix:_Richtige_und_falsche_Klassifikationen>`_

Ein weiteres Tool, um diese 4 Kombinationen leicht sichtbar zu machen, ist die Konfusionsmatrix: 

.. list-table:: Confusion Matrix
   :header-rows: 1
   :align: center

   * - True Class ↓ / Predicted Class →
     - Positive
     - Negative
   * - Positive (Actual Positive)
     - True Positive (TP)
     - False Negative (FN)
   * - Negative (Actual Negative)
     - False Positive (FP)
     - True Negative (TN)

Anhand unseres Corona-Schnelltest-Beispiels: 

Nehmen wir an, wir haben 100 Personen für den Testdatensatz an Corona-Schnelltests erfasst und
die sind wiefolgt aufgeteilt: 

.. list-table:: Confusion Matrix
   :header-rows: 1
   :align: center

   * - True Class ↓ / Predicted Class →
     - Positive
     - Negative
   * - Positive (Actual Positive)
     - 60 (TP)
     - 20 (FN)
   * - Negative (Actual Negative)
     - 10 (FP)
     - 10 (TN)
     
Daraus lässt sich folgendes "ablesen":

* True Positive (TP) = 60: 
    60 Personen sind laut Schnelltest infiziert (Positive) und sind tatsächlich infiziert (True).
* False Positive (FP) = 10: 
    10 Personen sind laut Schnelltest infiziert (Positive), sind in Wirklichkeit aber nicht infiziert (False).
* True Negative (TN) = 10: 
    10 Personen sind laut Schnelltest nicht-infiziert (Negative), und sind in Wirklichkeit auch wirklich gesund (True).
* False Negative (FN) = 20: 
    20 Personen sind laut Schnelltest nicht-infiziert (Negative), sind aber tatsächlich infiziert (False).

Die Konfusionsmatrix hilft stark dabei festzustellen, welche Art des Fehlers beim Klassifikator häufig(er) vorkommt. 

In unserem Beispiel ist der Corona-Schnelltest in 70 % der Fälle korrekt ((60 + 10) / 100), was erst mal kein schlechter Wert ist. 

Jedoch kommt in 10 % (20 / 100) aller Fälle ein False Negative Fehler vor. 
Das bedeutet, dass in 10 % aller Fälle, die Person als gesund ausgewiesen wird, obwohl sie eigentlich krank und ansteckend ist. 

Im Fall einer Viruserkrankung ist also nicht nur die Genauigkeit entscheidend, sondern vor allem die **False Negative Rate**.


Die wichtigsten (und meist genutzten) Metriken 
-----------------------------------------------

In der Industrie werden aktuell für Klassifikationsprobleme vor allem folgende Metriken genutzt (basierend auf den oben genannten Konzepten): 

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

False Negative Rate (FNR)
~~~~~~~~~~~~~~~~~~~~~~~~~~

Die False Negative Rate (FNR) wird in der Business-Welt nicht so häufig verwendet, 
sondern vor allem in spezifiellen Domänen wie in unserem Beispiel der medizinischen Tests:

.. math::
   \text{FNR} = \frac{\text{FN} }{\text{TN} + \text{FN}}

Die FNR ist also beim Evaluieren eines Tests einer hoch-ansteckenden Viruserkrankung ein wichtiger Indikator, 
da es fatale Konsequenzen haben könnte, wenn zu viele *False Negatives* ausgelassen werden.


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

*siehe auch*: `Bestimmtheitsmaß-Wiki <https://de.wikipedia.org/wiki/Bestimmtheitsma%C3%9F>`_

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
