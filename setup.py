from setuptools import setup, find_packages

setup(
    name='tp3-log3000',
    version='0.1.0',
    description='A simple calculator web app for LOG3000 TP3',
    author='Your Name',
    packages=find_packages(),
    install_requires=[
        'Flask',
        'pytest',
    ],
    include_package_data=True,
    python_requires='>=3.7',
)
