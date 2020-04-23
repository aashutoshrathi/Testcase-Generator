"""
Tests the generate function and the checks for identifying empty files.
"""

import os
import sys
import shutil
import pytest

from tc_generator.tc_gen import (IN_SOURCE, OUT_SOURCE, RINT, POWER, generate, check_empty,
                                 make_dirs, EmptyFileException, CompilationError, make_lf_ending)


TEST_FILES = 4 # Number of files to create for testing
TEST_LANG = 3 # Testing for Python


@pytest.fixture(autouse=True)
def make_input_files():
    """
    Creates the input files for testing
    """

    make_dirs()

    for i in range(0, TEST_FILES + 1):
        sys.stdout = open(os.path.join(IN_SOURCE, f'input{i:02d}.txt'), 'w+')

        required_input = RINT(5, POWER(10, (i // 2) + 1))
        print(required_input)  # Prints x into input file
        for _ in range(required_input):
            print(RINT(1, POWER(10, min(4, max(i // 2, 2)))))

        sys.stdout = sys.__stdout__

    yield

    shutil.rmtree(IN_SOURCE)
    shutil.rmtree(OUT_SOURCE)


def test_generate():
    """
    Tests the generate function by checking if corresponding output
    files are generated for each input file and if it throws error for
    no input files.
    """

    # Tests if generate() runs successfuly
    for i in range(0, TEST_FILES + 1):
        try:
            generate(TEST_LANG, i)
        except CompilationError:
            pytest.fail("Compilation Error")
        if not os.path.exists(os.path.join(OUT_SOURCE, f'output{i:02d}.txt')):
            pytest.fail("Output file not found")

    # Tests if generate() throws error
    for i in range(TEST_FILES + 1, TEST_FILES + 2):
        with pytest.raises(FileNotFoundError):
            generate(TEST_LANG, i)


def test_empty():
    """
    Checks if no empty files are being generated and if it correctly
    identifies them.
    """

    # Tests if the logic is not generating empty files
    for i in range(0, TEST_FILES + 1):
        generate(TEST_LANG, i)
        out_file = os.path.join(OUT_SOURCE, f'output{i:02d}.txt')
        try:
            check_empty(out_file)
        except EmptyFileException:
            pytest.fail("Empty file found!")

    # Tests if correctly identifies empty files
    for i in range(TEST_FILES + 1, TEST_FILES + 2):
        out_file = os.path.join(OUT_SOURCE, f'output{i:02d}.txt')
        file = open(out_file, 'w')
        file.close()
        with pytest.raises(Exception) as error:
            check_empty(out_file)
