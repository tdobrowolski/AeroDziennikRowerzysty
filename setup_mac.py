"""
Usage:
    python setup.py py2app

"""

from setuptools import setup

APP = ['Main.py']
DATA_FILES = ['baza.db', 'cyclelogo.ppm', 'ikona1.ppm', 'ikona2.ppm',  'ikona3.ppm', 'intro.ppm']
OPTIONS = {'iconfile':'Cycle.icns',}

setup(
    app = APP,
    data_files = DATA_FILES,
    options = {'py2app': OPTIONS},
    setup_requires = ['py2app'],
)
