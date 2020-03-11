'''
        Aashutosh Rathi
https://github.com/aashutoshrathi/
Testcase Generator for HackerRank

'''
from __future__ import print_function

import math
import os
import random
import shutil
import sys
import timeit
import zipfile

from lang_compiler import LANGS

platform = sys.platform
dirname = os.path.dirname(__file__) # Absolute path of the file

if sys.version[0] == '3':
    INPUT = input
    XRange = range

try:
    os.mkdir(os.path.join(dirname, 'input'))
    os.mkdir(os.path.join(dirname, 'output'))
except OSError:
    pass

POWER = math.pow
RINT = random.randint


def generate(choice, i):
    try:
        if os.system('%s < %s > %s' % (LANGS[choice - 1]['command'], 
                os.path.join(dirname, 'input', f'input{i:02d}.txt'),
                os.path.join(dirname, 'output', f'output{i:02d}.txt'))) != 0:
            raise Exception('Runtime error!')
    except Exception as error:
        print(error, file=sys.stderr)
        print("Looks like you don't have %s :/ \nYou can refer to %s for help." % (
            LANGS[choice - 1]['req'], LANGS[choice - 1]['link']), file=sys.stderr)
        sys.exit(1)


def compile_them(test_files, choice):
    try:
        if os.system(LANGS[choice - 1]['compile']) != 0:
            raise Exception('Compilation error!')
    except Exception as error:
        print(error, file=sys.stderr)
        print("Looks like you don't have %s :/ \nYou can refer to %s for help." % (
            LANGS[choice - 1]['req'], LANGS[choice - 1]['link']), file=sys.stderr)
        sys.exit(1)
    zip_them(test_files, choice)


def zip_them(test_files, choice):
    with zipfile.ZipFile(os.path.join(dirname, 'test-cases.zip'), 'w',
        zipfile.ZIP_DEFLATED) as zip_file:
        for i in XRange(0, test_files + 1):
            print('Zipping:', i, file=sys.stderr)
            exe_command = 'generate({0}, {1})'.format(choice, i)
            exe_time = timeit.timeit(
                exe_command, globals=globals(), number=1)
            print('Time taken to execute this TC %02f seconds' %
                  (exe_time), file=sys.stderr)
            f = open(os.path.join(dirname, 'output', 'output%02d.txt'% i), 'rt')
            try:
                if f.read() is '':
                    raise Exception('Blank output file!')
            except Exception as error:
                print(error, file=sys.stderr)
            f.close()
            zip_file.write(os.path.join(dirname, 'input', 'input%02d.txt' % i))
            zip_file.write(os.path.join(dirname, 'output', 'output%02d.txt' % i))


def main():
    try:
        choice = int(INPUT(
            "Enter your choice of language\n1. C\n2. C++\n3. Java\n4. Python\n5. C#\n6. Go\n"))
    except (SyntaxError, ValueError):
        print("You didn't enter a number!")
        sys.exit(1)
    if choice not in range(1, 7):
        print("Wrong choice entered!")
        sys.exit(1)

    test_files = 10  # number of test files, change it according to you.

    for i in XRange(0, test_files + 1):
        print('Generating:', i, file=sys.stderr)
        sys.stdout = open(os.path.join(dirname, 'input', 'input%02d.txt' % i), 'w')

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
    shutil.rmtree(os.path.join(dirname, 'input'))
    shutil.rmtree(os.path.join(dirname, 'output'))


if __name__ == "__main__":
    main()
