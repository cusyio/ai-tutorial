Prompting und Prompt-Engineering
================================

Der **Prompt** ist der Text, den Sie dem LLM als Eingabe geben. Wie Sie ihn formulieren, hat großen Einfluss auf die Antwort. Dieses Kapitel führt in die Grundlagen ein.

Was ist ein Prompt?
-------------------

Ein Prompt kann eine Frage sein („Was ist RAG?“), eine Anweisung („Fasse den folgenden Text in drei Sätzen zusammen“) oder eine Mischung aus Kontext und Aufgabe. Das Modell nutzt diesen Text, um den nächsten Token und damit die gesamte Antwort zu erzeugen.

Intuition: Klarheit hilft
-------------------------

Je klarer und eindeutiger die Aufgabe formuliert ist, desto zuverlässiger ist oft das Ergebnis. Vage Prompts („Erzähl was zu KI“) führen zu allgemeinen Antworten; spezifische Prompts („Erkläre in zwei Sätzen, was Tokenisierung ist“) führen zu fokussierteren Antworten.

Zero-Shot und Few-Shot
----------------------

* **Zero-Shot:** Sie stellen eine Frage oder geben eine Anweisung **ohne** Beispiele. Das Modell antwortet nur aus seiner Trainingserfahrung.
* **Few-Shot:** Sie geben **ein oder mehrere Beispiele** (Eingabe → gewünschte Ausgabe) im Prompt mit. Das Modell orientiert sich an diesem Muster.

Beispiel Few-Shot (konzeptionell):

.. code-block:: text

   Übersetze ins Deutsche:
   Hello → Hallo
   Good morning → Guten Morgen
   Thank you → 

Das Modell wird wahrscheinlich „Danke“ oder ähnlich ergänzen.

System-Prompt und Nutzer-Prompt
-------------------------------

Bei vielen APIs gibt es zwei Rollen:

* **System-Prompt:** Legt die „Rolle“ oder das Verhalten des Assistenten fest (z. B. „Du bist ein sachlicher Helfer. Antworte kurz.“). Der Nutzer sieht ihn oft nicht.
* **Nutzer-Prompt:** Die eigentliche Frage oder Anweisung des Nutzers.

Ein klares System-Prompt hilft, unerwünschtes Verhalten zu reduzieren und den Stil zu steuern.

In der Praxis: Wer nutzt System- und Nutzer-Prompt?
---------------------------------------------------

Die Trennung von System- und Nutzer-Prompt ist in vielen Produkten und APIs Standard:

* **ChatGPT (OpenAI):** Über die API können Sie eine „System-Nachricht“ setzen (z. B. „Du bist ein präziser technischer Redakteur“); die Nutzeranfragen sind die User-Messages.
* **Claude (Anthropic):** Ebenfalls mit System-Prompt konfigurierbar – z. B. für Ton, Format oder Domänen-Rolle.
* **Google Gemini / Vertex AI:** System Instruction und User-Input sind getrennt; ähnlich bei Microsoft Copilot (Azure OpenAI).
* **Llama-basierte Assistenten (z. B. über Ollama):** Viele Oberflächen erlauben einen System-Prompt für das Grundverhalten.
* **Ältere bzw. einfache Chat-APIs:** Teilweise nur ein einziger Prompt; dann muss die „Rolle“ direkt im Nutzertext stehen (z. B. „Du bist … Antworte als …“).

So können Sie Ihr Modell gezielt auf eine Aufgabe oder einen Stil trimmen – unabhängig vom konkreten Anbieter.

Praktische Tipps (kurz)
-----------------------

* **Aufgabe explizit machen:** Statt „Schreib was zu X“ besser „Erkläre X in drei Bulletpoints für Einsteiger.“
* **Format vorgeben:** „Antworte in maximal zwei Sätzen.“ / „Als Liste.“ / „Auf Deutsch.“
* **Kontext mitgeben:** Wenn die Antwort auf einem Dokument basieren soll, den relevanten Ausschnitt im Prompt mitliefern (dafür wird später RAG genutzt).

Grenzen
-------

Das Modell „merkt sich“ nur das, was im **aktuellen Kontext** (Context Window) steht. Es hat kein dauerhaftes Gedächtnis zwischen Anfragen. Für wissensbasierte Antworten aus eigenen Dokumenten nutzt man daher **RAG** (Retrieval-Augmented Generation).

Nächster Schritt
----------------

Damit Sie später **semantisch suchen** und **RAG** umsetzen können, brauchen Sie **Embeddings** – Vektoren, die die „Bedeutung“ von Text erfassen. Dafür geht es im nächsten Kapitel weiter: :doc:`embeddings`.
