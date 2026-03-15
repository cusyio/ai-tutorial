Regulatorisches: AI Act, DSGVO & Co. - Zusammenfassung
=======================================================

Einführung
-----------

Der **EU AI Act** stellt einen regulatorischen Rahmen dar, der den Einsatz von Künstlicher Intelligenz in Europa systematisch steuern soll. Gleichzeitig ist die **Datenschutz-Grundverordnung (DSGVO)** ein zentraler Pfeiler für den Schutz personenbezogener Daten in Europa. 

Dieses Kapitel gibt eine Zusammenfassung der wichtigsten regulatorischen Vorgaben und zeigt auf, **worauf Nutzer, Ingenieure und Unternehmen achten sollten**, wenn sie KI-gestützte Systeme entwickeln oder nutzen.

Risikobasierte Klassifizierung im AI Act
------------------------------------------

Der AI Act teilt KI-Systeme anhand ihres Risikopotenzials in unterschiedliche Kategorien ein:

* **Hochrisikobehaftete Systeme:** 
     Systeme, die in sicherheitskritischen Bereichen (Gesundheit, Verkehr, Justiz, kritische Infrastrukturen) eingesetzt werden. Diese unterliegen strengen Anforderungen hinsichtlich Testverfahren, Dokumentation und Überwachung.
* **Geringeres Risiko:** 
     Systeme mit weniger sensiblen Anwendungsbereichen profitieren von reduzierten regulatorischen Vorgaben.
* **Minimales Risiko:** 
     Anwendungen mit kaum relevanten Risiken sind praktisch keiner speziellen Regulierung unterworfen.

Die risikobasierte Klassifizierung sorgt für ein abgestuftes Vorgehen, das sowohl Schutz als auch Innovation ermöglicht.

Datenschutz & DSGVO: Worauf Entwickler und Nutzer achten sollten
------------------------------------------------------------------

Grundprinzipien der DSGVO
:::::::::::::::::::::::::::

KI-Systeme müssen sich an die **Grundprinzipien der DSGVO** halten, insbesondere:

* **Rechtmäßigkeit, Verarbeitung nach Treu und Glauben & Transparenz**
* **Zweckbindung:** 
     Daten dürfen nur für festgelegte, legitime Zwecke verarbeitet werden.
* **Datenminimierung:** 
     Es dürfen nur so viele Daten wie nötig verarbeitet werden.
* **Speicherbegrenzung:** 
     Daten dürfen nicht länger als nötig gespeichert werden.
* **Integrität und Vertraulichkeit:** 
     Sicherheitsmaßnahmen müssen unautorisierte Zugriffe verhindern.

Konkrete Anforderungen für KI-Entwicklung
:::::::::::::::::::::::::::::::::::::::::::::

Ingenieure sollten folgende Datenschutzmaßnahmen implementieren:

* **Datenanonymisierung und Pseudonymisierung:** 
     Reduzierung personenbezogener Bezüge in Daten.
* **Datensparsamkeit:** 
     Nur wirklich benötigte Daten speichern und verarbeiten.
* **Löschkonzepte:** 
     Mechanismen zur automatischen Datenlöschung oder zur Auskunftspflicht nach DSGVO-Art. 15.
* **Privacy by Design & Privacy by Default:** 
     Datenschutz muss von Anfang an in das KI-System integriert sein.

Nutzung von KI als Endanwender
::::::::::::::::::::::::::::::::::::

* **Transparenz prüfen:** 
     Anbieter müssen erklären, wie die KI Entscheidungen trifft.
* **Einwilligungen einholen:** 
     Falls personenbezogene Daten verarbeitet werden, muss eine Einwilligung vorliegen.
* **Recht auf Widerspruch nutzen:** 
     Nutzer haben das Recht, automatisierte Entscheidungen anzufechten.

Transparenzanforderungen
:::::::::::::::::::::::::::

Ein zentrales Element des AI Acts ist die **Forderung nach Transparenz**. Anbieter von KI-Systemen müssen klar und verständlich darlegen, wie ihre Systeme funktionieren und welche Daten zugrunde liegen.

* **Erklärbarkeit:** 
     Nutzer sollen nachvollziehen können, wie und warum ein System zu einer bestimmten Entscheidung gelangt.
* **Dokumentation:** 
     Es sind umfassende Informationen über Architektur, Trainingsdaten und Entscheidungsprozesse bereitzustellen.
* **Offenlegungspflichten:** 
     Hochrisiko-KI-Systeme müssen relevante Details veröffentlichen, um externe Prüfungen zu ermöglichen.

