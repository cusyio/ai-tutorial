Tag 1: Einführung, Überwachtes Lernen, Regression
==============================

Die Schulung wird mit den grundlegenden Konzepten der Künstlichen Intelligenz (KI) und Maschinellen Lernens (ML) eingeleitet und anhand praktischer Implementierungen veranschaulicht.


Gliederung
----------

.. list-table:: Schulungsstruktur für KI-Grundlagen: Tag 1
   :header-rows: 1

   * - Kapitel
     - Inhalte
   * - Einführung in Künstliche Intelligenz
     - Definition und Historie der KI, Unterschiedliche Formen der KI, Anwendungsfälle, ethische Fragestellungen
   * - Maschinelles Lernen: Konzepte und Typen
     - Begriffe: ML, Deep Learning, Reinforcement Learning; Beispiele für reale Anwendungen
   * - Überwachtes vs. Unüberwachtes Lernen
     - Klassifikation vs. Regression, Clustering-Methoden
   * - Trainingsdaten und Modellierung
     - Datenqualität, Feature Engineering, Modelltraining
   * - Evaluation von ML-Modellen
     - Metriken: Accuracy (Genauigkeit), Precision (Präzision), Recall, F1-Score, MSE
   * - Praktische Einführung: Lineare Regression
     - Implementierung eines ML-Modells mit scikit-learn
   * - Fallstudie: Vorhersage von Immobilienpreisen
     - Hands-on Beispiel mit einem realen Datensatz
   * - Diskussion und Fragen
     - Diskussion über Anwendungen von KI in verschiedenen Bereichen

Kapitel 1: Definition von Künstlicher Intelligenz
------------------
Künstliche Intelligenz (KI) bezeichnet die Fähigkeit eines Computers oder einer Maschine, menschenähnliche kognitive Funktionen auszuführen. Dazu gehören Aufgaben wie Lernen, Problemlösung, Mustererkennung und Entscheidungsfindung. Der Begriff KI wurde erstmals 1956 auf der Dartmouth Conference von John McCarthy geprägt. Heute umfasst KI eine Vielzahl von Techniken, darunter maschinelles Lernen, Deep Learning und Expertensysteme.

**Historische Entwicklung der KI**
Die Entwicklung der KI lässt sich in mehrere Phasen einteilen:

1. **1950er–1970er: Die Pionierzeit**

- Erste Algorithmen zur symbolischen Verarbeitung und regelbasierten Systeme wurden entwickelt.

