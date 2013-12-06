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
	