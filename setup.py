"""
A Python3 program that takes binary MARC records/lines (e.g. originally stored in a JSON value) as input and replace some characters in it to be really binary MARC compatible.
"""

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(name='replacemarcchars',
      version='0.0.1',
      description='a Python3 program that takes binary MARC records/lines (e.g. originally stored in a JSON value) as input and replace some characters in it to be really binary MARC compatible.',
      url='https://github.com/slub/replacemarcchars',
      author='Bernhard Hering, Bo Ferri',
      author_email='bernhard.hering@slub-dresden.de, zazi@smiy.org',
      license="Apache 2.0",
      packages=[
          'replacemarcchars',
      ],
      package_dir={'replacemarcchars': 'replacemarcchars'},
      install_requires=[
          'argparse>=1.4.0',
      ],
      entry_points={
          "console_scripts": ["replacemarcchars=replacemarcchars.replacemarcchars:run"]
      }
      )
