#!/usr/bin/env python
#-*- coding:utf-8 -*-

import os
from setuptools import setup, Extension, find_packages


try:
    from Cython.Build import cythonize
    with_cython = True
except ImportError:
    with_cython = False


dirname = os.path.abspath(__file__)[:-8]
dirname += ("/" if dirname[-1] != "/" else "") + "nngt/generation/"

ext = Extension(
    "nngt.generation._cconnect", # name of extension
    sources = [dirname + "cconnect.pyx", dirname + "func_connect.cpp"],
    extra_compile_args=["-std=c++11", "-fopenmp"],
    extra_link_args=["-std=c++11"],
    language="c++",
    include_dirs=[dirname],
    library_dirs = [dirname]
)

setup(
        name='nngt',
        version = '0.5',
        description = 'Package to study growth and activity of neural networks',
        package_dir={'': '.'},
        packages = find_packages('.'),

        # Include the non python files:
        package_data = { '': ['*.txt', '*.rst', '*.md', '*.default'] },

        # Requirements
        install_requires = [ 'numpy', 'scipy>=0.11', 'matplotlib' ],
        extras_require = {
            'PySide': ['PySide'],
            'PDF':  ["ReportLab>=1.2", "RXP"],
            'reST': ["docutils>=0.3"],
            'nx': ['networkx'],
            'ig': ['python-igraph']
        },
        entry_points = {
            #@todo
            #~ 'console_scripts': [
                #~ 'rst2pdf = nngt.tools.pdfgen [PDF]',
                #~ 'rst2html = nngt.tools.htmlgen'
            #~ ],
            #~ 'gui_scripts': [ 'netgen = nngt.gui.main.__main__:main [PySide]' ]
        },
        
        # Cython module
        ext_modules = cythonize([ext]) if with_cython else [],

        # Metadata
        url = 'https://github.com/Silmathoron/NNGT',
        author = 'Tanguy Fardet',
        author_email = 'tanguy.fardet@univ-paris-diderot.fr',
        license = 'GNU',
        keywords = 'neural network graph simulation NEST topology growth'
)
