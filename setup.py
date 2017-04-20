from setuptools import setup, find_packages

setup(
    name="yamldown",
    version="0.1.0",
    author="edouglass",
    author_email="edouglass@lbl.gov",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "pyYaml==3.12",
    ],
    long_description=open("README.md").read()
)
