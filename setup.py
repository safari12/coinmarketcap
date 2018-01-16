from setuptools import setup

with open('requirements.txt') as requirements:
    install_requires = requirements.read()

with open('test-requirements.txt') as test_requirements:
    tests_require = test_requirements.read()

setup(
    name='coinmarketcap',
    version='1.0.0',
    description='Coinmarketcap Wrapper',
    url='git@github.com:safari12/coinmarketcap.git',
    author='Reza Safari',
    author_email='rsafari.s@gmail.com',
    packages=['coinmarketcap', 'coinmarketcap.api'],
    install_requires=install_requires,
    tests_require=tests_require,
    keywords='coinmarketcap cryptocurrency bitcoin'
)
