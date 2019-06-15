from setuptools import setup, find_packages

setup(
    name='RPi_GPIO_Rotary',
    version='0.1.0',
    description='Simple module for getting values from KY040 and similar rotary encoders',
    url='https://github.com/AllanGallop/RPi_GPIO_Rotary',
    download_url='https://github.com/AllanGallop/RPi_GPIO_Rotary/archive/0.1.0.tar.gz',
    author='Allan Gallop',
    author_email='allangallop@gmail.com',
    keywords='rotary encoder KY040 raspberry pi GPIO',
    packages=find_packages(),
    install_requires=['RPi.GPIO'],
    classifiers=[
    'Development Status :: 4 - Beta',
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    ],
)