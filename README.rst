Schnelleinstieg
===============

Status
------

.. image:: https://img.shields.io/github/contributors/cusyio/ai-tutorial.svg
   :alt: Contributors
   :target: https://github.com/cusyio/ai-tutorial/graphs/contributors
.. image:: https://img.shields.io/github/license/cusyio/ai-tutorial.svg
   :alt: License
   :target: https://github.com/cusyio/ai-tutorial/blob/main/LICENSE

Installation
------------

#. Auschecken:

   .. code-block:: console

      $ git clone https://github.com/cusyio/ai-tutorial.git
      $ cd ai-tutorial

#. Installieren von Python-Paketen:

   .. code-block:: console

      $ uv sync --frozen

   Zum Erstellen der Dokumentations wird zusätzlich die Abhängigkeitsgruppe
   ``docs`` benötigt:

   .. code-block:: console

      $ uv sync --frozen --group docs

#. Erstellen der HTML-Dokumentation:

   Zum Erstellen der HTML-Dokumentation (inkl. Ausführung der Jupyter-Notebooks):

   .. code-block:: console

      $ uv run sphinx-build -b html docs docs/_build/html

   Das Ergebnis liegt in ``docs/_build/html/``; die Startseite ist
   ``docs/_build/html/index.html``.

   .. note::
      Für PDF- oder EPUB-Export wird ggf. **pandoc** benötigt (z. B. unter
      Debian/Ubuntu: ``sudo apt install pandoc``).

#. Erstellen eines PDF:

   Für PDF wird eine LaTeX-Installation benötigt:

   … auf Debian/Ubuntu:

   .. code-block:: console

      $ sudo apt install texlive-latex-recommended texlive-latex-extra texlive-fonts-recommended latexmk

   … auf macOS (MacTeX):

   .. code-block:: console

      $ brew install --cask mactex

   Anschließend:

   .. code-block:: console

      $ cd docs/
      $ make latexpdf

   Das PDF liegt in ``docs/_build/latex/AITutorial.pdf``.

Folgt uns
---------

* `GitHub <https://github.com/cusyio/ai-tutorial>`_

Pull-Requests
-------------

Wenn ihr Vorschläge für Verbesserungen und Ergänzungen habt, empfehlen wir euch,
einen `Fork <https://github.com/cusyio/ai-tutorial/fork>`_ unseres `GitHub
Repository <https://github.com/cusyio/ai-tutorial/>`_ zu erstellen und eure
Änderungen dort zu machen.

Die Entwicklungsumgebung könnt ihr erstellen mit

.. code-block:: console

   $ uv sync --frozen --group dev

Bevor ihr Commits macht, überprüft, ob die
pre-commit-Checks erfolgreich durchlaufen:

.. code-block:: console

   $ pre-commit install
