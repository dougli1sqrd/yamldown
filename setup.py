from setuptools import setup, find_packages

setup(
    name="yamldown",
    version="0.1.8",
    packages=["yamldown"],
    author="edouglass",
    author_email="edouglass@lbl.gov",
    url="https://github.com/dougli1sqrd/yamldown",
    download_url="https://github.com/dougli1sqrd/yamldown/archive/0.1.8.tar.gz",
    description="Python library for loading and dumping \"yamldown\" (markdown with embedded yaml) files.",
    long_description=open("README.md").read(),
    keywords=["yaml", "markdown"],
    install_requires=[
        "pyYaml",
    ],
)
