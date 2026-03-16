microGPT-Walkthrough: Wie ein minimales GPT funktioniert (optional)
====================================================================

Dieses Kapitel ist eine **optionale Vertiefung** für alle, die sehen möchten, wie ein **minimales GPT-ähnliches Modell** (im Stil von Andrej Karpathys minGPT/nanoGPT) grob aufgebaut ist. Es geht um **Konzepte und ausgewählte Code-Ausschnitte** – **keine** vollständige Implementierung. Nach dem Lesen versteht man die Schritte: Text → Tokens → Token-Embeddings → Transformer-Blöcke → Next-Token-Prediction.

Ziel und Vorwissen
------------------

* **Ziel:** Die zentralen Bausteine eines kleinen decoder-only Sprachmodells erkennen (Embedding, Attention, LM-Head) und in echtem Code wiederfinden.
* **Vorwissen:** Die Kapitel **LLM-Intuition**, **Tokenisierung** und **LLM-Interna** liefern die konzeptionelle Basis; hier geht es um den **Ablauf in Code**.

Hinweis: Eine vollständige, lauffähige Implementierung würde den Rahmen sprengen. Interessierte können Karpathys `nanoGPT`-Repository studieren; hier werden nur **Schlüsselstellen** hervorgehoben.

Überblick: Vom Text zum nächsten Token
--------------------------------------

Ein minimales GPT durchläuft grob diese Schritte:

.. code-block:: text

   Text  →  Token-IDs  →  Token-Embeddings  →  Transformer-Blöcke  →  Logits  →  nächster Token

Im Folgenden gehen wir jeden Schritt mit Intuition und ausgewählten Code-Fragmenten an.

Schritt 1: Text → Tokens (Tokenisierung)
----------------------------------------

**Intuition:** Der Rohtext wird in eine Folge von **Token-IDs** zerlegt (siehe :doc:`tokenization`). Das Modell arbeitet nur mit Zahlen.

**Typischer Code (konzeptionell):** Ein Tokenizer liefert eine Liste von IDs.

.. code-block:: python

   # Pseudocode / vereinfacht – z. B. mit tiktoken oder Hugging Face Tokenizer
   tokenizer = load_tokenizer("gpt2")  # oder ein anderer
   text = "Das Modell sagt das nächste"
   token_ids = tokenizer.encode(text)  # z. B. [1234, 567, 890, 234, 567]

Diese ``token_ids`` sind die Eingabe für das Modell.

Schritt 2: Token-Embeddings
----------------------------

**Intuition:** Jede Token-ID wird in einen **Vektor** (Embedding) einer festen Dimension übersetzt. So wird aus der diskreten ID eine kontinuierliche Darstellung, mit der das Netz rechnen kann.

**Typischer Code (PyTorch-Stil):** Ein eingebautes Embedding-Layer.

.. code-block:: python

   import torch.nn as nn

   # vocab_size = Größe des Wortschatzes, n_embd = Embedding-Dimension (z. B. 768)
   self.token_embedding_table = nn.Embedding(vocab_size, n_embd)
   # Eingabe: (batch, seq_len) → Ausgabe: (batch, seq_len, n_embd)
   tok_emb = self.token_embedding_table(token_ids)

Zusätzlich braucht das Modell **Positionsinformationen**, weil der Transformer von sich aus keine Reihenfolge kennt (siehe :doc:`llm_internals`). Oft ein weiteres Embedding-Layer für Positionen:

.. code-block:: python

   self.position_embedding_table = nn.Embedding(block_size, n_embd)
   pos_emb = self.position_embedding_table(torch.arange(seq_len))
   x = tok_emb + pos_emb  # (batch, seq_len, n_embd)
   # x geht in die Transformer-Blöcke
   return x

Schritt 3: Transformer-Blöcke (Attention + MLP)
------------------------------------------------

**Intuition:** Die eingebettete Folge durchläuft mehrere **Decoder-Blöcke**. Jeder Block enthält typischerweise:

* **Causale (masked) Self-Attention:** Jede Position darf nur auf **vorherige** Positionen (und sich selbst) schauen – so entsteht die autoregressive „von links nach rechts“-Struktur.
* **Feed-Forward (MLP):** Eine kleine zweilagige Netzwerk-Schicht pro Position.

