Nachtrag: Ensemble Methoden in ML
========================================

Definition: Was sind Ensemble-Methoden?
-----------------------------------------

Ensemble-Methoden sind Techniken im maschinellen Lernen, die mehrere Modelle kombinieren, um eine bessere Gesamtvorhersage zu erzielen. Anstatt sich auf ein einzelnes Modell zu verlassen, nutzen Ensemble-Methoden **die kollektive Intelligenz mehrerer schwächerer Modelle**, um **robustere und genauere Ergebnisse** zu erzielen. 

Warum Ensemble-Methoden?
--------------------------

* Sie **reduzieren Varianz und Overfitting**, indem sie Vorhersagen mehrerer Modelle mitteln oder gewichten.
* Sie **verbessern die Vorhersagegenauigkeit**, indem sie die Stärken mehrerer Algorithmen kombinieren.
* Sie **machen Modelle robuster gegenüber Rauschen und Ausreißern**.

Haupttypen von Ensemble-Methoden**
------------------------------------

Ensemble-Methoden lassen sich in zwei Hauptkategorien einteilen: **Bagging** und **Boosting**.

Bagging (Bootstrap Aggregating)
::::::::::::::::::::::::::::::::::::

Prinzip:
~~~~~~~~~~~~~

* **Ziel:** Reduzierung der Varianz durch die Kombination mehrerer schwacher Modelle.
* **Methode:** Mehrere Modelle werden auf unterschiedlichen zufälligen Teilmengen der Trainingsdaten trainiert (mit **Bootstrapping**) und ihre Vorhersagen gemittelt.
* **Wirkung:** Führt zu stabileren Modellen, da einzelne Modelle überdurchschnittliche Fehler ausgleichen können.

Beispiel: Random Forest
~~~~~~~~~~~~~~~~~~~~~~~~~

* Random Forest ist eine klassische Bagging-Methode.
* Es besteht aus mehreren **Entscheidungsbäumen**, die auf zufällig gewählten Trainingsdaten und Features trainiert werden.
* Die Vorhersagen werden entweder **gemittelt (Regression)** oder **per Mehrheitsentscheid (Klassifikation)** aggregiert.

Stärken von Bagging:
~~~~~~~~~~~~~~~~~~~~~~~~~

* Reduziert Overfitting durch Mittelung mehrerer Modelle.
* Verbessert Stabilität und Generalisierung.
* Gut für Modelle mit hoher Varianz (z. B. Entscheidungsbäume).

Schwächen von Bagging:
~~~~~~~~~~~~~~~~~~~~~~~~~

* Keine Verbesserung, wenn Basismodelle bereits sehr stabil sind.
* Erfordert ausreichend Trainingsdaten, um Bootstrapping effektiv zu nutzen.

Boosting
:::::::::::::

Prinzip:
~~~~~~~~~

* **Ziel:** Reduzierung von Bias durch das schrittweise Training mehrerer Modelle.
* **Methode:** Jedes neue Modell lernt aus den Fehlern des vorherigen Modells und passt sich iterativ an.
* **Wirkung:** Boosting kann schwache Modelle in sehr leistungsfähige Modelle umwandeln.

Beispiel: Gradient Boosting (z. B. XGBoost, LightGBM)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Anstatt mehrere unabhängige Modelle zu trainieren, werden **schwache Modelle sequentiell trainiert**.
* Jedes neue Modell konzentriert sich darauf, die **Fehler der vorherigen Modelle zu korrigieren**.
* Die finale Vorhersage ist eine gewichtete Kombination aller Modelle.

Stärken von Boosting
~~~~~~~~~~~~~~~~~~~~~~~~

✔ Reduziert Bias, indem es Fehler schrittweise korrigiert.
✔ Sehr leistungsfähig bei strukturierten Daten.
✔ Gute Ergebnisse mit wenigen Trainingsdaten.

Schwächen von Boosting:
~~~~~~~~~~~~~~~~~~~~~~~~

✖ Höheres Overfitting-Risiko, wenn zu viele Bäume verwendet werden.
✖ Langsameres Training als Bagging-Methoden.
✖ Schwieriger zu parallelisieren.

Vergleich von Bagging vs. Boosting
-----------------------------------

.. list-table:: Vergleich von Bagging und Boosting
   :header-rows: 1
   :widths: auto

   * - Merkmal
     - Bagging (z. B. Random Forest)
     - Boosting (z. B. XGBoost)
   * - Ziel
     - Reduziert Varianz
     - Reduziert Bias
   * - Modelltraining
     - Unabhängige Modelle
     - Sequentielle Modelle
   * - Overfitting
     - Gering
     - Höheres Risiko
   * - Trainingsgeschwindigkeit
     - Schnell (parallel)
     - Langsamer (sequentiell)
   * - Anwendungsfälle
     - Große Datenmengen mit hoher Varianz
     - Strukturierte Daten mit vielen Features


Wann sollte man welche Methode nutzen?
::::::::::::::::::::::::::::::::::::::::::

* Wenn Overfitting ein Problem ist → Bagging (z. B. Random Forest)
* Wenn das Modell zu hohe Bias-Fehler hat → Boosting (z. B. XGBoost, LightGBM).
* Wenn Rechenleistung ein Problem ist → Bagging (weil besser parallelisierbar).
* Wenn höchste Vorhersagegenauigkeit benötigt wird → Boosting.
