'''
        Aashutosh Rathi
https://github.com/aashutoshrathi/
Testcase Generator for HackerRank

'''
from __future__ import print_function
import os
import random
import shutil
import sys
import timeit
import zipfile
import math

if sys.version[0] == '3':
    raw_input = input
    xrange = range

try:
    os.mkdir('input')
    os.mkdir('output')
except OSError:
    pass

pwr = math.pow
rint = random.randint


def generate(choice, i):
    if choice == 1:  # Choice of language is C
        os.system('gcc -o logic logic.c')  # System call to compile .c file
        # System call to generate output files for C
        os.system(
            './logic < input/input%02d.txt > output/output%02d.txt' % (i, i))
    elif choice == 2:  # Choice of language is C++
        # System call to compile .cpp file
        os.system('g++ -o logic logic.cpp')
        # System call to generate output files for C++
        os.system(
            './logic < input/input%02d.txt > output/output%02d.txt' % (i, i))
    elif choice == 3:  # Choice of language is Java
        os.system('javac logic.java')  # System call to compile .java file
        # System call to generate output files for Java
        os.system(
            'java logic < input/input%02d.txt > output/output%02d.txt' % (i, i))
    elif choice == 4:  # Choice of language is Python
        # System call to generate output files for Python
        os.system(
            'python logic.py < input/input%02d.txt > output/output%02d.txt' % (i, i))


def zip_them(test_files, choice):
    with zipfile.ZipFile('test-cases.zip', 'w', zipfile.ZIP_DEFLATED) as zipFile:
        for i in xrange(0, test_files + 1):
            print('Zipping:', i, file=sys.stderr)
            exe_command = 'generate({0}, {1})'.format(choice, i)
            exe_time = timeit.timeit(
                exe_command, globals=globals(), number=1)
            print('Time taken to execute this TC %02f seconds' %
                  (exe_time), file=sys.stderr)

            zipFile.write('input/input%02d.txt' % i)
            zipFile.write('output/output%02d.txt' % i)


def main():
    choice = int(raw_input(
        "Enter your choice of language\n1 for C\n2 for C++\n3 for Java\n4 for Python\n"))
    if choice not in (1, 2, 3, 4):
        print("Wrong choice entered!")
        exit()

    test_files = 10  # number of test files, change it according to you.

    for i in xrange(0, test_files + 1):
        print('Generating:', i, file=sys.stderr)
        sys.stdout = open('input/input%02d.txt' % i, 'w')

        '''
        Input area will start here,
        everything that you print out here will be taken as input in your logic file.
        You can set difficulty of test cases all by you.
        '''

        # Input File Printing Starts
        if choice in (1, 2, 4):
            # number of test cases in (1,10^5)
            x = rint(5, pwr(10, (i // 2) + 1))
            print(x)  # Prints x into input file
            for _ in range(x):
                print(rint(1, pwr(10, min(4, max(i // 2, 2)))))
        elif choice == 3:
            print(rint(1, 5))

        sys.stdout.close()
        # Input File Printing Ends
    zip_them(test_files, choice)
    shutil.rmtree('input')
    shutil.rmtree('output')


if __name__ == "__main__":
    main()
