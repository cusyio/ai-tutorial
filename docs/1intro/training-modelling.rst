Trainingsdaten und Modellierung
===============================

Datenqualität und ihre Bedeutung
--------------------------------

* Gute Trainingsdaten sind essenziell für die Leistungsfähigkeit eines Modells.
* Aspekte der Datenqualität:

  Vollständigkeit
      Fehlende Werte können Modelle ungenau machen.
  Konsistenz
      Daten sollten einheitlich und korrekt sein.
  Ausreißererkennung
      Extreme Werte können Modelle verzerren.
  Datenverteilung
      Unausgewogene Datensätze (:abbr:`z.B. (zum Beispiel)` ungleich verteilte
      Klassen) beeinflussen Modellentscheidungen.

Feature Engineering
-------------------

Definition
~~~~~~~~~~

Feature Engineering ist die Kunst, relevante Eingangsvariablen für ein Modell zu
erstellen.

Beispiel
~~~~~~~~

`Kohorte <https://de.wikipedia.org/wiki/Kohorte_(Sozialwissenschaft)>`_

Typische Techniken
~~~~~~~~~~~~~~~~~~

Feature Skalierung
    Normalisierung und Standardisierung von Daten (:abbr:`z.B. (zum Beispiel)`
    Min-Max-Scaling, Z-Score-Normalisierung).
Feature Selektion
    Auswahl der wichtigsten Merkmale zur Reduktion von Overfitting.
Feature Transformation
    Anwendung von Logarithmus- oder Polynom-Transformationen zur Verbesserung
    der Modellleistung.
One-Hot-Encoding
    Umwandlung kategorialer Variablen in numerische Werte.

Modelltraining und Optimierung
------------------------------

- Schritte des Modelltrainings:

  1. **Datenaufteilung:** Aufteilung in Trainings-, Validierungs- und Testdatensätze.

  2. **Modellauswahl:** Auswahl eines geeigneten Algorithmus (z. B. Entscheidungsbaum, Random Forest, neuronale Netze).

  3. **Hyperparameter-Tuning:** Feinabstimmung der Modellparameter zur Optimierung der Leistung (z. B. Grid Search, Random Search).

  4. **Modellbewertung:** Verwendung von Metriken wie Genauigkeit, F1-Score oder Mean Squared Error zur Bewertung der Vorhersagequalität.

  5. **Modellbereitstellung:** Einsatz des trainierten Modells in einer produktiven Umgebung.

Praxisbeispiel: Modelltraining in Python
----------------------------------------

- Implementierung eines einfachen ML-Modells mit scikit-learn zur Vorhersage von Hauspreisen.

- Demonstration von Datenvorbereitung, Feature Engineering und Modelltraining.
