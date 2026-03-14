Schnelleinstieg
===============

Status
------

.. image:: https://img.shields.io/github/contributors/AInvone/Intro-in-KI-Schulung.svg
   :alt: Contributors
   :target: https://github.com/AInvone/Intro-in-KI-Schulung/graphs/contributors
.. image:: https://img.shields.io/github/license/AInvone/Intro-in-KI-Schulung.svg
   :alt: License
   :target: https://github.com/AInvone/Intro-in-KI-Schulung/blob/main/LICENSE

Installation
------------

#. Auschecken:

   .. code-block:: console

      $ git clone https://github.com/AInvone/Intro-in-KI-Schulung.git
      $ cd Intro-in-KI-Schulung

#. Installieren von Python-Paketen:

   … auf Linux/macOS:

   .. code-block:: console

      $ python3 -m venv .venv
      $ . .venv/bin/activate
      $ python -m pip install --upgrade pip
      $ python -m pip install --group dev

   … auf Windows:

   .. code-block:: ps1con

      C:> py -m venv .venv
      C:> .\.venv\Scripts\activate.bat
      C:> python -m pip install --upgrade pip
      C:> python -m pip install --group dev

   Für den reinen Dokumentations-Build reicht die Gruppe ``docs``:

   .. code-block:: console

      $ python -m pip install --group docs

#. Erstellen der HTML-Dokumentation:

   Zum Erstellen der HTML-Dokumentation (inkl. Ausführung der Jupyter-Notebooks):

   .. code-block:: console

      $ sphinx-build -b html docs/ docs/_build/html/

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

* `GitHub <https://github.com/AInvone/Intro-in-KI-Schulung>`_

Pull-Requests
-------------

Wenn ihr Vorschläge für Verbesserungen und Ergänzungen habt, empfehlen wir euch,
einen `Fork <https://github.com/AInvone/Intro-in-KI-Schulung/fork>`_ unseres
`GitHub Repository <https://github.com/AInvone/Intro-in-KI-Schulung/>`_ zu
erstellen und eure Änderungen dort zu machen. Bevor ihr Commits macht,
überprüft, ob die pre-commit-Checks erfolgreich durchlaufen:

.. code-block:: console

   $ pre-commit install
