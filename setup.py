from setuptools import setup, find_packages

setup(
    name='EDSA3',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='EDSA example python package',
    long_description=open('README.md').read(),
    url='https://github.com/NaadimAnath/EDSA3.git',
    author='NaadimAnath',
    author_email='anathnaadim706@gmail.com'
)
