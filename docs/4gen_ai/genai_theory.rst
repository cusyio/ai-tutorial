Theorie (Mathematik) hinter Generativer KI
==========================================

Wahrscheinlichkeitsmodelle
    Grundlagen der statistischen Modellierung.  
Transformer-Architektur
    Encoder-Decoder-Strukturen, Attention-Mechanismen und Selbstaufmerksamkeit.
Optimierungsalgorithmen
    Überblick über gängige Verfahren wie Adam und ihre mathematischen
    Grundlagen.

Wahrscheinlichkeitsmodelle
--------------------------

Statistische Modellierung bilden die mathematische Grundlage hinter der
Generativen KI. Generative KI-Modelle basieren auf dem Prinzip, die zugrunde
liegende Wahrscheinlichkeitsverteilung der Trainingsdaten zu erlernen. Dabei
wird angenommen, dass die beobachteten Daten aus einer bestimmten, aber oft
unbekannten Verteilung stammen. Durch die Anwendung von Konzepten wie der
Maximum-Likelihood-Schätzung und der Minimierung der Kreuzentropie wird
versucht, diese Verteilung zu approximieren.  Dies bildet die Grundlage dafür,
dass das Modell anschließend in der Lage ist, neue, statistisch konsistente
Datenpunkte zu generieren, die den Mustern und Strukturen der Trainingsdaten
entsprechen.

Generative Modelle basieren darauf, die zugrunde liegende
Wahrscheinlichkeitsverteilung der Daten zu approximieren. Dabei geht man davon
aus, dass jedes Datenbeispiel \(x\) mit einer Wahrscheinlichkeit \(P(x)\) aus
einer (meist unbekannten) Verteilung stammt. Das Ziel ist es, ein Modell mit
Parametern \(\theta\) so anzupassen, dass es diese Verteilung möglichst gut
erfasst.

Ein gängiger Ansatz hierfür ist die **Maximum-Likelihood-Schätzung (MLE)**. Die
Likelihood-Funktion für \(N\) unabhängige Datenbeispiele lautet:

.. math::
   L(\theta) = \prod_{i=1}^{N} P(x_i; \theta)

Statt direkt diese Funktion zu maximieren, wird oft der negative Log-Likelihood
minimiert:

.. math::
   -\sum_{i=1}^{N} \log(P(x_i; \theta))

In der Praxis wird häufig die **Kreuzentropie** (`Cross-Entropy
<https://de.wikipedia.org/wiki/Kreuzentropie>`_) als Verlustfunktion verwendet,
um den Unterschied zwischen der wahren Datenverteilung und der vom Modell
geschätzten Verteilung zu quantifizieren.

Transformer-Architektur
-----------------------

Die Transformer-Architektur bildet das Rückgrat moderner generativer Modelle und
hat die Art und Weise revolutioniert, wie Sequenzdaten verarbeitet werden –
insbesondere in der Generierung von Texten. Sie verzichtet auf rekurrente
Strukturen und setzt stattdessen vollständig auf Attention-Mechanismen. 

Die wichtigsten Bestandteile dieser Architektur sind:

Self-Attention, Multi-Head-Attention und Feed-Forward-Netzwerke. 

Self-Attention
~~~~~~~~~~~~~~

Im Zentrum steht das Konzept der Selbstaufmerksamkeit (Self-Attention), das dem
Modell ermöglicht, Beziehungen zwischen allen Elementen einer Eingabesequenz
simultan zu berücksichtigen. 

Jeder Eingabesequenz werden drei unterschiedliche Vektorrepräsentationen
zugeordnet:

- **Query (Q)**
- **Key (K)**
- **Value (V)**

Die Self-Attention berechnet, wie stark jedes Element einer Sequenz mit allen
anderen in Beziehung steht. Dies erfolgt über die folgende Berechnung:

.. math::
   \text{Attention}(Q, K, V) = \text{softmax}\left(\frac{QK^T}{\sqrt{d_k}}\right)V

Hierbei ist \(d_k\) die Dimension der Key-Vektoren. Die Division durch
\(\sqrt{d_k}\) verhindert, dass die resultierenden Werte zu groß werden und die
Softmax-Funktion verzerrt.

Multi-Head-Attention
~~~~~~~~~~~~~~~~~~~~

Die Multi-Head-Attention erlaubt es dem Modell, verschiedene Aspekte der
Beziehungen in parallelen "Aufmerksamkeits-Köpfen" zu betrachten.

Anstatt nur eine einzige Attention-Berechnung durchzuführen, wird der
Mechanismus in mehrere parallele "Köpfe" (Heads) aufgeteilt. Jeder Kopf führt
eine eigene Attention-Berechnung durch und fokussiert dabei auf unterschiedliche
Aspekte der Eingabesequenz. Die Resultate der einzelnen Köpfe werden
anschließend zusammengeführt, um eine reichhaltige, kontextabhängige Darstellung
zu erhalten.


Feed-Forward-Netzwerke
~~~~~~~~~~~~~~~~~~~~~~

Nach der Attention folgt ein vollständig verbundenes Feed-Forward-Netzwerk, das
positionweise auf jede Eingaberepräsentation angewandt wird. Typischerweise
besteht dieses Netzwerk aus zwei linearen Transformationen mit einer
*nichtlinearen* Aktivierungsfunktion (z. B. ReLU) dazwischen, die für die
Modellierung komplexer Zusammenhänge notwendig sind:

.. math::
   \text{FFN}(x) = \max(0, xW_1 + b_1)W_2 + b_2

Diese Schicht hilft dabei, die aus der Attention extrahierten Merkmale weiter zu
verarbeiten und komplexe nichtlineare Zusammenhänge zu modellieren.

