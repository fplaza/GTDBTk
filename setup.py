#!/usr/bin/env python

from setuptools import setup

import os


def version():
    setupDir = os.path.dirname(os.path.realpath(__file__))
    versionFile = open(os.path.join(setupDir, 'src', 'VERSION'))
    return versionFile.read().strip()

setup(
    name='gtdbtk',
    version=version(),
    author='Pierre-Alain Chaumeil and Donovan Parks',
    author_email='p.chaumeil@uq.edu.au',
    maintainer='Pierre-Alain Chaumeil and Donovan Parks',
    maintainer_email='donovan.parks@gmail.com',
    packages=['gtdbtk', 'gtdbtk.config', 'gtdbtk.external'],
    scripts=['bin/gtdbtk'],
    package_data={'gtdbtk': ['VERSION']},
    url='http://pypi.python.org/pypi/gtdbtk/',
    license='GPL3',
    description='A toolkit for assigning objective taxonomic classifications to bacterial and archaeal genomes.',
    classifiers=[
          'Development Status :: 4 - Beta',
          'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
          'Natural Language :: English',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Topic :: Scientific/Engineering :: Bio-Informatics',
          ],
    install_requires=[],
)