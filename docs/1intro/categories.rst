Kategorien von Aufgaben
=======================

Maschinelles Lernen kann für verschiedene **Aufgabentypen** eingesetzt werden,
abhängig davon, ob das Ziel eine **Vorhersage, Gruppierung oder
Entscheidungsoptimierung** ist. In diesem Kapitel werden die vier Hauptarten von
ML-Aufgaben vorgestellt: :ref:`regression`, :ref:`classification`,
:ref:`clustering` und :ref:`autonomous`.

.. _regression:

Regression
----------

* Sie ist eine Technik zur **Vorhersage von kontinuierlichen Werten** auf Basis
  von Eingabedaten.
* Sie wird genutzt, wenn das Ziel eine numerische Größe ist, :abbr:`z.B.
  (zum Beispiel)` Preis, Temperatur oder Umsatzprognose.

Beispiele
~~~~~~~~~

Immobilienpreise vorhersagen
    Basierend auf Faktoren wie Größe, Lage und Baujahr.
Wettervorhersagen
    Prognose der Temperatur für den nächsten Tag.
Finanzmarktanalysen
    Vorhersage von Aktienkursen oder Umsatzentwicklungen.

Typische Algorithmen
~~~~~~~~~~~~~~~~~~~~

* Lineare Regression
* Multiple Regression
* Polynomial Regression
* Neuronale Netze für kontinuierliche Vorhersagen

.. _classification:

Klassifikation
--------------

Definition
~~~~~~~~~~

* Klassifikation ist eine Methode zur **Zuordnung von Datenpunkten zu diskreten
  Kategorien**.
* Das Ziel ist, eine Entscheidung über eine vordefinierte Anzahl von Klassen zu
  treffen.

Beispiele
~~~~~~~~~

E-Mail-Spam-Erkennung
    Klassifizierung von E-Mails als "Spam" oder "Nicht-Spam".
Diagnosen in der Medizin
    Erkennung von Krankheiten anhand von Symptomen.
Bilderkennung
    Identifizierung von Objekten auf Fotos (Hund vs. Katze).

Typische Algorithmen
~~~~~~~~~~~~~~~~~~~~

* Entscheidungsbäume
* Random Forest
* Support Vector Machines (SVM)
* Neuronale Netze für Bilderkennung (CNNs)

.. _clustering:

Clustering
----------

Definition
~~~~~~~~~~

* Clustering ist eine Technik des **unüberwachten Lernens**, bei der Daten ohne
  vorherige Labels in Gruppen eingeteilt werden.
* Das Ziel ist es, Muster oder Strukturen in den Daten zu erkennen.

Beispiele
~~~~~~~~~

Kundensegmentierung
    Kunden anhand ihres Kaufverhaltens in Gruppen einteilen.
Genanalyse
    Identifikation von ähnlichen genetischen Mustern.
Betrugserkennung
    Auffinden verdächtiger Transaktionsmuster.

Typische Algorithmen
~~~~~~~~~~~~~~~~~~~~

* K-Means-Clustering
* DBSCAN (Density-Based Spatial Clustering)
* Hierarchisches Clustering

.. _autonomous:

Autonome Aufgaben
-----------------

Definition
~~~~~~~~~~

* Autonome Aufgaben erfordern eine Kombination aus **überwachtem, unüberwachtem
  und bestärkendem Lernen**, um **eigenständig Entscheidungen** zu treffen und
  sich an neue Situationen anzupassen.
* Diese Aufgaben sind besonders anspruchsvoll, da sie oft
  **Echtzeit-Entscheidungen** erfordern.

Beispiele
~~~~~~~~~

Selbstfahrende Autos
    Kombination aus Bilderkennung, Reinforcement Learning und Sensorfusion zur
    sicheren Navigation.
Industrielle Robotik
    Roboter, die sich an neue Umgebungen anpassen und Produktionslinien
    optimieren.
Dynamische Preisgestaltung
    Systeme, die in Echtzeit Preisentscheidungen treffen, basierend auf Angebot
    und Nachfrage.

