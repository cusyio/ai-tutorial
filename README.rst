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
.. image:: https://readthedocs.org/projects/ai-tutorial/badge/?version=latest
   :alt: Docs
   :target: https://ai-tutorial.readthedocs.io/de/latest/

Installation
------------

#. Auschecken:

   .. code-block:: console

      $ git clone git@github.com:cusyio/ai-tutorial.git

#. Installieren von Python-Paketen:

   … auf Linux/macOS:

   .. code-block:: console

      $ python3 -m venv .venv
      $ . .venv/bin/activate
      $ python -m pip install --upgrade pip
      $ python -m pip install -e ".[dev]"

   … auf Windows:

   .. code-block:: ps1con

      C:> py -m venv .venv
      C:> .\.venv\Scripts\activate.bat
      C:> python -m pip install --upgrade pip
      C:> python -m pip install -e ".[dev]"

#. Erstellen der HTML-Dokumentation:

   .. note::
      pandoc muss installiert sein.

      … auf Debian/Ubuntu:

      .. code-block:: console

         $  sudo apt install pandoc

   Zum Erstellen der HTML-Dokumentation führt den folgenden Befehl aus:

   .. code-block:: console

      $ sphinx-build -ab html docs/ docs/_build/html/

#. Erstellen eines PDF:

   Zum Erstellen einer PDF-Dokumentation benötigt ihr zusätzliche Pakete, die
   ihr installieren könnt

   … auf Debian/Ubuntu mit

   .. code-block:: console

      $ sudo apt install texlive-latex-recommended texlive-latex-extra texlive-fonts-recommended latexmk

   … auf macOS mit

   .. code-block:: console

      $ brew cask install mactex
      …
      🍺  mactex was successfully installed!
      $ curl --remote-name https://www.tug.org/fonts/getnonfreefonts/install-getnonfreefonts
      $ sudo texlua install-getnonfreefonts
      …
      mktexlsr: Updating /usr/local/texlive/2020/texmf-dist/ls-R...
      mktexlsr: Done.

   Anschließend könnt ihr ein PDF generieren mit:

   .. code-block:: console

    $ cd docs/
    $ make latexpdf
    …
    The LaTeX files are in _build/latex.
    Run 'make' in that directory to run these through (pdf)latex
    …

   Das PDF findet ihr dann in ``docs/_build/latex/pythonbasics.pdf``.

Folgt uns
---------

* `GitHub <https://github.com/cusyio/ai-tutorial>`_

Pull-Requests
-------------

Wenn ihr Vorschläge für Verbesserungen und Ergänzungen habt, empfehlen wir euch,
einen `Fork <https://github.com/cusyio/ai-tutorial/fork>`_ unseres
`GitHub Repository <https://github.com/cusyio/ai-tutorial/>`_ zu
erstellen und eure Änderungen dort zu machen. Bevor ihr Commits macht,
überprüft, ob die pre-commit-Checks erfolgreich durchlaufen:

.. code-block:: console

   $ cd ai-tutorial
   $ pre-commit install
