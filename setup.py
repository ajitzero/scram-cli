from setuptools import setup

setup(
    name="scram",
    version='1.0',
    py_modules=['scram', 'encoder'],
    install_requires=[
        'Click',
        'Pyperclip',
    ],
    entry_points='''
        [console_scripts]
        scram=scram:cli
    ''',
)