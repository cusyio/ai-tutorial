Tag 3: Reinforcement Learning (RL)
=======================

**Recap der wichtigsten Themen des zweiten Tages**

- Wiederholung der zentralen Konzepte von **Neuronalen Netzen und Deep Learning**

- Verständnis der **Forwardpropagation und Backwardpropagation**

- **Loss Functions und ihre Rolle in Gradient Descent**

- Bedeutung von **Optimierungsverfahren** wie Adam und SGD

- Diskussion über Anwendungen von **CNNs für Bildklassifikation**

- Systemüberblick Training, Testing, Inferencing, CI/CD 

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

4. **Aktion (Action):** Die Entscheidung, die der Agent in einem Zustand trifft.

5. **Belohnung (Reward):** Signal, das die Qualität einer Aktion beschreibt.

6. **Policy (Strategie):** Funktion, die bestimmt, welche Aktion in welchem Zustand gewählt wird.

7. **Wertfunktion (Value Function):** Erwartete zukünftige Belohnung eines Zustands.

---

**Kapitel 14: Markov-Entscheidungsprozesse (MDP)**
- RL basiert auf **Markov-Entscheidungsprozessen (MDP)**, die aus folgendem bestehen:
  
  1. **S** – Menge aller möglichen Zustände.

  2. **A** – Menge aller möglichen Aktionen.

  3. **P(s' | s, a)** – Übergangswahrscheinlichkeit von Zustand \(s\) zu \(s'\) nach Aktion \(a\).

  4. **R(s, a)** – Belohnung für das Ausführen von Aktion \(a\) in Zustand \(s\).

  5. **\(\gamma\) (Discount Factor)** – Faktor für zukünftige Belohnungen (zwischen 0 und 1).

- Das Ziel ist, eine **optimale Policy** zu finden, die die **kumulierte langfristige Belohnung maximiert**.

---

**Kapitel 15: Wertbasierte Methoden – Q-Learning**

**Q-Learning Algorithmus:**

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
