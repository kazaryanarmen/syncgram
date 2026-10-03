# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import sys

# Указываем путь к корню проекта (на два уровня выше от docs/source),
# чтобы Sphinx мог импортировать модуль SyncGram
sys.path.insert(0, os.path.abspath("../../"))

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'SyncGram'
copyright = '2026, Armen'
author = 'Armen'
release = '0.0.3'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',    # Автоматическое чтение докстрингов из кода
    'sphinx.ext.viewcode',   # Ссылки на исходный код в документации
    'sphinx.ext.napoleon',   # Поддержка стилей Google / NumPy для докстрингов
]

templates_path = ['_templates']
exclude_patterns = []

language = 'en'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# Тема Read the Docs
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']