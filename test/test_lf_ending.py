"""
Tests if all files have lf endings.
"""

import os
import sys
import shutil
import pytest

from tc_generator.tc_gen import (IN_SOURCE, OUT_SOURCE, RINT, POWER,
                                 generate, make_dirs, make_lf_ending)


TEST_FILES = 4 # Number of files to create for testing
TEST_LANG = 3 # Testing for Python


@pytest.fixture(autouse=True)
def make_tc_files():
    """
    Creates the TC files for testing
    """

    make_dirs()

    for i in range(0, TEST_FILES + 1):
        in_file = os.path.join(IN_SOURCE, f'input{i:02d}.txt')
        out_file = os.path.join(OUT_SOURCE, f'output{i:02d}.txt')
        sys.stdout = open(in_file, 'w+')

        required_input = RINT(5, POWER(10, (i // 2) + 1))
        print(required_input)  # Prints x into input file
        for _ in range(required_input):
            print(RINT(1, POWER(10, min(4, max(i // 2, 2)))))

        sys.stdout = sys.__stdout__

        generate(TEST_LANG, i)

        make_lf_ending(in_file)
        make_lf_ending(out_file)

    yield

    shutil.rmtree(IN_SOURCE)
    shutil.rmtree(OUT_SOURCE)


def test_lf_ending():
    """
    Checks if all the input and output files ahev lf style file endings.
    """

    for i in range(0, TEST_FILES + 1):
        with open(os.path.join(IN_SOURCE, f'input{i:02d}.txt'), 'rb') as in_file:
            content = in_file.read()
            if content.find(b'\r') != -1:
                pytest.fail("'\\r' character found in input!")
        with open(os.path.join(OUT_SOURCE, f'output{i:02d}.txt'), 'rb') as out_file:
            content = out_file.read()
            if content.find(b'\r') != -1:
                pytest.fail("'\\r' character found in output!")