Die Details (Query, Key, Value, Multi-Head) stehen in :doc:`llm_internals` und :doc:`genai_theory`. Hier nur eine **Struktur** als Orientierung:

.. code-block:: python

   class Block(nn.Module):
       def __init__(self, n_embd, n_head, ...):
           super().__init__()
           self.sa = CausalSelfAttention(...)   # masked, decoder-only
           self.ffwd = nn.Sequential(
               nn.Linear(n_embd, 4 * n_embd),
               nn.GELU(),
               nn.Linear(4 * n_embd, n_embd),
           )
       def forward(self, x):
           x = x + self.sa(x)   # Residual
           x = x + self.ffwd(x)
           return x

Die Eingabe ``x`` hat die Form ``(batch, seq_len, n_embd)``; nach allen Blöcken hat sie dieselbe Form.

Schritt 4: Vom letzten versteckten Zustand zu Logits (LM-Head)
--------------------------------------------------------------

**Intuition:** Am Ende der Blöcke haben wir pro Position einen Vektor der Dimension ``n_embd``. Das Modell soll aber **eine Wahrscheinlichkeit pro Token im Wortschatz** ausgeben – also „welcher Token kommt als Nächstes?“ Dafür wird die letzte Position (oder der letzte versteckte Zustand) durch eine lineare Schicht auf ``vocab_size`` viele Logits abgebildet.

.. code-block:: python

   self.lm_head = nn.Linear(n_embd, vocab_size, bias=False)
   logits = self.lm_head(x[:, -1, :])  # nur letzte Position: (batch, vocab_size)
   # logits[i] = „Score“ für Token i als nächstes Token
   probs = F.softmax(logits, dim=-1)
   next_token_id = torch.argmax(probs, dim=-1)  # oder Sampling aus probs
   return logits, next_token_id

**Next-Token-Prediction:** Beim Training vergleichen wir ``logits`` mit dem tatsächlich nächsten Token (Cross-Entropy-Verlust). Beim Generieren wählen wir den nächsten Token (argmax oder Sampling), hängen ihn an die Eingabe an und wiederholen – so entsteht Token für Token der generierte Text.

Zusammenfassung der Datenfluss-Kette
------------------------------------

.. code-block:: text

   Text
     → Tokenizer: token_ids (batch, seq_len)
     → token_embedding_table: (batch, seq_len, n_embd)
     → + position_embedding
     → N × Block(Attention + MLP): (batch, seq_len, n_embd)
     → lm_head auf letzte Position: (batch, vocab_size) = Logits
     → softmax → Wahrscheinlichkeiten → nächster Token (argmax oder Sampling)
     → Anhängen an Eingabe, wiederholen → generierter Text

Warum „minimal“?
----------------

Ein **vollständiges** GPT enthält zusätzlich: Layer-Norm, mehrere Köpfe in der Attention, Dropout, korrekte Maskierung, Tokenizer-Details, Training-Loop, Lernraten-Scheduling usw. Hier sollten nur die **konzeptionellen Kerne** sichtbar werden – Embedding, Block-Struktur, LM-Head und Next-Token-Prediction.

Weiterführende Ressourcen
-------------------------

* **nanoGPT (Karpathy):** Kleine, gut lesbare Implementierung auf GitHub – ideal zum Selbststudium und zum Nachvollziehen jeder Zeile.
* **LLM-Interna** (:doc:`llm_internals`): Konzepte von Attention und Decoder-only ohne Code-Tiefgang.
* **Theorie hinter Generativer KI** (:doc:`genai_theory`): Mathematische Details zu Attention und Optimierung.

Nächster Schritt
----------------

Wer die **mathematische** Seite (Attention-Formeln, Wahrscheinlichkeitsmodell) vertiefen möchte, findet sie in :doc:`genai_theory`. Für die **Nutzung** von LLMs in Produkten reicht das hier Gelernte zusammen mit dem Rest des GenAI-Lernpfads (Embeddings, RAG, Prompting).
