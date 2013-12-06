import sys
import os
import getopt

try:
	import Image
except ImportError:
	print 'Cannot import module Image. glida_png2mol.py requires PIL (Python Imaging Library)'
	print 'You can download the latest version at http://www.pythonware.com/products/pil/'
try:
	import pybel
except ImportError:
	print 'Cannot import module pybel. glida_png2mol.py requires Pybel and OpenBabel)'
	print 'You can download the latest version at http://openbabel.org/wiki/Get_Open_Babel'
	
MARGIN_VERTICAL = 8
MARGIN_HORIZONTAL = 5
CHAR_WIDTH_SPACE = 0
CHAR_HEIGHT_SPACE = 2
CHAR_WIDTH = 8
CHAR_HEIGHT = 10
lettersMap = {}
lettersScore={}
imgFile = None

def initLettersMap():
	
	letterA = [
	  0, 0, 0, 1, 1, 0, 0, 0,
	  0, 0, 1, 0, 0, 1, 0, 0,
	  0, 1, 0, 0, 0, 0, 1, 0,
	  0, 1, 0, 0, 0, 0, 1, 0,
	  0, 1, 0, 0, 0, 0, 1, 0,
	  0, 1, 1, 1, 1, 1, 1, 0,
	  0, 1, 0, 0, 0, 0, 1, 0,
	  0, 1, 0, 0, 0, 0, 1, 0,
	  0, 1, 0, 0, 0, 0, 1, 0,
	  0, 1, 0, 0, 0, 0, 1, 0,
	  0, 0, 0, 0, 0, 0, 0, 0,
	  0, 0, 0, 0, 0, 0, 0, 0
	]
	letterB = [
	  0, 1, 1, 1, 1, 1, 0, 0,
	  0, 1, 0, 0, 0, 0, 1, 0,
	  0, 1, 0, 0, 0, 0, 1, 0,
	  0, 1, 0, 0, 0, 0, 1, 0,
	  0, 1, 1, 1, 1, 1, 0, 0,
	  0, 1, 0, 0, 0, 0, 1, 0,
	  0, 1, 0, 0, 0, 0, 1, 0,
	  0, 1, 0, 0, 0, 0, 1, 0,
	  0, 1, 0, 0, 0, 0, 1, 0,
	  0, 1, 1, 1, 1, 1, 0, 0,
	  0, 0, 0, 0, 0, 0, 0, 0,
	  0, 0, 0, 0, 0, 0, 0, 0
	]
	letterC = [
	  0, 0, 1, 1, 1, 1, 0, 0,
	  0, 1, 0, 0, 0, 0, 1, 0,
	  0, 1, 0, 0, 0, 0, 0, 0,
	  0, 1, 0, 0, 0, 0, 0, 0,
	  0, 1, 0, 0, 0, 0, 0, 0,
	  0, 1, 0, 0, 0, 0, 0, 0,
	  0, 1, 0, 0, 0, 0, 0, 0,
	  0, 1, 0, 0, 0, 0, 0, 0,
	  0, 1, 0, 0, 0, 0, 1, 0,
	  0, 0, 1, 1, 1, 1, 0, 0,
	  0, 0, 0, 0, 0, 0, 0, 0,
	  0, 0, 0, 0, 0, 0, 0, 0
	]
	letterD = [
	  0, 1, 1, 1, 1, 0, 0, 0,
	  0, 1, 0, 0, 0, 1, 0, 0,
	  0, 1, 0, 0, 0, 0, 1, 0,
	  0, 1, 0, 0, 0, 0, 1, 0,
	  0, 1, 0, 0, 0, 0, 1, 0,
	  0, 1, 0, 0, 0, 0, 1, 0,
	  0, 1, 0, 0, 0, 0, 1, 0,
	  0, 1, 0, 0, 0, 0, 1, 0,
	  0, 1, 0, 0, 0, 1, 0, 0,
	  0, 1, 1, 1, 1, 0, 0, 0,
	  0, 0, 0, 0, 0, 0, 0, 0,
	  0, 0, 0, 0, 0, 0, 0, 0
	]
	letterE = [
	  0, 1, 1, 1, 1, 1, 1, 0,
	  0, 1, 0, 0, 0, 0, 0, 0,
	  0, 1, 0, 0, 0, 0, 0, 0,
	  0, 1, 0, 0, 0, 0, 0, 0,
	  0, 1, 1, 1, 1, 1, 0, 0,
	  0, 1, 0, 0, 0, 0, 0, 0,
	  0, 1, 0, 0, 0, 0, 0, 0,
	  0, 1, 0, 0, 0, 0, 0, 0,
	  0, 1, 0, 0, 0, 0, 0, 0,
	  0, 1, 1, 1, 1, 1, 1, 0,
	  0, 0, 0, 0, 0, 0, 0, 0,
	  0, 0, 0, 0, 0, 0, 0, 0
	]
	letterF = [
	  0, 1, 1, 1, 1, 1, 1, 0,
	  0, 1, 0, 0, 0, 0, 0, 0,
	  0, 1, 0, 0, 0, 0, 0, 0,
	  0, 1, 0, 0, 0, 0, 0, 0,
	  0, 1, 1, 1, 1, 1, 0, 0,
	  0, 1, 0, 0, 0, 0, 0, 0,
	  0, 1, 0, 0, 0, 0, 0, 0,
	  0, 1, 0, 0, 0, 0, 0, 0,
	  0, 1, 0, 0, 0, 0, 0, 0,
	  0, 1, 0, 0, 0, 0, 0, 0,
	  0, 0, 0, 0, 0, 0, 0, 0,
	  0, 0, 0, 0, 0, 0, 0, 0
	]
	letterG = [
	  0, 0, 1, 1, 1, 1, 0, 0,
	  0, 1, 0, 0, 0, 0, 1, 0,
	  0, 1, 0, 0, 0, 0, 0, 0,
	  0, 1, 0, 0, 0, 0, 0, 0,
	  0, 1, 0, 0, 0, 0, 0, 0,
	  0, 1, 0, 0, 1, 1, 1, 0,
	  0, 1, 0, 0, 0, 0, 1, 0,
	  0, 1, 0, 0, 0, 0, 1, 0,
	  0, 1, 0, 0, 0, 1, 1, 0,
	  0, 0, 1, 1, 1, 0, 1, 0,
	  0, 0, 0, 0, 0, 0, 0, 0,
	  0, 0, 0, 0, 0, 0, 0, 0
	]
	letterH = [
	  0, 1, 0, 0, 0, 0, 1, 0,
	  0, 1, 0, 0, 0, 0, 1, 0,
	  0, 1, 0, 0, 0, 0, 1, 0,
	  0, 1, 0, 0, 0, 0, 1, 0,
	  0, 1, 1, 1, 1, 1, 1, 0,
	  0, 1, 0, 0, 0, 0, 1, 0,
	  0, 1, 0, 0, 0, 0, 1, 0,
	  0, 1, 0, 0, 0, 0, 1, 0,
	  0, 1, 0, 0, 0, 0, 1, 0,
	  0, 1, 0, 0, 0, 0, 1, 0,
	  0, 0, 0, 0, 0, 0, 0, 0,
	  0, 0, 0, 0, 0, 0, 0, 0
	]
	letterI = [
	  0, 1, 1, 1, 1, 1, 0, 0,
	  0, 0, 0, 1, 0, 0, 0, 0,
	  0, 0, 0, 1, 0, 0, 0, 0,
	  0, 0, 0, 1, 0, 0, 0, 0,
	  0, 0, 0, 1, 0, 0, 0, 0,
	  0, 0, 0, 1, 0, 0, 0, 0,
	  0, 0, 0, 1, 0, 0, 0, 0,
	  0, 0, 0, 1, 0, 0, 0, 0,
	  0, 0, 0, 1, 0, 0, 0, 0,
	  0, 1, 1, 1, 1, 1, 0, 0,
	  0, 0, 0, 0, 0, 0, 0, 0,
	  0, 0, 0, 0, 0, 0, 0, 0
	]
	letterJ = [
	  0, 0, 0, 0, 0, 0, 0, 0,
	  0, 1, 0, 0, 0, 0, 0, 0,
	  0, 0, 0, 0, 0, 0, 0, 0,
	  0, 0, 0, 0, 0, 0, 0, 0,
	  0, 0, 0, 0, 0, 0, 0, 0,
	  0, 0, 0, 0, 0, 0, 0, 0,
	  0, 0, 0, 0, 0, 0, 0, 0,
	  0, 0, 0, 0, 0, 0, 0, 0,
	  0, 0, 0, 0, 0, 0, 0, 0,
	  0, 0, 0, 0, 0, 0, 0, 0,
	  0, 0, 0, 0, 0, 0, 0, 0,
	  0, 0, 0, 0, 0, 0, 0, 0
	]
	letterK = [
	  0, 1, 0, 0, 0, 0, 1, 0,
	  0, 1, 0, 0, 0, 1, 0, 0,
	  0, 1, 0, 0, 1, 0, 0, 0,
	  0, 1, 0, 1, 0, 0, 0, 0,
	  0, 1, 1, 0, 0, 0, 0, 0,
	  0, 1, 1, 0, 0, 0, 0, 0,
	  0, 1, 0, 1, 0, 0, 0, 0,
	  0, 1, 0, 0, 1, 0, 0, 0,
	  0, 1, 0, 0, 0, 1, 0, 0,
	  0, 1, 0, 0, 0, 0, 1, 0,
	  0, 0, 0, 0, 0, 0, 0, 0,
	  0, 0, 0, 0, 0, 0, 0, 0
	]
	letterL = [
	  0, 1, 0, 0, 0, 0, 0, 0,
	  0, 1, 0, 0, 0, 0, 0, 0,
	  0, 1, 0, 0, 0, 0, 0, 0,
	  0, 1, 0, 0, 0, 0, 0, 0,
	  0, 1, 0, 0, 0, 0, 0, 0,
	  0, 1, 0, 0, 0, 0, 0, 0,
	  0, 1, 0, 0, 0, 0, 0, 0,
	  0, 1, 0, 0, 0, 0, 0, 0,
	  0, 1, 0, 0, 0, 0, 0, 0,
	  0, 1, 1, 1, 1, 1, 1, 0,
	  0, 0, 0, 0, 0, 0, 0, 0,
	  0, 0, 0, 0, 0, 0, 0, 0
	]
	letterM = [
	  1, 0, 0, 0, 0, 0, 1, 0,
	  1, 1, 0, 0, 0, 1, 1, 0,
	  1, 1, 0, 0, 0, 1, 1, 0,
	  1, 0, 1, 0, 1, 0, 1, 0,
	  1, 0, 1, 0, 1, 0, 1, 0,
	  1, 0, 0, 1, 0, 0, 1, 0,
	  1, 0, 0, 1, 0, 0, 1, 0,
	  1, 0, 0, 0, 0, 0, 1, 0,
	  1, 0, 0, 0, 0, 0, 1, 0,
	  1, 0, 0, 0, 0, 0, 1, 0,
	  0, 0, 0, 0, 0, 0, 0, 0,
	  0, 0, 0, 0, 0, 0, 0, 0
	]
	letterN = [
	  0, 1, 0, 0, 0, 0, 1, 0,
	  0, 1, 1, 0, 0, 0, 1, 0,
	  0, 1, 1, 0, 0, 0, 1, 0,
	  0, 1, 0, 1, 0, 0, 1, 0,
	  0, 1, 0, 1, 0, 0, 1, 0,
	  0, 1, 0, 0, 1, 0, 1, 0,
	  0, 1, 0, 0, 1, 0, 1, 0,
	  0, 1, 0, 0, 0, 1, 1, 0,
	  0, 1, 0, 0, 0, 1, 1, 0,
	  0, 1, 0, 0, 0, 0, 1, 0,
	  0, 0, 0, 0, 0, 0, 0, 0,
	  0, 0, 0, 0, 0, 0, 0, 0
	]
	letterO = [
	  0, 0, 1, 1, 1, 1, 0, 0,
	  0, 1, 0, 0, 0, 0, 1, 0,
	  0, 1, 0, 0, 0, 0, 1, 0,
	  0, 1, 0, 0, 0, 0, 1, 0,
	  0, 1, 0, 0, 0, 0, 1, 0,
	  0, 1, 0, 0, 0, 0, 1, 0,
	  0, 1, 0, 0, 0, 0, 1, 0,
	  0, 1, 0, 0, 0, 0, 1, 0,
	  0, 1, 0, 0, 0, 0, 1, 0,
	  0, 0, 1, 1, 1, 1, 0, 0,
	  0, 0, 0, 0, 0, 0, 0, 0,
	  0, 0, 0, 0, 0, 0, 0, 0
	]
	letterP = [
	  0, 1, 1, 1, 1, 1, 0, 0,
	  0, 1, 0, 0, 0, 0, 1, 0,
	  0, 1, 0, 0, 0, 0, 1, 0,
	  0, 1, 0, 0, 0, 0, 1, 0,
	  0, 1, 1, 1, 1, 1, 0, 0,
	  0, 1, 0, 0, 0, 0, 0, 0,
	  0, 1, 0, 0, 0, 0, 0, 0,
	  0, 1, 0, 0, 0, 0, 0, 0,
	  0, 1, 0, 0, 0, 0, 0, 0,
	  0, 1, 0, 0, 0, 0, 0, 0,
	  0, 0, 0, 0, 0, 0, 0, 0,
	  0, 0, 0, 0, 0, 0, 0, 0
	]
	letterQ = [
	  0, 0, 0, 0, 0, 0, 0, 0,
	  0, 0, 0, 0, 0, 0, 0, 0,
	  1, 0, 0, 0, 0, 0, 0, 0,
	  0, 0, 0, 0, 0, 0, 0, 0,
	  0, 0, 0, 0, 0, 0, 0, 0,
	  0, 0, 0, 0, 0, 0, 0, 0,
	  0, 0, 0, 0, 0, 0, 0, 0,
	  0, 0, 0, 0, 0, 0, 0, 0,
	  0, 0, 0, 0, 0, 0, 0, 0,
	  0, 0, 0, 0, 0, 0, 0, 0,
	  0, 0, 0, 0, 0, 0, 0, 0,
	  0, 0, 0, 0, 0, 0, 0, 0
	]
	letterR = [
	  0, 0, 0, 0, 0, 0, 0, 0,
	  0, 0, 0, 0, 0, 0, 0, 0,
	  0, 1, 0, 0, 0, 0, 0, 0,
	  0, 0, 0, 0, 0, 0, 0, 0,
	  0, 0, 0, 0, 0, 0, 0, 0,
	  0, 0, 0, 0, 0, 0, 0, 0,
	  0, 0, 0, 0, 0, 0, 0, 0,
	  0, 0, 0, 0, 0, 0, 0, 0,
	  0, 0, 0, 0, 0, 0, 0, 0,
	  0, 0, 0, 0, 0, 0, 0, 0,
	  0, 0, 0, 0, 0, 0, 0, 0,
	  0, 0, 0, 0, 0, 0, 0, 0
	]
	letterS = [
	  0, 0, 1, 1, 1, 1, 0, 0,
	  0, 1, 0, 0, 0, 0, 1, 0,
	  0, 1, 0, 0, 0, 0, 1, 0,
	  0, 1, 0, 0, 0, 0, 0, 0,
	  0, 0, 1, 1, 0, 0, 0, 0,
	  0, 0, 0, 0, 1, 1, 0, 0,
	  0, 0, 0, 0, 0, 0, 1, 0,
	  0, 1, 0, 0, 0, 0, 1, 0,
	  0, 1, 0, 0, 0, 0, 1, 0,
	  0, 0, 1, 1, 1, 1, 0, 0,
	  0, 0, 0, 0, 0, 0, 0, 0,
	  0, 0, 0, 0, 0, 0, 0, 0
	]
	letterT = [
	  0, 0, 0, 0, 0, 0, 0, 0,
	  0, 0, 0, 0, 0, 0, 0, 0,
	  0, 0, 0, 1, 0, 0, 0, 0,
	  0, 0, 0, 0, 0, 0, 0, 0,
	  0, 0, 0, 0, 0, 0, 0, 0,
	  0, 0, 0, 0, 0, 0, 0, 0,
	  0, 0, 0, 0, 0, 0, 0, 0,
	  0, 0, 0, 0, 0, 0, 0, 0,
	  0, 0, 0, 0, 0, 0, 0, 0,
	  0, 0, 0, 0, 0, 0, 0, 0,
	  0, 0, 0, 0, 0, 0, 0, 0,
	  0, 0, 0, 0, 0, 0, 0, 0
	]
	letterU = [
	  0, 0, 0, 0, 0, 0, 0, 0,
	  0, 0, 0, 0, 0, 0, 0, 0,
	  0, 0, 0, 0, 1, 0, 0, 0,
	  0, 0, 0, 0, 0, 0, 0, 0,
	  0, 0, 0, 0, 0, 0, 0, 0,
	  0, 0, 0, 0, 0, 0, 0, 0,
	  0, 0, 0, 0, 0, 0, 0, 0,
	  0, 0, 0, 0, 0, 0, 0, 0,
	  0, 0, 0, 0, 0, 0, 0, 0,
	  0, 0, 0, 0, 0, 0, 0, 0,
	  0, 0, 0, 0, 0, 0, 0, 0,
	  0, 0, 0, 0, 0, 0, 0, 0
	]
	letterV = [
	  1, 0, 0, 0, 0, 0, 1, 0,
	  1, 0, 0, 0, 0, 0, 1, 0,
	  1, 0, 0, 0, 0, 0, 1, 0,
	  0, 1, 0, 0, 0, 1, 0, 0,
	  0, 1, 0, 0, 0, 1, 0, 0,
	  0, 1, 0, 0, 0, 1, 0, 0,
	  0, 0, 1, 0, 1, 0, 0, 0,
	  0, 0, 1, 0, 1, 0, 0, 0,
	  0, 0, 0, 1, 0, 0, 0, 0,
	  0, 0, 0, 1, 0, 0, 0, 0,
	  0, 0, 0, 0, 0, 0, 0, 0,
	  0, 0, 0, 0, 0, 0, 0, 0
	]
	letterW = [
	  0, 0, 0, 0, 0, 0, 0, 0,
	  0, 0, 0, 0, 0, 0, 0, 0,
	  0, 0, 0, 0, 0, 0, 1, 0,
	  0, 0, 0, 0, 0, 0, 0, 0,
	  0, 0, 0, 0, 0, 0, 0, 0,
	  0, 0, 0, 0, 0, 0, 0, 0,
	  0, 0, 0, 0, 0, 0, 0, 0,
	  0, 0, 0, 0, 0, 0, 0, 0,
	  0, 0, 0, 0, 0, 0, 0, 0,
	  0, 0, 0, 0, 0, 0, 0, 0,
	  0, 0, 0, 0, 0, 0, 0, 0,
	  0, 0, 0, 0, 0, 0, 0, 0
	]
	letterX = [
	  0, 0, 0, 0, 0, 0, 0, 0,
	  0, 0, 0, 0, 0, 0, 0, 0,
	  0, 0, 0, 0, 0, 0, 0, 1,
	  0, 0, 0, 0, 0, 0, 0, 0,
	  0, 0, 0, 0, 0, 0, 0, 0,
	  0, 0, 0, 0, 0, 0, 0, 0,
	  0, 0, 0, 0, 0, 0, 0, 0,
	  0, 0, 0, 0, 0, 0, 0, 0,
	  0, 0, 0, 0, 0, 0, 0, 0,
	  0, 0, 0, 0, 0, 0, 0, 0,
	  0, 0, 0, 0, 0, 0, 0, 0,
	  0, 0, 0, 0, 0, 0, 0, 0
	]
	letterY = [
	  0, 0, 0, 0, 0, 0, 0, 0,
	  0, 0, 0, 0, 0, 0, 0, 0,
	  0, 0, 0, 0, 0, 0, 0, 0,
	  1, 0, 0, 0, 0, 0, 0, 0,
	  0, 0, 0, 0, 0, 0, 0, 0,
	  0, 0, 0, 0, 0, 0, 0, 0,
	  0, 0, 0, 0, 0, 0, 0, 0,
	  0, 0, 0, 0, 0, 0, 0, 0,
	  0, 0, 0, 0, 0, 0, 0, 0,
	  0, 0, 0, 0, 0, 0, 0, 0,
	  0, 0, 0, 0, 0, 0, 0, 0,
	  0, 0, 0, 0, 0, 0, 0, 0
	]
	letterZ = [
	  0, 1, 1, 1, 1, 1, 1, 0,
	  0, 0, 0, 0, 0, 0, 1, 0,
	  0, 0, 0, 0, 0, 0, 1, 0,
	  0, 0, 0, 0, 0, 1, 0, 0,
	  0, 0, 0, 0, 1, 0, 0, 0,
	  0, 0, 0, 1, 0, 0, 0, 0,
	  0, 0, 1, 0, 0, 0, 0, 0,
	  0, 1, 0, 0, 0, 0, 0, 0,
	  0, 1, 0, 0, 0, 0, 0, 0,
	  0, 1, 1, 1, 1, 1, 1, 0,
	  0, 0, 0, 0, 0, 0, 0, 0,
	  0, 0, 0, 0, 0, 0, 0, 0
	]
	lettera = [
	  0, 0, 0, 0, 0, 0, 0, 0, 
	  0, 0, 0, 0, 0, 0, 0, 0, 
	  0, 0, 0, 0, 0, 0, 0, 0, 
	  0, 0, 1, 1, 1, 1, 0, 0, 
	  0, 1, 0, 0, 0, 0, 1, 0,
	  0, 0, 0, 0, 1, 1, 1, 0, 
	  0, 0, 1, 1, 0, 0, 1, 0, 
	  0, 1, 0, 0, 0, 0, 1, 0, 
	  0, 1, 0, 0, 0, 1, 1, 0, 
	  0, 0, 1, 1, 1, 0, 1, 0, 
	  0, 0, 0, 0, 0, 0, 0, 0, 
	  0, 0, 0, 0, 0, 0, 0, 0 
	  ]
	lettere = [
	  0, 0, 0, 0, 0, 0, 0, 0, 
	  0, 0, 0, 0, 0, 0, 0, 0, 
	  0, 0, 0, 0, 0, 0, 0, 0, 
	  0, 0, 1, 1, 1, 1, 0, 0, 
	  0, 1, 0, 0, 0, 0, 1, 0,
	  0, 1, 0, 0, 0, 0, 1, 0, 
	  0, 1, 1, 1, 1, 1, 1, 0, 
	  0, 1, 0, 0, 0, 0, 0, 0, 
	  0, 1, 0, 0, 0, 0, 0, 0, 
	  0, 0, 1, 1, 1, 1, 0, 0, 
	  0, 0, 0, 0, 0, 0, 0, 0, 
	  0, 0, 0, 0, 0, 0, 0, 0 
	  ]
	letterg = [
	  0, 0, 0, 0, 0, 0, 0, 0, 
	  0, 0, 0, 0, 0, 0, 0, 0, 
	  0, 0, 0, 0, 0, 0, 1, 0, 
	  0, 0, 1, 1, 1, 0, 1, 0, 
	  0, 1, 0, 0, 0, 1, 0, 0,
	  0, 1, 0, 0, 0, 1, 0, 0, 
	  0, 1, 0, 0, 0, 1, 0, 0, 
	  0, 0, 1, 1, 1, 0, 0, 0, 
	  0, 0, 1, 0, 0, 0, 0, 0, 
	  0, 0, 1, 1, 1, 1, 0, 0, 
	  0, 1, 0, 0, 0, 0, 1, 0, 
	  0, 1, 0, 0, 0, 0, 1, 0 
	  ]  
	letteri = [
	  0, 0, 0, 1, 0, 0, 0, 0, 
	  0, 0, 0, 1, 0, 0, 0, 0, 
	  0, 0, 0, 0, 0, 0, 0, 0, 
	  0, 0, 1, 1, 0, 0, 0, 0, 
	  0, 0, 0, 1, 0, 0, 0, 0,
	  0, 0, 0, 1, 0, 0, 0, 0, 
	  0, 0, 0, 1, 0, 0, 0, 0, 
	  0, 0, 0, 1, 0, 0, 0, 0, 
	  0, 0, 0, 1, 0, 0, 0, 0, 
	  0, 1, 1, 1, 1, 1, 0, 0, 
	  0, 0, 0, 0, 0, 0, 0, 0, 
	  0, 0, 0, 0, 0, 0, 0, 0 
	  ]  
	letterl = [
	  0, 0, 1, 1, 0, 0, 0, 0, 
	  0, 0, 0, 1, 0, 0, 0, 0, 
	  0, 0, 0, 1, 0, 0, 0, 0, 
	  0, 0, 0, 1, 0, 0, 0, 0, 
	  0, 0, 0, 1, 0, 0, 0, 0,
	  0, 0, 0, 1, 0, 0, 0, 0, 
	  0, 0, 0, 1, 0, 0, 0, 0, 
	  0, 0, 0, 1, 0, 0, 0, 0, 
	  0, 0, 0, 1, 0, 0, 0, 0, 
	  0, 1, 1, 1, 1, 1, 0, 0, 
	  0, 0, 0, 0, 0, 0, 0, 0, 
	  0, 0, 0, 0, 0, 0, 0, 0 
	]
	letterm = [
	  0, 0, 0, 0, 0, 0, 0, 0, 
	  0, 0, 0, 0, 0, 0, 0, 0, 
	  0, 0, 0, 0, 0, 0, 0, 0, 
	  1, 1, 1, 0, 1, 1, 0, 0, 
	  1, 0, 0, 1, 0, 0, 1, 0,
	  1, 0, 0, 1, 0, 0, 1, 0, 
	  1, 0, 0, 1, 0, 0, 1, 0, 
	  1, 0, 0, 1, 0, 0, 1, 0, 
	  1, 0, 0, 1, 0, 0, 1, 0, 
	  1, 0, 0, 1, 0, 0, 1, 0, 
	  0, 0, 0, 0, 0, 0, 0, 0, 
	  0, 0, 0, 0, 0, 0, 0, 0 
	]
	lettern = [
	  0, 0, 0, 0, 0, 0, 0, 0, 
	  0, 0, 0, 0, 0, 0, 0, 0, 
	  0, 0, 0, 0, 0, 0, 0, 0, 
	  0, 1, 0, 1, 1, 1, 0, 0, 
	  0, 1, 1, 0, 0, 0, 1, 0,
	  0, 1, 0, 0, 0, 0, 1, 0, 
	  0, 1, 0, 0, 0, 0, 1, 0, 
	  0, 1, 0, 0, 0, 0, 1, 0, 
	  0, 1, 0, 0, 0, 0, 1, 0, 
	  0, 1, 0, 0, 0, 0, 1, 0, 
	  0, 0, 0, 0, 0, 0, 0, 0, 
	  0, 0, 0, 0, 0, 0, 0, 0 
	]
	lettero = [
	  0, 0, 0, 0, 0, 0, 0, 0, 
	  0, 0, 0, 0, 0, 0, 0, 0, 
	  0, 0, 0, 0, 0, 0, 0, 0, 
	  0, 0, 1, 1, 1, 1, 0, 0, 
	  0, 1, 0, 0, 0, 0, 1, 0,
	  0, 1, 0, 0, 0, 0, 1, 0, 
	  0, 1, 0, 0, 0, 0, 1, 0, 
	  0, 1, 0, 0, 0, 0, 1, 0, 
	  0, 1, 0, 0, 0, 0, 1, 0, 
	  0, 0, 1, 1, 1, 1, 0, 0, 
	  0, 0, 0, 0, 0, 0, 0, 0, 
	  0, 0, 0, 0, 0, 0, 0, 0 
	]
	letterp = [
	  0, 0, 0, 0, 0, 0, 0, 0, 
	  0, 0, 0, 0, 0, 0, 0, 0, 
	  0, 0, 0, 0, 0, 0, 0, 0, 
	  0, 1, 0, 1, 1, 1, 0, 0, 
	  0, 1, 1, 0, 0, 0, 1, 0,
	  0, 1, 0, 0, 0, 0, 1, 0, 
	  0, 1, 0, 0, 0, 0, 1, 0, 
	  0, 1, 0, 0, 0, 0, 1, 0, 
	  0, 1, 1, 0, 0, 0, 1, 0, 
	  0, 1, 0, 1, 1, 1, 0, 0, 
	  0, 1, 0, 0, 0, 0, 0, 0, 
	  0, 1, 0, 0, 0, 0, 0, 0 
	]
	letterr = [
	  0, 0, 0, 0, 0, 0, 0, 0, 
	  0, 0, 0, 0, 0, 0, 0, 0, 
	  0, 0, 0, 0, 0, 0, 0, 0, 
	  0, 1, 0, 1, 1, 1, 0, 0, 
	  0, 1, 1, 0, 0, 0, 1, 0,
	  0, 1, 0, 0, 0, 0, 0, 0, 
	  0, 1, 0, 0, 0, 0, 0, 0, 
	  0, 1, 0, 0, 0, 0, 0, 0, 
	  0, 1, 0, 0, 0, 0, 0, 0, 
	  0, 1, 0, 0, 0, 0, 0, 0, 
	  0, 0, 0, 0, 0, 0, 0, 0, 
	  0, 0, 0, 0, 0, 0, 0, 0 
	]
	letters = [
	  0, 0, 0, 0, 0, 0, 0, 0, 
	  0, 0, 0, 0, 0, 0, 0, 0, 
	  0, 0, 0, 0, 0, 0, 0, 0, 
	  0, 0, 1, 1, 1, 1, 0, 0, 
	  0, 1, 0, 0, 0, 0, 1, 0,
	  0, 1, 0, 0, 0, 0, 0, 0, 
	  0, 0, 1, 1, 1, 1, 0, 0, 
	  0, 0, 0, 0, 0, 0, 1, 0, 
	  0, 1, 0, 0, 0, 0, 1, 0, 
	  0, 0, 1, 1, 1, 1, 0, 0, 
	  0, 0, 0, 0, 0, 0, 0, 0, 
	  0, 0, 0, 0, 0, 0, 0, 0 
	]
	lettergl = [
	  0, 0, 1, 1, 1, 1, 0, 0,
	  0, 0, 0, 1, 0, 0, 0, 0,
	  0, 0, 0, 1, 0, 0, 0, 0,
	  0, 0, 0, 1, 0, 0, 0, 0,
	  0, 0, 0, 1, 0, 0, 0, 0,
	  0, 0, 0, 1, 0, 0, 0, 0,
	  0, 0, 0, 1, 0, 0, 0, 0,
	  0, 0, 0, 1, 0, 0, 0, 0,
	  0, 0, 0, 1, 0, 0, 0, 0,
	  0, 1, 1, 1, 1, 1, 0, 0,
	  0, 0, 0, 0, 0, 0, 0, 0,
	  0, 0, 0, 0, 0, 0, 0, 0
	]
	letter1 = [
	  0, 0, 0, 0, 1, 0, 0, 0,
	  0, 0, 0, 1, 1, 0, 0, 0, 
	  0, 0, 1, 0, 1, 0, 0, 0,
	  0, 0, 0, 0, 1, 0, 0, 0,
	  0, 0, 0, 0, 1, 0, 0, 0, 
	  0, 0, 0, 0, 1, 0, 0, 0, 
	  0, 0, 0, 0, 1, 0, 0, 0,
	  0, 0, 0, 0, 1, 0, 0, 0, 
	  0, 0, 0, 0, 1, 0, 0, 0,
	  0, 0, 1, 1, 1, 1, 1, 0, 
	  0, 0, 0, 0, 0, 0, 0, 0, 
	  0, 0, 0, 0, 0, 0, 0, 0 
	]
	letter2 = [
	  0, 0, 1, 1, 1, 1, 0, 0, 
	  0, 1, 0, 0, 0, 0, 1, 0, 
	  0, 1, 0, 0, 0, 0, 1, 0, 
	  0, 0, 0, 0, 0, 0, 1, 0, 
	  0, 0, 0, 0, 1, 1, 0, 0, 
	  0, 0, 0, 1, 0, 0, 0, 0, 
	  0, 0, 1, 0, 0, 0, 0, 0, 
	  0, 1, 0, 0, 0, 0, 0, 0, 
	  0, 1, 0, 0, 0, 0, 0, 0,
	  0, 1, 1, 1, 1, 1, 1, 0,
	  0, 0, 0, 0, 0, 0, 0, 0,
	  0, 0, 0, 0, 0, 0, 0, 0 
	]
	letter3 = [
	  0, 0, 1, 1, 1, 1, 0, 0, 
	  0, 1, 0, 0, 0, 0, 1, 0, 
	  0, 1, 0, 0, 0, 0, 1, 0, 
	  0, 0, 0, 0, 0, 0, 1, 0, 
	  0, 0, 0, 1, 1, 1, 0, 0, 
	  0, 0, 0, 0, 0, 0, 1, 0, 
	  0, 0, 0, 0, 0, 0, 1, 0, 
	  0, 1, 0, 0, 0, 0, 1, 0, 
	  0, 1, 0, 0, 0, 0, 1, 0, 
	  0, 0, 1, 1, 1, 1, 0, 0, 
	  0, 0, 0, 0, 0, 0, 0, 0,
	  0, 0, 0, 0, 0, 0, 0, 0 
	]
	letter4 = [
	  0, 0, 0, 0, 0, 1, 0, 0, 
	  0, 0, 0, 0, 1, 1, 0, 0,
	  0, 0, 0, 1, 0, 1, 0, 0, 
	  0, 0, 1, 0, 0, 1, 0, 0, 
	  0, 1, 0, 0, 0, 1, 0, 0,
	  0, 1, 0, 0, 0, 1, 0, 0,
	  0, 1, 1, 1, 1, 1, 1, 0, 
	  0, 0, 0, 0, 0, 1, 0, 0, 
	  0, 0, 0, 0, 0, 1, 0, 0,
	  0, 0, 0, 0, 0, 1, 0, 0, 
	  0, 0, 0, 0, 0, 0, 0, 0,
	  0, 0, 0, 0, 0, 0, 0, 0
	]
	letter5 = [
	  0, 1, 1, 1, 1, 1, 1, 0, 
	  0, 1, 0, 0, 0, 0, 0, 0, 
	  0, 1, 0, 0, 0, 0, 0, 0, 
	  0, 1, 0, 0, 0, 0, 0, 0, 
	  0, 1, 1, 1, 1, 1, 0, 0, 
	  0, 0, 0, 0, 0, 0, 1, 0, 
	  0, 0, 0, 0, 0, 0, 1, 0, 
	  0, 0, 0, 0, 0, 0, 1, 0, 
	  0, 1, 0, 0, 0, 0, 1, 0,
	  0, 0, 1, 1, 1, 1, 0, 0, 
	  0, 0, 0, 0, 0, 0, 0, 0, 
	  0, 0, 0, 0, 0, 0, 0, 0 
	]
	letter6 = [
	  0, 0, 0, 1, 1, 1, 0, 0,
	  0, 0, 1, 0, 0, 0, 0, 0, 
	  0, 1, 0, 0, 0, 0, 0, 0, 
	  0, 1, 0, 0, 0, 0, 0, 0, 
	  0, 1, 1, 1, 1, 1, 0, 0, 
	  0, 1, 0, 0, 0, 0, 1, 0, 
	  0, 1, 0, 0, 0, 0, 1, 0, 
	  0, 1, 0, 0, 0, 0, 1, 0, 
	  0, 1, 0, 0, 0, 0, 1, 0, 
	  0, 0, 1, 1, 1, 1, 0, 0, 
	  0, 0, 0, 0, 0, 0, 0, 0, 
	  0, 0, 0, 0, 0, 0, 0, 0
	]
	letter7 = [
	  0, 1, 1, 1, 1, 1, 1, 0, 
	  0, 0, 0, 0, 0, 0, 1, 0, 
	  0, 0, 0, 0, 0, 0, 1, 0, 
	  0, 0, 0, 0, 0, 1, 0, 0, 
	  0, 0, 0, 0, 0, 1, 0, 0, 
	  0, 0, 0, 0, 0, 1, 0, 0, 
	  0, 0, 0, 0, 1, 0, 0, 0, 
	  0, 0, 0, 0, 1, 0, 0, 0, 
	  0, 0, 0, 0, 1, 0, 0, 0, 
	  0, 0, 0, 0, 1, 0, 0, 0, 
	  0, 0, 0, 0, 0, 0, 0, 0, 
	  0, 0, 0, 0, 0, 0, 0, 0 
	]
	letter8 = [
	  0, 0, 1, 1, 1, 1, 0, 0,
	  0, 1, 0, 0, 0, 0, 1, 0, 
	  0, 1, 0, 0, 0, 0, 1, 0, 
	  0, 1, 0, 0, 0, 0, 1, 0, 
	  0, 0, 1, 1, 1, 1, 0, 0, 
	  0, 1, 0, 0, 0, 0, 1, 0, 
	  0, 1, 0, 0, 0, 0, 1, 0, 
	  0, 1, 0, 0, 0, 0, 1, 0, 
	  0, 1, 0, 0, 0, 0, 1, 0, 
	  0, 0, 1, 1, 1, 1, 0, 0, 
	  0, 0, 0, 0, 0, 0, 0, 0, 
	  0, 0, 0, 0, 0, 0, 0, 0 
	]
	letter9 = [
	  0, 0, 1, 1, 1, 1, 0, 0,
	  0, 1, 0, 0, 0, 0, 1, 0,
	  0, 1, 0, 0, 0, 0, 1, 0, 
	  0, 1, 0, 0, 0, 0, 1, 0, 
	  0, 0, 1, 1, 1, 1, 1, 0, 
	  0, 0, 0, 0, 0, 0, 1, 0, 
	  0, 0, 0, 0, 0, 0, 1, 0,
	  0, 0, 0, 0, 0, 0, 1, 0,
	  0, 0, 0, 0, 0, 1, 0, 0, 
	  0, 0, 1, 1, 1, 0, 0, 0,
	  0, 0, 0, 0, 0, 0, 0, 0, 
	  0, 0, 0, 0, 0, 0, 0, 0 
	]
	letter0 = [
	  0, 0, 0, 1, 1, 0, 0, 0, 
	  0, 0, 1, 0, 0, 1, 0, 0, 
	  0, 1, 0, 0, 0, 0, 1, 0, 
	  0, 1, 0, 0, 0, 0, 1, 0, 
	  0, 1, 0, 0, 0, 0, 1, 0,
	  0, 1, 0, 0, 0, 0, 1, 0, 
	  0, 1, 0, 0, 0, 0, 1, 0, 
	  0, 1, 0, 0, 0, 0, 1, 0, 
	  0, 0, 1, 0, 0, 1, 0, 0, 
	  0, 0, 0, 1, 1, 0, 0, 0, 
	  0, 0, 0, 0, 0, 0, 0, 0, 
	  0, 0, 0, 0, 0, 0, 0, 0 
	]
	letterminus = [
	  0, 0, 0, 0, 0, 0, 0, 0,
	  0, 0, 0, 0, 0, 0, 0, 0, 
	  0, 0, 0, 0, 0, 0, 0, 0,
	  0, 0, 0, 0, 0, 0, 0, 0, 
	  0, 0, 0, 0, 0, 0, 0, 0, 
	  0, 1, 1, 1, 1, 1, 1, 0, 
	  0, 0, 0, 0, 0, 0, 0, 0, 
	  0, 0, 0, 0, 0, 0, 0, 0, 
	  0, 0, 0, 0, 0, 0, 0, 0, 
	  0, 0, 0, 0, 0, 0, 0, 0, 
	  0, 0, 0, 0, 0, 0, 0, 0, 
	  0, 0, 0, 0, 0, 0, 0, 0 
	]
	letterplus = [
	  0, 0, 0, 0, 0, 0, 0, 0, 
	  0, 0, 0, 0, 0, 0, 0, 0, 
	  0, 0, 0, 0, 0, 0, 0, 0, 
	  0, 0, 0, 0, 0, 0, 0, 0, 
	  0, 0, 0, 0, 0, 0, 0, 0, 
	  0, 0, 0, 0, 0, 0, 0, 0, 
	  0, 0, 0, 0, 1, 1, 0, 0, 
	  0, 0, 0, 0, 0, 0, 0, 0, 
	  0, 0, 0, 0, 0, 0, 0, 0, 
	  0, 0, 0, 0, 0, 0, 0, 0, 
	  0, 0, 0, 0, 0, 0, 0, 0, 
	  0, 0, 0, 0, 0, 0, 0, 0
	]
	letterdot = [
	  0, 0, 0, 0, 0, 0, 0, 0,
	  0, 0, 0, 0, 0, 0, 0, 0, 
	  0, 0, 0, 0, 0, 0, 0, 0, 
	  0, 0, 0, 0, 0, 0, 0, 0, 
	  0, 0, 0, 0, 0, 0, 0, 0, 
	  0, 0, 0, 0, 0, 0, 0, 0, 
	  0, 0, 0, 0, 0, 0, 0, 0,
	  0, 0, 0, 0, 0, 0, 0, 0, 
	  0, 0, 0, 1, 1, 0, 0, 0, 
	  0, 0, 0, 1, 1, 0, 0, 0, 
	  0, 0, 0, 0, 0, 0, 0, 0, 
	  0, 0, 0, 0, 0, 0, 0, 0 
	]
	letterspace = [
	  0, 0, 0, 0, 0, 0, 0, 0,
	  0, 0, 0, 0, 0, 0, 0, 0,
	  0, 0, 0, 0, 0, 0, 0, 0, 
	  0, 0, 0, 0, 0, 0, 0, 0, 
	  0, 0, 0, 0, 0, 0, 0, 0, 
	  0, 0, 0, 0, 0, 0, 0, 0,
	  0, 0, 0, 0, 0, 0, 0, 0,
	  0, 0, 0, 0, 0, 0, 0, 0, 
	  0, 0, 0, 0, 0, 0, 0, 0, 
	  0, 0, 0, 0, 0, 0, 0, 0, 
	  0, 0, 0, 0, 0, 0, 0, 0, 
	  0, 0, 0, 0, 0, 0, 0, 0 
	]
	lettersMap = {}
	lettersMap[str(letterA)] = "A"
	lettersMap[str(letterB)] = "B"
	lettersMap[str(letterC)] = "C"
	lettersMap[str(letterD)] = "D"
	lettersMap[str(letterE)] = "E"
	lettersMap[str(letterF)] = "F"
	lettersMap[str(letterG)] = "G"
	lettersMap[str(letterH)] = "H"
	lettersMap[str(letterI)] = "I"
	lettersMap[str(letterJ)] = "J"
	lettersMap[str(letterK)] = "K"
	lettersMap[str(letterL)] = "L"
	lettersMap[str(letterM)] = "M"
	lettersMap[str(letterN)] = "N"
	lettersMap[str(letterO)] = "O"
	lettersMap[str(letterP)] = "P"
	lettersMap[str(letterQ)] = "Q"
	lettersMap[str(letterR)] = "R"
	lettersMap[str(letterS)] = "S"
	lettersMap[str(letterT)] = "T"
	lettersMap[str(letterU)] = "U"
	lettersMap[str(letterV)] = "V"
	lettersMap[str(letterW)] = "W"
	lettersMap[str(letterX)] = "X"
	lettersMap[str(letterY)] = "Y"
	lettersMap[str(letterZ)] = "Z"
	lettersMap[str(letter1)] = "1"
	lettersMap[str(letter2)] = "2"
	lettersMap[str(letter3)] = "3"
	lettersMap[str(letter4)] = "4"
	lettersMap[str(letter5)] = "5"
	lettersMap[str(letter6)] = "6"
	lettersMap[str(letter7)] = "7"
	lettersMap[str(letter8)] = "8"
	lettersMap[str(letter9)] = "9"
	lettersMap[str(letter0)] = "0"
	lettersMap[str(lettera)] = "a"
	lettersMap[str(lettere)] = "e"
	lettersMap[str(letterg)] = "g"
	lettersMap[str(letteri)] = "i"
	lettersMap[str(letterl)] = "l"
	lettersMap[str(letterm)] = "m"
	lettersMap[str(lettern)] = "n"
	lettersMap[str(lettero)] = "o"
	lettersMap[str(letterp)] = "p"
	lettersMap[str(letterr)] = "r"
	lettersMap[str(letters)] = "s"
	lettersMap[str(lettergl)] = "l"
	lettersMap[str(letterminus)] = "-"
	lettersMap[str(letterplus)] = "+"
	lettersMap[str(letterdot)] = "."
	lettersMap[str(letterspace)] = " "
	
	return lettersMap
	

