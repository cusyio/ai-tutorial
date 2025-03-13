Definitionen und Grundprinzipien in Reinforcement Learning (RL)
====================================================================

Definitionen
------------------------------

- Reinforcement Learning (RL) ist eine Form des **selbstlernenden maschinellen Lernens**, bei dem ein Agent durch **Belohnung und Bestrafung** lernt.

- Ziel ist es, eine **Strategie (Policy)** zu erlernen, die langfristig die **höchste kumulierte Belohnung** maximiert.

- Anders als beim überwachten Lernen gibt es **keine direkten Labels**, sondern nur **Rückmeldungen** basierend auf den getroffenen Entscheidungen.

Grundprinzipien
------------------------------

1. **Agent:** Der lernende KI-Teilnehmer.

2. **Umgebung (Environment):** Die Welt, in der der Agent agiert.

3. **Zustand (State):** Der aktuelle Status der Umgebung.

4. **Aktion (Action):** Die Entscheidung, die der Agent in einem Zustand trifft. Wir kennen die Menge aller Aktionen, die der Agent im Voraus ausführen kann.

5. **Belohnung (Reward):** Das Signal, das die Qualität einer Aktion beschreibt.

6. **Policy (Strategie):** Die Strategie bestimmt, welche Aktion in welchem Zustand gewählt wird.
Die Strategie ist der "Denkprozess", der der Auswahl einer Aktion zugrunde liegt.
Meist handelt es sich hierbei um eine Wahrscheinlichkeitsverteilung, die der Menge der Aktionen zugewiesen wird.
Aktionen mit hoher Belohnung haben eine hohe Wahrscheinlichkeit und vice versa. Wenn eine Aktion eine niedrige Wahrscheinlichkeit hat, bedeutet es aber nicht, dass sie gar nicht ausgewählt wird. Deren Wahl passiert nur weniger wahrscheinlich.

7. **Wertfunktion (Value Function):** Erwartete zukünftige Belohnung eines Zustands.


Beispiel zur Veranschaulichung
------------------------------

Stellen wir uns einen Roboter in neinem Raum vor, der selbst erlernen soll, wie er am besten zum Ausgang findet.

- Der **Agent** ist der Roboter.

- Die **Umgebung** ist der Raum mit Wänden, potenziellen Hindernissen und dem Ausgang.

- Der **Zustand** beschreibt die aktuelle Position des Roboters im Raum.

- Die **Aktionen** bestehen aus vier Bewegungsmöglichkeiten: **oben, unten, links, rechts**. (in 2D-Darstellung)

- Die **Belohnung** beträgt **+100**, wenn der Roboter den Ausgang findet, und **-100**, wenn er gegen eine Wand läuft, und **-1** bei jedem Schritt, er macht ohne zum Ziel zu kommen. 

- Die **Policy (Strategie)** bestimmt, welche Aktion der Roboter in welchem Zustand ausführt.

- Die **Wertfunktion** bewertet, wie vorteihaft ein Zustand langfristig ist.

Das Ziel des Roboters liegt darin, durch **Versuch und Irrtum** (Trial and Error) die optimale **Strategie** zu lernen, um den Ausgang so effizient wie möglich zu erreichen.
