from setuptools import setup, find_packages

setup(
    name="spectre-loc",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        'shodan',
        'python-dotenv',
        'rich'
    ],
    entry_points={
        'console_scripts': [
            'spectre-loc=spectre.cli:main', # Menghubungkan command terminal ke cli.py
        ],
    },
)