#!/usr/bin/env python
from distutils.core import setup

setup(
    name='p_toolkit',
    version='v1.0',
    author='Amy Goldlist, Veronique Mulholland and Esteban Angel',
    packages=['p_toolkit'],
    author_email= 'na',
    license='MIT',
    description='A toolkit for adjusting and visualizing p values.',
    url = ['https://github.com/UBC-MDS/p_toolkit_Python'],
    download_url = 'https://github.com/UBC-MDS/p_toolkit_Python/archive/3.0.4.tar.gz',
    keywords = ['pvalues'],
    install_requires=['numpy', 'pandas']
    )
