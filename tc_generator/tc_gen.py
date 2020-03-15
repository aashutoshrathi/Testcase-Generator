'''
        Aashutosh Rathi
https://github.com/aashutoshrathi/
Testcase Generator for HackerRank

'''

__all__ = ['DIRNAME', 'IN_SOURCE', 'OUT_SOURCE', 'POWER', 'RINT', 'TC_SOURCE', 'generate',
  'compile_them', 'zip_codechef', 'zip_hackerrank', 'zip_hackerearth', 'zip_them']

import math
import os
import random
import shutil
import sys
import timeit
import zipfile

from tc_generator.lang_compiler import LANGS

DIRNAME = os.path.dirname(__file__) # Absolute path of the file
IN_SOURCE = os.path.join(DIRNAME, 'input')
OUT_SOURCE = os.path.join(DIRNAME, 'output')
TC_SOURCE = os.path.join(DIRNAME, 'test-cases')
POWER = math.pow
RINT = random.randint


def generate(lang_choice, i):
    try:
        if os.system(f"{LANGS[lang_choice]['command']} < \
          {os.path.join(IN_SOURCE, f'input{i:02d}.txt')} > \
            {os.path.join(OUT_SOURCE, f'output{i:02d}.txt')}") != 0:
            raise Exception('Runtime error!')
    except Exception as error:
        print(error, file=sys.stderr)
        print(f"Looks like you don't have {LANGS[lang_choice]['req']} :/", file=sys.stderr)
        print(f"You can refer to {LANGS[lang_choice]['link']} for help.", file=sys.stderr)
        sys.exit(1)


def compile_them(lang_choice):
    try:
        if os.system(LANGS[lang_choice]['compile']) != 0:
            raise Exception('Compilation error!')
    except Exception as error:
        print(error, file=sys.stderr)
        print(f"Looks like you don't have {LANGS[lang_choice]['req']} :/", file=sys.stderr)
        print(f"You can refer to {LANGS[lang_choice]['link']} for help.", file=sys.stderr)
        sys.exit(1)


def zip_hackerrank():
    with zipfile.ZipFile(TC_SOURCE + '.zip', 'w', \
        zipfile.ZIP_DEFLATED) as zip_file:
        for in_file in os.listdir(IN_SOURCE):
            zip_file.write(os.path.join(IN_SOURCE, in_file), \
                os.path.join('input', in_file))
        for out_file in os.listdir(OUT_SOURCE):
            zip_file.write(os.path.join(OUT_SOURCE, out_file), \
                os.path.join('output', out_file))
    print(f"Test cases saved in {TC_SOURCE + '.zip'}")


def zip_hackerearth():
    with zipfile.ZipFile(TC_SOURCE + '.zip', 'w', \
        zipfile.ZIP_DEFLATED) as zip_file:
        for in_file in os.listdir(IN_SOURCE):
            zip_file.write(os.path.join(IN_SOURCE, in_file), \
                in_file.replace('put', ''))
        for out_file in os.listdir(OUT_SOURCE):
            zip_file.write(os.path.join(OUT_SOURCE, out_file), \
                out_file.replace('put', ''))
    print(f"Test cases saved in {TC_SOURCE + '.zip'}")


def zip_codechef():
    if not os.path.exists(TC_SOURCE):
        os.mkdir(TC_SOURCE)
    for in_file in os.listdir(IN_SOURCE):
        shutil.copy(os.path.join(IN_SOURCE, in_file), TC_SOURCE)
    for out_file in os.listdir(OUT_SOURCE):
        shutil.copy(os.path.join(OUT_SOURCE, out_file), TC_SOURCE)
    print(f"Test cases saved in {TC_SOURCE} folder")


def zip_them(test_files, lang_choice, pltfrm_choice):
    for i in range(0, test_files + 1):
        print(f'Generating output: {i}')
        exe_command = 'generate({0}, {1})'.format(lang_choice, i)
        exe_time = timeit.timeit(exe_command, globals=globals(), number=1)
        print(f'Time taken to execute this TC {exe_time:02f} seconds', \
            file=sys.stderr)
        out_file = os.path.join(OUT_SOURCE, f'output{i:02d}.txt')
        try:
            if os.stat(out_file).st_size == 0:
                raise Exception('Blank output file!')
        except Exception as error:
            print(error, file=sys.stderr)
    print('Zipping ... ')

    switcher = {
      1: zip_hackerrank,
      2: zip_hackerearth,
      3: zip_codechef
    }

    zip_choice  = switcher.get(pltfrm_choice)
    zip_choice()


def main():

    if not os.path.exists(IN_SOURCE):
      os.mkdir(IN_SOURCE)
    if not os.path.exists(OUT_SOURCE):
      os.mkdir(OUT_SOURCE)

    try:
        lang_choice = int(input(
            "Enter your choice of language\n1. C\n2. C++\n3. Java\n4. Python\n5. C#\n6. Go\n"))
        pltfrm_choice = int(input(
            "Enter your choice of platform\n1. HackerRank\n2. HackerEarth\n3. CodeChef\n"))
    except (SyntaxError, ValueError):
        print("You didn't enter a number!")
        sys.exit(1)

    if lang_choice not in range(1, 7):
        print("Wrong choice entered!")
        sys.exit(1)
    if pltfrm_choice not in range(1, 4):
        print("Wrong choice entered!")
        sys.exit(1)

    lang_choice -= 1
    test_files = 10  # number of test files, change it according to you.

    for i in range(0, test_files + 1):
        print(f'Generating input: {i}')
        sys.stdout = open(os.path.join(IN_SOURCE, f'input{i:02d}.txt'), 'w')

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

        sys.stdout = sys.__stdout__
        # Input File Printing Ends

    compile_them(lang_choice)
    zip_them(test_files, lang_choice, pltfrm_choice)

    shutil.rmtree(IN_SOURCE)
    shutil.rmtree(OUT_SOURCE)


if __name__ == "__main__":
    main()
