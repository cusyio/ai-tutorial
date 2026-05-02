LLM-Interna (optional): Konzepte der Transformer-Architektur
=============================================================

**Recap:** Wir haben den Lernpfad von LLM-Intuition über Tokens, Prompting, Embeddings, semantische Ähnlichkeit, Suche und RAG bis zu den Grenzen von LLMs durchlaufen. **Warum dieses Kapitel (optional):** Wer verstehen möchte, *wie* ein Transformer-Modell grob aufgebaut ist, findet hier die **konzeptionellen Bausteine** – Token-Embedding, Self-Attention, Decoder-only, Next-Token-Prediction. Es geht um **Konzepte und ausgewählte Code-Snippets**, **nicht** um eine vollständige Implementierung. Für einen **Code-orientierten** Gang durch ein minimales GPT siehe :doc:`microgpt_walkthrough`.

Ziel
----

* Die wichtigsten **architektonischen Ideen** kennen: Einbettung von Tokens, Self-Attention, Decoder-only-Generierung.
* **Ausgewählte Code-Snippets** als Illustration sehen – keine komplette Nachimplementierung.

Ausgangspunkt: Token → Vektor
-----------------------------

Jeder Token wird zunächst in einen **Vektor** (Embedding) abgebildet. Diese Einbettung ist gelernt und liegt in einer Lookup-Tabelle (Embedding-Layer).

.. code-block:: python

   # Konzeptionell: Token-IDs werden zu Vektoren der Dimension d_model
   # (In PyTorch z.B.: nn.Embedding(vocab_size, d_model))
   token_ids = [12, 45, 78]  # Beispiel-IDs
   # → Matrix der Form (seq_len, d_model)

Positionen
----------

Da der Transformer keine feste Reihenfolge „sieht“, werden **Positionsinformationen** hinzugefügt (Positional Encodings oder learnable Position Embeddings). So weiß das Modell, an welcher Stelle ein Token steht.

Self-Attention (Kernidee)
-------------------------

**Self-Attention** ermöglicht es, dass jede Position alle anderen Positionen „befragen“ kann: Welche anderen Tokens sind für die aktuelle Position relevant? Dafür werden aus den Eingabevektoren **Query (Q)**, **Key (K)** und **Value (V)** abgeleitet. Die Ähnlichkeit zwischen Queries und Keys steuert, wie stark die Values an jeder Position gewichtet werden.

.. code-block:: text

   Vereinfacht: Attention(Q, K, V) = softmax(Q K^T / sqrt(d)) · V
   → Jede Position erhält einen gewichteten Mix aus allen Value-Vektoren.

Die mathematischen Details und die Formeln stehen in der **Theorie hinter Generativer KI** (:doc:`genai_theory`).

Multi-Head-Attention
--------------------

Statt nur einer Attention-Berechnung gibt es mehrere „Köpfe“ (Heads), die parallel verschiedene Aspekte der Beziehungen zwischen Tokens erfassen. Die Ausgaben der Köpfe werden zusammengeführt und weiterverarbeitet.

Decoder-only und Next-Token-Prediction
--------------------------------------

Moderne LLMs wie GPT sind **decoder-only**: Sie verarbeiten den Text von links nach rechts und nutzen **masked** (causale) Attention – jede Position darf nur auf vorherige Positionen schauen. So wird Schritt für Schritt das **nächste Token** vorhergesagt; daraus entsteht die Generierung.

Keine Vollimplementierung hier
------------------------------

Eine vollständige Implementierung eines kleinen Sprachmodells würde den Rahmen dieses Kurses sprengen. Das Kapitel **microGPT-Walkthrough** (:doc:`microgpt_walkthrough`) zeigt ausgewählte Code-Bausteine (Text→Tokens→Embeddings→Transformer→Next-Token) im Stil von Karpathys minGPT/nanoGPT. Interessierte können sich außerdem an folgenden Ressourcen orientieren:

* **nanoGPT / minGPT** (Karpathy): Kleine, gut dokumentierte Implementierungen zum Selbststudium.
* **Hugging Face Transformers:** Fertige Modelle und Tokenizer; der Fokus hier liegt auf Nutzung und Konzepten, nicht auf dem Nachbau der Architektur.

Theorie vertiefen
-----------------

Die **mathematische und konzeptionelle Vertiefung** – Wahrscheinlichkeitsmodelle, Transformer-Architektur im Detail, Optimierungsalgorithmen – steht im Kapitel **Theorie hinter Generativer KI** (:doc:`genai_theory`). Dort werden u. a. bedingte Wahrscheinlichkeiten, Self-Attention und Optimizer behandelt.

Kurz zusammengefasst
--------------------

* Tokens werden zu Vektoren (Embeddings), Positionen werden kodiert.
* **Self-Attention** und **Multi-Head-Attention** sind die zentralen Bausteine für Kontext.
* **Decoder-only** mit kausaler Attention führt zur Next-Token-Prediction und damit zur Textgenerierung.
* Vollimplementierungen gehören ins Selbststudium; hier standen Konzepte und ausgewählte Snippets im Vordergrund.

Nächster Schritt
----------------

Wer diese Konzepte in **ausgewählten Code-Bausteinen** wiederfinden möchte, findet im **microGPT-Walkthrough** (:doc:`microgpt_walkthrough`) einen Gang durch Text→Tokens→Embeddings→Transformer→Next-Token. Die **Theorie hinter Generativer KI** (:doc:`genai_theory`) liefert die mathematischen Details.
