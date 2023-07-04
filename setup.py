from setuptools import find_packages, setup
from typing import List
HYPEN_DOT = "-e ."
def get_requirements(file_path:str)->List[str]:
    '''
    This function reads the requirements.txt file and returns a list of requirements
    '''
    requirements  = []
    with open(file_path, "r") as f:
        requirements = f.readlines()
        requirements = [req.replace("\n", "") for req in requirements]
        if HYPEN_DOT in requirements:
            requirements.remove(HYPEN_DOT)
    return requirements

setup(

    name='my_package',
    version='0.1.0',
    author='Umair',
    author_email="umairejazbutt@gmail.com", 
    packages=find_packages(),
    install_requires = get_requirements("requirements.txt"),
)