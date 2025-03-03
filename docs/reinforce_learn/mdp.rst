Markov-Entscheidungsprozesse (MDP)
------------------------------

Die meisten der Reinforment Learning Probleme können mit dem Framework des Markov-Entscheidungsprozess (Markov Decision Process, MDP) gelöst werden.

Der MDP ist ein mathematisches Framework für die Modellierung von Entscheidungsproblemen, bei denen die Ergebnisse teilweise zufällig und teilweise kontrollierbar sind.

**Recap**

**Markov-Eigenschaft**

Ein Zustand S_t ist dann und nur dann ein Markov-Zustand, wenn folgendes zutrifft:

.. math:: 
   P[S_{t+1} | S_t] = P(S_{t+1} | S_1,S_2, ...,S_t)

Das heißt, dass der aktuelle Zustand des Roboters nur von seinem unmittelbar vorhergehenden Zustand (bzw. dem vorherigen Zeitschritt) abhängt und nicht von den weiteren vorherigen Zuständen.

**Markov-Prozess**

Ein Markov-Prozess wird definiert von (S,P), wobei S die Menge aller Zustände ist und P die Übergangswahrscheinlichkeit von Zustand s nach Zustand s' ist:

.. math:: 
   P_{ss'} = P[S_{t+1} = s' | S_t = s]

Das MDP-Framework besteht somit aus den folgenden Komponenten:

  1. **S** – Menge aller möglichen Zustände: alle möglichen und erlaubten Positionen im Raum.

  2. **A** – Menge aller möglichen Aktionen: die vier Bewegungsmöglichkeiten oben, unten, links, rechts.

  3. **P(s' | s, a)** – Übergangswahrscheinlichkeit von Zustand \(s\) zu \(s'\) nach Aktion \(a\): die Wahrscheinlichkeit, dass der Roboter nach der Aktion in einen neuen Zustand übergeht.

  4. **R(s, a)** – Belohnung für das Ausführen von Aktion \(a\) in Zustand \(s\).

  5. **\(\gamma\) (Discount Factor)** – Faktor für zukünftige Belohnungen (zwischen 0 und 1).

Das Ziel ist, eine **optimale Policy** zu finden, die die **kumulierte langfristige Belohnung maximiert**.
