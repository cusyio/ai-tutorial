Lernpfad: Generative KI und LLMs
================================

Dieser Abschnitt führt Sie durch die Konzepte der **generativen KI** und **Large Language Models (LLMs)** in einer klaren, praxisnahen Reihenfolge. Die folgenden Kapitel bauen aufeinander auf.

Konzeptioneller Ablauf
----------------------

Der Lernpfad folgt dieser Progression:

.. code-block:: text

   Text  →  Tokens  →  Embeddings  →  semantische Ähnlichkeit  →  Retrieval  →  RAG  →  [optional: LLM-Interna]

**Kurz erklärt:**

1. **Text** – Ausgangspunkt: natürlichsprachliche Eingaben und Dokumente.
2. **Tokens** – Wie LLMs Text in Einheiten zerlegen (Tokenisierung); Grundlage für alle weiteren Schritte.
3. **Embeddings** – Texte werden zu Vektoren; dadurch wird „Bedeutung“ vergleichbar.
4. **Semantische Ähnlichkeit** – Wie man misst, ob zwei Texte inhaltlich nah beieinander liegen (z. B. Kosinusähnlichkeit).
5. **Retrieval** – Suche in einem Dokumentenkorpus basierend auf Bedeutung (semantische Suche).
6. **RAG (Retrieval-Augmented Generation)** – Kombination aus Retrieval und LLM: relevante Stellen werden ermittelt und dem Modell als Kontext mitgegeben, um fundierte Antworten zu erzeugen.
7. **Optional: LLM-Interna** – Vertiefung, wie ein Transformer-Modell grob aufgebaut ist (Attention, Next-Token-Prediction); für Interessierte.

Die gleichen Konzepte stecken hinter Produkten wie **ChatGPT**, **Claude**, **Gemini** oder **RAG-Copilots** – hier lernen Sie die Bausteine, die dort genutzt werden.

Hinweis zu den Kapiteln
-----------------------

* Die **Hauptkapitel** (von der Einführung bis RAG und Grenzen) bilden den Kern des GenKI-Blocks. Sie können nacheinander durchgearbeitet werden.
* Das **Glossar (LLM-Lingo)** steht als Referenz zur Verfügung – Sie können dort jederzeit Begriffe nachschlagen.
* Die **Transformer-Theorie** und **LLM-Interna** sind als **optionale Vertiefung** gekennzeichnet und erscheinen nach RAG und Grenzen & Risiken.

Nächster Schritt
----------------

Beginnen Sie mit der **Einführung in Generative KI** (:doc:`genai_intro`) und danach mit **LLM-Intuition** (:doc:`llm_intuition`).
