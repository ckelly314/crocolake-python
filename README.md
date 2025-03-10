## CrocoLake-Python

CrocoLake-Python is a collection of Jupyter notebooks that shows how to interface with CrocoLake and Argo's parquet databases with Python.

### Table of Contents
1. [Usage](#usage)
2. [Databases](#databases)
3. [Contact](#contact)

### Usage
To install the necessary packages, run:

``` sh
pip install .
```

You can then launch any notebook from the `notebooks` folder and execute it. Each example needs a specific dataset, and contains code to download it to your local machine.

Note that there are a couple of ways to load parquet datasets in a dataframe in Python: using `pyarrow` and using `dask`. Examples 1 and 2 show both, while the other examples use the one that in my experience is most efficient (i.e. `dask`).

### Databases

The following databases are currently available:

* Argo 'ALL': contains all real time and adjusted variables as reported in the core ('<PLATFORM_NUMBER>_prof.nc') and synthetic ('<PLATFORM_NUMBER>_Sprof.nc') profile files, for the physical and biogeochemical versions respectively;
* Argo 'QC': contains the best available data, that is real time values are reported only when delayed values are not available. More details here.
* CrocoLake: contains the best available data from Argo, GLODAP, and Spray Gliders. More details here.

Each database comes in 'PHY' and 'BGC' versions.

### Contact

For any questions, bugs, missing information, etc, open an issue or [get in touch](enrico.milanese@whoi.edu)!
