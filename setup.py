# -*- coding: utf-8 -*-

from setuptools import setup

setup(
    name         = 'PyChat',
    version      = '0.2.1',
    description  = 'A lightweight cross-platforms chat program',
    url          = 'http://github.com/Remigascou/PyChat',
    author       = 'Remi GASCOU',
    author_email = 'remi.gascou@gmail.com',
    license      = 'GPL2',
    packages     = [
        'PyChat',
        'PyChat/lib/core',
        'PyChat/lib/ui'
    ],
    zip_safe     = False
)
