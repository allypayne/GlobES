# File Explanations

## [create_binary_reduced_molecules.py](/create_binary_reduced_molecules.py)
- This file converts the atmospheric files E-0 through E-5 of the varying Earth atmospheric compositions to binary format to be compatible with GlobES
- "reduced_molecules" refers to the reduction from the full list of molecules in "ATMOSPHERE-LAYERS-MOLECULES" to only including "ATMOSPHERE-GAS" for the analysis in the binary files
    - these molecules are used to perform an exact continued analysis of the varying Earth abundances from Checlair 2021
- All the binary files for GlobES have been downloaded

## [create_1d_create_3d.py](/create_1d_create_3d.py)
-this file creates the config files for both the 1d and 3d models from the 6 earth amtmosphere files to use in psg
- runs the 1d files directly to the API for the 1d files (had some issues making it work for the 3d files)

pixel_movie.ipynb
## [pixel_movie.ipynb](/pixel_movie.ipynb)
-Provides code to take an Earth image and download multiple versions of the image shown with increasing pixelation
-This notebook compiles the output images and creates an animation/ gif to be used in an upcoming presentation
-The gif describes visually how information is lost as a high resolution model is reduced to a 1d model
