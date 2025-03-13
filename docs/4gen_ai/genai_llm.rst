Einführung zu LLM (Large Language Models)
=========================================

- **LLM-Lingo:** Must-Know Terms

https://github.com/aishwaryanr/awesome-generative-ai-guide/blob/main/resources/llm_lingo/llm_lingo_p1.pdf

https://python-basics-tutorial.readthedocs.io/en/latest/_sources/appendix/glossary.rst.txt



LLM-Lingo: Baseline & Fine-Tuning
:::::::::::::::::::::::::::::::::::

* **Foundation Model:** 
     Ein großes, vortrainiertes KI-Modell, das als Basis für spezifischere Aufgaben genutzt wird.
* **Transformer:** 
     Architektur für neuronale Netzwerke, die auf selbst-attention basiert und die Grundlage für viele LLMs ist.
* **Prompting:** 
     Technik zur Steuerung eines LLMs durch gezielte Texteingaben.
* **Context-Length:** 
     Die maximale Anzahl an Token, die ein LLM in einer einzelnen Abfrage berücksichtigen kann.
* **Few-Shot Learning vs Zero-Shot Learning vs In-Context Learning:** 
     Methoden, wie Modelle mit wenigen oder keinen Beispielen neue Aufgaben lösen.
* **RAG (Retrieval-Augmented Generation):** 
     Eine Methode, um LLMs mit externen Datenquellen zu erweitern und aktuelle Informationen zu nutzen.
* **Knowledge Base (KB):** 
     Eine strukturierte Datensammlung zur Unterstützung von LLMs bei der Wissensabrufung.
* **Vector Database:** 
     Eine spezialisierte Datenbank für das Speichern und Abrufen von embeddings, um semantische Suchanfragen zu ermöglichen.
* **Fine-Tuning:** 
     Anpassung eines vortrainierten Modells auf spezifische Aufgaben durch weiteres Training mit neuen Daten.
* **Instruction Tuning:** 
     Spezialisierte Form des Fine-Tunings, bei dem Modelle für bestimmte Instruktionen optimiert werden.
* **Hallucination:**
     Falsch generierte Informationen durch ein LLM, die nicht auf den Trainingsdaten basieren.
* **SFT (Supervised Fine-Tuning):** 
     Feinabstimmung eines Modells mit gekennzeichneten Daten.
* **Contrastive Learning:** 
     Trainingsmethode, die die Unterschiede zwischen ähnlichen und unähnlichen Datenpunkten lernt.
* **Pruning:** 
     Technik zur Reduzierung der Modellkomplexität durch Entfernen weniger wichtiger Parameter.

LLM-Lingo: RAG + LLM Agents
:::::::::::::::::::::::::::::::::::

* **Chunking:** 
     Zerlegung von langen Texten in kleinere Abschnitte für bessere Verarbeitung durch LLMs.
* **Indexing:** 
     Prozess zur schnellen Suche und zum Abruf von Informationen aus einer Datenbank.
* **Embedded Model:** 
     Ein Modell, das Text oder andere Daten in numerische Vektoren umwandelt.
* **Vector Search:** 
     Suche innerhalb einer Vektordatenbank, um semantisch ähnliche Ergebnisse zu finden.
* **Retrieval:** 
     Abruf relevanter Informationen zur Verbesserung der Generierung durch ein LLM.
* **AGI (Artificial General Intelligence):** 
     Hypothetische KI mit menschenähnlicher Intelligenz und universeller Problemlösungsfähigkeit.
* **LLM Agent:** 
     Ein autonom arbeitendes KI-Modul, das durch LLMs gesteuert wird und Aktionen ausführt.
* **Agent Memory:** 
     Speichersystem für einen LLM-Agenten, um vergangene Interaktionen zu nutzen.
* **Agent Planning:** 
     Strategie, mit der LLM-Agenten langfristige Aktionen planen.
* **Function Calling:** 
     Prozess, bei dem ein LLM externe Funktionen oder APIs zur Verarbeitung von Aufgaben aufruft.


LLM-Lingo: Enterprise Ready LLMs
:::::::::::::::::::::::::::::::::::

