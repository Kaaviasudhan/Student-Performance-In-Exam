#Purpose of setup.py - Responsible for entire ML project as a package
#py venv - py 3.12.2
from setuptools import find_packages,setup
from typing import List #function return in the form of list

#initalizing variable for .e
HYPEN_E_DOT='-e .'

def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]     #to remove "\n" while reading every line

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    
    return requirements


setup(
    name='Student-Performance-Analysis',
    version='0.0.1',
    author='Kaavi',
    author_email='kaaviasudhancit716@gmail.com',
    packages=find_packages(), #finds all __init__.py to create packages
    install_requires=get_requirements('requirements.txt')
)