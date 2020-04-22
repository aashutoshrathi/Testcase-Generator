"""
        Aashutosh Rathi
https://github.com/aashutoshrathi/
Testcase Generator for HackerRank, HackerEarth and CodeChef

Usage: Run 'python tc_gen.py' and follow the prompt to select
language and platform for testcase generation.

To change input file logic, go to the line with the comment
"# Input area will start here" and edit the lines below, according
to the pattern you want.
"""

__all__ = ['DIRNAME', 'IN_SOURCE', 'OUT_SOURCE', 'POWER', 'RINT', 'TC_SOURCE', 'generate',
           'compile_them', 'zip_codechef', 'zip_hackerrank', 'zip_hackerearth', 'zip_them',
           'check_empty', 'make_dirs', 'Error', 'EmptyFileException', 'CompilationError',
           'RunError', 'ValueOutsideRange', 'make_lf_ending']

import math
import os
import random
import shutil
import sys
import timeit
import zipfile
import subprocess

from tc_generator.lang_compiler import LANGS


class Error(Exception):
    """Base class for other exceptions."""
    pass

class EmptyFileException(Error):
    """Raised when output file is empty"""
    pass

class CompilationError(Error):
    """Raised when logic program is not compiled properly"""
    pass

class RunError(Error):
    """Raised when logic program encounters runtime error"""
    pass

class ValueOutsideRange(Error):
    """Raised when value entered is outside range"""
    pass



DIRNAME = os.path.abspath(os.path.dirname(__file__)) # Absolute path of the file
IN_SOURCE = os.path.join(DIRNAME, 'input')
OUT_SOURCE = os.path.join(DIRNAME, 'output')
TC_SOURCE = os.path.join(DIRNAME, 'test-cases')
TC_ZIP = TC_SOURCE + '.zip'
POWER = math.pow
RINT = random.randint
WINDOWS_LINE_ENDING = b'\r\n'
UNIX_LINE_ENDING = b'\n'


def make_dirs():
    """Deletes old directories and creates new ones."""

    shutil.rmtree(IN_SOURCE, ignore_errors=True)
    shutil.rmtree(OUT_SOURCE, ignore_errors=True)
    shutil.rmtree(TC_SOURCE, ignore_errors=True)
    try:
        os.remove(TC_ZIP)
    except OSError:
        pass

    os.mkdir(IN_SOURCE)
    os.mkdir(OUT_SOURCE)


def check_empty(file):
    """Raises exception if file is empty."""

    if os.stat(file).st_size == 0:
        raise EmptyFileException('Empty output file!')


def make_lf_ending(file):
    """Converts all crlf line endings to lf"""

    with open(file, 'rb') as in_file:
        content = in_file.read()
    content = content.replace(WINDOWS_LINE_ENDING, UNIX_LINE_ENDING)
    with open(file, 'wb') as out_file:
        out_file.write(content)


def compile_them(lang_choice):
    """
    Compiles the code.
    Raises error if there's some compilation error.

    Argument:
    lang_choice -- The choice of language which is chosen by the user
    """

    # Don't run compile for Python
    if lang_choice == 3:
        return

    compiled = subprocess.Popen(LANGS[lang_choice]['compile'],
                                stdin=subprocess.PIPE,
                                stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE,
                                universal_newlines=True)
    sdout,stderr = compiled.communicate()
    if stderr:
        raise CompilationError(f'Compilation error!\n{stderr}')


def generate(lang_choice, i):
    """
    Passes input through the compiled code (Except for Python) and generates
    output files.
    Raises error if there's a problem while running.

    Argument:
    lang_choice -- The choice of language which is chosen by the user
    i           -- 'i'th testcase for which output is to be generated
    """

    with open(os.path.join(IN_SOURCE, f'input{i:02d}.txt'), 'r+') as in_file:
        with open(os.path.join(OUT_SOURCE, f'output{i:02d}.txt'), 'w+') as out_file:
            generated = subprocess.Popen(LANGS[lang_choice]['command'],
                                         stdin=in_file,
                                         stdout=out_file,
                                         stderr=subprocess.PIPE,
                                         universal_newlines=True)

    sdout,stderr = generated.communicate()
    if stderr:
        raise RunError(f'Runtime error!\n{stderr}')


def zip_hackerrank():
    """
    Zips files into 'test-cases.zip'.
    Input files are named as input<number>.txt and are placed inside
    'input' directory in zip.
    Output files are named as output<number>.txt and are placed inside
    'output' directory in zip.
    """

    with zipfile.ZipFile(TC_ZIP, 'w', \
        zipfile.ZIP_DEFLATED) as zip_file:
        for in_file in os.listdir(IN_SOURCE):
            zip_file.write(os.path.join(IN_SOURCE, in_file), \
                os.path.join('input', in_file))
        for out_file in os.listdir(OUT_SOURCE):
            zip_file.write(os.path.join(OUT_SOURCE, out_file), \
                os.path.join('output', out_file))
    print(f"Test cases saved in {TC_ZIP}")


