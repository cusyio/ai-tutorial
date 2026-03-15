Semantische Suche
==================

**Recap:** Wir haben **Embeddings** (Text als Vektor) und ein Maß für **semantische Ähnlichkeit** (z. B. Kosinusähnlichkeit) – also eine Zahl, die sagt, wie „nah“ zwei Texte im Vektorraum sind. **Warum dieses Kapitel:** Jetzt setzen wir beides ein: **Semantische Suche** bedeutet, in einem Korpus von Dokumenten die Stellen zu finden, die **inhaltlich** zu einer Frage passen – indem wir die Embeddings der Frage mit denen der Chunks vergleichen und die ähnlichsten auswählen (Retrieval). Das ist die Grundlage für **RAG**.

Idee
----

1. Wir haben einen **Korpus** (z. B. FAQs, Handbuchtexte, Schulungsunterlagen).
2. Jeder relevante Abschnitt („Chunk“) wird in einen **Vektor** (Embedding) umgewandelt und gespeichert.
3. Bei einer **Anfrage** wird die Frage ebenfalls in einen Vektor umgewandelt.
4. Wir suchen die Chunks, deren Vektoren der **Anfrage am ähnlichsten** sind – das sind die semantisch relevanten Treffer.

Ähnlichkeitsmaß: Kosinusähnlichkeit
-----------------------------------

Die **Kosinusähnlichkeit** (cosine similarity) misst den Winkel zwischen zwei Vektoren: Werte nahe 1 bedeuten sehr ähnlich, nahe 0 unabhängig, negativ entgegengesetzt. Für Embeddings reicht oft die vereinfachte Idee: **größerer Wert = ähnlicher**.

.. code-block:: python

   import numpy as np

   def cosine_similarity(a, b):
       return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

Bei vielen Chunks berechnen wir die Ähnlichkeit der Anfrage zu jedem Chunk-Vektor und sortieren nach diesem Wert – die Top-k sind die **retrieval**-Ergebnisse.

Ablauf in der Praxis
--------------------

#. **Indexierung (einmalig):** Dokumente in sinnvolle Chunks zerlegen (z. B. nach Absätzen oder fester Token-Anzahl), jeden Chunk embedden und die Vektoren speichern (z. B. in einer Liste oder einer einfachen „Vector Store“-Struktur).
#. **Anfrage:** Nutzerfrage embedden.
#. **Retrieval:** Ähnlichkeit zwischen Anfrage-Vektor und allen Chunk-Vektoren berechnen, Top-k Chunks auswählen.
#. Diese Chunks können dann an ein LLM übergeben werden – das ist der Kern von **RAG**.

Einfacher Vector Store
----------------------

Für Schulungszwecke reicht ein simpler Ansatz: Embeddings in einer Liste oder in NumPy-Arrays halten und bei jeder Anfrage die Ähnlichkeit zu allen Vektoren berechnen. Für große Korpora nutzt man später spezialisierte Lösungen (z. B. FAISS, Chroma, andere Vector-DBs).

Semantische Suche in der Praxis
--------------------------------

Die gleiche Idee – Anfrage und Dokumente in Vektoren abbilden, dann nach Ähnlichkeit sortieren – steckt in vielen Produkten:

* **Suchfunktion in Dokumenten:** z. B. „Suche nach Konzept X“ in Confluence, Notion oder firmeninternen Wikis, die mit Embeddings arbeiten.
* **Support-Chatbots:** Relevante FAQ-Abschnitte oder Handbuchstellen werden zur Nutzerfrage abgerufen (Vorstufe zu RAG).
* **Suchmaschinen mit KI:** Dienste wie Perplexity oder Bing Chat nutzen semantische Komponenten, um Treffer zu ranken oder Kontext für das LLM zu holen.
* **Enterprise Search / Copilots:** Microsoft 365 Copilot, Salesforce Einstein usw. durchsuchen interne Dokumente oft über Embeddings und semantische Nähe.
* **Recherche- und Wissens-Tools:** Verschiedene „AI Research“- oder Dokumenten-Assistenten basieren auf Embedding-Indexen und Top-k-Retrieval.

Damit ist semantische Suche kein reines Laborthema, sondern Alltag in modernen KI-gestützten Anwendungen.

Kurz zusammengefasst
--------------------

* Semantische Suche = Suche nach **Bedeutung**, nicht nur nach exakten Wörtern.
* Dafür: Texte und Anfrage in Embeddings umwandeln, dann Ähnlichkeit (z. B. Kosinus) berechnen und die besten Treffer auswählen.
* Diese Treffer bilden die Grundlage für **RAG**: Kontext für das LLM.

Nächster Schritt
----------------

Retrieval liefert die **relevantesten Chunks** zu einer Frage. Diese Chunks werden dem LLM als **Kontext** mitgegeben – das ist der Kern von **RAG**. Im Kapitel **RAG – Retrieval-Augmented Generation** (:doc:`rag_intro`) wird erklärt, wie Retrieval und LLM zusammenspielen; im Notebook :doc:`rag_practice` lässt sich der Ablauf lokal durchspielen. Danach folgen **Grenzen und Risiken** (:doc:`llm_limitations`) und optional **LLM-Interna** (:doc:`llm_internals`).
