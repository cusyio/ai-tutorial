Lernpfad: Generative KI und LLMs
================================

Dieser Abschnitt führt durch die Konzepte der **generativen KI** und **Large Language Models (LLMs)** in einer klaren, praxisnahen Reihenfolge. Jedes Kapitel baut auf dem vorherigen auf: Am Ende eines Kapitels steht kurz, *was wir gelernt haben* und *warum das nächste Konzept folgt*.

Konzeptioneller Ablauf
----------------------

Der Lernpfad folgt genau dieser Progression:

.. code-block:: text

   Text  →  Tokens  →  Prompting  →  Embeddings  →  semantische Ähnlichkeit  →  Semantische Suche (Retrieval)  →  RAG  →  Grenzen  →  [optional: LLM-Interna / microGPT]

**Schritt für Schritt:**

1. **Text** – Ausgangspunkt: natürlichsprachliche Eingaben und Dokumente.
2. **Tokens** – LLMs arbeiten mit Einheiten (Tokens), nicht mit Rohtext. Tokenisierung zerlegt Text in diese Einheiten; Kontextlänge und Kosten werden in Token gemessen.
3. **Prompting** – Wie wir dem Modell Eingaben geben (Fragen, Anweisungen, Beispiele), damit es die gewünschte Art von Antwort liefert.
4. **Embeddings** – Texte werden zu Vektoren abgebildet; dadurch wird „Bedeutung“ im gleichen Raum darstellbar und vergleichbar.
5. **Semantische Ähnlichkeit** – Damit aus Vektoren echte **Suche** wird, brauchen wir ein Maß: Wie ähnlich sind zwei Vektoren? Die Kosinusähnlichkeit misst die „Richtung“ und ist die Brücke von Embeddings zur Suche.
6. **Semantische Suche (Retrieval)** – Im Korpus suchen wir die Chunks, deren Embeddings der Anfrage am ähnlichsten sind (Top-k). Das ist **Retrieval** – die Grundlage für RAG.
7. **RAG (Retrieval-Augmented Generation)** – Retrieval + LLM: Relevante Stellen aus den Dokumenten werden ermittelt und dem Modell als Kontext mitgegeben; das Modell antwortet auf Basis dieses Kontexts.
8. **Grenzen und Risiken** – Halluzinationen, Bias, Aktualität, Sicherheit – wichtig für den verantwortungsvollen Einsatz.
9. **Optional: LLM-Interna / microGPT-Walkthrough** – Wie ein Transformer grob aufgebaut ist (Attention, Next-Token-Prediction) bzw. wie ein minimales GPT im Code aussieht; für Interessierte.

Die gleichen Konzepte stecken hinter Produkten wie **ChatGPT**, **Claude**, **Gemini** oder **RAG-Copilots** – hier werden die Bausteine erklärt, die dort genutzt werden.

Hinweis zu den Kapiteln
-----------------------

* Die **Hauptkapitel** (Einführung → LLM-Intuition → Tokens → Prompting → Embeddings → Semantische Ähnlichkeit → Semantische Suche → RAG → Grenzen) bilden den Kern. Jedes Kapitel enthält einen kurzen Recap und leitet zum nächsten über.
* Das **Glossar (LLM-Lingo)** steht als Referenz zur Verfügung – Begriffe können dort jederzeit nachgeschlagen werden.
* **LLM-Interna**, **microGPT-Walkthrough** und **Theorie hinter Generativer KI** sind **optionale Vertiefungen** und erscheinen nach dem Haupt-Lernpfad.

Nächster Schritt
----------------

Weiter mit der **Einführung in Generative KI** (:doc:`genai_intro`) und danach **LLM-Intuition** (:doc:`llm_intuition`).
