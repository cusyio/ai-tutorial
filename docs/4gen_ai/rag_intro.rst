RAG – Retrieval-Augmented Generation
=====================================

**Recap:** Mit **Embeddings** und **semantischer Ähnlichkeit** (Kosinus) haben wir die **relevantesten Chunks** zu einer Frage gefunden – das ist **Retrieval** (Semantische Suche). **Warum dieses Kapitel:** Diese Treffer sollen nicht nur angezeigt, sondern vom LLM genutzt werden. **RAG** verbindet **Retrieval** mit **Generation**: Relevante Textstellen werden aus den eigenen Dokumenten geholt und dem LLM als **Kontext** mitgegeben. So kann das Modell auf **dieses Wissen** antworten, ohne es im Training gesehen zu haben.

Problem ohne RAG
----------------

Ein LLM kennt nur das, was in seinem **Kontext-Fenster** steht und was es aus dem Training „weiß“. Es hat keinen Zugriff auf interne Dokumente, aktuellen FAQs oder Schulungsunterlagen. Ohne RAG antwortet es nur aus dem Trainingswissen – oft generisch oder veraltet.

Lösung: Kontext einspritzen
---------------------------

Bei RAG passiert grob Folgendes:

#. **Anfrage:** Der Nutzer stellt eine Frage.
#. **Retrieval:** Mit einem Embedding-Modell und semantischer Suche werden die **relevantesten Abschnitte** aus dem Dokumentenkorpus gefunden (z. B. Top-3 oder Top-5).
#. **Prompt bauen:** Diese Abschnitte werden als **Kontext** in einen Prompt eingefügt, z. B.: „Antworte nur auf Basis des folgenden Kontexts. Kontext: … Frage: …“
#. **Generation:** Das LLM erzeugt eine Antwort, die auf dem gegebenen Kontext basiert.

.. code-block:: text

   [Kontext aus den Dokumenten]
   +
   [Nutzerfrage]
   →
   [Antwort des LLMs, am Kontext orientiert]

Vorteile
--------

* **Aktuell:** Dokumente können jederzeit ergänzt oder geändert werden; das Modell nutzt den abgerufenen Kontext.
* **Nachvollziehbar:** Die Antwort beruht auf angegebenen Textstellen; die Quellen lassen sich prüfen.
* **Kein Feintuning nötig:** RAG funktioniert mit Standard-LLMs; das Wissen steckt in den Dokumenten und im Retrieval.

RAG in der Praxis: Wo man ihm begegnet
--------------------------------------

RAG ist kein Nischenkonzept, sondern in vielen Produkten und Diensten im Einsatz:

* **ChatGPT (OpenAI):** Mit „Dateien anhängen“ oder „Browse“ werden Dokumente bzw. das Web als Kontext genutzt – im Kern ein RAG-ähnlicher Ablauf (Retrieval + Kontext für das Modell).
* **Perplexity, You.com:** Suchanfragen werden mit abgerufenen Web- oder Dokumentenstellen angereichert; das LLM antwortet auf Basis dieses Kontexts.
* **Notion AI, Confluence AI:** Fragen zu eigenen Notizen oder Wikis – Retrieval aus den Dokumenten, dann Generierung der Antwort.
* **Unternehmens-Assistenten / Copilots:** Microsoft 365 Copilot, Salesforce Einstein, interne „Firmen-Chatbots“ holen oft relevante Stellen aus Handbüchern, FAQs oder Tickets und füttern damit das LLM.
* **Support- und Dokumentations-Tools:** Viele KI-Chatbots für Kundenservice oder Technische Dokumentation nutzen RAG, um nur aus freigegebenen Quellen zu antworten.

So lässt sich das in diesem Kurs Gelernte (Retrieval, Kontext, Prompt) in echten Anwendungen wiedererkennen.

Lokale Umsetzung (ohne externe LLM-API)
----------------------------------------

Für Schulungen und Übungen lässt sich RAG **lokal** durchspielen:

* **Embeddings:** Ein lokales Modell (z. B. ``sentence-transformers``) erzeugt Vektoren für Dokumenten-Chunks und für die Frage.
* **Retrieval:** Semantische Suche (z. B. Kosinusähnlichkeit) wählt die passenden Chunks aus.
* **Antwort:** Entweder nutzen wir ein **lokales kleines LLM** (z. B. über Ollama, llama.cpp) oder wir zeigen im Notebook nur den **gebauten Prompt** (Kontext + Frage) und lassen die eigentliche Generierung optional bzw. als Platzhalter – so läuft alles ohne externe API.

Das Notebook **RAG-Praxis** (:doc:`rag_practice`) zeigt genau diesen Ablauf: Indexierung, Retrieval und Kontext-Prompt – ausführbar ohne Cloud-LLM.

Grenzen und Risiken
-------------------

* Retrieval kann **irrelevante** Chunks liefern; dann kann die Antwort trotzdem „halluzinieren“ oder abweichen.
* **Kontextlänge:** Nur so viel Kontext passt ins Modell wie das Context Window erlaubt.
* Weitere Grenzen von LLMs (Halluzinationen, Bias, Aktualität) behandelt das Kapitel **Grenzen und Risiken von LLMs** (:doc:`llm_limitations`).

Nächster Schritt
----------------

* **Praxis:** Im Notebook :doc:`rag_practice` wird der RAG-Ablauf Schritt für Schritt nachgebaut (lokal, ohne externe LLM-API).
* **Grenzen:** Bevor wir optional in die Architektur eintauchen, lohnt sich ein Blick auf **Grenzen und Risiken von LLMs** (:doc:`llm_limitations`) – Halluzinationen, Bias, Aktualität, Sicherheit.
* **Optional:** Danach folgen **LLM-Interna** (:doc:`llm_internals`) und der **microGPT-Walkthrough** (:doc:`microgpt_walkthrough`) für alle, die sehen möchten, wie ein minimales GPT im Code aufgebaut ist.
