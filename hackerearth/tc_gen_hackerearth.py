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

from lang_compiler import LANGS

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


def main():
    choice = int(INPUT("Enter your choice of language\n1. C\n2. C++\n3. Java\n4. Python\n5. C#\n6. Go\n"))
    if choice not in range(1, 7):
        print("Wrong choice entered!")
        exit()

    test_files = 10  # number of test files, change it according to you.

    for i in XRange(0, test_files + 1):
        print('Generating:', i, file=sys.stderr)
        sys.stdout = open('input2/input%02d.txt' % i, 'w')

        '''
        Input area will start here,
        everything that you print out here will be taken as input in your logic file.
        '''

        # Input File Printing Starts
        # number of test cases in (1,10^5)
        required_input = RINT(5, POWER(10, (i // 2) + 1))
        print(required_input)  # Prints x into input file
        for _ in range(required_input):
            print(RINT(1, POWER(10, min(4, max(i // 2, 2)))))

        sys.stdout.close()
        # Input File Printing Ends



if __name__ == "__main__":
    main()
