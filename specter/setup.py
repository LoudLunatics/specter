from setuptools import setup, find_packages

setup(
    name='specter',
    version='1.2.0',
    # find_packages() akan otomatis mencari folder yang ada init.py nya
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'python-dotenv',
        'rich',
    ],
    entry_points={
        'console_scripts': [
            'specter=specter.cli:main',
        ],
    },
)
