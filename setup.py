from setuptools import setup, find_packages

setup(
    name='specter',
    version='1.2.0',
    description='Ghost Network Recon Engine (Standalone Nmap Scanner)',
    author='LoudLunatics',
    # find_packages() otomatis mencari folder yang punya init.py
    packages=find_packages(),
    # Menginstruksikan Python untuk menyertakan file non-python jika ada
    include_package_data=True,
    python_requires='>=3.6',
    install_requires=[
        'python-dotenv',
        'rich',
        # nmap tidak perlu ditulis di sini karena diurus oleh pacman (depends)
    ],
    entry_points={
        'console_scripts': [
            # perintah_di_terminal = nama_folder.nama_file:nama_fungsi
            'specter=specter.cli:main',
        ],
    },
)
