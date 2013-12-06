GLIDA_PNG2MOL
=============

PNG2MOL converts the PNG MOL file format from GLIDA database (GPCR-Ligand Database) to standard TXT MOL and PDB file format.

GLIDA PNG2MOL
=============

PNG2MOL converts the PNG MOL file format from GLIDA database (GPCR-Ligand Database) to standard TXT MOL and PDB file format. PNG2MOL requires Open Babel, Pybel nad PIL (Python Imaging Library) libraries to work. PNG2MOL is  available as python module and as a script.


./datasetlarge 	- contains 120 png mol example files

./datasetsmall 	- contains 16 png mol example files

./module	- contains png2mol.py, map.py, example.py and example2.py files	

./script	- contains glida_png2mol.py file


PYTHON MODULE:
==============

To use png2mol module directly from python shell,  simply copy png2mol.py and map.py files into your pythonpath/site-packages directory. Depending on platfrom, usually it's "C:\PythonXY\Lib\site-packages" for Windows and "/usr/local/lib/pythonX.Y/site-packages" for Unix. After that you should be able to import png2mol directly from python shell. The module takes as an argument the path to the input file and returns a dictionary where the keys are strings 'mol' or 'pdb' and the values are a string representing of mol and pdb file format. The example of usage are provided in example.py and example2.py files.

MODULE USAGE:
-------------

from png2mol import png2mol 

import the png2mol module

filepath = file.name		        

assign an input file path to a variable filepath

fileparse = png2mol(filepath)	  

convert the file using the png2mol module and assign the result to a variable fileparse	

PNGmol = fileparse['mol']	     

returns a string representation of a mol fileformat using key 'mol' and assigns it to a variable PNGmol

PNGpdb = fileparse['pdb']       

returns a string representation of a pdb fileformat using key 'pdb' and assigns it to a                                 variable PNGpdb

EXEMPLE USAGE:
--------------

example.py
example2.py -s source direcotry -d destination directory

-s source directory	
 
  Necessary argument. This is the path to the directory with GLIDA PNG MOL files.
  
-d destination directory
  
  Optional argument. This is the path where the MOL files will be saved. PDB files will be saved in 
  ./destination directory/PDB. If this option is not used, the output files will be saved in the source directory.  


PYTHON SCRIPT:
==============

glida_png2mol.py file  is an independent script.  

SCRIPT USAGE:
-------------

glida_png2mol.py -s source directory -d destination directory

-s source directory	
  
  Necessary argument. This is the path to the directory with GLIDA PNG MOL files.
  
-d destination directory	
  
  Optional argument. This is the path where the MOL files will be saved. PDB files will be saved in 
  ./destination directory/PDB. If this option is not used, the output files will be saved in the source directory. 
  If input files contains characters which are not recognized, these files will be convereted,  but places where the
  characters are not recognized, will be identified with "#" for the MOL files and "X" for PDB files. Incomplete files
  will be saved in  ./destination directory/incomplete/mol and ./destination directory/incomplete/pdb directories.