Diese Transparenzmaßnahmen dienen dazu, Missbrauch zu verhindern und Vertrauen in KI-Systeme zu stärken.

Sicherheits- und Datenschutzvorgaben
:::::::::::::::::::::::::::::::::::::

* **Datensicherheit:** 
     KI-Systeme müssen gegen Manipulationen und Cyberangriffe geschützt sein.
* **Systemresilienz:** 
     Maßnahmen müssen sicherstellen, dass KI-Systeme auch unter Störungsszenarien zuverlässig arbeiten.
* **Erkennung und Reduktion von Bias:** 
     Trainingsdaten sollten regelmäßig auf Verzerrungen geprüft werden.
* **Regelmäßige Audits:** 
     Hochrisiko-KI muss wiederholt geprüft und dokumentiert werden.

Haftungsregelungen & Verantwortung
::::::::::::::::::::::::::::::::::::

Wer haftet im Fehlerfall? Der AI Act definiert klare Haftungsregelungen:

* **Verantwortlichkeit der Anbieter:**
     Hersteller und Betreiber haften für Schäden durch KI-Systeme.
* **Transparenz bei Fehlern:** 
     Fehler müssen rückverfolgbar sein, um Verantwortlichkeiten zu klären.
* **Schadensersatz:** 
     Nutzer können bei nachgewiesenem Schaden Ersatz fordern.

Wichtig für Ingenieure: Implementierung von Mechanismen, die Fehler und deren Ursachen nachvollziehbar machen.

Auswirkungen auf Forschung & Entwicklung
:::::::::::::::::::::::::::::::::::::::::::::

* **Förderung von Innovation:** 
     Der AI Act stellt sicher, dass Innovation durch regulatorische Standards nicht behindert wird.
* **Regulierung von Open-Source-KI:** 
     Diskutiert wird, ob Open-Source-Modelle besonderen Regeln unterliegen.
* **Kooperation zwischen Stakeholdern:** 
     Industrie, Forschung und Politik müssen zusammenarbeiten, um die Sicherheit von KI-Systemen zu gewährleisten.

Best Practices für KI-Entwicklung
::::::::::::::::::::::::::::::::::::

Um regulatorische Anforderungen zu erfüllen, sollten Entwickler folgende Punkte beachten:


Modell-Pipeline & Infrastruktur
::::::::::::::::::::::::::::::::::::

* **Dokumentation:** 
     KI-Modelle müssen vollständig dokumentiert werden (Trainingsdaten, Entscheidungsprozesse, Evaluierungen).
* **Bias-Reduktion:** 
     Methoden wie Fairness Constraints und Debiasing-Techniken einsetzen.
* **Explainability & XAI:** 
     Erklärbare KI-Modelle nutzen, um Nachvollziehbarkeit sicherzustellen.
* **Versionierung:** 
     Modellversionen und Updates mit vollständiger Historie speichern.
* **Human-in-the-Loop:** 
     Automatische Entscheidungen durch menschliche Kontrolle ergänzen.

Datenschutzgerechte Architektur
::::::::::::::::::::::::::::::::::::

* **Datenminimierung:** 
     Nur notwendige Daten speichern und verarbeiten.
* **Differential Privacy:** 
     Mechanismen, die individuelle Datenschutzrisiken minimieren.
* **Verschlüsselung & Zugriffskontrollen:** 
     Sicherheitsmechanismen zur Datenspeicherung und -übertragung.

Verantwortungsbewusste Nutzung von LLMs
:::::::::::::::::::::::::::::::::::::::::

* **Sichere Prompt-Designs:** 
     Schutz vor adversarial attacks und Manipulation durch bösartige Prompts.
* **Prüfung auf Halluzinationen:** 
     KI-generierte Inhalte regelmäßig auf Richtigkeit überprüfen.
* **Einhaltung ethischer Grundsätze:** 
     Keine diskriminierenden oder gesellschaftsschädlichen Outputs.

Fazit
:::::::::

Der AI Act und die DSGVO setzen Regeln für den Umgang mit KI-Systemen. Entwickler müssen:

* **Transparenz und Datenschutz priorisieren.**
* **Modelle sicher und robust gestalten.**
* **Regulatorische Vorgaben in der Infrastruktur umsetzen.**
* **Verantwortung für KI-generierte Entscheidungen übernehmen.**

Während der AI Act den **Einsatz von KI regelt**, sorgt die DSGVO für den **Schutz personenbezogener Daten** – zusammen bilden sie die Grundlage für eine sichere und ethische KI-Nutzung.

Diese Zusammenfassung gibt eine Orientierungshilfe für Ingenieure und Nutzer, die mit KI-Systemen arbeiten.