def zip_hackerearth():
    """
    Zips files into 'test-cases.zip'.
    Input files are named as in<number>.txt and are placed inside the zip.
    Output files are named as out<number>.txt and are placed inside the zip.
    """

    with zipfile.ZipFile(TC_ZIP, 'w', \
        zipfile.ZIP_DEFLATED) as zip_file:
        for in_file in os.listdir(IN_SOURCE):
            zip_file.write(os.path.join(IN_SOURCE, in_file), \
                in_file.replace('put', ''))
        for out_file in os.listdir(OUT_SOURCE):
            zip_file.write(os.path.join(OUT_SOURCE, out_file), \
                out_file.replace('put', ''))
    print(f"Test cases saved in {TC_ZIP}")


def zip_codechef():
    """
    Places files inside 'test-cases' directory.
    Input files are named as input<number>.txt and are placed inside the directory.
    Output files are named as output<number>.txt and are placed inside the directory.
    """

    if not os.path.exists(TC_SOURCE):
        os.mkdir(TC_SOURCE)
    for in_file in os.listdir(IN_SOURCE):
        shutil.copy(os.path.join(IN_SOURCE, in_file), TC_SOURCE)
    for out_file in os.listdir(OUT_SOURCE):
        shutil.copy(os.path.join(OUT_SOURCE, out_file), TC_SOURCE)
    print(f"Test cases saved in {TC_SOURCE} directory")


def zip_them(test_files, lang_choice, pltfrm_choice):
    """
    Calls generate function for each test case, checks for empty output files and
    then calls the zipping function for the platform chosen by the user.

    Arguments:
    test_files    -- The number of test case files to be generated
    lang_choice   -- The choice of language which is chosen by the user
    pltfrm_choice -- The choice of platform which is chosen by the user
    """

    platforms = [zip_hackerrank, zip_hackerearth, zip_codechef]

    for i in range(0, test_files + 1):
        print(f'Generating output: {i}')

        exe_command = f'generate({lang_choice}, {i})'

        try:
            exe_time = timeit.timeit(exe_command, globals=globals(), number=1)
        except RunError as run_error:
            print(run_error, file=sys.stderr)
            print(f"Looks like you don't have {LANGS[lang_choice]['req']} :/", file=sys.stderr)
            print(f"You can refer to {LANGS[lang_choice]['link']} for help.", file=sys.stderr)
            sys.exit(1)
        except FileNotFoundError as no_file:
            print(no_file, file=sys.stderr)
            sys.exit(1)

        print(f'Time taken to execute this TC {exe_time:02f} seconds')

        out_file = os.path.join(OUT_SOURCE, f'output{i:02d}.txt')
        make_lf_ending(out_file)
        try:
            check_empty(out_file)
        except EmptyFileException as empty_file:
            print(empty_file, file=sys.stderr)

    print('Zipping ... ')
    zip_choice = platforms[pltfrm_choice]
    zip_choice()


def main():
    """
    Takes in the choice of language and platform from the user, creates input files as per the
    logic defined in the input area and calls in the complie_them and zip_them function.
    """

    try:
        lang_choice = int(input(
            "Enter your choice of language\n1. C\n2. C++\n3. Java\n4. Python\n5. C#\n6. Go\n"))
        pltfrm_choice = int(input(
            "Enter your choice of platform\n1. HackerRank\n2. HackerEarth\n3. CodeChef\n"))
        if lang_choice not in range(1, 7):
            raise ValueOutsideRange("Choice of language should be in 1 to 6!")
        if pltfrm_choice not in range(1, 4):
            raise ValueOutsideRange("Choice of platform should be in 1 to 3!")
    except (SyntaxError, ValueError) as err:
        print(err, file=sys.stderr)
        print("You didn't enter a number!", file=sys.stderr)
        sys.exit(1)
    except ValueOutsideRange as val_err:
        print(val_err, file=sys.stderr)
        print("Wrong choice entered!", file=sys.stderr)
        sys.exit(1)

    make_dirs()

    lang_choice -= 1
    pltfrm_choice -= 1
    test_files = 10  # number of test files, change it according to you.

    for i in range(0, test_files + 1):
        print(f'Generating input: {i}')
        in_file = os.path.join(IN_SOURCE, f'input{i:02d}.txt')
        sys.stdout = open(in_file, 'w')

        # Input area will start here,
        # everything that you print out here will be taken as input in your logic file.

        # Input File Printing Starts
        # number of test cases in (1,10^5)
        required_input = RINT(5, POWER(10, (i // 2) + 1))
        print(required_input)  # Prints x into input file
        for _ in range(required_input):
            print(RINT(1, POWER(10, min(4, max(i // 2, 2)))))

        # Input File Printing Ends
        sys.stdout = sys.__stdout__

        make_lf_ending(in_file)

    try:
        compile_them(lang_choice)
    except CompilationError as comp_error:
        print(comp_error, file=sys.stderr)
        print(f"Looks like you don't have {LANGS[lang_choice]['req']} :/", file=sys.stderr)
        print(f"You can refer to {LANGS[lang_choice]['link']} for help.", file=sys.stderr)
        sys.exit(1)

    zip_them(test_files, lang_choice, pltfrm_choice)

    shutil.rmtree(IN_SOURCE)
    shutil.rmtree(OUT_SOURCE)


if __name__ == "__main__":
    main()
