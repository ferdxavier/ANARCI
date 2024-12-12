import os, subprocess
from setuptools import setup
#from setuptools.command.install import install

def find_relative_path_HMMs():
    relative_path_hmms = 'lib/python/anarci/dat/HMMs'
    path_hmms = os.path.join(os.getcwd(), relative_path_hmms)
    itens_hmms = os.listdir(path_hmms)
    hmmr_files = []
    for item in itens_hmms:
        hmmr_files.append(relative_path_hmms +'/' +item)
    return hmmr_files

# Run the Pipeline script
def run_dependencies_by_pipelinesh():
    subprocess.run(["/bin/bash", "./build_pipeline/RUN_pipeline.sh"])

# Pre-installation routine
run_dependencies_by_pipelinesh()
relative_path_HMMs = find_relative_path_HMMs()

setup(name='anarci',
      version='1.3',
      description='Antibody Numbering and Receptor ClassIfication',
      author='James Dunbar',
      author_email='opig@stats.ox.ac.uk',
      url='http://opig.stats.ox.ac.uk/webapps/ANARCI',
      packages=['anarci'],
      package_dir={'anarci': 'lib/python/anarci'},
      # Copia os binário para o direto bin do ambiente
      data_files = [ ('bin', ['bin/muscle', 'bin/muscle_macOS', 'bin/ANARCI'] ), 
                     ('lib/python/anarci/dat/HMMs', relative_path_HMMs)
                    ],
      include_package_data = True,
      # Coloca os binários no contexto da venv / env
      scripts=['bin/ANARCI'],
      #cmdclass={"install": CustomInstallCommand, }, # Run post-installation routine
    )