- Alan Turings berühmter "Turing-Test" (https://en.wikipedia.org/wiki/Turing_test) stellte eine frühe Methode zur Bewertung der Intelligenz einer Maschine vor.

- In den 1960er Jahren entstanden erste Expertensysteme, die regelbasierte Entscheidungsfindung ermöglichten.

2. **1980er – 1990er: Erste Fortschritte und Rückschläge**

- KI erlebte durch das Aufkommen von neuronalen Netzen und maschinellem Lernen einen Aufschwung.

- Aufgrund hoher Rechenkosten und begrenzter Datenverfügbarkeit flachte das Interesse an KI in den späten 1980er Jahren ab.

3. **2000er – heute: Der Durchbruch dank Big Data und Deep Learning**

- Fortschritte in Rechenleistung, Cloud Computing und die Verfügbarkeit großer Datenmengen haben KI auf ein neues Niveau gehoben.

- Tiefe neuronale Netze ermöglichen Fortschritte in Spracherkennung, Bildverarbeitung und autonomem Fahren.

**Unterschiedliche Formen der Künstlichen Intelligenz**

KI kann auf verschiedene Art und Weisen in verschiedene Kategorien unterteilt werden. Eine Möglichkeit ist die Kategorisierung nach ihrem Funktionsumfang und ihren Anwendungsmöglichkeiten, wie von Prof. Arend Hintze definiert, Forscher und Professor der Integrative Biology an der Michigan State University (https://theconversation.com/understanding-the-four-types-of-ai-from-reactive-robots-to-self-aware-beings-67616, https://mindsquare.de/knowhow/kuenstliche-intelligenz/#der-turing-test):

1. **Reaktive KI (Reactive AI)**

Die erste Stufe der KI kann als "Reaktive KI" bezeichent und als ein Ur-Typ der KI angesehen werden. Sie hat weder "Gedächtnis" noch "Lernfähigkeit" und kann nur auf Eingaben reagieren für genau die eine Aufgabe, wofür sie programmiert wurde. Es ist nicht in der Lage, zukünftige Ergebnisse vorherzusagen, wenn es nicht mit den entsprechenden Informationen gefüttert wurde.

Beispiel: Schachcomputer wie IBM Deep Blue, der auf Basis aktueller Züge die bestmöglichen Entscheidungen trifft.

2. **Begrenzte Gedächtnis-KI (Limited Memory AI)**

Die zweite Stufe der KI kann Informationen aus vergangenen Interaktionen nutzen, um zukünftige Entscheidungen zu verbessern.

Beispiel: Selbstfahrende Autos, die Sensordaten aus der Umgebung speichern und auf Basis vorheriger Erfahrungen optimieren.

Die erste und zweite Stufen der KI sind bereits teilweise im Einsatz, mit unterschiedlichen technischen Reifegrad in diversen Domänen. 

3. **Theorie des Geistes-KI (Theory of Mind AI)** *(noch in der Forschung)*

Im Gegensatz zu den ersten beiden Formen der KI hätten die 3. und die 4. Form der KI ein eigenes Bewusstsein und Verständnis für sich selbst. Intelligente Systeme der Stufe 3 könnten menschliche Emotionen wahrnehmen und verstehen, sowie auch deren eigenes Verhalten entsprechend anpassen. 

Ziel: KI mit Verständnis für Emotionen und sozialen Kontext.

Potenzielles Beispiel: Fortgeschrittene humanoide Roboter mit sozialem Bewusstsein.

4. **Selbstbewusste KI (Self-Aware AI)** *(hypothetisch)*

Diese Stufe der KI hätte ein eigenes Bewusstsein und ein Verständnis für sich selbst und käme somit dem menschlichen Bewusstsein (der menschlichen Intelligenz) am nächsten.

Ob und wann die Entwicklung der KI jemals diese Stufe erreichen wird, ist noch viel umstritten - bisher wurde es nur in Science-Fiction Werken dargestellt.

**Prädiktive vs. Generative KI**

Die aktuell in der Industrie gängigen Formen der KI lassen sind insbesondere in **prädiktive KI** und **generative KI** unterscheiden:

1. **Prädiktive KI**

   - Diese KI nutzt historische Daten, um **zukünftige Ereignisse vorherzusagen**.

   - Verwendete Algorithmen: Regression, Entscheidungsbäume, neuronale Netze.

   - Beispiele:

     - Vorhersage von Aktienkursen oder Wetterverhältnissen.

     - Diagnose von Krankheiten basierend auf medizinischen Daten.

     - Betrugserkennung im Finanzsektor.

2. **Generative KI**

   - Diese KI erzeugt **neue Inhalte**, die zuvor nicht explizit in den Trainingsdaten enthalten waren.

   - Verwendete Modelle: Generative Adversarial Networks (GANs), Transformer-Modelle (z. B. GPT, DALL·E).

   - Beispiele:

     - Erstellung von Bildern, Musik oder Texten (z. B. KI-generierte Kunst, Chatbots).

     - Übersetzung und Zusammenfassung von Texten.

     - Deepfake-Technologien.

**Bedeutung dieser Unterscheidung**

- Prädiktive KI wird hauptsächlich in **Analytik und Entscheidungsfindung** eingesetzt, während generative KI für **Kreativität und Content-Erzeugung** genutzt wird.

- In der Praxis werden oft **beide Ansätze kombiniert**, z. B. wenn eine prädiktive KI Markttrends analysiert und eine generative KI dazu passende Werbeinhalte erstellt.


**Anwendungsfälle von KI**

KI findet heute in zahlreichen Bereichen Anwendung, darunter:

- **Gesundheitswesen:** Diagnosestellung durch KI-gestützte Bildverarbeitung, Medikamentenentwicklung.

- **Finanzwesen:** Automatische Betrugserkennung, algorithmischer Handel.

- **Industrie:** Automatisierung von Prozessen, Qualitätskontrolle in der Fertigung.

- **Autonome Systeme:** Selbstfahrende Autos, Drohnen, Robotersteuerung.

- **Sprachverarbeitung:** Sprachassistenten wie Siri, Alexa oder Google Assistant.

- **Kreative Anwendungen:** Generierung von Texten, Musik und Kunst durch KI.

**Ethische Fragestellungen in der KI**

Mit der rasanten Entwicklung der KI gehen auch bedeutende ethische Fragen einher:

- **Bias und Diskriminierung:** KI-Modelle können bestehende Vorurteile aus Trainingsdaten übernehmen.

- **Arbeitsplatzverdrängung:** Automatisierung kann menschliche Arbeitsplätze gefährden.

- **Transparenz und Erklärbarkeit:** Viele KI-Modelle, insbesondere Deep Learning, sind schwer zu interpretieren.

- **Verantwortung und Haftung:** Wer ist verantwortlich, wenn eine KI fehlerhafte oder schädliche Entscheidungen trifft?

- **Datenschutz:** KI-Anwendungen erfordern oft große Datenmengen, was Datenschutzprobleme aufwirft.



Kapitel 2: Maschinelles Lernen (ML): Konzepte und Typen
--------------------------------------------------

.. note:: 
  **TODO: MIT CODE BEISPIEL!**
  https://www.python4data.science/de/latest/productive/dvc/dag.html 

**Definition und Konzepte des Maschinellen Lernens (ML)**

Maschinelles Lernen (Machine Learning, ML) ist ein Teilgebiet der Künstlichen Intelligenz, das Computern ermöglicht, aus Daten zu lernen, anstatt explizit programmiert zu werden. Es gibt drei Hauptarten des ML:

1. **Überwachtes Lernen (Supervised Learning)**
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ 

Beim **überwachten Lernen** werden Modelle mit **gelabelten Daten** trainiert. 

Das bedeutet, dass für jeden Eingabedatensatz ein bekanntes **Ziel** existiert.

Das Ziel des Modells ist es, eine Funktion zu lernen, die den Zusammenhang zwischen Eingaben und Ausgaben erfasst. 

Überwachtes Lernen kann sowohl für Regression als auch für Klassifikation genutzt werden.

Beispiele hierfür sind:

- **Klassifikation:** Vorhersage diskreter Kategorien (z. B. Spam-Filter, Bilderkennung von Hunden und Katzen).

- **Regression:** Vorhersage kontinuierlicher Werte (z. B. Hauspreisvorhersage anhand der Wohnfläche).

**Theoretische Konzepte des Überwachten Lernens**

- **Trainingsprozess:**

  - Das Modell wird mit einem Trainingsdatensatz trainiert, in dem **Eingaben (Features)** und die zugehörigen **Zielwerte (Labels)** bekannt sind.

  - Die Lernfunktion (oft als **Hypothesenfunktion** bezeichnet) wird durch das Training optimiert.

- **Modellbewertung:**

  - Das trainierte Modell wird anhand neuer Daten getestet, um sicherzustellen, dass es generalisiert und nicht nur die Trainingsdaten auswendig gelernt hat.

  - Typische Metriken: Genauigkeit, Präzision, Recall und F1-Score, Mean Squared Error (MSE).

2. **Unüberwachtes Lernen (Unsupervised Learning)**
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Beim **unüberwachten Lernen** gibt es **keine gelabelten Daten**.

Das Modell versucht, Muster oder Strukturen in den Daten zu entdecken.

Dies eignet sich besonders für **Explorative Datenanalyse**, bei der keine festen Kategorien bekannt sind. 

Unüberwachtes Lernen kann direkt für Klassifikationsprobleme genutzt werden; aber nur indirekt für Regressionsprobleme, z.B. als Vorverarbeitungsschritt oder zur Merkmalextraktion, um Regression effektiver zu machen. 


Typische Anwendungen sind:

1. **Clustering:**

- Ziel: Datenpunkte in Gruppen einteilen, basierend auf Ähnlichkeit.

- Beispiele:

  - Kundensegmentierung für personalisierte Werbung.

  - Erkennung von ähnlichen Produkten in Online-Shops.

  - Gruppierung von genetischen Mustern in der Biologie. 

  - Betrugserkennung durch Anomalie-Analyse in Banktransaktionen.

2. **Dimensionsreduktion:**

- Ziel: Komplexe Daten in eine einfachere Form umwandeln.

- Beispiele:

  - Hauptkomponentenanalyse (PCA) zur Reduzierung hochdimensionaler Daten.

  - Visualisierung von großen Datenmengen.

  - Feature-Auswahl für effizientere Modellberechnungen.


3. **Theoretische Konzepte des Unüberwachten Lernens**

- **Clustering-Algorithmen:**

  - **K-Means:** Teilt Daten in eine vordefinierte Anzahl von Clustern ein.

  - **Hierarchisches Clustering:** Erstellt eine baumartige Struktur zur Clusterbildung.

  - **DBSCAN:** Erkennt Cluster basierend auf der Dichte der Datenpunkte.

- **Dimensionsreduktionstechniken:**

  - **PCA (Principal Component Analysis):** Extrahiert die wichtigsten Variablen aus großen Datensätzen.

  - **t-SNE (t-Distributed Stochastic Neighbor Embedding):** Visualisiert komplexe Datensätze in 2D oder 3D.

**Vergleich: Überwachtes vs. Unüberwachtes Lernen**
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table:: Vergleich von Überwachtem und Unüberwachtem Lernen
  :header-rows: 1

  * - Merkmal
    - Überwachtes Lernen
    - Unüberwachtes Lernen
  * - Datenverfügbarkeit
    - Gelabelte Daten notwendig
    - Keine Labels erforderlich
  * - Ziel
    - Vorhersage einer bekannten Zielvariable
    - Identifikation von Mustern oder Strukturen
  * - Typische Algorithmen
    - Lineare Regression, Entscheidungsbäume, Neuronale Netze
    - K-Means, DBSCAN, PCA
  * - Anwendungsbereiche
    - Klassifikation, Regression
    - Clustering, Dimensionsreduktion

3. **Reinforcement Learning (Bestärkendes Lernen, RL)**
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. **Definition:**

   - Beim **Reinforcement Learning** (Bestärkenden Lernen, RL) lernt ein Agent durch **Interaktion mit einer Umgebung**, wobei er **Belohnungen oder Bestrafungen** erhält.

   - Das Ziel des RL ist es, eine **Optimierungsstrategie** zu entwickeln, die langfristig die höchste Gesamtbelohnung erzielt.

   - Es handelt sich um eine Form des **Lernens durch Versuch und Irrtum**, ähnlich wie ein Mensch, der durch Erfahrung lernt.

2. **Grundprinzipien von Reinforcement Learning:**

   - **Agent** – Das KI-System, das lernt (z. B. ein Roboter, ein autonomes Auto, ein Schachprogramm).

   - **Umgebung (Environment)** – Alles außerhalb des Agents, mit dem er interagiert.

   - **Zustand (State)** – Eine Momentaufnahme der Umgebung, die den Agenten beeinflusst.

   - **Aktion (Action)** – Eine Entscheidung, die der Agent in einem bestimmten Zustand trifft.

   - **Belohnung (Reward)** – Eine numerische Bewertung der Aktion, die dem Agenten signalisiert, ob er sich der optimalen Lösung nähert oder nicht.

   - **Richtlinien (Policy)** – Eine Strategie, die den besten nächsten Schritt für den Agenten bestimmt.

   - **Qualitäts-Wert (Q-Value)** – Eine Bewertung, wie gut eine bestimmte Aktion in einem Zustand langfristig ist.

3. **Beispiele für RL-Anwendungen:**

- **Spielstrategien:** AlphaGo von DeepMind besiegte menschliche Meister im Go-Spiel durch RL.

- **Autonome Fahrzeuge:** Lernen, sicher zu fahren, indem sie Belohnungen für sichere Entscheidungen erhalten.

- **Robotik:** Industrieroboter optimieren ihre Bewegungen, um Aufgaben effizienter zu erledigen.

- **Algorithmischer Handel:** KI-Agenten lernen, wann sie Aktien kaufen oder verkaufen sollen.

4. **Wichtige RL-Algorithmen:**

- **Q-Learning:** Eine tabellenbasierte Methode zur Speicherung der besten Aktionen.

- **Deep Q-Networks (DQN):** Eine Erweiterung von Q-Learning unter Verwendung von neuronalen Netzen.

- **Policy-Gradient-Verfahren:** Statt Werte zu lernen, lernt das Modell direkt eine optimale Strategie.

- **Proximal Policy Optimization (PPO):** Häufig in modernen RL-Anwendungen eingesetzt (z. B. bei OpenAI Gym).

5.  **Herausforderungen im RL:**

- **Exploration vs. Exploitation:** Ein Agent muss entscheiden, ob er eine **neue Strategie** testet oder eine **bereits bekannte, aber möglicherweise nicht optimale** Strategie nutzt.

- **Belohnungsdesign:** Ein schlecht definierter Belohnungsmechanismus kann dazu führen, dass das Modell unerwartete oder unerwünschte Strategien lernt.

- **Rechenaufwand:** RL benötigt oft viele Trainingsdurchläufe und Rechenleistung.

.. seealso::
   * :doc:`day3` 




.. https://python-basics-tutorial.readthedocs.io/en/latest/appendix/glossary.html


.. glossary:

   Eingangsschicht
   Input Layer
       Nimmt Daten auf (z. B. Pixelwerte eines Bildes).




4. **Deep Learning (DL) als spezialisierte Form des ML**
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Definition:**

- Deep Learning (DL) ist ein Teilgebiet des maschinellen Lernens, das auf **künstlichen neuronalen Netzen (KNNs)** basiert.

- Es verwendet **mehrere Schichten von Neuronen** (daher der Begriff „Deep“), um hochkomplexe Muster in Daten zu lernen.

- Deep Learning ist besonders leistungsfähig bei **Bildverarbeitung, Spracherkennung und natürlicher Sprachverarbeitung (NLP).**

**Aufbau eines neuronalen Netzes:**

:term:`Input Layer`
    Nimmt Daten auf (z. B. Pixelwerte eines Bildes).



2. **Verborgene Schichten (Hidden Layers):** Extrahieren Merkmale und erkennen Muster.

3. **Ausgangsschicht (Output Layer):** Gibt das Ergebnis der Berechnung aus (z. B. Klassifizierung in „Hund“ oder „Katze“).

**Arten von neuronalen Netzwerken:**

- **Feedforward Neural Networks (FNN):** Einfachste Form, bei der Informationen nur in eine Richtung fließen.

- **Convolutional Neural Networks (CNN):** Besonders geeignet für **Bildverarbeitung** (z. B. Gesichtserkennung, medizinische Bilddiagnostik).

- **Recurrent Neural Networks (RNN):** Nutzen vergangene Informationen zur Verarbeitung von **sequenziellen Daten** (z. B. Sprachverarbeitung, Zeitreihenanalyse).

- **Transformer-Modelle:** Revolutionierten die **Natürliche Sprachverarbeitung (NLP)** (z. B. GPT-Modelle, BERT, T5).

**Beispiele für Anwendungen von Deep Learning:**

- **Bilderkennung:** Automatische Erkennung von Objekten in Bildern.

- **Sprachverarbeitung (NLP):** Chatbots, automatische Übersetzungen (Google Translate, ChatGPT).

- **Autonome Systeme:** Steuerung von selbstfahrenden Autos und Robotern.

- **Medizinische Diagnosen:** Krebsfrüherkennung in MRT-Scans mit neuronalen Netzen.

**Herausforderungen im Deep Learning:**

- **Erklärbarkeit:** DL-Modelle sind oft **Black Boxes**, deren Entscheidungen schwer nachvollziehbar sind.

- **Datenbedarf:** Sehr große Mengen an **trainingsdaten** sind notwendig.

- **Rechenleistung:** DL benötigt leistungsfähige GPUs oder TPUs.

**Zukunft von Deep Learning:**

- **Edge AI:** Deep Learning wird zunehmend auf Edge-Geräten (Smartphones, IoT-Geräte) ausgeführt.

- **Hybride Systeme:** Kombination von Deep Learning mit Reinforcement Learning für **komplexe Entscheidungsprozesse**.

- **Quanten-KI:** Erste Ansätze zur Beschleunigung von Deep-Learning-Modellen mit Quantencomputing.



Kapitel 3: Kategorien von Aufgaben: Regression, Klassifikation, Clustering, Autonome Aufgaben, Generative Aufgaben
--------------------------------------------------------------------------------------

Maschinelles Lernen kann für verschiedene **Aufgabentypen** eingesetzt werden, abhängig davon, ob das Ziel eine **Vorhersage, Gruppierung oder Entscheidungsoptimierung** ist. In diesem Kapitel werden die vier Hauptarten von ML-Aufgaben vorgestellt: **Regression, Klassifikation, Clustering und autonome Aufgaben.**

**I. Regression**

**Definition:**

- Regression ist eine Technik zur **Vorhersage von kontinuierlichen Werten** auf Basis von Eingabedaten.

- Sie wird genutzt, wenn das Ziel eine numerische Größe ist, z. B. Preis, Temperatur oder Umsatzprognose.

**Beispiele für Regression:**

- **Immobilienpreise vorhersagen:** Basierend auf Faktoren wie Größe, Lage und Baujahr.

- **Wettervorhersagen:** Prognose der Temperatur für den nächsten Tag.

- **Finanzmarktanalysen:** Vorhersage von Aktienkursen oder Umsatzentwicklungen.

**Typische Algorithmen:**

- Lineare Regression

- Multiple Regression

- Polynomial Regression

- Neuronale Netze für kontinuierliche Vorhersagen

-------

**II. Klassifikation**

**Definition:**

- Klassifikation ist eine Methode zur **Zuordnung von Datenpunkten zu diskreten Kategorien**.

- Das Ziel ist, eine Entscheidung über eine vordefinierte Anzahl von Klassen zu treffen.

**Beispiele für Klassifikation:**

- **E-Mail-Spam-Erkennung:** Klassifizierung von E-Mails als "Spam" oder "Nicht-Spam".

- **Diagnosen in der Medizin:** Erkennung von Krankheiten anhand von Symptomen.

- **Bilderkennung:** Identifizierung von Objekten auf Fotos (Hund vs. Katze).

**Typische Algorithmen:**

- Entscheidungsbäume

- Random Forest

- Support Vector Machines (SVM)

- Neuronale Netze für Bilderkennung (CNNs)

-----

**III. Clustering**

**Definition:**

- Clustering ist eine Technik des **unüberwachten Lernens**, bei der Daten ohne vorherige Labels in Gruppen eingeteilt werden.

- Das Ziel ist es, Muster oder Strukturen in den Daten zu erkennen.

**Beispiele für Clustering:**

- **Kundensegmentierung:** Kunden anhand ihres Kaufverhaltens in Gruppen einteilen.

- **Genanalyse:** Identifikation von ähnlichen genetischen Mustern.

- **Betrugserkennung:** Auffinden verdächtiger Transaktionsmuster.

**Typische Algorithmen:**

- K-Means-Clustering

- DBSCAN (Density-Based Spatial Clustering)

- Hierarchisches Clustering

------

**IV. Autonome Aufgaben**

**Definition:**

- Autonome Aufgaben erfordern eine Kombination aus **überwachtem, unüberwachtem und bestärkendem Lernen**, um **eigenständig Entscheidungen** zu treffen und sich an neue Situationen anzupassen.

- Diese Aufgaben sind besonders anspruchsvoll, da sie oft **Echtzeit-Entscheidungen** erfordern.

**Beispiele für autonome Aufgaben:**

- **Selbstfahrende Autos:** Kombination aus Bilderkennung, Reinforcement Learning und Sensorfusion zur sicheren Navigation.

- **Industrielle Robotik:** Roboter, die sich an neue Umgebungen anpassen und Produktionslinien optimieren.

- **Dynamische Preisgestaltung:** Systeme, die in Echtzeit Preisentscheidungen treffen, basierend auf Angebot und Nachfrage.

**Technologien hinter autonomen Aufgaben:**

- **Reinforcement Learning (RL):** Algorithmen lernen durch Belohnungssysteme.

- **Neuronale Netze:** Deep Learning wird genutzt, um Sensordaten zu verarbeiten.

- **Edge Computing:** Echtzeit-Datenverarbeitung für schnelle Reaktionen.


-------

**V. Generative Aufgaben**

Definition:
	-	Generative KI zielt darauf ab, neue Daten zu erzeugen, die den Muster der Trainingsdaten folgen, aber nicht identisch mit ihnen sind.
	-	Diese Technologie basiert auf Modellen, die durch unüberwachtes oder selbstüberwachtes Lernen trainiert werden und dann neue Inhalte generieren.

Beispiele für generative Aufgaben:
	-	Bildgenerierung:
	  - Erstellung neuer Bilder auf Basis bestehender Stile (z. B. DeepDream, DALL·E).
	  - Erstellung realistischer Gesichter mit GANs (z. B. „ThisPersonDoesNotExist.com“).
	-	Textgenerierung:
	  -	Chatbots wie ChatGPT, die menschenähnliche Texte generieren.
	  -	Automatische Textzusammenfassungen oder Artikelgenerierung.
	-	Musik und Audio:
	  -	KI-gestützte Musikkomposition (z. B. OpenAIs Jukebox).
	  -	Stimmenklonen und Deepfake-Audio.
	-	Code-Generierung:
	  -	KI-Systeme wie GitHub Copilot oder AlphaCode, die Programmiercode generieren.
	-	3D- und Videogenerierung:
	  -	Synthese neuer 3D-Modelle für Videospiele oder Animationen.
	  -	KI-generierte Deepfake-Videos.

Typische Algorithmen:
	-	Generative Adversarial Networks (GANs)

	 - Lernen zwei konkurrierende Netzwerke: ein „Generator“ und ein „Diskriminator“.

	 - Beispiel: Stiltransfer von Gemälden auf Fotos.
	-	Variational Autoencoders (VAEs)
	  -	Lernen eine kompakte Darstellung der Daten und können daraus neue Instanzen generieren.
	-	Transformer-Modelle (z. B. GPT, BERT, T5)
	  -	Werden für Text- und Codegenerierung eingesetzt.
	-	Diffusionsmodelle (DALL·E, Stable Diffusion)
	  -	Besonders leistungsfähig für hochwertige Bilderzeugung.

Zusammenfassung: 

- Generative KI ist eine eigene Aufgabenkategorie, da sie keine Vorhersage- oder Gruppierungsaufgabe erfüllt, sondern neue Inhalte erstellt.
	
- Sie nutzt tiefe neuronale Netze, insbesondere GANs, Transformer-Modelle und Diffusionsmodelle.
	
- Generative KI wird zunehmend wichtiger in Bereichen wie Kunst, Design, Code, Audio und Sprache.
-------

**VI. Vergleich der ML-Aufgabentypen**

.. list-table:: Vergleich von Regression, Klassifikation, Clustering und autonomen Aufgaben
   :header-rows: 1

   * - Merkmal
     - Regression
     - Klassifikation
     - Clustering
     - Autonome Aufgaben
     - Generative Aufgaben
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

---

**Fazit**

- Regression, Klassifikation und Clustering gehören zu den klassischen Aufgaben des maschinellen Lernens.

- Autonome Systeme sind eine anspruchsvolle Anwendung, die verschiedene ML-Techniken kombiniert.

- Je nach Daten und Zielsetzung kann eine Kombination dieser Methoden sinnvoll sein.



Kapitel 4: Trainingsdaten und Modellierung
------------------------------------------

**Datenqualität und ihre Bedeutung**

- Gute Trainingsdaten sind essenziell für die Leistungsfähigkeit eines Modells.

- Aspekte der Datenqualität:

  - **Vollständigkeit:** Fehlende Werte können Modelle ungenau machen.

  - **Konsistenz:** Daten sollten einheitlich und korrekt sein.

  - **Ausreißererkennung:** Extreme Werte können Modelle verzerren.

  - **Datenverteilung:** Unausgewogene Datensätze (z. B. ungleich verteilte Klassen) beeinflussen Modellentscheidungen.

**Feature Engineering**

- Feature Engineering ist die Kunst, relevante Eingangsvariablen für ein Modell zu erstellen.

Beispiel: Cohorte (Generation) vs. Alters-cohorte (https://de.wikipedia.org/wiki/Kohorte_(Sozialwissenschaft))

- Typische Techniken:

  - **Feature Skalierung:** Normalisierung und Standardisierung von Daten (z. B. Min-Max-Scaling, Z-Score-Normalisierung).

  - **Feature Selektion:** Auswahl der wichtigsten Merkmale zur Reduktion von Overfitting.

  - **Feature Transformation:** Anwendung von Logarithmus- oder Polynom-Transformationen zur Verbesserung der Modellleistung.

  - **One-Hot-Encoding:** Umwandlung kategorialer Variablen in numerische Werte.

**Modelltraining und Optimierung**

- Schritte des Modelltrainings:

  1. **Datenaufteilung:** Aufteilung in Trainings-, Validierungs- und Testdatensätze.

  2. **Modellauswahl:** Auswahl eines geeigneten Algorithmus (z. B. Entscheidungsbaum, Random Forest, neuronale Netze).

  3. **Hyperparameter-Tuning:** Feinabstimmung der Modellparameter zur Optimierung der Leistung (z. B. Grid Search, Random Search).

  4. **Modellbewertung:** Verwendung von Metriken wie Genauigkeit, F1-Score oder Mean Squared Error zur Bewertung der Vorhersagequalität.

  5. **Modellbereitstellung:** Einsatz des trainierten Modells in einer produktiven Umgebung.

**Praxisbeispiel: Modelltraining in Python**

- Implementierung eines einfachen ML-Modells mit scikit-learn zur Vorhersage von Hauspreisen.

- Demonstration von Datenvorbereitung, Feature Engineering und Modelltraining.


Kapitel 5: Evaluation von ML-Modellen
--------------------------------------

**Warum ist die Modellbewertung wichtig?**

- Die Evaluation von ML-Modellen stellt sicher, dass das Modell zuverlässig und generalisierbar ist.

- Ein gut evaluiertes Modell verhindert Overfitting und hilft, die besten Algorithmen und Parameter auszuwählen.

**Wichtige Metriken für Klassifikationsprobleme**
1. **Accuracy (Genauigkeit):**

Prozentsatz der korrekten Vorhersagen.

Formel: 

.. math::     
     \text{Accuracy} = \frac{\text{Anzahl der korrekten Vorhersagen}}{\text{Gesamtanzahl der Vorhersagen}}

ACHTUNG! Accuracy hat eine Einschränkung bei (stark) unausgewogenen Datensätzen, da sie hier irreführend sein kann.

2. **Precision (Präzision):**

Precision ist der Anteil der tatsächlich positiven Vorhersagen unter allen als positiv klassifizierten Instanzen.

Die Formel hierfür lautet:

.. math::
     \text{Precision} = \frac{TP}{TP + FP}
   
Precision wird vor allem bevorzugt, wenn falsch-positive Fehler besonders kritisch sind (z. B. Spam-Erkennung).

3. **Recall (Sensitivität):**

Recall ist der Anteil der korrekten positiven Vorhersagen unter allen tatsächlichen positiven Fällen.

Die Formel hierfür lautet:

.. math::
     \text{Recall} = \frac{TP}{TP + FN}
   
Recall ist eine wichtige Metrik, wenn es entscheidend ist, möglichst alle positiven Fälle zu erfassen (z. B. Krebsdiagnosen).

4. **F1-Score:**

Der F1-Score ist Harmonic Mean von Präzision und Recall, um ein ausgewogenes Maß zu erhalten.

Die Formel dafür lautet:

.. math:: 
  \text{F1-Score} = 2 \times \frac{\text{Precision} \times \text{Recall}}{\text{Precision} + \text{Recall}}
   
Der F1-Score ist besonders nützlich bei unausgewogenen Datensätzen (unbiased data sets).

**Wichtige Metriken für Regressionsprobleme**

1. **Mean Squared Error, MSE (Mittlerer quadratischer Fehler):**

Der MSE berechnet den Durchschnitt der quadrierten Fehler zwischen vorhergesagten und tatsächlichen Werten.

Die Formel dafür lautet:

.. math:: 
  \text{MSE} = \frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2 

Somit bestraft der MSE große Fehler stärker als kleine Fehler.

2. **Mean Absolute Error, MAE (Mittlerer absoluter Fehler):**

Der MAE berechnet den Durchschnitt der absoluten Differenzen zwischen vorhergesagten und tatsächlichen Werten.

Die Formel dafür lautet: 

.. math:: 
    \text{MAE} = \frac{1}{n} \sum_{i=1}^{n} |y_i - \hat{y}_i|


3. **R²-Koeffizient (Bestimmtheitsmaß):**

   - Zeigt, wie gut das Modell die Varianz der Zielvariable erklärt.

   - Wertebereich: 0 (keine Erklärung) bis 1 (perfekte Erklärung).

**Praktische Anwendung: Evaluierung eines Modells in Python**

Ein Beispiel zur Berechnung dieser Metriken mit `scikit-learn`:

.. py:function:: python:

  from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

  # Beispiel: Tatsächliche Labels und Vorhersagen

  true_labels = [1, 0, 1, 1, 0, 1, 0, 0, 1, 0]
  
  predicted_labels = [1, 0, 1, 0, 0, 1, 0, 1, 1, 0]

  # Berechnung der Metriken

  accuracy = accuracy_score(true_labels, predicted_labels)
  
  precision = precision_score(true_labels, predicted_labels)
  
  recall = recall_score(true_labels, predicted_labels)
  
  f1 = f1_score(true_labels, predicted_labels)

  print(f'Accuracy: {accuracy}, Precision: {precision}, Recall: {recall}, F1-Score: {f1}')
  
  return (accuracy, precision, recall, f1)


Kapitel 6: Praktische Einführung: Lineare Regression
-----------------------------------------------------

**Was ist Lineare Regression?**

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

**Schritte zur Implementierung eines ML-Modells mit scikit-learn**

1. **Daten laden und vorbereiten**

   - Import von Bibliotheken und Laden eines Datensatzes.

   - Aufteilung der Daten in Trainings- und Testsets.

2. **Modell erstellen und trainieren**

   - Ein Lineares Regressionsmodell aus `scikit-learn` erstellen und trainieren.

3. **Modell evaluieren**

   - Vorhersagen treffen und mit Metriken wie dem mittleren quadratischen Fehler (MSE) bewerten.

**Code-Beispiel: siehe unten**


Kapitel 7: Fallstudie: Vorhersage von Immobilienpreisen
--------------------------------------------------------

**Ziel dieser Fallstudie**

- Anwendung der erlernten Methoden zur Vorhersage von Immobilienpreisen.

- Verwendung eines realen Datensatzes zur Modellierung.

- Umsetzung in Python mit `scikit-learn`.

**Schritte zur Umsetzung**

1. **Daten laden und verstehen**

   - Nutzung eines offenen Datensatzes (z. B. `Boston Housing Dataset` oder `Kaggle Immobilienpreise`).

   - Untersuchung der Datenverteilung, Korrelationen und möglicher Ausreißer.

2. **Datenvorbereitung**

   - Umwandlung kategorischer Merkmale (One-Hot-Encoding).

   - Normalisierung und Skalierung numerischer Merkmale.

   - Aufteilung in Trainings- und Testdaten.

3. **Modelltraining mit Lineare Regression**

   - Trainieren eines **Linearen Regressionsmodells** mit `scikit-learn`.

   - Verwendung von Metriken zur Bewertung der Modellgüte (z. B. MSE, R²).

4. **Modellbewertung und Interpretation**

   - Bewertung der Modellperformance auf dem Testdatensatz.

   - Interpretation der wichtigsten Einflussgrößen.

**Code-Beispiel: Vorhersage von Immobilienpreisen**

.. code-block:: python

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
   df['PRICE'] = boston.target

   # Aufteilung in Merkmale (X) und Zielvariable (y)
   X = df.drop('PRICE', axis=1)
   y = df['PRICE']

   # Aufteilung in Trainings- und Testsets
   X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

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
   print(f'Mittlerer quadratischer Fehler (MSE): {mse}')
   print(f'Bestimmtheitsmaß (R²): {r2}')

   # Visualisierung der Vorhersagen
   plt.scatter(y_test, y_pred, alpha=0.7)
   plt.xlabel('Tatsächliche Preise')
   plt.ylabel('Vorhergesagte Preise')
   plt.title('Tatsächliche vs. Vorhergesagte Immobilienpreise')
   plt.show()

**Erklärung des Codes:**

- **Datensatz laden:** Wir verwenden das `Boston Housing Dataset`, das verschiedene Merkmale von Häusern enthält.

- **Datenvorverarbeitung:** Skalierung der numerischen Variablen zur besseren Modellleistung.

- **Modelltraining:** Wir verwenden eine einfache lineare Regression.

- **Modellbewertung:** Berechnung des mittleren quadratischen Fehlers (MSE) und des Bestimmtheitsmaßes (R²).

- **Visualisierung:** Darstellung der tatsächlichen vs. vorhergesagten Werte zur Überprüfung der Modellgüte.


Kapitel 8: Diskussion und Fragen
---------------------------------

**Ziel der Diskussion**

- Reflexion der erlernten Inhalte und Beantwortung offener Fragen.

- Gemeinsamer Austausch über die praktische Anwendbarkeit von KI in verschiedenen Branchen.

**Diskussion über Anwendungen von KI in verschiedenen Bereichen**

1. **Gesundheitswesen**

   - Einsatz von KI für medizinische Diagnosen (z. B. Krebsfrüherkennung mittels Bildverarbeitung).

   - Personalisierte Medizin basierend auf Patientendaten.

   - Automatisierte Medikamentenentwicklung und klinische Studienoptimierung.

2. **Finanzwesen**

   - Algorithmischer Handel und automatisierte Investitionsstrategien.

   - Betrugserkennung in Echtzeit durch Anomalieerkennung.

   - Risikoanalysen für Kreditbewilligungen.

3. **Industrie und Fertigung**

   - Predictive Maintenance (vorausschauende Wartung von Maschinen).

   - Automatisierung in der Fertigung mit KI-gesteuerten Robotern.

   - Optimierung von Lieferketten durch intelligente Planungssysteme.

4. **Mobilität und Transport**

   - Autonome Fahrzeuge und intelligente Verkehrssteuerung.

   - KI-gestützte Routenoptimierung für Logistikunternehmen.

   - Fahrgastprognosen im öffentlichen Verkehr.

5. **E-Commerce und Marketing**

   - Personalisierte Produktempfehlungen (z. B. Amazon, Netflix).

   - Chatbots für Kundenservice und automatisierte Bestellprozesse.

   - Dynamische Preisgestaltung durch KI-Analyse von Markttrends.

6. **Recht und Verwaltung**

   - Automatisierte Vertragsanalyse und Dokumentenprüfung.

   - KI zur Unterstützung juristischer Entscheidungen.

   - Öffentliche Verwaltung und KI-gestützte Bürgerdienste.

**Offene Diskussion und Fragen**

- Welche KI-Technologien haben das größte Potenzial für die Zukunft?

- Welche Herausforderungen und ethischen Bedenken gibt es in den jeweiligen Bereichen?

- Wie kann KI für nachhaltige Entwicklungen genutzt werden?


Zusätzliche Materialien
-----------------------
- Einführung in `Scikit-Learn <https://scikit-learn.org/stable/>`_
- NumPy- und Pandas-Dokumentation für Datenverarbeitung
- Matplotlib für Visualisierung
- TensorFlow/Keras für Deep Learning (für spätere Module)


