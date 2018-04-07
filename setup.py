# Written by Sergio La Rosa (sergio.larosa89@gmail.com)
# and John Leonardo (hey@jdleo.me)
# Part of "pydevrant" package
# https://github.com/SergioLaRosa/pydevrant

from setuptools import setup

try:
   import pypandoc
   long_description = pypandoc.convert('README.md', 'rst')
except (IOError, ImportError):
   long_description = ''

setup(
    name='pydevrant',
    version='0.2',
    description='Unofficial Python wrapper for the public devRant API',
    long_description=long_description,
    url='https://github.com/SergioLaRosa/pydevrant',
    author='Sergio La Rosa',
    author_email='sergio.larosa89@gmail.com',
    license='MIT',
    packages=['pydevrant'],
    install_requires=['requests'],
    zip_safe=False)
