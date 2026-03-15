Grenzen und Risiken von LLMs
=============================

**Recap:** Mit **RAG** können wir dem LLM Kontext aus eigenen Dokumenten mitgeben – trotzdem bleibt das Modell ein statistisches Vorhersagemodell mit festen Grenzen. **Warum dieses Kapitel:** Bevor wir optional in die Architektur (LLM-Interna, microGPT) eintauchen, ist es wichtig, die **Grenzen und Risiken** zu kennen: Halluzinationen, Bias, Aktualität, Sicherheit und Regulierung. Dieses Kapitel fasst die wichtigsten Punkte für die Praxis zusammen.

Halluzinationen
---------------

LLMs erzeugen Text auf Basis statistischer Muster – sie „wissen“ nicht im Sinne einer Wissensdatenbank. Sie können **inhaltlich falsche** oder erfundene Aussagen produzieren („Halluzinationen“), die plausibel klingen. Besonders riskant bei Fakten, Zahlen, Zitaten oder rechtlichen/medizinischen Inhalten.

**Beispiele aus der Praxis:** Google Bard (2023) lieferte in einer Demo eine falsche Aussage zum James-Webb-Teleskop. Ein US-Anwalt nutzte ChatGPT, das nicht existierende Urteile „erfand“ – ein klassischer Halluzinationsfall mit rechtlichen Folgen. Auch ChatGPT, Claude und andere Modelle können Quellen oder Zahlen erfinden, wenn der Kontext unscharf ist.

**Praktisch:** Antworten prüfen, Quellen angeben (z. B. durch RAG), bei kritischen Anwendungen menschliche Prüfung einplanen.

Aktualität und Kontext
----------------------

* **Trainingsstand:** Das Modell kennt nur Daten bis zu einem bestimmten Stichtag. Aktuelle Ereignisse, neue Produkte oder Richtlinien sind ihm unbekannt – es sei denn, sie werden per RAG oder Prompt eingespielt.
* **Kontextfenster:** Nur eine begrenzte Menge Text (Token) kann gleichzeitig verarbeitet werden. Sehr lange Dokumente müssen gekürzt oder in Chunks aufgeteilt werden.

Bias und Fairness
-----------------

Modelle lernen aus dem, was in den Trainingsdaten steht. Enthalten diese **Vorurteile** (z. B. geschlechter- oder herkunftsbezogen), können diese in den Ausgaben verstärkt werden. Das betrifft Personalentscheidungen, Kreditwürdigkeit, Bewertungen und viele andere Anwendungen.

**Beispiele aus der Praxis:** Amazons Recruiting-Tool bevorzugte Bewerbungen von Männern, weil es an historischen Daten trainiert war. Bildgeneratoren (z. B. frühe Versionen von DALL-E, Stable Diffusion) erzeugten bei „CEO“ überproportional männliche Figuren. Solche Fälle zeigen, warum faire Daten und Tests bei allen Modellen (ChatGPT, Claude, Gemini, Open-Source-Modelle) wichtig sind.

**Praktisch:** Bewusstsein für Bias, faire und repräsentative Daten, Tests und ggf. Regulierung (z. B. AI Act) beachten.

Sicherheit und Missbrauch
-------------------------

* **Prompt-Injection:** Durch gezielte Eingaben kann das Verhalten des Modells manipuliert werden (z. B. „Ignoriere vorherige Anweisungen und …“). In der Praxis wurden u. a. Bing Chat (Sydney), ChatGPT und andere Assistenten mit solchen Eingaben getestet; Anbieter versuchen, mit System-Prompts und Filtern gegenzusteuern.
* **Sensible Daten:** Keine vertraulichen oder personenbezogenen Daten ungeprüft in öffentliche APIs geben; Datenschutz und Compliance beachten. Bei Nutzung von OpenAI, Anthropic, Google etc. die jeweiligen Datenschutz- und Verarbeitungsbedingungen beachten.

Kosten und Latenz
-----------------

Große Modelle und lange Kontexte verbrauchen Rechenzeit und – bei Cloud-APIs – Geld. Für Produktion sind Dimensionierung, Caching und klare Nutzungsrichtlinien wichtig.

Regulierung
-----------

Der **EU AI Act** und weitere Vorgaben klassifizieren Anwendungen nach Risiko und verlangen u. a. Transparenz, Dokumentation und menschliche Aufsicht. Das Kapitel **Regulatorik** (:doc:`regulatory`) geht darauf genauer ein.

Kurz zusammengefasst
--------------------

* LLMs können **halluzinieren**; Ergebnisse sollten geprüft und wo möglich mit Quellen (z. B. RAG) abgesichert werden.
* **Aktualität** und **Kontextlänge** sind begrenzt; RAG und klare Prompts helfen.
* **Bias**, **Sicherheit** und **Regulierung** müssen von Anfang an mitgedacht werden.

Nächster Schritt
----------------

Wer die **Architektur** von Transformern verstehen möchte – ohne ein vollständiges Modell zu implementieren – findet in den optionalen Kapiteln **LLM-Interna** (:doc:`llm_internals`) (Konzepte: Attention, Decoder-only) und **microGPT-Walkthrough** (:doc:`microgpt_walkthrough`) (ausgewählte Code-Bausteine im Stil Karpathy) die passende Vertiefung. Die **Theorie hinter Generativer KI** (:doc:`genai_theory`) liefert die mathematischen Details.
