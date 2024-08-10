from setuptools import find_packages, setup
from typing import List

def get_requiremetns(filepath:str)->List[str]:
    requirements = []
    with open(filepath) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]

        return requirements

setup(
    name='WaferFaultDetection',
    version='0.0.1',
    author='Ankit',
    author_email='ankit1.saramati@south.du.ac.in',
    install_requires=get_requiremetns("requirements.txt"),
    packages=find_packages() # every folder in the root directory will be considered as a package
)
