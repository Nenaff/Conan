#!/usr/bin/env python

from setuptools import setup, find_packages

requirements = [x.strip() for x in open("requirements.txt", "r").readlines()]

setup(name='Conanmail',
      version='1.0.17',
      description='Helping you delete your old accounts',
      author='Nenaff',
      author_email='frightful.steam416@4wrd.cc',
      packages=find_packages(),
      url='https://github.com/Nenaff/Conan',
      install_requires=requirements,
      package_data={'conan': ['IMAP.json', 'web/*']},
      entry_points={
            'console_scripts': [
                    'conan = conan.main:main'
            ]
        },
      python_requires='>=3.6'
)