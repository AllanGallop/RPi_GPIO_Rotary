from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='RPi_GPIO_Rotary',
    version='0.1.0',
    description='Simple module for getting values from KY040 and similar rotary encoders',
    long_description=long_description,
    url='https://github.com/AllanGallop/RPi_GPIO_Rotary',
    author='Allan Gallop',
    author_email='allangallop@gmail.com',
    keywords='PYPI rotary encoder KY040 raspberry pi GPIO',
    packages=find_packages(),
    install_requires=['RPi.GPIO']
)