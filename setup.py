from setuptools import setup, find_packages
from os.path import join, dirname

import print_date

root = dirname(__file__)


def _get_requirements():
    return open(join(root, 'requirements.txt')).read()


setup(
    name='print_date',
    version=print_date.__version__,
    packages=find_packages(),
    long_description=open(join(root, 'README.txt')).read(),

    entry_points={
        'console_scripts': [
            'print_date = print_date.scripts.main:main',
        ]
    },

    install_requires=_get_requirements()
)
