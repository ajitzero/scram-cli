from setuptools import setup

setup(
    name="scram",
    version='0.1',
    py_modules=['scram'],
    install_requires=[
        'Click',
        'pyperclip',
    ],
    entry_points='''
        [console_scripts]
        scram=scram:cli
        scramx=scramx:cli
    ''',
)