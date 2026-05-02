Generative KI
=======================

**Recap der wichtigsten Themen des dritten Tages**

- Wiederholung der zentralen Konzepte von **Reinforcement Learning**

- **Q-Funktionen und ihre Rolle im Reinforcement Learning**

- Diskussion über Anwendungen von **Reinforcement Learning**

- Offene Fragen und Klarstellungen


**Hauptkapitel (Lernpfad)**

.. list-table::
   :header-rows: 1

   * - Kapitel
     - Inhalte
   * - Einführung in Generative KI
     - Konzepte und Grundlagen
   * - Lernpfad (Roadmap)
     - Text → Tokens → Prompting → Embeddings → semant. Ähnlichkeit → Suche → RAG → optional Interna
   * - LLM-Intuition
     - Was ein Sprachmodell macht (Next-Token-Prediction)
   * - Tokenisierung
     - Tokens, Tokenizer, Kontextlänge
   * - Prompt-Engineering
     - Zero-Shot, Few-Shot, System-Prompt
   * - Embeddings
     - Text als Vektor, Bedeutung im Raum
   * - Semantische Ähnlichkeit
     - Vektorvergleich, Kosinusähnlichkeit, Brücke zur Suche
   * - Semantische Suche
     - Retrieval mit Embeddings und Top-k
   * - RAG (Einführung)
     - Retrieval-Augmented Generation, Konzept
   * - RAG-Praxis (Notebook)
     - Lokaler RAG-Ablauf ohne externe LLM-API
   * - Grenzen und Risiken von LLMs
     - Halluzinationen, Bias, Sicherheit, Regulierung

**Optionale Vertiefung (LLM-Interna)**

.. list-table::
   :header-rows: 1

   * - Kapitel
     - Inhalte
   * - Theorie hinter Generative KI
     - Wahrscheinlichkeitsmodelle, Transformer, Optimierung (nach RAG/Kapitel)
   * - LLM-Interna (konzeptionell)
     - Attention, Decoder-only, ausgewählte Code-Snippets (keine Vollimplementierung)
   * - microGPT-Walkthrough (optional)
     - Minimales GPT im Stil Karpathy: Text→Tokens→Embeddings→Transformer→Next-Token (Schlüsselcode)

**Referenz (außerhalb des Haupt-Lernflusses)**

.. list-table::
   :header-rows: 1

   * - Kapitel
     - Inhalte
   * - LLM-Lingo (Glossar)
     - Begriffserklärungen zum Nachschlagen

**Weitere Kapitel**

.. list-table::
   :header-rows: 1

   * - Kapitel
     - Inhalte
   * - Infrastruktur und Architektur
     - Hardware, Software-Frameworks, Architekturüberblick
   * - Hands-on Beispiel
     - Lokales LLM mit Feintuning auf domänspezifischen Daten
   * - Generative KI und Agents
     - Definition von Agents, Integration von LLMs, Beispiele
   * - Diskussion
     - Stärken und Schwächen der GenAI, Herausforderungen und Bottlenecks
   * - Regulatorik
     - AI Act

Ethische Fallbeispiele
----------------------

Die folgenden Beispiele zeigen, warum Ethik und Regulierung (z. B. AI Act) in der Praxis wichtig sind – von frühen Chatbot-Vorfällen bis zu aktuellen Fällen von Bias und Diskriminierung.

**Ältere Beispiele**

* **Microsoft Tay (2016):** Der erste Chatbot von Microsoft hatte kaum inhaltliche Grenzen und wurde binnen kurzer Zeit gezielt zu beleidigenden und rechtsextremen Aussagen manipuliert. Die einzige KPI war damals „wie viele Reaktionen man bekommt“ – radikale Thesen erzeugten die meisten Rückmeldungen. Siehe `Tay (Bot) (Wikipedia)
  <https://de.wikipedia.org/wiki/Tay_(Bot)>`_.

* **Österreichisches Arbeitsamt (AMS):** Ein algorithmisches System empfahl u. a., dass Frauen systematisch schlechter bezahlte Jobs akzeptieren sollten (vgl. z. B. `futurezone.at
  <https://futurezone.at/netzpolitik/computer-sagt-nein-algorithmus-gibt-frauen-weniger-chancen-beim-ams/400345297>`_).

**Neuere Beispiele (u. a. 2018–2025)**

* **Schweden – Försäkringskassan:** Das schwedische Sozialversicherungsamt setzte einen KI-Algorithmus zur Betrugserkennung ein, der laut Recherchen u. a. Frauen, Migranten und Geringverdienende deutlich häufiger als andere verdächtigte. Mangelnde Transparenz und fehlende Kontrolle führten zu jahrelanger Diskriminierung (vgl. z. B. `infosperber.ch
  <https://www.infosperber.ch/gesellschaft/sozialversicherungen/schweden-frauen-arme-und-migranten-unter-ki-generalverdacht/>`_).

* **Bias bei Kredit und Bewerbung:** KI-Systeme in Kreditvergabe oder Bewerbungsvorauswahl können historische Diskriminierung (z. B. gegen Frauen) in den Trainingsdaten verstärken. Bekannt wurden u. a. Amazons Recruiting-Tool und Studien zu KI-Krediten, die Frauen benachteiligen – und damit die Notwendigkeit von fairen Daten, Transparenz und Regulierung unterstreichen.

.. toctree::
   :hidden:
   :titlesonly:
   :maxdepth: 0

   genai_intro
   genai_roadmap
   llm_intuition
   tokenization
   prompt_engineering
   embeddings
   semantic_similarity
   semantic_search
   rag_intro
   rag_practice
   llm_limitations
   genai_theory
   llm_internals
   microgpt_walkthrough
   microgpt-karpathy
   genai_llm
   genai_infrastructure
   llm_1
   llm_2
   customer-churn-data-creation
   customer-churn-2
   genai_agents
   regulatory
   abschluss
