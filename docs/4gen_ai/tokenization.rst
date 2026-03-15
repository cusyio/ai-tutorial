Tokens und Tokenisierung
=========================

**Recap:** Ein LLM sagt den **nächsten Token** vorher – es arbeitet also mit diskreten Einheiten, nicht mit Rohtext. **Warum dieses Kapitel:** Damit das Modell überhaupt rechnen kann, muss Text in diese Einheiten (Tokens) zerlegt und in Zahlen (IDs) abgebildet werden. Dieses Kapitel erklärt die Idee und zeigt einfache Beispiele.

Warum nicht einfach Wörter?
----------------------------

Modelle arbeiten mit Zahlen, nicht mit Buchstaben. Außerdem sind „Wörter“ in verschiedenen Sprachen und Schreibweisen uneinheitlich. Daher führt man eine **Tokenisierung** ein: Der Text wird in feste Einheiten (Tokens) aufgeteilt, die dann in Zahlen (IDs) umgewandelt werden.

Was ist ein Token?
------------------

Ein **Token** kann sein:

* ein ganzes Wort (z. B. „Haus“),
* ein Teil eines Wortes (z. B. „Lern“, „ung“),
* ein Zeichen oder ein Sonderzeichen.

Die genaue Aufteilung hängt vom **Tokenizer** ab (z. B. BPE, WordPiece). Wichtig: Ein Token ist **nicht** immer ein Wort – „Tokenisierung“ könnte z. B. in „Token“, „is“, „ier“, „ung“ zerlegt werden.

Beispiel (konzeptionell)
------------------------

.. code-block:: text

   Text:     "Einführung in KI"
   Tokens:   ["Einführung", " in", " KI"]   (vereinfacht; je nach Tokenizer anders)
   IDs:      [1234, 56, 789]                (Beispielzahlen)

Das Modell arbeitet mit den IDs; der Tokenizer übersetzt hin und her.

Warum ist das relevant?
--------------------------------

* **Kontextlänge** wird in Token gemessen – nicht in Zeichen oder Wörtern. Eine „Context Length“ von 4096 bedeutet 4096 Tokens.
* **Kosten** bei API-Modellen werden oft pro Token abgerechnet.
* **Chunking** bei RAG: Dokumente werden sinnvoll in Token-Größen zerlegt; die Tokenisierung hilft, Grenzen zu setzen.

Kontextlängen in der Praxis (Beispiele)
---------------------------------------

Verschiedene Anbieter und Modelle unterstützen unterschiedlich große Kontextfenster. Zur Einordnung ein Überblick bekannter Modelle (Stand grob 2024/2025; Werte können sich mit neuen Versionen ändern):

* **OpenAI:** ChatGPT 3.5 (z. B. 4K bzw. 16K Token bei Turbo-Varianten), GPT-4 (8K/32K), GPT-4o (128K Token) – längere Kontexte erlauben z. B. ganze Dokumente oder lange Chatverläufe.
* **Anthropic:** Claude 3 (z. B. 100K Token), Claude 3.5 Sonnet/Opus (bis 200K Token) – genutzt für Analyse langer Texte und RAG-Anwendungen.
* **Google:** Gemini 1.5 Pro bzw. 2.0 (z. B. 1 Mio. Token und mehr) – sehr große Kontexte für Dokumenten- und Code-Analysen.
* **DeepSeek:** DeepSeek V3 / R1 (Reasoning) mit z. B. 64K–128K Token – Beispiel eines leistungsstarken Modells eines anderen Anbieters.
* **Meta:** Llama 3 (z. B. 8K–128K je nach Variante) – oft als Basis für lokale oder angepasste Lösungen genutzt.

An solchen Werten wird klar: Kontextlänge ist ein zentrales Leistungsmerkmal; sie begrenzt, wie viel Vorwissen und wie lange Dokumente das Modell „auf einmal“ berücksichtigen kann.

Einfaches Beispiel mit Python
------------------------------

Mit der Bibliothek ``tiktoken`` (z. B. für OpenAI-Modelle) lassen sich Texte tokenisieren, **ohne** ein Modell aufzurufen:

.. code-block:: python

   import tiktoken

   enc = tiktoken.get_encoding("cl100k_base")  # z. B. GPT-4
   text = "Einführung in die Tokenisierung."
   tokens = enc.encode(text)
   print("Anzahl Token:", len(tokens))
   print("Token-IDs:", tokens)
   # Dekodierung zurück zu Text:
   print(enc.decode(tokens))

Ähnliche Funktionen bieten andere Bibliotheken (z. B. ``transformers`` mit ``AutoTokenizer``) für verschiedene Modelle.

Kurz zusammengefasst
--------------------

* Text wird durch einen **Tokenizer** in **Tokens** zerlegt und in **IDs** abgebildet.
* Tokens sind nicht immer ganze Wörter; die Länge von Kontext und Kosten wird in Token gezählt.
* Für RAG und Prompt-Engineering ist es hilfreich, ungefähr zu wissen, wie viele Tokens ein Text hat.

Nächster Schritt
----------------

Tokens und Kontextlänge sind die technische Basis. Damit das Modell die **gewünschte Art** von Antwort liefert, müssen wir die Eingabe gezielt formulieren. Im Kapitel **Prompting und Prompt-Engineering** (:doc:`prompt_engineering`) geht es darum, wie wir Fragen und Anweisungen so formulieren, dass das Modell die gewünschte Antwort liefert – und wo die Grenzen liegen (z. B. wann wir RAG brauchen).
