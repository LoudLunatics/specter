from setuptools import setup, find_packages

setup(
    name="specter",
    version="1.2.0",
    # Kita tunjuk langsung folder 'specter' sebagai paket utamanya
    packages=['specter'],
    package_dir={'': '.'}, 
    include_package_data=True,
    install_requires=[
        'rich'
    ],
    entry_points={
        'console_scripts': [
            # Memanggil fungsi main di specter/cli.py
            'specter=specter.cli:main', 
        ],
    },
)
