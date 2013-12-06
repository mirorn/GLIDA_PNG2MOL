import sys
import os
import getopt
import Bio.PDB

try:
	import Image
except ImportError:
	print 'Cannot import module Image. png2mol.py requires PIL (Python Imaging Library)'
	print 'You can download the latest version at http://www.pythonware.com/products/pil/'
try:
	import pybel
except ImportError:
	print 'Cannot import module pybel. png2mol.py requires Pybel and OpenBabel)'
	print 'You can download the latest version at http://openbabel.org/wiki/Get_Open_Babel'
try:
	from map import initLettersMap
except ImportError:
	print 'Cannot import module map. Module map.py must be in the same dircetory as png2mol.py'

def png2mol(pngfile):	
	MARGIN_VERTICAL = 8
	MARGIN_HORIZONTAL = 5
	CHAR_WIDTH_SPACE = 0
	CHAR_HEIGHT_SPACE = 2
	CHAR_WIDTH = 8
	CHAR_HEIGHT = 10
	lettersMap = {}
	lettersScore={}
	imgFile = None


	def readChar(data, line, charPos):
		letter = []
		subLineStart = line * (CHAR_HEIGHT + CHAR_HEIGHT_SPACE) + MARGIN_VERTICAL
		subCharStart = charPos * (CHAR_WIDTH + CHAR_WIDTH_SPACE) + MARGIN_HORIZONTAL

		for subLine in range(0,CHAR_HEIGHT + CHAR_HEIGHT_SPACE):
			for subChar in range(0,CHAR_WIDTH + CHAR_WIDTH_SPACE):
				letter.append(data[(subCharStart + subChar),(subLineStart + subLine)])
		
		letterString = None
		letterString = lettersMap.get(str(letter), None)
		
		if letterString == None:
			lettersfromMap = initLettersMap()
			for i in lettersfromMap:
				lettersScore [i] = score(str(letter),i) 
			for key in lettersScore.keys():
				if lettersScore[key] == min(lettersScore.values()):
					if lettersScore[key] < 5:
						letterString = lettersfromMap[key]
					else:
						letterString = None
						
		if letterString == None:
			print "Error: Unknown character in line " + str(line+1) + " at " + str(charPos+1) + " position"
			
		if letterString == None:
			return "#"
			
		return letterString

	def score(w,l):
		count=0
		for i, item in enumerate(l):
			if item != w[i]:
				count +=1
		return count

	file=Image.open(pngfile)
	if file.getcolors()==None:
		pass
	else:
		if file.mode=='P' and file.size[0]==570 and (file.getcolors())[0][1]==0 and (file.getcolors())[1][1]==1:
			file=Image.open(pngfile)
			frame=file.load()

			height = file.size[1]
			width = file.size[0]
			linesCount = 0
			charsCount = 0

			lettersMap = initLettersMap()
			height -= MARGIN_VERTICAL * 2
			linesCount = height / (CHAR_HEIGHT + CHAR_HEIGHT_SPACE)

			width -= MARGIN_HORIZONTAL * 2
			charsCount = width / (CHAR_WIDTH + CHAR_WIDTH_SPACE)
			textFile = ""
			for line in range(0,linesCount):
				for charPos in range(0,charsCount):
					textFile += readChar(frame, line, charPos)
				textFile += "\n";
	#return textFile
			pdbFile = (pybel.readstring("mol", textFile)).write("pdb")
	dict ={'mol':textFile, 'pdb':pdbFile}
	return dict