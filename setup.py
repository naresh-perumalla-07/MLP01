from setuptools import find_packages,setup

from typing import List

HYPEN='-e .'

def get_req(file_path:str)->List[str]:

    require=[]

    with open('requirements.txt')as file_obj:
        require=file_obj.readlines()
        require=[req.replace("\n","")for req in require]

        if HYPEN in require:
            require.remove(HYPEN)

    return require


setup(
    name="mlp01",
    version="0.0.1",
    author="naresh",
    author_email="naresh53@gmail.com",
    packages=find_packages(),
    install_requires=get_req("requirements.txt")
)

