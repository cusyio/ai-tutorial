Semantische Ähnlichkeit: Vektoren vergleichen
=============================================

Im Kapitel **Embeddings** haben wir Texte in Vektoren übersetzt – zwei inhaltlich ähnliche Texte liegen im Vektorraum nah beieinander. Damit daraus **Suche** und später **RAG** werden können, brauchen wir ein klares Kriterium: **Wann sind zwei Vektoren „ähnlich“?** Dieses Kapitel erklärt die Idee mit Intuition zuerst, dann ein Maß (Kosinusähnlichkeit) und warum genau das die Brücke zu semantischer Suche schlägt.

Recap: Wozu brauchen wir das?
-----------------------------

* **Bisher:** Wir haben Text in **Embeddings** (Vektoren fester Länge) umgewandelt. Ähnliche Bedeutung → ähnliche Vektoren.
* **Jetzt:** Wir brauchen eine **Zahl**, die sagt, wie ähnlich zwei Vektoren sind – damit wir z. B. die „nächsten“ Dokumente zu einer Frage finden können.
* **Später:** In **Semantische Suche** nutzen wir genau dieses Maß, um aus vielen Chunks die relevantesten auszuwählen; daraus entsteht **Retrieval** und dann **RAG**.

Intuition: Nähe im Raum
-----------------------

Stellen wir uns zwei Vektoren als **Pfeile** im Raum vor (in der Praxis haben sie z. B. 384 oder 768 Dimensionen, die Idee bleibt gleich). Zwei Texte mit ähnlicher Bedeutung sollen „nah“ beieinander liegen. Was heißt „nah“?

* **Option 1 – Abstand:** Je kürzer der Abstand zwischen den Spitzen der Pfeile, desto ähnlicher. Das funktioniert, aber die **Länge** der Vektoren kann stören: Ein langer und ein kurzer Vektor können inhaltlich gleich ausgerichtet sein; der Abstand wäre trotzdem groß.
* **Option 2 – Richtung:** Wir ignorieren die Länge und schauen auf die **Richtung**. Zwei Vektoren, die in die gleiche Richtung zeigen, sind „ähnlich“ – unabhängig davon, ob sie lang oder kurz sind.

Für Texte und Embeddings ist die **Richtung** meist aussagekräftiger als der reine Abstand. Das führt direkt zum **Kosinus**.

Kosinusähnlichkeit (Intuition)
------------------------------

Der **Winkel** zwischen zwei Vektoren beschreibt, ob sie in die gleiche Richtung zeigen (Winkel 0°), senkrecht stehen (90°) oder entgegengesetzt sind (180°). Der **Kosinus** dieses Winkels liefert eine einfache Zahl:

* **cos ≈ 1:** Vektoren zeigen in die gleiche Richtung → sehr ähnlich.
* **cos ≈ 0:** Vektoren stehen senkrecht → unabhängig / nicht ähnlich.
* **cos ≈ -1:** Vektoren zeigen entgegengesetzt → sehr unähnlich.

Bei typischen Embedding-Modellen liegen die Werte oft zwischen 0 und 1; negative Werte sind möglich, aber seltener. **Größerer Kosinus = ähnlicher.**

Beispiel (konzeptionell)
------------------------

.. code-block:: text

   Frage:     "Was ist RAG?"
   Chunk A:   "RAG kombiniert Retrieval mit einem Sprachmodell."
   Chunk B:   "Das Wetter ist heute schön."

   → Embedding von Frage und Chunk A haben hohe Kosinusähnlichkeit.
   → Embedding von Frage und Chunk B haben niedrige Kosinusähnlichkeit.
   → Für semantische Suche sortieren wir Chunks nach dieser Ähnlichkeit und wählen die Top-k.

Formel und Code
---------------

Mathematisch ist die **Kosinusähnlichkeit** das Skalarprodukt der (normierten) Vektoren:

.. code-block:: text

   cos(a, b) = (a · b) / (||a|| · ||b||)

Dabei ist ``a · b`` das Skalarprodukt und ``||a||`` die Länge (Norm) von ``a``. So wird nur die Richtung verglichen.

.. code-block:: python

   import numpy as np


   def cosine_similarity(a, b):
       return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))


   # Beispiel: zwei Vektoren (z. B. aus einem Embedding-Modell)
   vec_frage = np.array([0.1, 0.9, 0.2, ...])  # Embedding der Frage
   vec_chunk = np.array([0.15, 0.85, 0.25, ...])  # Embedding eines Chunks
   score = cosine_similarity(vec_frage, vec_chunk)  # z. B. 0.92 → sehr ähnlich

Warum Embeddings semantische Suche ermöglichen
----------------------------------------------

* **Ohne Embeddings:** Wir könnten nur nach **exakten Wörtern** suchen („RAG“, „Retrieval“). Synonyme oder umschreibende Sätze würden nicht gefunden.
* **Mit Embeddings:** Jeder Text wird zu einem Punkt im gleichen Vektorraum. **Bedeutung** wird durch die Lage erfasst – ähnliche Inhalte liegen nah beieinander.
* **Mit Kosinusähnlichkeit:** Wir haben ein klares, rechnerisch einfaches Maß für „wie ähnlich“. So können wir aus hunderten oder tausenden Chunks die **relevantesten** zur Anfrage auswählen – das ist der Kern von **Retrieval** und damit die Grundlage für **RAG**.

Kurz zusammengefasst
--------------------

* **Vektorähnlichkeit** lässt sich über Richtung (Winkel) messen – unabhängig von der Vektorlänge.
* **Kosinusähnlichkeit** ist dafür das Standardmaß: Werte nahe 1 = ähnlich, nahe 0 = unabhängig.
* Embeddings + Kosinusähnlichkeit sind die **Brücke** von „Text als Vektor“ zu **semantischer Suche** und **RAG**.

Nächster Schritt
----------------

Im Kapitel **Semantische Suche** (:doc:`semantic_search`) setzen wir genau das um: Wir haben einen Korpus aus Chunks, jede Anfrage wird zu einem Vektor, und mit der Kosinusähnlichkeit finden wir die **Top-k** relevanten Chunks – die wir später dem LLM als Kontext für RAG mitgeben.
