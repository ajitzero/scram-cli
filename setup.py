from setuptools import setup

setup(
    name="scram",
    version='1.0',
    py_modules=['scram'],
    install_requires=[
        'Click',
        'pyperclip',
    ],
    entry_points='''
        [console_scripts]
        scram=scram:cli
    ''',
)