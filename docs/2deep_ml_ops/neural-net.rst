Neuronale Netze und Deep Learning – Theorie
============================================

Grundlagen:
----------------------------------------------------------

Was sind künstliche neuronale Netze? Wie unterscheiden sie sich von klassischen ML-Modellen?

* Künstliche neuronale Netze bestehen aus **Schichten von Neuronen**, die durch gewichtete Verbindungen miteinander verbunden sind.
* Aufbau eines neuronalen Netzes: **Eingabeschicht, versteckte Schichten, Aktivierungsfunktionen, Ausgangsschicht.**
* Jedes Neuron führt eine Berechnung basierend auf einer **Aktivierungsfunktion** durch und gibt das Ergebnis an die nächste Schicht weiter.


.. figure:: ../_static/images/day2-deepLearn.png
   :alt: Illustration von Deep Neural Networks
   :align: center
   :width: 700px

   **Abbildung 1:** Deep Neural Networks, source: `Lamarr-Institute <https://lamarr-institute.org/blog/deep-neural-networks/>`_, https://lamarr-institute.org/wp-content/uploads/deepLearn_2_EN.png 


Wichtige Aktivierungsfunktionen:
::::::::::::::::::::::::::::::::

* **ReLU (Rectified Linear Unit):** 

Häufig in CNNs verwendet, eliminiert negative Werte.

* **Sigmoid:** 

Wandelt Werte in einen Bereich zwischen 0 und 1 um, nützlich für Wahrscheinlichkeitsprognosen.

* **Softmax:** 

Wird in Klassifikationsproblemen für mehr als zwei Klassen genutzt.


Fortgeschrittene Deep-Learning-Techniken:
::::::::::::::::::::::::::::::::::::::::::

* Convolutional Neural Networks (CNNs) für **Bildverarbeitung**.

Eine gute dynamische Darstellung, wie das Zusammenspiel zwischen den Schichten 
bei einem CNN funktioniert, kann in diesem Video gefunden werden: 
https://www.youtube.com/watch?v=ip2HYPC_T9Q 

* Recurrent Neural Networks (RNNs) für **Sequenz- und Textverarbeitung**.

* Transformer-Modelle für **NLP (z. B. BERT, GPT).**


Forwardpropagation (Vorwärtsdurchlauf):
----------------------------------------------------------

1. Die Eingabedaten werden in das Netzwerk eingespeist.

2. In jeder Schicht wird die gewichtete Summe der Eingänge berechnet:

   .. math::
      z = w_1 x_1 + w_2 x_2 + ... + w_n x_n + b

3. Diese gewichtete Summe wird durch eine **Aktivierungsfunktion** transformiert (z. B. ReLU, Sigmoid, Softmax), um **nicht-lineare Abhängigkeiten** abzubilden.

4. Die Ausgabe der einen Schicht wird als Eingabe an die nächste Schicht weitergegeben, bis die letzte Schicht erreicht ist.

5. Am Ende der Forward Propagation wird die Loss Function berechnet.


Loss Functions (Verlustfunktionen) und ihre Rolle:
----------------------------------------------------------

Eine **Loss Function** 

* misst die Differenz zwischen der Vorhersage des Modells und dem tatsächlichen Wert.
* gibt an, wie gut oder schlecht das Modell arbeitet.
* wird während der Backpropagation genutzt, um die Gewichte des Netzwerks zu aktualisieren.

Typische Loss Functions:
:::::::::::::::::::::::::

Mean Squared Error (MSE)
~~~~~~~~~~~~~~~~~~~~~~~~

Wird für **Regressionsprobleme** verwendet:

   .. math::
      MSE = \frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2

* Bestraft größere Fehler überproportional.

* Gut für kontinuierliche Werte wie Preisprognosen.

Cross-Entropy Loss
~~~~~~~~~~~~~~~~~~~~~~

Wird für **Klassifikationsprobleme** verwendet:

   .. math::
      L = -\sum y_i \log(\hat{y}_i)

* Erhöht die Strafe, wenn das Modell sehr sicher, aber falsch ist.

* Wird z. B. bei **Softmax-Klassifikationen** genutzt.

Zusammenhang zwischen Loss Function und Gradient Descent:
----------------------------------------------------------

* Gradient Descent ist der Algorithmus, der die Gewichte des Modells so anpasst, dass die Loss Function minimiert wird.

* Die Ableitung der Loss Function bestimmt die Richtung, in die die Gewichte aktualisiert werden.

Formel für das Gewicht-Update:
:::::::::::::::::::::::::::::::

Das Wichtigste an einem Modell sind die **Gewichte (weights)**. 
Diese werden während der **Backwardpropagation (Rückwärtsdurchlauf)**-Phase aktualisiert, 
indem man das Produkt der Learning-Rate (\alpha) und der Ableitung der Loss-Funktion 
von den aktuellen Gewichten subtrahiert: 

  .. math::
     w := w - \alpha \frac{\partial L}{\partial w}



Backwardpropagation (Rückwärtsdurchlauf):
----------------------------------------------------------

* Nachdem in der Forwardpropagation die Input-Daten durch das Neural Network propagiert sind, werden die Ausgaben des Networks mit den gewünschten Ausgaben verglichen. 
* Deren Differenz wird als der Fehler des Netzwerks in diesem Durchgang erachtet, d.h. Loss. 
* Dieser Fehler wird dann in der `Backwardpropagation <https://de.wikipedia.org/wiki/Backpropagation>`_ über die letzten Schicht (Ausgabeschicht) zurück zur Eingabeschicht durch das Netzwerk propagiert, um **die Gewichte der Neuronen zu aktualisieren**.

* Die Berechnung erfolgt mit Hilfe der **Kettenregel der Ableitungen**, um die Gradienten für jedes Gewicht zu bestimmen:

..   .. math::
..      rac{\partial L}{\partial w} = rac{\partial L}{\partial y} \cdot rac{\partial y}{\partial z} \cdot rac{\partial z}{\partial w}

* In jeder Epoche passt das Modell diese Parameter an und verringert so den Verlust, indem es dem Fehlergradienten folgt. 
`Backpropagation <https://www.geeksforgeeks.org/backpropagation-in-neural-network/>`_ verwendet häufig Optimierungsalgorithmen wie Gradientenabstieg (Gradient Descent) oder stochastischer Gradientenabstieg (stochastic Gradient Descent). 
* Der Algorithmus berechnet den Gradienten mit Hilfe der Kettenregel aus der Infinitesimalrechnung und kann so effektiv durch komplexe Schichten im neuronalen Netz navigieren, um die Kostenfunktion zu minimieren.

* Somit werden während der Backpropagation-Phase durch die Anwendung von z.B. **Gradientenabstiegsverfahrens (Gradient Descent)**  die Gewichte so angepasst, dass der Gesamtfehler des Netzwerks iterativ minimiert und somit das Modell optimiert wird.

