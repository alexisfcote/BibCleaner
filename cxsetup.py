import sys
from cx_Freeze import setup, Executable
import os


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"packages": ["BibCleaner"], "include_files": ["favicon.png"]} 


# GUI applications require a different base on Windows (the default is for a
# console application).
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(name="BibCleaner",
      version="0.3",
      description='bibtex file cleaner',
      author='Alexis Fortin-Côté',
      author_email='alexisfcote@gmail.com',
      url='https://github.com/alexisfcote/BibCleaner',
      long_description=read('README.txt'),
      options={"build_exe": build_exe_options},
      executables=[Executable("BibCleaner.py", base=base)])
