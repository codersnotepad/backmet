from setuptools import setup, find_packages

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

requirements = ["numpy>=1.18.1", "matplotlib>=3.1.3"]

setup(
    name="backmet",
    version="0.0.1",
    author="Timote WB",
    author_email="timote.wb@gmail.com",
    description="A collection of backtest metric functions.",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/codersnotepad/techind",
    packages=find_packages(),
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
)
