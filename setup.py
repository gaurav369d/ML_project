from setuptools import find_packages, setup
from typing import List

def get_requirments(file_path:str)-> List[str]:
    '''
    This Function will regturn the list of requirments
    '''
    requirements=[]

    with open(file_path) as file_obj:
        requirements=file_obj.readline()
        requirements=[req.replace('\n',"") for req in requirements]

    return requirements


setup(
    name="ML_Project",
    version="0.0.1",
    author="Gaurav",
    author_email="gauravborthakur369@gmail.com",
    packages=find_packages(),
    install_requires=get_requirments("requirements.txt")
)