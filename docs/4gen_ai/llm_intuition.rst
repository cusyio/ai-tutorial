LLM-Intuition: Was macht ein Sprachmodell?
==========================================

In diesem Kapitel geht es darum, **ohne Formeln** zu verstehen, was ein Large Language Model (LLM) eigentlich tut.

Die zentrale Idee
-----------------

Stellen wir uns vor: Wir lesen einen Satz und sollen das nächste Wort ergänzen – z. B. „Der Himmel ist …“. Wir wählen ein Wort, das **in den Kontext passt** (z. B. „blau“, „bewölkt“). Ein LLM macht im Kern genau das: Es sagt auf Basis des bisherigen Textes das **nächste Wort** (bzw. die nächste Einheit, den *Token*) vorher.

.. code-block:: text

   Eingabe:  "Maschinelles Lernen ist …"
   Modell:   wahrscheinlich "ein" oder "eine" oder "die" … (nächster Token)

Das Modell hat aus riesigen Textmengen gelernt, welche Fortsetzungen typisch sind. Es „versteht“ den Text nicht im menschlichen Sinne, aber es erfasst **statistische Muster** und Kontext.

Warum „groß“ (Large)?
---------------------

Je mehr Parameter und Trainingsdaten ein solches Modell hat, desto besser kann es längere und komplexere Abhängigkeiten nutzen – daher „Large“ Language Model. Für die Intuition reicht: Das Modell ist im Wesentlichen ein **Vorhersagegerät für den nächsten Token**.

Beispiele bekannter LLMs (Praxis)
---------------------------------

Genau dieses Prinzip steckt hinter den Modellen, die aus Produkten und Schlagzeilen bekannt sind:

* **ChatGPT** (OpenAI) – baut auf Modellen wie GPT-3.5 und GPT-4 auf; Next-Token-Prediction in der Breite nutzbar.
* **Claude** (Anthropic) – ebenfalls ein autoregressives Sprachmodell, z. B. für Assistenten und lange Kontexte.
* **Gemini** (Google) – multimodales Modell mit starkem Fokus auf Text und Code; gleiche Grundidee: nächsten Token vorhersagen.
* **Llama** (Meta) – Open-Weight-Modellreihe, oft für Forschung, lokale Installationen und angepasste Anwendungen.
* **DeepSeek** (DeepSeek AI) – leistungsstarkes Modell u. a. für Code und Reasoning; Beispiel eines Anbieters außerhalb der „Big Tech“-Runde.

Alle diese Systeme sind im Kern **Sprachmodelle**, die aus Kontext den nächsten Token erzeugen – nur Größe, Training und Produkteinbettung unterscheiden sie.

Von der Vorhersage zum generierten Text
---------------------------------------

* Wir geben einen **Prompt** ein (z. B. eine Frage oder einen Anweisungstext).
* Das Modell erzeugt Token für Token den **nächsten** Token.
* Dieser wird wieder zur Eingabe hinzugefügt, und so weiter – bis eine Antwort oder ein Abschluss entsteht.

So entstehen ganze Sätze oder Absätze. Die Qualität hängt stark vom **Prompt** und von der **Kontextlänge** (wie viel vorheriger Text das Modell „sehen“ darf) ab.

Wichtige Begriffe (kurz)
-------------------------

* **Token:** Die kleinste Einheit, die das Modell verarbeitet (oft Teilwörter, nicht immer ganze Wörter).
* **Prompt:** Der Text, den wir dem Modell als Eingabe geben.
* **Kontext / Context Length:** Der Bereich des bisherigen Textes, den das Modell bei der Vorhersage berücksichtigt.

Diese Begriffe werden in den folgenden Kapiteln (Tokenisierung, Prompt-Engineering) vertieft.

Nächster Schritt
----------------

Als Nächstes geht es um **Tokens und Tokenisierung** (:doc:`tokenization`): Wie aus Text die Einheiten werden, die das Modell verarbeitet.
