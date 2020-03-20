"""
Tests the generate function and the checks for identifying blank files.
"""

import os
import sys
import shutil
import pytest

from tc_generator.tc_gen import (IN_SOURCE, OUT_SOURCE, RINT, POWER, generate)

TEST_FILES = 4 # Number of files to create for testing
TEST_LANG = 3 # Testing for Python


@pytest.fixture(autouse=True)
def make_input_files():
    """
    Creates the input files for testing
    """

    if not os.path.exists(IN_SOURCE):
        os.mkdir(IN_SOURCE)
    if not os.path.exists(OUT_SOURCE):
        os.mkdir(OUT_SOURCE)

    for i in range(0, TEST_FILES + 1):
        sys.stdout = open(os.path.join(IN_SOURCE, f'input{i:02d}.txt'), 'w')

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
        generate(TEST_LANG, i)
        if not os.path.exists(os.path.join(OUT_SOURCE, f'output{i:02d}.txt')):
            assert False

    # Tests if generate() throws error
    for i in range(TEST_FILES + 1, TEST_FILES + 2):
        with pytest.raises(SystemExit) as sys_exit:
            generate(TEST_LANG, i)
        assert sys_exit.value.code == 1


def test_blank():
    """
    Checks if no blank files are being generated and if it correctly
    identifies a blank file.
    """

    # Tests if the logic is not generating blank files
    for i in range(0, TEST_FILES + 1):
        generate(TEST_LANG, i)
        out_file = os.path.join(OUT_SOURCE, f'output{i:02d}.txt')
        assert os.stat(out_file).st_size != 0

    # Tests if correctly identifies blank files
    for i in range(TEST_FILES + 1, TEST_FILES + 2):
        out_file = os.path.join(OUT_SOURCE, f'output{i:02d}.txt')
        file = open(out_file, 'w')
        file.close()
        assert os.stat(out_file).st_size == 0