* **LLM Bias:** 
     Verzerrungen in der Modellvorhersage aufgrund von Trainingsdaten.
* **XAI (Explainable AI):** 
     Techniken zur Nachvollziehbarkeit und Erklärung von KI-Modellen.
* **Responsible AI:** 
     Ethik und Sicherheit im KI-Einsatz, um Fairness und Transparenz sicherzustellen.
* **AI Governance:** 
     Richtlinien und Prozesse zur Überwachung und Regulierung von KI-Systemen.
* **Compliance:** 
     Einhaltung gesetzlicher Vorgaben für den KI-Einsatz.
* **GDPR (General Data Protection Regulation):** 
     Europäische Datenschutzverordnung zur Regulierung personenbezogener Daten.
* **Alignment:** 
     Abstimmung von KI-Modellen mit menschlichen Werten und Sicherheitsrichtlinien.
* **Model Ethics:** 
     Ethikrichtlinien zur Vermeidung von Diskriminierung und Missbrauch durch KI.
* **PII (Personally Identifiable Information):** 
     Daten, die eine Person eindeutig identifizieren können.
* **LLMOps:** 
     Operationalisierung und Wartung von LLMs in produktiven Umgebungen.

LLM-Lingo: LLM Vulnerabilities and Attacks
:::::::::::::::::::::::::::::::::::::::::::

* **Adversarial Attacks:** 
     Gezielte Angriffe zur Manipulation von KI-Modellen.
* **Black-Box Attacks:** 
     Angriffe auf Modelle ohne direkten Zugriff auf deren interne Strukturen.
* **White-Box Attacks:** 
     Angriffe mit vollständigem Wissen über das Zielmodell.
* **Vulnerability:** 
     Schwachstellen in KI-Modellen, die ausgenutzt werden können.
* **Deep Fakes:** 
     Manipulierte Bilder oder Videos, die durch generative KI erstellt wurden.
* **Jailbreaking:** 
     Umgehung von Sicherheitsmechanismen eines KI-Modells.
* **Prompt Injection:** 
     Manipulation eines LLMs durch gezielte Eingaben, um unerwünschte Antworten zu erzeugen.
* **Prompt Leaking:** 
     Ungewollte Offenlegung interner Modellinformationen durch spezielle Eingaben.
* **Red-Teaming:** 
     Sicherheitsprüfung eines KI-Systems durch gezielte Tests auf Schwachstellen.
* **Robustness:** 
     Widerstandsfähigkeit eines Modells gegenüber Angriffen oder fehlerhaften Eingaben.
* **Watermarking:** 
     Techniken zur Kennzeichnung von KI-generierten Inhalten.

Learning Paradigms
:::::::::::::::::::::

* **Unsupervised Learning:** 
     Lernen aus nicht gekennzeichneten Daten ohne direkte Vorgaben.
* **Supervised Learning:** 
     Lernen aus gekennzeichneten Daten mit definierten Zielwerten.
* **Reinforcement Learning:** 
     Lernen durch Belohnungen und Bestrafungen in einer Umgebung.
* **Meta-Learning:** 
     Lernen, wie man effizient neue Aufgaben erlernen kann.
* **Multi-Task Learning:** 
     Training eines Modells auf mehrere Aufgaben gleichzeitig.
* **Zero-Shot Learning:** 
     Fähigkeit eines Modells, neue Aufgaben ohne vorheriges Training zu lösen.
* **Few-Shot Learning:** 
     Lernen aus wenigen Beispielen zur Lösung neuer Aufgaben.
* **Online Learning:** 
     Kontinuierliches Training eines Modells mit neuen Daten.
* **Continual Learning:** 
     Fähigkeit eines Modells, Wissen über Zeit zu behalten und zu erweitern.
* **Federated Learning:** 
     Dezentrale Modelloptimierung über mehrere Datenquellen ohne direkte Datenweitergabe.
* **Adversarial Learning:** 
     Training eines Modells mit simulierten Angriffen zur Robustheitssteigerung.
* **Active Learning:** 
     Modell kann gezielt Daten zur Verbesserung anfordern.
