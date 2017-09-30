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

try:
	os.mkdir('input')
	os.mkdir('output')
except OSError:
	pass

tf = 10 # number of test files, change it according to you.

for i in xrange(0, tf + 1):
	print >> sys.stderr, 'Generating:', i
	sys.stdout = open('input/input%02d.txt' % i, 'wb')
	
	'''
	Input area will start here,
	everything that you print out here will be taken as input in your logic file.
	You can set difficulty of test cases all by you.
	'''

	sys.stdout.close()
	# Input File Printing Ends


'''
Output generation and zipping starts here
just replace '<filename>' with your actual filename everywhere

'''
with zipfile.ZipFile('test-cases.zip', 'w', zipfile.ZIP_DEFLATED) as zf: # You can change zip filename as per your wish.
	for i in xrange(0, tf + 1):
		print >> sys.stderr, 'Zipping:', i # Will show status of which TC output is generated.
		os.system('javac <filename>.java') # System call to compile your file
		os.system('java <filename> < input/input%02d.txt > output/output%02d.txt' % (i, i))
		zf.write('input/input%02d.txt' % i)
		zf.write('output/output%02d.txt' % i)