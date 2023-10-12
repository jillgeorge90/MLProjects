from setuptools import find_packages,setup
from typing import List

def get_require(file_path:str)->List[str]:
    """
    This will return list of requirements

    """
    HYPHON_DOT_E = "-e ."
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements =[req.replace("\n"," ")for req in requirements]

        if HYPHON_DOT_E in requirements:
            requirements.remove(HYPHON_DOT_E)
    return requirements


setup(
    name='MLProjects',
    version='0.0.1',
    author='George',
    author_email='jillgeorgevia@gmail.com',
    packages=find_packages(),
    install_requires=get_require('requirements.txt')
)