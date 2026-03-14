Q-Learning - Theorie und Anwendung
===================================

Q-Learning ist eine **wertbasierte Methode** im **Reinforcement Learning**, 
die auf **Markov-Entscheidungsprozessen (MDP)** basiert. 

(Einschub: Es gibt *"wertbasierte Methode"* und *"policy-basierte"* Methode. 
*"Policy-basierte"* Methoden lernen direkt eine Strategie (Policy), die eine Aktion für jeden Zustand bestimmt. 
**Beispiel**: Anstatt Q-Werte zu berechnen, trainiert ein neuronales Netz eine Policy, die dem Agenten sagt, welche Aktion er ausführen soll, ohne dass er Q-Werte speichert.
)

Ziel ist es, eine **optimale Policy** zu erlernen, die den Agenten dazu befähigt, langfristig die höchste kumulierte Belohnung zu erzielen. 
Dabei wird ein sogenannter **Q-Wert** berechnet, der beschreibt, wie vorteilhaft es ist, in einem bestimmten Zustand eine bestimmte Aktion auszuführen.

Wie funktioniert Q-Learning?
::::::::::::::::::::::::::::

In "Q-Learning" bezieht sich "Q" auf die Zielfunktion, die der Algorithmus berechnen und optimieren soll: die erwartete Belohnung (die Qualität) einer Aktion, die in einem bestimmten Zustand durchgeführt wird.

In der Durchführung basiert Q-Learning auf einer sogenannten **Q-Tabelle**, in der für jede Kombination aus **(Zustand, Aktion)** ein Wert gespeichert wird. 

Dieser Q-Wert wird iterativ verbessert, indem der Agent die Umgebung erkundet und aus seinen Erfahrungen lernt. 
Der Kern des Algorithmus besteht in der folgenden Update-Regel, die sich an der **Bellman-Gleichung** orientiert:

  .. math::
     Q(s,a) = Q(s,a) + \alpha (R + \gamma \max Q(s',a') - Q(s,a))

Erklärung der Formel:
~~~~~~~~~~~~~~~~~~~~~~~~

* **Q(s, a):** 
     Der aktuelle geschätzte Wert für Zustand `s` und Aktion `a`.
* **R:** 
     Die Belohnung für die durchgeführte Aktion `a`.
* **γ (Gamma):** 
     Der **Discount-Faktor**, der den Einfluss zukünftiger Belohnungen bestimmt (zwischen 0 und 1).
* **max Q(s', a'):** 
     Der maximale Q-Wert des nächsten möglichen Zustands `s'`.
* **α (Alpha):** 
     Die **Lernrate**, die bestimmt, wie stark neue Informationen alte Werte überschreiben.


Q-Learning Algorithmus
:::::::::::::::::::::::

Der Algorithmus läuft iterativ in folgenden Schritten ab:

1. **Agent befindet sich in einem Zustand `s`.**
2. **Wählt eine Aktion `a` basierend auf einer Policy (z. B. zufällig oder nach maximalem Q-Wert).**
3. **Führt die Aktion aus und erhält eine Belohnung `R`.**
4. **Wechselt in den nächsten Zustand `s'`.**
5. **Aktualisiert den Q-Wert gemäß der obigen Formel.**
6. **Wiederholt den Prozess, bis das Modell konvergiert.**


Exploration vs. Exploitation
::::::::::::::::::::::::::::::

Ein zentraler Aspekt von Q-Learning ist das Gleichgewicht zwischen **Exploration** (Entdeckung neuer Strategien) und **Exploitation** (Nutzung bekannter, erfolgreicher Strategien):

* **Exploration:** 
     Der Agent wählt **zufällige Aktionen**, um neue Wege und bessere Entscheidungen zu entdecken. Dies ist wichtig, damit das Modell nicht in einer **lokalen Optimallösung** stecken bleibt.
* **Exploitation:** 
     Sobald das Modell genug Wissen gesammelt hat, wird es **die beste bekannte Aktion auswählen**, um die Belohnung zu maximieren.

Ein häufiger Ansatz ist die **ε-greedy Policy**, bei der der Agent mit einer Wahrscheinlichkeit von **ε** zufällige Aktionen ausprobiert (Exploration) und mit Wahrscheinlichkeit **1 - ε** die beste bekannte Aktion nutzt (Exploitation). Während des Trainings kann **ε allmählich reduziert werden**, um den Fokus mit der Zeit mehr auf **Exploitation** zu legen.


Verbindung zwischen Markov-Prozessen und Q-Learning
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::

Q-Learning ist direkt mit **Markov-Entscheidungsprozessen (MDP)** verbunden. 

Ein MDP besteht aus:

* **S (States):** 
     Die Menge aller möglichen Zustände, in denen sich der Agent befinden kann.
* **A (Actions):** 
     Die Menge aller möglichen Aktionen, die der Agent ausführen kann.
* **P(s' | s, a) (Transition Model):** 
     Die Wahrscheinlichkeit, dass der Agent nach der Aktion `a` von `s` nach `s'` wechselt.
* **R(s, a) (Reward):** 
     Die Belohnung, die der Agent für eine Aktion `a` in Zustand `s` erhält.
* **γ (Discount Factor):** 
     Der Faktor, der bestimmt, wie stark zukünftige Belohnungen gewichtet werden.

**Warum ist das wichtig?**

* Q-Learning braucht **keine direkte Kenntnis** über die Wahrscheinlichkeiten der Übergänge **P(s' | s, a)**.
* Stattdessen lernt das Modell **aus Erfahrungen**, indem es durch Versuch und Irrtum die Q-Werte verbessert.
* Damit kann Q-Learning auf **komplexe Umgebungen angewendet werden, in denen die Übergangswahrscheinlichkeiten nicht explizit bekannt sind.**

Erfahrungsspeicherung: Replay Buffer und Experience Replay
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::

In klassischen Q-Learning-Implementierungen gibt es eine Herausforderung: Die Agenten lernen direkt aus **den neuesten Erfahrungen**, was dazu führen kann, dass das Modell instabil wird oder suboptimale Strategien lernt.

Hier kommen zwei Konzepte ins Spiel:

**Replay Buffer**
~~~~~~~~~~~~~~~~~~~~~~~

* Ein Speicher, in dem frühere Erfahrungen (`(s, a, r, s')`) abgelegt werden.
* Statt nur aus der neuesten Interaktion zu lernen, werden vergangene Erfahrungen zufällig ausgewählt.
* Dies verhindert **Korrelationen** zwischen aufeinanderfolgenden Lernerfahrungen und stabilisiert das Lernen.

**Experience Replay**
~~~~~~~~~~~~~~~~~~~~~~~

* Eine Technik, bei der das Modell nicht nur aus den neuesten Daten lernt, sondern **frühere Episoden erneut durchspielt**.
* Dadurch können **seltener auftretende, aber wichtige Erfahrungen** mehrfach genutzt werden.
* Besonders nützlich in **Deep Q-Learning**, wenn neuronale Netze zur Approximation der Q-Werte eingesetzt werden.


Deep Q-Networks (DQN):
:::::::::::::::::::::::::::::::::::::

- Ersetzt die **Q-Tabelle durch ein neuronales Netz**, das **Q-Werte approximiert**.

- Verwendet Replay Buffers zur Speicherung vergangener Erfahrungen.

- Führt **Experience Replay** aus, um stabileres Lernen zu ermöglichen.
