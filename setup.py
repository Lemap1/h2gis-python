from setuptools import find_packages, setup

setup(
    name='h2gis',
    packages=find_packages(),
    version='0.0.1',
    description='A python library to use a h2gis database',
    author='Lemap',
    setup_requires=['pytest-runner'],
    tests_require=['pytest==4.4.1'],
)