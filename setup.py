from setuptools import find_packages, setup
from typing import List

def get_requirements()->List[str]:
    """
    This function returns the list of requirements
    """
    requirement_list:List[str]=[]

    try:
        # open and read requirements.txt file
        with open('requirements.txt','r') as file:
            # Read lines from the file
            lines = file.readlines()

            # process each lines
            for line in lines:
                # strip whitespace and newline characters
                requirement = line.strip()
                #Ignore empty lines and -e .
                if requirement and requirement !='-e .':
                    requirement_list.append(requirement)
    except FileNotFoundError:
        print("requirements.txt. file not found")    



    return requirement_list
print(get_requirements)   


setup(
    name=   'AI-TRAVEL-PLANNER'
    version="O.O.1",
    author="Eby Thomas",
    author_email="ebykachappillil@gmail.com",
    install_requires= get_requirements
)