from setuptools import setup, find_packages
from codecs import open
from os import path, chdir

here = path.abspath(path.dirname(__file__))

chdir(path.join(here, "src"))

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='ibunfuck',
    version='0.1',
    description='Removes unnecessary changes from iOS/OSX repositories',
    url='https://github.com/Reflejo/ib-unfuck-git',
    author='Martin Conte Mac Donell',
    author_email='Reflejo@gmail.com',
    license='MIT',
    install_requires=['unidiff', 'gitpython', 'lxml'],
    packages=["."],
    scripts=['../scripts/ibunfuck']
)