Technologien
~~~~~~~~~~~~

Reinforcement Learning (RL):
    Algorithmen lernen durch Belohnungssysteme.
Neuronale Netze
    Deep Learning wird genutzt, um Sensordaten zu verarbeiten.
Edge Computing
    Echtzeit-Datenverarbeitung für schnelle Reaktionen.

.. _generative:

Generative Aufgaben
-------------------

Definition
~~~~~~~~~~

* Generative KI zielt darauf ab, neue Daten zu erzeugen, die den Muster der
  Trainingsdaten folgen, aber nicht identisch mit ihnen sind.
* Diese Technologie basiert auf Modellen, die durch unüberwachtes oder
  selbstüberwachtes Lernen trainiert werden und dann neue Inhalte generieren.

Beispiele
~~~~~~~~~

* Bildgenerierung:

  * Erstellung neuer Bilder auf Basis bestehender Stile (:abbr:`z.B. (zum
    Beispiel)` DeepDream, DALL·E).
  * Erstellung realistischer Gesichter mit GANs (:abbr:`z.B. (zum Beispiel)`
    „ThisPersonDoesNotExist.com“).

* Textgenerierung:

  * Chatbots wie ChatGPT, die menschenähnliche Texte generieren.
  * Automatische Textzusammenfassungen oder Artikelgenerierung.

* Musik und Audio:

  * KI-gestützte Musikkomposition (:abbr:`z.B. (zum Beispiel)` OpenAIs Jukebox).
  * Stimmenklonen und Deepfake-Audio.

* Code-Generierung:

  * KI-Systeme wie GitHub Copilot oder AlphaCode, die Programmiercode
    generieren.

* 3D- und Videogenerierung:

  * Synthese neuer 3D-Modelle für Videospiele oder Animationen.
  * KI-generierte Deepfake-Videos.

Typische Algorithmen
~~~~~~~~~~~~~~~~~~~~

* Generative Adversarial Networks (GANs)

  * Lernen zwei konkurrierende Netzwerke: ein „Generator“ und ein
    „Diskriminator“.

  * Beispiel: Stiltransfer von Gemälden auf Fotos.

* Variational Autoencoders (VAEs)

  * Lernen eine kompakte Darstellung der Daten und können daraus neue Instanzen generieren.

* Transformer-Modelle (:abbr:`z.B. (zum Beispiel)` GPT, BERT, T5)

  * Werden für Text- und Codegenerierung eingesetzt.

* Diffusionsmodelle (DALL·E, Stable Diffusion)

  * Besonders leistungsfähig für hochwertige Bilderzeugung.

Zusammenfassung
~~~~~~~~~~~~~~~

* Generative KI ist eine eigene Aufgabenkategorie, da sie keine Vorhersage- oder
  Gruppierungsaufgabe erfüllt, sondern neue Inhalte erstellt.
* Sie nutzt tiefe neuronale Netze, insbesondere GANs, Transformer-Modelle und
  Diffusionsmodelle.
* Generative KI wird zunehmend wichtiger in Bereichen wie Kunst, Design, Code,
  Audio und Sprache.

Vergleich der ML-Aufgabentypen
------------------------------

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
   * - Beispiele
     - Preisprognosen, Finanzanalysen
     - Bilderkennung, Spam-Filter
     - Kundensegmentierung, Anomalieerkennung
     - Selbstfahrende Autos, Industrieroboter
     - KI-generierte Bilder, Texte, Musik
   * - Typische Algorithmen
     - Lineare Regression, neuronale Netze
     - Entscheidungsbäume, SVM
     - K-Means, DBSCAN
     - Reinforcement Learning, Deep Learning
     - GANs, VAEs, Transformer

Fazit
-----

* Regression, Klassifikation und Clustering gehören zu den klassischen Aufgaben
  des maschinellen Lernens.
* Autonome Systeme sind eine anspruchsvolle Anwendung, die verschiedene
  ML-Techniken kombiniert.
* Je nach Daten und Zielsetzung kann eine Kombination dieser Methoden sinnvoll
  sein.
