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

DIRNAME = os.path.dirname(__file__) # Absolute path of the file
IN_SOURCE = os.path.join(DIRNAME, 'input')
OUT_SOURCE = os.path.join(DIRNAME, 'output')
TC_SOURCE = os.path.join(DIRNAME, 'test-cases')


if sys.version[0] == '3':
    INPUT = input
    XRange = range


if not os.path.exists(IN_SOURCE):
    os.mkdir(IN_SOURCE)
if not os.path.exists(OUT_SOURCE):
    os.mkdir(OUT_SOURCE)


POWER = math.pow
RINT = random.randint


def generate(lang_choice, i):
    try:
        if os.system('%s < %s > %s' % (LANGS[lang_choice - 1]['command'], \
                os.path.join(IN_SOURCE, f'input{i:02d}.txt'), \
                os.path.join(OUT_SOURCE, f'output{i:02d}.txt'))) != 0:
            raise Exception('Runtime error!')
    except Exception as error:
        print(error, file=sys.stderr)
        print("Looks like you don't have %s :/ \nYou can refer to %s for help." % (
            LANGS[lang_choice - 1]['req'], LANGS[lang_choice - 1]['link']), \
                file=sys.stderr)
        sys.exit(1)


def compile_them(lang_choice):
    try:
        if os.system(LANGS[lang_choice - 1]['compile']) != 0:
            raise Exception('Compilation error!')
    except Exception as error:
        print(error, file=sys.stderr)
        print("Looks like you don't have %s :/ \nYou can refer to %s for help." % (
            LANGS[lang_choice - 1]['req'], LANGS[lang_choice - 1]['link']), \
                file=sys.stderr)
        sys.exit(1)


def zip_hackerrank():
    with zipfile.ZipFile(os.path.join(DIRNAME, 'test-cases.zip'), 'w', \
        zipfile.ZIP_DEFLATED) as zip_file:
        for in_file in os.listdir(IN_SOURCE):
            zip_file.write(os.path.join(IN_SOURCE, in_file), \
                os.path.join('input', in_file))
        for out_file in os.listdir(OUT_SOURCE):
            zip_file.write(os.path.join(OUT_SOURCE, out_file), \
                os.path.join('output', out_file))


def zip_hackerearth():
    with zipfile.ZipFile(os.path.join(DIRNAME, 'test-cases.zip'), 'w', \
        zipfile.ZIP_DEFLATED) as zip_file:
        for in_file in os.listdir(IN_SOURCE):
            zip_file.write(os.path.join(IN_SOURCE, in_file), \
                in_file.replace('put', ''))
        for out_file in os.listdir(OUT_SOURCE):
            zip_file.write(os.path.join(OUT_SOURCE, out_file), \
                out_file.replace('put', ''))


def zip_codechef():
    if not os.path.exists(TC_SOURCE):
        os.mkdir(TC_SOURCE)
    for in_file in os.listdir(IN_SOURCE):
        shutil.copy(os.path.join(IN_SOURCE, in_file), TC_SOURCE)
    for out_file in os.listdir(OUT_SOURCE):
        shutil.copy(os.path.join(OUT_SOURCE, out_file), TC_SOURCE)


def zip_them(test_files, lang_choice, pltfrm_choice):
    for i in XRange(0, test_files + 1):
        print(f'Generating output: {i:2d}', file=sys.stderr)
        exe_command = 'generate({0}, {1})'.format(lang_choice, i)
        exe_time = timeit.timeit(exe_command, globals=globals(), number=1)
        print('Time taken to execute this TC %02f seconds' %
              (exe_time), file=sys.stderr)
        out_file = os.path.join(OUT_SOURCE, 'output%02d.txt'% i)
        try:
            if os.stat(out_file).st_size == 0:
                raise Exception('Blank output file!')
        except Exception as error:
            print(error, file=sys.stderr)
    print('Zipping...', file=sys.stderr)
    if pltfrm_choice == 1:
        zip_hackerrank()
    elif pltfrm_choice == 2:
        zip_hackerearth()
    elif pltfrm_choice == 3:
        zip_codechef()
    else:
        print('Wrong choice of platform!', file=sys.stderr)
        sys.exit(1)


def main():
    try:
        lang_choice = int(INPUT(
            "Enter your choice of language\n1. C\n2. C++\n3. Java\n4. Python\n5. C#\n6. Go\n"))
    except (SyntaxError, ValueError):
        print("You didn't enter a number!")
        sys.exit(1)
    if lang_choice not in range(1, 7):
        print("Wrong choice entered!")
        sys.exit(1)

    try:
        pltfrm_choice = int(INPUT(
            "Enter your choice of platform\n1. HackerRank\n2. HackerEarth\n3. CodeChef\n"))
    except (SyntaxError, ValueError):
        print("You didn't enter a number!")
        sys.exit(1)
    if pltfrm_choice not in range(1, 4):
        print("Wrong choice entered!")
        sys.exit(1)

    test_files = 10  # number of test files, change it according to you.

    for i in XRange(0, test_files + 1):
        print(f'Generating input: {i:2d}', file=sys.stderr)
        sys.stdout = open(os.path.join(IN_SOURCE, 'input%02d.txt' % i), 'w')

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
    compile_them(lang_choice)
    zip_them(test_files, lang_choice, pltfrm_choice)
    shutil.rmtree(IN_SOURCE)
    shutil.rmtree(OUT_SOURCE)


if __name__ == "__main__":
    main()
