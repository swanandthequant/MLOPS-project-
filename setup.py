# ...existing code...
from setuptools import setup, find_packages
from typing import List

def get_requirements(file_path: str) -> List[str]:
    requirements_lst: List[str] = []
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            for line in lines:
                requirements = line.strip()
                # Ignoring empty lines and -e.
                if requirements and requirements != '-e .':
                    requirements_lst.append(requirements)

    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")

    return requirements_lst

setup(
    name="network_security_project",
    version="0.1",
    author="Swanand Patil",
    author_email="swanandpatil409@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements('requirement.txt')
)
# ...existing code...

                    
