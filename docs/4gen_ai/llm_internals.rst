LLM-Interna (optional): Konzepte der Transformer-Architektur
=============================================================

Dieses Kapitel ist **optional** und richtet sich an alle, die verstehen möchten, *wie* ein Transformer-Modell grob aufgebaut ist. Es geht um **Konzepte und ausgewählte Bausteine** – **nicht** um eine vollständige Implementierung eines Modells wie microGPT oder eines kompletten Transformers.

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
   token_ids = [12, 45, 78]   # Beispiel-IDs
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

Die mathematischen Details und die Formeln finden Sie in der **Theorie hinter Generativer KI** (:doc:`genai_theory`).

Multi-Head-Attention
--------------------

Statt nur einer Attention-Berechnung gibt es mehrere „Köpfe“ (Heads), die parallel verschiedene Aspekte der Beziehungen zwischen Tokens erfassen. Die Ausgaben der Köpfe werden zusammengeführt und weiterverarbeitet.

Decoder-only und Next-Token-Prediction
--------------------------------------

Moderne LLMs wie GPT sind **decoder-only**: Sie verarbeiten den Text von links nach rechts und nutzen **masked** (causale) Attention – jede Position darf nur auf vorherige Positionen schauen. So wird Schritt für Schritt das **nächste Token** vorhergesagt; daraus entsteht die Generierung.

Keine Vollimplementierung hier
------------------------------

Eine vollständige Implementierung eines kleinen Sprachmodells (z. B. im Stil von Karpathys nanoGPT/microGPT) würde den Rahmen dieses Kurses sprengen. Interessierte können sich an folgenden Ressourcen orientieren:

* **nanoGPT / microGPT** (Karpathy): Kleine, gut dokumentierte Implementierungen zum Selbststudium.
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
