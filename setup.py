# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

from PROJECTNAME import __version__


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='sample',
    version=__version__,
    description='Sample template to be used for other repositories',
    long_description=readme,
    author='Matthew Vanhoutte',
    author_email='me@matthewvanhoutte.com',
    url='https://github.com/matthewvanhoutte/pytemplate',
    license=license,
    packages=find_packages(exclude=('tests', 'docs')),
    include_package_data=True,
    zip_safe=True
)

