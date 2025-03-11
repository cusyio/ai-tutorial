Vertiefung: Neuronale Netze, Deep Learning, Systemüberblick, Use Case Fallgruben
------------------------------------------------------------------------------------------------------------

**Recap Tag 1**

- Zusammenfassung der Konzepte aus Tag 1: Überwachtes, unüberwachtes und bestärkendes Lernen.

- Wichtige Begriffe: **Modell, Trainingsdaten, Testdaten.**

- Diskussion der zentralen Herausforderungen im ML: **Bias, Datenqualität, Modellinterpretierbarkeit.**

- Offene Fragen und Klarstellungen



* Logistic Regression 
* Decision Tree => Random Forest 
* SVM ()

.. list-table:: Vergleich von Regression, Klassifikation, Clustering und autonomen Aufgaben
   :header-rows: 1

   * - Merkmal
     - :ref:`regression`
     - :ref:`classification`
     - :ref:`clustering`
     - :ref:`autonomous`
     - :ref:`generative`
   * - Art der Vorhersage
     - Kontinuierlicher Wert
     - Diskrete Klassen
     - Gruppenbildung ohne Labels
     - Eigenständige Entscheidungsfindung
     - Erzeugung neuer Daten
   * - Use Case Beispiele
     - Preisprognosen, Finanzanalysen
     - Bilderkennung, Spam-Filter
     - Kundensegmentierung, Anomalieerkennung
     - Selbstfahrende Autos, Industrieroboter
     - KI-generierte Bilder, Texte, Musik
   * - Gängige "Klassischen" Algorithmen
     - Lineare Regression, neuronale Netze
     - Decision Trees (Entscheidungsbäume), Random Forest, SVM
     - K-Means Clustering, K-nearest neighbour (kNN), DBSCAN
     - Reinforcement Learning, Deep Learning
     - GANs, VAEs, Transformer


Heutiger Kursinhalt
~~~~~~~~~~~~~~~~~~~~


.. list-table:: 
   :header-rows: 1

   * - Kapitel
     - Inhalte
   * - Recap der wichtigsten Themen
     - Wiederholung der ML-Konzepte, Diskussion, Quiz
   * - Modellverhalten 
     - Overfitting, Regularisierung und Optimierung
   * - Theorie: Neuronale Netze und Deep Learning
     - Aufbau, Backpropagation, Aktivierungsfunktionen
   * - Praxis: Bildklassifikation mit CNNs
     - Implementierung mit TensorFlow/Keras
   * - Diskussion: Use Case Fallgruben
     - Churn Prediction, Herausforderungen, Modellwahl


.. toctree::
   :hidden:
   :titlesonly:
   :maxdepth: 0

   deduplicate
   modellverhalten
   neural-net
   neural-net-optimize
   cnn-beispiel
   mlops
