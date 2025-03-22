from setuptools import setup, find_packages

setup(
    name='my_awesome_lib',
    version='1.0.0',
    description='Biblioteka Python do operacji na danych, tekstach i obliczeń matematycznych.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Przemysław Kierasinski',
    url='https://github.com/Preziu97/zadanie3',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    install_requires=[
    ],
    python_requires='>=3.6',
)
