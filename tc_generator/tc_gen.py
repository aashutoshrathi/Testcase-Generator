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


def generate(choice, i):
    try:
        if platform.system()=='Windows':
            os.system('%s < input/input%02d.txt > output/output%02d.txt' %
                      (LANGS[choice - 1]['commandW'], i, i))
        else:
            os.system('%s < input/input%02d.txt > output/output%02d.txt' %
                      (LANGS[choice - 1]['commandL'], i, i))
        
    except Exception:
        print("Looks like you don't have {0} :/ \nYou can refer to {1} for help.".format(
            LANGS[choice - 1]['req'], LANGS[choice - 1]['link']))


def compile_them(test_files, choice):
    if platform.system()=='Windows':
        if os.system(LANGS[choice - 1]['compileW']) == 0:
            zip_them(test_files, choice)
    else:
        if os.system(LANGS[choice - 1]['compileL']) == 0:
            zip_them(test_files, choice)

def zip_them(test_files, choice):
    with zipfile.ZipFile('test-cases.zip', 'w', zipfile.ZIP_DEFLATED) as zip_file:
        for i in XRange(0, test_files + 1):
            print('Zipping:', i, file=sys.stderr)
            exe_command = 'generate({0}, {1})'.format(choice, i)
            exe_time = timeit.timeit(
                exe_command, globals=globals(), number=1)
            print('Time taken to execute this TC %02f seconds' %
                  (exe_time), file=sys.stderr)
            f = open('output/output%02d.txt' % i, 'rt')
            try:
                if f.read() is '':
                    raise Exception('blank output file')
            except Exception as error:
                print(repr(error))
            f.close()
            zip_file.write('input/input%02d.txt' % i)
            zip_file.write('output/output%02d.txt' % i)


def main():
    '''choice = int(INPUT(
        "Enter your choice of language\n1. C\n2. C++\n3. Java\n4. Python\n5. C#\n6. Go\n"))'''
    choice = int(sys.argv[1])
    if choice not in range(1, 7):
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
        # number of test cases in (1,10^5)
        required_input = RINT(5, POWER(10, (i // 2) + 1))
        print(required_input)  # Prints x into input file
        for _ in range(required_input):
            print(RINT(1, POWER(10, min(4, max(i // 2, 2)))))

        sys.stdout.close()
        # Input File Printing Ends
    compile_them(test_files, choice)
    shutil.rmtree('input')
    shutil.rmtree('output')


if __name__ == "__main__":
    main()
