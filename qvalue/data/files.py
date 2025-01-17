"""
Location of data files
======================

Use as ::

    from qvalue.data.files import *

"""

__all__ = [
    "MDANALYSIS_LOGO",  # example file of MDAnalysis logo
]

import importlib.resources

data_directory = importlib.resources.files("qvalue") / "data"

MDANALYSIS_LOGO = data_directory / "mda.txt"
DCD = data_directory / 'movie.dcd'
PDB = data_directory / 'native.pdb'
REF = data_directory / 'crystal_structure-openmmawsem.pdb'
INFO = data_directory / 'info.dat'
