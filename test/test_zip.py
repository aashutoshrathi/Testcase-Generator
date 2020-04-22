"""
Tests all the zip functions.
"""

import os
import sys
import shutil
import zipfile
import pytest

from tc_generator.tc_gen import (TC_SOURCE, IN_SOURCE, OUT_SOURCE, RINT, POWER,
                                 generate, zip_codechef, zip_hackerearth,
                                 zip_hackerrank, make_dirs, make_lf_ending)


TEST_FILES = 4 # Number of files to create for testing
TEST_LANG = 3 # Testing for Python
TC_ZIP = TC_SOURCE + '.zip'


@pytest.fixture(autouse=True)
def make_tc_files():
    """
    Creates the TC files for testing
    """

    make_dirs()

    for i in range(0, TEST_FILES + 1):
        sys.stdout = open(os.path.join(IN_SOURCE, f'input{i:02d}.txt'), 'w+')

        required_input = RINT(5, POWER(10, (i // 2) + 1))
        print(required_input)  # Prints x into input file
        for _ in range(required_input):
            print(RINT(1, POWER(10, min(4, max(i // 2, 2)))))

        sys.stdout = sys.__stdout__
        generate(TEST_LANG, i)

    yield

    shutil.rmtree(IN_SOURCE)
    shutil.rmtree(OUT_SOURCE)


def test_zip_codechef():
    """
    Checks if the zip_codechef function saves testcases in the correct structure
    of all input files as input<number>.txt and output files as output<number>.txt
    inside the test-cases directory.
    """

    zip_codechef()
    tc_files = os.listdir(TC_SOURCE)
    generated_files = []
    for i in range(0, TEST_FILES + 1):
        generated_files.append(f'input{i:02d}.txt')
        generated_files.append(f'output{i:02d}.txt')
    print(sorted(tc_files), file=sys.stderr)
    print(sorted(generated_files), file=sys.stderr)
    if sorted(tc_files) != sorted(generated_files):
        pytest.fail("zip_codechef() failed!")

    shutil.rmtree(TC_SOURCE)


def test_zip_hackerearth():
    """
    Checks if the zip_hackerearth function saves testcases in the correct structure
    of all input files as in<number>.txt and output files as out<number>.txt
    inside test-cases.zip.
    """

    zip_hackerearth()
    zip_file = zipfile.ZipFile(TC_ZIP)
    tc_files = zip_file.namelist()
    zip_file.close()
    generated_files = []
    for i in range(0, TEST_FILES + 1):
        generated_files.append(f'in{i:02d}.txt')
        generated_files.append(f'out{i:02d}.txt')
    if sorted(tc_files) != sorted(generated_files):
        pytest.fail("zip_hackerearth() failed!")

    os.remove(TC_ZIP)


def test_zip_hackerrank():
    """
    Checks if the zip_hackerrank function saves testcases in the correct structure
    of all input files as input<number>.txt and output files as output<number>.txt
    inside test-cases.zip.
    """

    zip_hackerrank()
    zip_file = zipfile.ZipFile(TC_ZIP)
    tc_files = zip_file.namelist()
    zip_file.close()
    generated_files = []
    for i in range(0, TEST_FILES + 1):
        generated_files.append(f'input/input{i:02d}.txt')
        generated_files.append(f'output/output{i:02d}.txt')
    if sorted(tc_files) != sorted(generated_files):
        pytest.fail("zip_hackerrank() failed!")

    os.remove(TC_ZIP)
