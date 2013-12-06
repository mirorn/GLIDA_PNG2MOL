import os
from png2mol import png2mol


file = open ('../datasetsmall/As.png', 'r')
print 'Reading file from ', file.name
filepath = file.name
print 'Converting file', os.path.basename(filepath)
fileparse = png2mol(filepath)
PNGmol = fileparse['mol']
PNGpdb = fileparse['pdb']
molfile = open('molfile.mol', 'w')
molfile.write(PNGmol)
molfile.close()
pdbfile = open('pdbfile.pdb', 'w')
pdbfile.write(PNGpdb)
pdbfile.close()
print 'DONE'

