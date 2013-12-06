import sys
import os
import getopt
import Image
from png2mol import png2mol

def checkDIR(dir):
	if dir == src:
		if not os.path.isdir(dir):
			print 'Directory', dir , 'does not exist'
			sys.exit()
	else:
		if not os.path.isdir(dir):
			print 'Directory', dir, 'does not exist'
			print 'Creating ', dir
			os.makedirs(dir)		
	return dir
	
def main(argv):
	srcdir = ''
	dstdir = ''
	try:
		opts, args =  getopt.getopt(argv,"hs:d:",["source=", "destination="])
	except getopt.GetoptError:
		print 'example2.py -s <source dir> -d <destination dir>'
		sys.exit(2)
	for opt, arg in opts:
		if opt == '-h':
			print 'example2.py -s <source dir> -d <destination dir>'
			sys.exit()
		elif opt in ("-s", "--source"):
			srcdir = arg
			dstdir = arg
		elif opt in ("-d", "--destination"):
			dstdir = arg
	return srcdir, dstdir
	
if __name__ == "__main__":
	src, dst = main(sys.argv[1:])
	
src = checkDIR(src) 
dst = checkDIR(dst)
fileList = []
fileListM = []
fileListP = []

for files in os.listdir(src):
	if files.endswith(".png"):
		file=Image.open(os.path.join(src, files))#
		if file.getcolors()==None:
			pass
		else:
			if file.mode=='P' and file.size[0]==570 and (file.getcolors())[0][1]==0 and (file.getcolors())[1][1]==1:
				fileList.append(files)
if len(fileList) == 0:	
	print 'No files found in: ' + src
else:
	print 'Found ' + str(len(fileList)) + ' compatible PNG files in: ' + src
	print "Reading image(s)..."
	for i in fileList:					
		file2 = open(os.path.join(src,i), 'r')#
		filepath = file2.name
		print 'Converting file ' + i + ' to ' + i[:len(i)-4] + '.mol'
		print 'Converting file ' + i + ' to ' + i[:len(i)-4] + '.pdb'
		fileparse = png2mol(filepath)
		PNGmol = fileparse['mol']
		PNGpdb = fileparse['pdb']
		molfile = open(os.path.join(dst, i[:len(i)-4] + '.mol'), 'w')
		molfile.write(PNGmol)
		molfile.close()
		fileListM.append(molfile)
		dst2 = checkDIR(os.path.join(dst, 'pdb'))
		pdbfile = open(os.path.join(dst2, i[:len(i)-4] + '.pdb'), 'w')
		pdbfile.write(PNGpdb)
		pdbfile.close()
		fileListP.append(pdbfile)
		fileListD = fileListM + fileListP
		
print str(len(fileList)) + ' PNG files converted '
print str(len(fileListM)) + ' mol files saved in ' + dst
print str(len(fileListP)) + ' pdb files saved in ' + dst2
print 'Saved ' + str(len(fileListM)+len(fileListP)) + ' files in total'

