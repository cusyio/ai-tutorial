Changelog
=========

Alle nennenswerten Änderungen an diesem Projekt werden in dieser Datei
dokumentiert.

Das Format basiert auf `Keep a Changelog
<https://keepachangelog.com/en/1.0.0/>`_ und dieses Projekt hält sich an
`Calendar Versioning <https://calver.org>`_.

Die erste Zahl der Version ist das Jahr. Die zweite Zahl wird mit jeder Version
erhöht, beginnend bei 1 für jedes Jahr. Die dritte Zahl ist für Notfälle, wenn
wir Zweige für ältere Versionen starten müssen.

.. unreleased

Unreleased
----------

Changed
~~~~~~~

* **Dokumentation:** Projekt-URLs und README auf Repository AInvone/Intro-in-KI-Schulung umgestellt; PDF-Pfad auf ``docs/_build/latex/AITutorial.pdf`` korrigiert.
* **Dokumentation:** Beschreibung in pyproject.toml auf „Einführung in KI“ (ML, Deep Learning, RL, GenKI) erweitert.
* **Dokumentation:** Indices und Tabellen (genindex, modindex, search) auf der Startseite wieder aktiviert.
* **Dokumentation:** Tag-4-Toctree neu sortiert: GenAI-Einführung/Theorie/Infrastruktur/LLM zuerst, dann Ensemble & Churn, dann Agents, Regulatorik, Abschluss.
* **Build:** Sphinx-Version auf ``>=8,<9`` angehoben; nbsphinx_allow_errors auf False gesetzt (Notebooks sollen fehlerfrei laufen). Bei Build-Fehlern durch Notebooks in ``docs/conf.py`` vorübergehend wieder auf True setzen.
* **README:** Build-Anleitung vereinfacht; Hinweis auf ``pip install --group docs`` und PDF/EPUB-Pfad ergänzt.
* **docs/1intro/extra.rst:** Links durch direkte URLs zu Python4DataScience (NumPy, pandas) und PyViz (Matplotlib) ersetzt, damit die Links auch ohne Intersphinx funktionieren.

Added
~~~~~

* 🎉 Create initial project structure
