from setuptools import setup, find_packages
from typing import List




#Declaring vaariables for setup function
PROJECT_NAME = "housing-predictor"
VERSION = "0.0.1"
AUTHOR = "venktat satish"
DESCRIPTION = "Tis is a first FSDS Nov batch Machine Learning Project"
REQUIREMENT_FILE_NAME = "requirements.txt"

def get_requirements_list()->List[str]:
    '''
    Description: This function is going to return list of requirements 
    mentioned in requirements.txt file 

    return: This function is going to return list which will contain name
    of libraries mentioned in the requirements.txt file
    '''
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        return requirement_file.readlines().remove("-e .")



setup(
name=PROJECT_NAME,
version=VERSION,
author=AUTHOR,
description=DESCRIPTION,
packages=find_packages(),
install_requires=get_requirements_list()
)

