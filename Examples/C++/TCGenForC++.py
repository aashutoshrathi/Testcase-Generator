'''
		Aashutosh Rathi
https://github.com/aashutoshrathi/
Testcase Generator for HackerRank

'''


import os
import random
import sys
import zipfile
import math
import shutil

try:
	os.mkdir('input')
	os.mkdir('output')
except OSError:
	pass

pwr = math.pow
rint = random.randint

tf = 10 # number of test files, change it according to you.


for i in xrange(0, tf + 1):
	print >> sys.stderr, 'Generating:', i
	sys.stdout = open('input/input%02d.txt' % i, 'wb')
	
	'''
	Input area will start here,
	everything that you print out here will be taken as input in your logic file.
	You can set difficulty of test cases all by you.
	'''

	### Input File Printing Start
	x = rint(5, pwr(10, (i//2) + 1)) # number of test cases in (1,10^5)
	print x # Prints x into input file
	for z in range (x):
		print rint(1,pwr(10,min(4,max(i/2,2)))) 
	sys.stdout.close()
	### Input File Printing Ends


with zipfile.ZipFile('test-cases.zip', 'w', zipfile.ZIP_DEFLATED) as zf:
	for i in xrange(0, tf + 1):
		print >> sys.stderr, 'Zipping:', i
		os.system('g++ -o logic logic.cpp')
		os.system('./logic < input/input%02d.txt > output/output%02d.txt' % (i, i))
		zf.write('input/input%02d.txt' % i)
		zf.write('output/output%02d.txt' % i)

shutil.rmtree('input')
shutil.rmtree('output')