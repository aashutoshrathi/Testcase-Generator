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

choice = int(raw_input("Enter your choice of language\n1 for C\n2 for C++\n3 for Java\n4 for Python\n"))
if choice != 1 and choice != 2 and choice != 3 and choice != 4:
    print("Wrong choice entered!")
    exit()

tf = 10  # number of test files, change it according to you.

for i in xrange(0, tf + 1):
    print >> sys.stderr, 'Generating:', i
    sys.stdout = open('input/input%02d.txt' % i, 'wb')

    '''
    Input area will start here,
    everything that you print out here will be taken as input in your logic file.
    You can set difficulty of test cases all by you.
    '''

    # Input File Printing Starts

    sys.stdout.close()
    # Input File Printing Ends


'''
Output generation and zipping starts here
just replace '<filename>' with your actual filename everywhere

'''
# You can change zip filename as per your wish.
with zipfile.ZipFile('test-cases.zip', 'w', zipfile.ZIP_DEFLATED) as zf:
    for i in xrange(0, tf + 1):
        print >> sys.stderr, 'Zipping:', i  # Will show status of which TC output is generated.

        if choice == 1:  # Choice of language is C
            os.system('gcc -o <filename> <filename>.c')  # System call to compile .c file
            # System call to generate output files for C
            os.system('./<filename> < input/input%02d.txt > output/output%02d.txt' % (i, i))
        elif choice == 2:  # Choice of language is C++
            os.system('g++ -o <filename> <filename>.cpp')  # System call to compile .cpp file
            # System call to generate output files for C++
            os.system('./<filename> < input/input%02d.txt > output/output%02d.txt' % (i, i))
        elif choice == 3:  # Choice of language is Java
            os.system('javac <filename>.java')  # System call to compile .java file
            # System call to generate output files for Java
            os.system('java <filename> < input/input%02d.txt > output/output%02d.txt' % (i, i))
        elif choice == 4:  # Choice of language is Python
            # System call to generate output files for Python
            os.system('python <filename>.py < input/input%02d.txt > output/output%02d.txt' % (i, i))

        zf.write('input/input%02d.txt' % i)
        zf.write('output/output%02d.txt' % i)

shutil.rmtree('input')
shutil.rmtree('output')
