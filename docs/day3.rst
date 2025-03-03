Tag 3: Reinforcement Learning (RL)
=======================

**Recap der wichtigsten Themen des zweiten Tages**

- Wiederholung der zentralen Konzepte von **Neuronalen Netzen und Deep Learning**

- Verständnis der **Forwardpropagation und Backwardpropagation**

- **Loss Functions und ihre Rolle in Gradient Descent**

- Diskussion über Anwendungen von **CNNs für Bildklassifikation**

- MLOps: Training, Testing, Inferencing, CI/CD 

- Offene Fragen und Klarstellungen


.. list-table:: Schulungsstruktur für KI-Grundlagen: Tag 3
   :header-rows: 1

   * - Kapitel
     - Inhalte
   * - Recap der wichtigsten Themen
     - Wiederholung von Deep Learning und CNNs
   * - Einführung in Reinforcement Learning
     - Konzepte, Agent, Umgebung, Belohnungen
   * - Markov-Entscheidungsprozesse
     - Definition, Zustände, Aktionen, Wertfunktionen
   * - Wertbasierte Methoden – Q-Learning
     - Theorie, Q-Tabelle, Deep Q-Networks (DQN)
   * - Praxis: Q-Learning in OpenAI Gym
     - Implementierung mit Python


**Definition:**

- Reinforcement Learning (RL) ist eine Form des **selbstlernenden maschinellen Lernens**, bei dem ein Agent durch **Belohnung und Bestrafung** lernt.

- Ziel ist es, eine **Strategie (Policy)** zu erlernen, die langfristig die **höchste kumulierte Belohnung** maximiert.

- Anders als beim überwachten Lernen gibt es **keine direkten Labels**, sondern nur **Rückmeldungen** basierend auf den getroffenen Entscheidungen.

**Grundprinzipien:**

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


**Beispiel zur Veranschaulichung**

Stellen wir uns einen Roboter in neinem Raum vor, der selbst erlernen soll, wie er am besten zum Ausgang findet. 

- Der **Agent** ist der Roboter. 

- Die **Umgebung** ist der Raum mit Wänden, potenziellen Hindernissen und dem Ausgang. 

- Der **Zustand** beschreibt die aktuelle Position des Roboters im Raum. 

- Die **Aktionen** bestehen aus vier Bewegungsmöglichkeiten: **oben, unten, links, rechts**. (in 2D-Darstellung)

- Die **Belohnung** beträgt **+1**, wenn der Roboter den Ausgang findet, und **-1**, wenn er gegen eine Wand läuft. 

- Die **Policy (Strategie)** bestimmt, welche Aktion der Roboter in welchem Zustand ausführt. 

- Die **Wertfunktion** bewertet, wie vorteihaft ein Zustand langfristig ist. 

Das Ziel des Roboters liegt darin, durch **Versuch und Irrtum** (Trial and Error) die optimale **Strategie** zu lernen, um den Ausgang so effizient wie möglich zu erreichen. 

---

**Kapitel 14: Markov-Entscheidungsprozesse (MDP)**

Die meisten der Reinforment Learning Probleme können mit dem Framework des Markov-Entscheidungsprozess (Markov Decision Process, MDP) gelöst werden. 

Der MDP ist ein mathematisches Framework für die Modellierung von Entscheidungsproblemen, bei denen die Ergebnisse teilweise zufällig und teilweise kontrollierbar sind. 

**Recap**
---------

**Markov-Eigenschaft** 

Ein Zustand S_t ist dann und nur dann ein Markov-Zustand, wenn folgendes zutrifft: 

.. math:: 
   P[S_(t+1) | S_t] = P(S_(t+1) | S_1,S_2, ...,S_t)

Das heißt, dass der aktuelle Zustand des Roboters nur von seinem unmittelbar vorhergehenden Zustand (bzw. dem vorherigen Zeitschritt) abhängt und nicht von den weiteren vorherigen Zuständen. 

**Markov-Prozess**

Ein Markov-Prozess wird definiert von (S,P), wobei S die Menge aller Zustände ist und P die Übergangswahrscheinlichkeit von Zustand s nach Zustand s' ist:

.. math:: 
   P_s_s' = P[S_t_+_1 = s' | S_t=s]

Das MDP-Framework besteht somit aus den folgenden Komponenten:
  
  1. **S** – Menge aller möglichen Zustände: alle möglichen und erlaubten Positionen im Raum.

  2. **A** – Menge aller möglichen Aktionen: die vier Bewegungsmöglichkeiten oben, unten, links, rechts.

  3. **P(s' | s, a)** – Übergangswahrscheinlichkeit von Zustand \(s\) zu \(s'\) nach Aktion \(a\): die Wahrscheinlichkeit, dass der Roboter nach der Aktion in einen neuen Zustand übergeht. 

  4. **R(s, a)** – Belohnung für das Ausführen von Aktion \(a\) in Zustand \(s\).

  5. **\(\gamma\) (Discount Factor)** – Faktor für zukünftige Belohnungen (zwischen 0 und 1).

Das Ziel ist, eine **optimale Policy** zu finden, die die **kumulierte langfristige Belohnung maximiert**.

---

**Kapitel 15: Wertbasierte Methoden – Q-Learning**

**Q-Learning Algorithmus:**

In "Q-Learning" bezieht sich "Q" auf die Zielfunktion, die der Algorithmus berechnen und optimieren soll: die erwartete Belohnung (die Qualität) einer Aktion, die in einem bestimmten Zustand durchgeführt wird.

- Speichert eine **Q-Tabelle**, die Werte für jede **(Zustand, Aktion)-Kombination** enthält.

- Aktualisiert sich mit der **Bellman-Gleichung:**
  
  .. math::
     Q(s,a) = Q(s,a) + \alpha (R + \gamma \max Q(s',a') - Q(s,a))
  
- Verwendet **Exploration vs. Exploitation:**

  - **Exploration:** Zufällige Aktionen testen, um neue Strategien zu entdecken.

  - **Exploitation:** Beste bekannte Aktion nutzen, um Belohnung zu maximieren.

**Deep Q-Networks (DQN):**

- Ersetzt die **Q-Tabelle durch ein neuronales Netz**, das **Q-Werte approximiert**.

- Verwendet Replay Buffers zur Speicherung vergangener Erfahrungen.

- Führt **Experience Replay** aus, um stabileres Lernen zu ermöglichen.

**Code-Beispiel: Einfaches Q-Learning für eine OpenAI Gym-Umgebung**

.. code-block:: python

   import numpy as np
   import gym

   # OpenAI Gym Umgebung
   env = gym.make("FrozenLake-v1", is_slippery=False)
   Q = np.zeros([env.observation_space.n, env.action_space.n])
   alpha = 0.1  # Lernrate
   gamma = 0.99  # Discount-Faktor
   epsilon = 0.1  # Zufällige Exploration

   for episode in range(1000):
       state = env.reset()[0]
       done = False
       while not done:
           if np.random.rand() < epsilon:
               action = env.action_space.sample()
           else:
               action = np.argmax(Q[state])
           
           next_state, reward, done, _, _ = env.step(action)
           Q[state, action] += alpha * (reward + gamma * np.max(Q[next_state]) - Q[state, action])
           state = next_state

   print("Q-Tabelle:")
   print(Q)
