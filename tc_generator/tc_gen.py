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
    INPUT = input
    XRange = range

try:
    os.mkdir('input')
    os.mkdir('output')
except OSError:
    pass

POWER = math.pow
RINT = random.randint


def generate(choice, i):
    try:
        if choice == 1:  # Choice of language is C
            os.system(
                './logic < input/input%02d.txt > output/output%02d.txt' %
                (i, i))

        elif choice == 2:  # Choice of language is C++
            os.system(
                './logic < input/input%02d.txt > output/output%02d.txt' %
                (i, i))

        elif choice == 3:  # Choice of language is Java
            os.system(
                'java logic < input/input%02d.txt > output/output%02d.txt' %
                (i, i))
        elif choice == 4:  # Choice of language is Python
            # System call to generate output files for Python
            os.system(
                'python logic.py < input/input%02d.txt > output/output%02d.txt' %
                (i, i))

    except BaseException:
        print("No compiler found")


def compile_them(choice):
    if choice == 1:  # Choice of language is C
        os.system('gcc -o logic logic.c')  # System call to compile .c file
    elif choice == 2:  # Choice of language is C++
        # System call to compile .cpp file
        os.system('g++ -o logic logic.cpp')
    elif choice == 3:  # Choice of language is Java
        os.system('javac logic.java')  # System call to compile .java file


def zip_them(test_files, choice):
    with zipfile.ZipFile('test-cases.zip', 'w', zipfile.ZIP_DEFLATED) as zip_file:
        for i in XRange(0, test_files + 1):
            print('Zipping:', i, file=sys.stderr)
            exe_command = 'generate({0}, {1})'.format(choice, i)
            exe_time = timeit.timeit(
                exe_command, globals=globals(), number=1)
            print('Time taken to execute this TC %02f seconds' %
                  (exe_time), file=sys.stderr)

            zip_file.write('input/input%02d.txt' % i)
            zip_file.write('output/output%02d.txt' % i)


def main():
    choice = int(INPUT(
        "Enter your choice of language\n1 for C\n2 for C++\n3 for Java\n4 for Python\n"))
    if choice not in (1, 2, 3, 4):
        print("Wrong choice entered!")
        exit()

    test_files = 10  # number of test files, change it according to you.

    for i in XRange(0, test_files + 1):
        print('Generating:', i, file=sys.stderr)
        sys.stdout = open('input/input%02d.txt' % i, 'w')

        '''
        Input area will start here,
        everything that you print out here will be taken as input in your logic file.
        '''

        # Input File Printing Starts

        if choice in (1, 2, 4):
            # number of test cases in (1,10^5)
            required_input = RINT(5, POWER(10, (i // 2) + 1))
            print(required_input)  # Prints x into input file
            for _ in range(required_input):
                print(RINT(1, POWER(10, min(4, max(i // 2, 2)))))
        elif choice == 3:
            print(RINT(1, 5))

        sys.stdout.close()
        # Input File Printing Ends
    compile_them(choice)
    zip_them(test_files, choice)
    shutil.rmtree('input')
    shutil.rmtree('output')


if __name__ == "__main__":
    main()
