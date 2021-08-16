"""
https://packaging.python.org/tutorials/packaging-projects/

"""
import setuptools

from wow_playground import project_properties

with open('README.md', 'r') as desc_file:
    long_description = desc_file.read()

with open('requirements.txt', 'r') as req_file:
    requirements_list = req_file.readlines()

setuptools.setup(
    name=project_properties.name,
    version=project_properties.version,

    description='',
    long_description=long_description,
    long_description_content_type='text/markdown',

    python_requires='>=3.7',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],

    packages=setuptools.find_packages(),
    install_requires=requirements_list,
    dependency_links=[],  # should be able to install AirSim or submodules from here
)