def readChar(data, line, charPos):
	global badChar
	badChar = 0
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
		badChar=1
	if letterString == None:
		return "#"
		
	return letterString

def score(w,l):
	count=0
	for i, item in enumerate(l):
		if item != w[i]:
			count +=1
	return count
	
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
		print 'glida_png2mol.py -s <source dir> -d <destination dir>'
		sys.exit(2)
	for opt, arg in opts:
		if opt == '-h':
			print 'glida_png2mol.py -s <source dir> -d <destination dir>'
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
fileListB = []
fileListG = []
fileListM = []
for files in os.listdir(src):
	if files.endswith(".png"):
		file=Image.open(os.path.join(src, files))
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
		file=Image.open(os.path.join(src,i))
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
		nfile = i
		print 'Converting file ' + i + ' to ' + i[:len(nfile)-4] + '.mol'
		for line in range(0,linesCount):
			for charPos in range(0,charsCount):
				textFile += readChar(frame, line, charPos)
				if badChar >=5:
					fileListB.append(i)
					fileListB=list(set(fileListB))
				else:
					pass
			textFile += "\n";
		if i in fileListB:
			dst2 = checkDIR(os.path.join(dst, 'incomplete', 'mol'))	
			dstpdb2 = checkDIR(os.path.join(dst, 'incomplete', 'pdb'))
			logfile = open(os.path.join(dst2, nfile[:len(nfile)-4] + '.mol'), 'w')
			
			print 'Converting file ' + i + ' to ' + i[:len(i)-4] + '.pdb'
			molfile2 = pybel.readstring("mol", textFile)
			logfile2 = open(os.path.join(dstpdb2, i[:len(i)-4] + '.pdb'), 'w')
			logfile2.write(molfile2.write("pdb"))
			logfile2.close()
			
		else:
			dstpdb = checkDIR(os.path.join(dst, 'pdb'))
			logfile = open(os.path.join(dst, nfile[:len(nfile)-4] + '.mol'), 'w')
			fileListG.append(i)
			print 'Converting file ' + i + ' to ' + i[:len(i)-4] + '.pdb'
			molfile = pybel.readstring("mol", textFile)
			logfile3 = open(os.path.join(dstpdb, i[:len(i)-4] + '.pdb'), 'w')
			logfile3.write(molfile.write("pdb"))
			logfile3.close()
		logfile.write(textFile)
		logfile.close()	
		
	
	print str(len(fileListG)) + ' PNG files converted successfully'
	print str(len(fileListG)) + ' mol files saved in ' + dst
	if len(fileListB) != 0:
		print str(len(fileListB)) + ' mol files requires check for missing symbols'
		print str(len(fileListB)) + ' mol files saved in ' + dst2
	print str(len(fileListG)) + ' pdb files saved in ' + dstpdb
	if len(fileListB) != 0:
		print str(len(fileListB)) + ' pdb files requires check for missing symbols'
		print str(len(fileListB)) + ' pdb files saved in ' + dstpdb2
	print 'Saved ' + str(2*len(fileListG) + 2*len(fileListB)) + ' files in total'
