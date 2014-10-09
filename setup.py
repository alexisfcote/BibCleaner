from setuptools import setup, find_packages
import os


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name='bibCleaner',
    packages=find_packages(),
    version='0.2',
    description='bibtex file cleaner',
    author='Alexis Fortin-Côté',
    author_email='alexisfcote@gmail.com',
    long_description=read('README.txt'),
    url='https://pypi.python.org/pypi',
    keywords="bibtex latex bib clean",
    license='GPLv3',
    classifiers=[
        'Environment :: X11 Applications :: Qt',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: POSIX :: Linux',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python',
        'Topic :: Utilities'
    ],
    install_requires=['PyQt4'],
    entry_points={
        'console_scripts': [
            'BibCleaner=BibCleaner:main',
        ],
    },
)
