"""Configuração do Sphinx para a documentação do StandAuto."""

import os
import sys

# Permite ao Sphinx encontrar os módulos Python (que estão na pasta acima de docs/)
sys.path.insert(0, os.path.abspath(".."))

# -- Informação do projeto ---------------------------------------------------
project = "StandAuto"
author = "Marcio Galamba, David Silva, Laurindo Lila"
copyright = "2026, " + author
version = "1.0"
release = "1.0.0"

# -- Configuração geral ------------------------------------------------------
extensions = [
    "sphinx.ext.autodoc",   # lê as docstrings do código
    "sphinx.ext.napoleon",  # entende docstrings no formato Google (Args:, Returns:)
    "sphinx.ext.viewcode",  # adiciona links para o código fonte
]
napoleon_google_docstring = True
napoleon_numpy_docstring = False
autodoc_member_order = "bysource"

language = "pt_PT"
exclude_patterns = ["_build"]

# -- Saída HTML --------------------------------------------------------------
html_theme = "sphinx_rtd_theme"
html_title = "StandAuto — Documentação"