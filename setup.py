from setuptools import setup

setup(
    name="scram",
    version='0.1',
    py_modules=['scram'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        scram=scram:cli
    ''',
)