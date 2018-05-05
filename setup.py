try:
    from setuptools import setup, Extension
except ImportError :
    raise ImportError("setuptools module required, please go to https://pypi.python.org/pypi/setuptools and follow the instructions for installing setuptools")


setup(
    name='dedupe-variable-textwmd',
    url='https://github.com/rizki96/dedupe-variable-textwmd',
    version='0.0.1',
    description='Word Mover Distance method for text field',
    packages=['dedupe.variables'],
    install_requires=['dedupe',
                      'gensim==1.0.1',
                      'pyemd==0.4.4'],
    license='The MIT License: http://www.opensource.org/licenses/mit-license.php'
    )