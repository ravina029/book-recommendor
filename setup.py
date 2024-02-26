#this file is created using touch stup.py command in terminal
# stup.py will help us tyo create our entire application as a package and deploy in pypy. from there anybody can install and use it.

from setuptools import setup,find_packages
from typing import List
def get_requirements(file_path:str)->List[str]:
  '''this function will return the list of requirements
   '''

  HYPHEN_E_DOT='-e .'
  with open(file_path) as file_obj:
       requirements=file_obj.readlines()
       requirements=[req.replace("\n","")for req in requirements]

       if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

  return requirements        

with open('README.md','r', encoding='utf-8') as f:
    long_description=f.read()




setup(
    name='book recommendor',
    version='0.0.1',
    author='ravina',
    author_email='vermaravina029@gmail.com',
    description='small python package for book recommender system',
    long_description=long_description,
    long_description_content='text/markdown',
    url=f'https://github.com/ravina029/book-recommendor',
    project_urls={"Bug Tracker":f'https://github.com/ravina029/book-recommendor/issues',},
    package_dir={"":"src"},
    packages=find_packages(where="src"),
    install_requires=get_requirements('requirements.txt')
    )