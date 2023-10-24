# File Explanations

## [create_binary_reduced_molecules.py](/create_binary_reduced_molecules.py)
- This file converts the atmospheric files E-0 through E-5 of the varying Earth atmospheric compositions to binary format to be compatible with GlobES
- "reduced_molecules" refers to the reduction from the full list of molecules in "ATMOSPHERE-LAYERS-MOLECULES" to only including "ATMOSPHERE-GAS" for the analysis in the binary files
    - these molecules are used to perform an exact continued analysis of the varying Earth abundances from Checlair 2021
- All the binary files for GlobES have been downloaded

## [create_1d_create_3d.py](/create_1d_create_3d.py)
-this file creates the config files for both the 1d and 3d models from the 6 earth amtmosphere files to use in psg
