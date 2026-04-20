from setuptools import setup, find_packages

setup(
    name="specter",
    version="1.2.0",
    # find_packages otomatis mencari folder 'specter' yang punya __init__.py
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'rich' # shodan dan python-dotenv resmi dihapus!
        # nmap tidak ditulis di sini karena dia aplikasi sistem, bukan paket Python
    ],
    entry_points={
        'console_scripts': [
            # Panggil fungsi main() di cli.py yang ada di dalam folder specter (-ER)
            'specter=specter.cli:main', 
        ],
    },
)