from setuptools import setup, find_packages

with open("README.md", 'r') as f:
    long_description = f.read()

def parse_requirements(filename):
    with open(filename, 'r') as f:
        return [line.strip() for line in f if line.strip() and not line.startswith('#')]

setup(
    name='crocolake-python',
    version='0.0.1',
    description='Jupyter notebooks to use CrocoLake',
    license="GNU GPLv3",
    long_description=long_description,
    author='Enrico Milanese',
    author_email='enrico.milanese@whoi.edu',
    packages=find_packages(),
    install_requires=[
        'argopy==0.1.15',
        'bokeh',
        'cartopy',
        'dask',
        'dask[dataframe]',
        'distributed',
        'gsw',
        'jupyterlab',
        'matplotlib',
        'numpy==1.26.4',
        'pandas',
        'psutil==5.9.8',
        'pyarrow',
        'pytest',
        'setuptools',
        'tqdm',
        'urllib3==1.26.6',
        'xarray',
    ],
    entry_points={
        'console_scripts': [
            'download_db = scripts.download_db:main',
        ],
    },
)
