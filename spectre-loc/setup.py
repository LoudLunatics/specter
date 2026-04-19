from setuptools import setup

setup(
    name='specter',          # Berubah jadi specter
    version='1.2.0',         # Versi baru
    packages=['specter'],    # Target folder baru
    install_requires=[
        'python-dotenv==1.0.1',
        'rich==13.7.1'
    ],
    entry_points={
        'console_scripts': [
            'specter=specter.cli:main',  # Perintah panggilannya sekarang 'specter'
        ],
    },
)
