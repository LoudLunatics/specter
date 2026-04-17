from setuptools import setup

setup(
    name='spectre-loc',
    version='1.0.2', # Kita naikkan ke 1.0.2 agar Pacman tahu ada update
    packages=['spectre'], # 🚨 CARA EKSPLISIT: Paksa Python membungkus folder 'spectre'
    install_requires=[
        'shodan==1.31.0',
        'python-dotenv==1.0.1',
        'rich==13.7.1'
    ],
    entry_points={
        'console_scripts': [
            'spectre-loc=spectre.cli:main',
        ],
    },
)
