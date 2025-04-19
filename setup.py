from setuptools import find_packages, setup 
from typing import List

def get_requirements(file_path: str) -> List[str]:
    """
    Reads requirements.txt and returns a clean list of packages,
    excluding lines like '-e .'
    """
    requirements = []
    with open(file_path) as file_obj:
        for line in file_obj:
            clean_line = line.strip()
            if clean_line and not clean_line.startswith("-e"):
                requirements.append(clean_line)
    return requirements


setup(
    name="Student_Project",
    version="0.0.1",
    author="Sai Sri Movya Sonti",
    author_email="movya.ms@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)