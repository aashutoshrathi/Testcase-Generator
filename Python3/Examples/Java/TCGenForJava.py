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

rint = random.randint

tf = 10 # number of test files, change it according to you.

for i in range(0, tf + 1):
	print ('Generating:', i, file=sys.stderr)
	sys.stdout = open('input/input%02d.txt' % i, 'w')
	
	'''
	Input area will start here,
	everything that you print out here will be taken as input in your logic file.
	You can set difficulty of test cases all by you.
	'''

	### Input File Printing Start
	x = rint(1, 100) # number of test cases in (1,100)
	print(x) # Prints x into input file
	for z in range (x):
		print(rint(1, 100000)) 
	sys.stdout.close()
	### Input File Printing Ends


'''
Output generation and zipping starts here
just replace '<filename>' with your actual filename everywhere

'''
with zipfile.ZipFile('test-cases.zip', 'w', zipfile.ZIP_DEFLATED) as zf: # You can change zip filename as per your wish.
	for i in range(0, tf + 1):
		print('Zipping:', i, file=sys.stderr) # Will show status of which TC output is generated.
		os.system('javac logic.java') # System call to compile your file
		os.system('java logic < input/input%02d.txt > output/output%02d.txt' % (i, i))
		zf.write('input/input%02d.txt' % i)
		zf.write('output/output%02d.txt' % i)

shutil.rmtree('input')
shutil.rmtree('output')
