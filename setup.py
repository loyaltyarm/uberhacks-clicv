from setuptools import setup


setup(
    name='cliCV',
    version='1.0',
    py_modules=['clicv'],
    install_requires=[
        'Click',
        'colorama',
    ],
    entry_points='''
        [console_scripts]
        clicv=clicv:cli
    ''',
)
