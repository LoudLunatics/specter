from setuptools import setup, find_packages

setup(
    name='specter',
    version='1.2.0',
    # find_packages() akan otomatis mencari folder yang punya init.py
    packages=find_packages(), 
    include_package_data=True,
    install_requires=[
        'python-dotenv',
        'rich',
    ],
    entry_points={
        'console_scripts': [
            # Artinya: panggil fungsi main() di dalam file cli.py yang ada di folder specter
            'specter=specter.cli:main', 
        ],
    },
)
