import shutil, os, subprocess
import site, sys
#from importlib import util
from setuptools import setup, find_packages
from setuptools.command.install import install

class CustomInstallCommand(install):
    def run(self):
        install.run(self)
        # Pega o diretorio bin 
       
        ANARCI_BIN = sys.executable
        print(sys.version)
        print(f'subprocess.__path__ --------> {self.exec_prefix}')
        print(f'os.getgwd-----> { os.getcwd() } ')
        print(f'sys.prefix -----> { sys.prefix } ')
        print(f'sys.exec_prefix -----> {sys.exec_prefix } ')
        print(f'sys.prefix + "/bin" -----> {sys.prefix + "/bin"}')
        print(sys.prefix +'/lib/python' +sys.version[:3] +'/site-packages')
        print(f'ANARCI_BIN ----: {ANARCI_BIN}')
        print(f'site.getsitepackages()[0], "anarci")-----: {site.getsitepackages()[0]}')
        print(f'ANARCI_BIN = sys.executable.split("python")[0]-----: {sys.executable}')
        print('sys.prefix -----> {sys.prefix}')
      

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
                     ('lib/python/anarci/dat/HMMs', ['lib/python/anarci/dat/HMMs/ALL.hmm', 
                              'lib/python/anarci/dat/HMMs/ALL.hmm.h3f',
                              'lib/python/anarci/dat/HMMs/ALL.hmm.h3i',
                              'lib/python/anarci/dat/HMMs/ALL.hmm.h3m',
                              'lib/python/anarci/dat/HMMs/ALL.hmm.h3p'])],
      include_package_data = True,
      # Coloca os binários no contexto da venv / env
      scripts=['bin/ANARCI'],
      cmdclass={"install": CustomInstallCommand, }, # Run post-installation routine
)

