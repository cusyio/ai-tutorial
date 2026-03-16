Embeddings: Text als Vektor
============================

**Recap:** Wir haben gesehen, wie wir dem Modell über **Prompts** Eingaben geben – aber das Modell hat keinen Zugriff auf unsere Dokumente oder Datenbanken. **Warum dieses Kapitel:** Damit wir „ähnliche“ Texte finden können (z. B. welche Dokumentenabschnitte zu einer Frage passen), brauchen wir eine Darstellung von Text, die **Bedeutung** vergleichbar macht. Dafür wird Text in Zahlenvektoren übersetzt – solche Vektoren heißen **Embeddings**. Dieses Kapitel erklärt die Idee und den Nutzen.

Intuition
---------

Stellen wir uns vor: Jeder Satz oder jeder Absatz wird durch einen Punkt in einem hochdimensionalen Raum dargestellt. Zwei Texte mit **ähnlicher Bedeutung** liegen nah beieinander; unterschiedliche Themen liegen weiter auseinander. Ein **Embedding-Modell** erzeugt aus Text genau solche Punkte (Vektoren).

.. code-block:: text

   "Maschinelles Lernen ist ein Teil der KI."
   "KI umfasst unter anderem maschinelles Lernen."
   → Beide erhalten ähnliche Vektoren (nahe im Vektorraum).

Wofür braucht man Embeddings?
------------------------------

* **Semantische Suche:** Dokumente finden, die inhaltlich zu einer Frage passen – auch ohne exakte Wortübereinstimmung.
* **RAG:** Relevante Textstellen aus einem Korpus holen und dem LLM als Kontext mitgeben.
* **Klassifikation, Clustering:** Texte nach Thema gruppieren oder kategorisieren.

Technisch: Ein Modell, eine Funktion
-------------------------------------

Ein **Embedding-Modell** ist eine Funktion (oft ein kleines neuronales Netz), die einen Text (oder eine Liste von Tokens) auf einen Vektor fester Länge abbildet, z. B. 384 oder 768 Dimensionen. Diese Modelle sind oft speziell trainiert, sodass semantisch ähnliche Texte ähnliche Vektoren bekommen.

Lokale Embedding-Modelle
-------------------------

Um **ohne externe API** zu arbeiten, eignen sich lokale Modelle, z. B. über die Bibliothek ``sentence-transformers``:

* Kleine, schnelle Modelle (z. B. ``all-MiniLM-L6-v2``) laufen auf CPU.
* Man gibt Text ein und erhält einen Vektor zurück – ideal für semantische Suche und RAG-Übungen.

Embeddings in der Praxis: Anbieter und Modelle
-----------------------------------------------

Für semantische Suche und RAG werden in der Praxis oft folgende Embedding-Lösungen genutzt (Auswahl, Stand grob 2024/2025):

* **OpenAI:** ``text-embedding-3-small`` / ``text-embedding-3-large`` – über die API; hohe Qualität, Abrechnung pro Token.
* **Cohere:** „embed“-Modelle – häufig für RAG und Suche in Produkten integriert.
* **Google:** Vertex AI Embedding API, z. B. „text-embedding-004“ – in Google-Cloud-Projekten für semantische Suche und RAG.
* **Open Source (lokal):** ``sentence-transformers`` (z. B. ``all-MiniLM-L6-v2``, ``paraphrase-multilingual``) – keine API nötig, gut für Schulungen und datensensible Umgebungen.
* **Weitere Anbieter:** z. B. Mistral Embeddings, Voyage AI – zeigen, dass Embeddings ein zentraler Baustein vieler KI-Stacks sind.

Je nach Anforderung (Kosten, Latenz, Datenschutz, Mehrsprachigkeit) wählt man API oder lokales Modell.

Beispiel (konzeptionell)
------------------------

.. code-block:: python

   from sentence_transformers import SentenceTransformer

   model = SentenceTransformer("all-MiniLM-L6-v2")
   vec = model.encode("Einführung in Embeddings.")
   # vec ist ein Array mit z. B. 384 Zahlen
   print(vec.shape)  # (384,)

Mehrere Sätze auf einmal zu embedden ist effizienter (Batch). Die konkrete Nutzung für **Suche** folgt in den Kapiteln :doc:`semantic_similarity` (Wie messen wir Ähnlichkeit?) und :doc:`semantic_search` (Retrieval im Korpus).

Wichtig
--------

* Embeddings erfassen **semantische Ähnlichkeit**, nicht nur Wortgleichheit.
* Die Dimension (z. B. 384) ist fest; alle Texte werden in denselben Raum abgebildet.
* Für RAG verwenden wir dieselben Embeddings für Fragen und für Dokumenten-Chunks – dann können wir die „nächsten“ Chunks zur Frage finden.

Nächster Schritt
----------------

Embeddings liefern Vektoren – aber **wann** sind zwei Vektoren „ähnlich“? Dafür brauchen wir ein klares Maß (z. B. Kosinusähnlichkeit). Im Kapitel **Semantische Ähnlichkeit** (:doc:`semantic_similarity`) wird erklärt, wie wir Vektorähnlichkeit messen und warum genau das die Brücke zu semantischer Suche und RAG schlägt. Danach folgt **Semantische Suche** (:doc:`semantic_search`) – die konkrete Anwendung: die relevantesten Chunks im Korpus finden.
