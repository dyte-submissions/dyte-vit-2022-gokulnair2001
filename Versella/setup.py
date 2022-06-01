from setuptools import setup, find_packages

setup(
    name='Versella',
    version='0.0.0',
    packages=find_packages(),
    install_requires= [
        "click",
        "urlopen"
    ],
    entry_points='''
    [console_scripts]
    versella=cli:cli
    versellaX=cli:find
    '''
)
