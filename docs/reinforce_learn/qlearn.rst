Wertbasierte Methoden – Q-Learning
-------------------------------------

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
           Q[state, action] += alpha * (
               reward + gamma * np.max(Q[next_state]) - Q[state, action]
           )
           state = next_state

   print("Q-Tabelle:")
   print(Q)
