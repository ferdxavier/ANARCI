import shutil, os, subprocess
import site, sys
#from importlib import util
from setuptools import setup, find_packages
from setuptools.command.install import install

class CustomInstallCommand(install):
    def run(self):
        install.run(self)
      

setup(name='anarci',
      version='1.3',
      description='Antibody Numbering and Receptor ClassIfication',
      author='James Dunbar',
      author_email='opig@stats.ox.ac.uk',
      url='http://opig.stats.ox.ac.uk/webapps/ANARCI',
      packages=['anarci'],
      package_dir={'anarci': 'lib/python/anarci'},
      # Copia os binário para o direto bin do ambiente
      data_files = [ ('bin', ['bin/muscle', 'bin/muscle_macOS', 'bin/ANARCI']), 
                     ('lib', os.listdir(os.getcwd() +'/lib/python/anarci/dat/HMMs'))],
                     """
                              ['lib/python/anarci/dat/HMMs/ALL.hmm', 
                              'lib/python/anarci/dat/HMMs/ALL.hmm.h3f',
                              'lib/python/anarci/dat/HMMs/ALL.hmm.h3i',
                              'lib/python/anarci/dat/HMMs/ALL.hmm.h3m',
                              'lib/python/anarci/dat/HMMs/ALL.hmm.h3p'])],
                     """
      include_package_data = True,
      # Coloca os binários no contexto da venv / env
      scripts=['bin/ANARCI'],
      cmdclass={"install": CustomInstallCommand, }, # Run post-installation routine
)