Somit ermöglichen diese Mechanismen es, längere Abhängigkeiten und feinkörnige
Details in Sequenzdaten zu erfassen, was wesentlich zur Qualität der generierten
Inhalte beiträgt.

Zusätzliche Elemente
~~~~~~~~~~~~~~~~~~~~

Residual-Verbindungen
    Diese addieren den Eingang einer Schicht zu ihrem Ausgang, um den
    Informationsfluss zu verbessern und das Verschwinden von Gradienten zu
    verhindern.
Layer-Normalization
    Eine Normierungstechnik, die dazu beiträgt, die Stabilität und Effizienz des
    Trainings zu erhöhen.

Ein typischer Transformer-Block besteht somit aus:

#. Multi-Head-Self-Attention
#. Add & Norm (Residual-Verbindung plus Layer-Normalization)
#. Feed-Forward-Netzwerk
#. Add & Norm (erneut Residual-Verbindung plus Layer-Normalization)


.. figure:: ../_static/images/04_transformer_diagram.png
   :alt: Transformer-Modellarchitektur
   :align: center
   :width: 700px

   **Abbildung 1:** Transformer-Modellarchitektur mit originaler Position der
   Layer-Normalisierung. [#]_ [#]_

Optimierungsalgorithmen
-----------------------

Der Trainingsprozess generativer Modelle (so wie bei generell allen
Deep-Learning-Modellen) basiert auf iterativen Optimierungsmethoden, bei denen
die Modellparameter so angepasst werden, dass der Fehler (Verlustfunktion)
zwischen den generierten und den echten Daten minimiert wird.  Zentral hierbei
ist der Einsatz von Gradientenabstiegsverfahren. Neben dem klassischen
Gradientenabstieg existieren verschiedene weiterentwickelte Algorithmen, die
adaptive Lernraten und Momentum nutzen.

Grundlegender Gradientenabstieg
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Beim grundlegenden Gradientenabstieg wird bei jedem Schritt die Parameteraktualisierung wie folgt durchgeführt:

.. math::
   \theta_{t+1} = \theta_t - \eta \nabla L(\theta_t)

wobei \(\eta\) die Lernrate ist und \(\nabla L(\theta_t)\) den Gradienten der Verlustfunktion bezüglich der Parameter \(\theta_t\) darstellt.

AdaGrad
~~~~~~~

AdaGrad passt die Lernrate für jeden Parameter individuell an, indem es die Summe der Quadrate der bisherigen Gradienten berücksichtigt. Für den Parameter \(\theta_i\) erfolgt die Aktualisierung:

.. math::
   \theta_{t+1} = \theta_t - \frac{\eta}{\sqrt{G_{t,ii} + \epsilon}} \nabla \theta_t

Dabei akkumuliert \(G_{t,ii}\) die Summe der Quadrate der Gradienten für \(\theta_i\) bis zum Zeitpunkt \(t\) und \(\epsilon\) ist eine kleine Konstante zur Vermeidung einer Division durch Null. AdaGrad ist besonders nützlich bei spärlichen Daten, führt aber manchmal zu einer zu schnellen Reduktion der Lernrate.

RMSProp
~~~~~~~

RMSProp modifiziert AdaGrad, indem es statt der kumulierten Summe einen exponentiell gewichteten gleitenden Durchschnitt der quadratischen Gradienten verwendet. Dies verhindert, dass die Lernrate zu stark abnimmt:

.. math::
   E[g^2]_t = \gamma E[g^2]_{t-1} + (1-\gamma)(\nabla \theta_t)^2

.. math::
   \theta_{t+1} = \theta_t - \frac{\eta}{\sqrt{E[g^2]_t + \epsilon}} \nabla \theta_t

Hierbei ist \(\gamma\) ein Zerfallsfaktor, der bestimmt, wie stark frühere Gradienten gewichtet werden.

Adam (Adaptive Moment Estimation)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Adam kombiniert die Ideen von RMSProp mit der Integration von Momentum. Es
berechnet sowohl einen gleitenden Durchschnitt der Gradienten als auch der
quadrierten Gradienten:

.. math::
   m_t = \beta_1 m_{t-1} + (1-\beta_1) \nabla \theta_t

.. math::
   v_t = \beta_2 v_{t-1} + (1-\beta_2)(\nabla \theta_t)^2

Da die Schätzungen in den ersten Schritten verzerrt sein können, werden sie wie folgt korrigiert:

.. math::
   \hat{m}_t = \frac{m_t}{1-\beta_1^t}, \quad \hat{v}_t = \frac{v_t}{1-\beta_2^t}

Die Parameter werden dann aktualisiert mittels:

.. math::
   \theta_{t+1} = \theta_t - \eta \frac{\hat{m}_t}{\sqrt{\hat{v}_t} + \epsilon}

Adam vereint somit die Vorteile von AdaGrad und RMSProp und ist weit verbreitet, weil es die Lernraten dynamisch anpasst und stabile Konvergenzen auch in tiefen Netzwerken ermöglicht.

Die Wahl und Konfiguration des Optimierungsalgorithmus ist entscheidend für die Trainingsdynamik und die Leistungsfähigkeit des endgültigen Modells.

----

.. rubric:: Footnotes

.. [#] Transformer-wikipedia: https://de.wikipedia.org/wiki/Transformer_%28Maschinelles_Lernen%29#/media/Datei:Transformer,_full_architecture.png 
.. [#] Transformer-diagram: https://raw.githubusercontent.com/dvgodoy/dl-visuals/main/Transformers/full_transformer.png 
