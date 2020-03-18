import os
import sys
import shutil
import zipfile
import pytest

from tc_generator.tc_gen import *

TEST_FILES = 4 # Number of files to create for testing
TEST_LANG = 3 # Testing for Python
TC_ZIP = TC_SOURCE + '.zip'


@pytest.fixture(autouse=True)
def make_input_files():
    # Generate input files for testing
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
        generate(TEST_LANG, i)

    yield

    shutil.rmtree(IN_SOURCE)
    shutil.rmtree(OUT_SOURCE)


def test_zip_codechef():
    # Tests if zipping correctly for CodeChef
    zip_codechef()
    tc_files = os.listdir(TC_SOURCE)
    generated_files = []
    for i in range(0, TEST_FILES + 1):
      generated_files.append(f'input{i:02d}.txt')
      generated_files.append(f'output{i:02d}.txt')
    if sorted(tc_files) != sorted(generated_files):
      assert False

    shutil.rmtree(TC_SOURCE)


def test_zip_hackerearth():
    # Tests if zipping correctly for HackerEarth
    zip_hackerearth()
    zip_file = zipfile.ZipFile(TC_ZIP)
    tc_files = zip_file.namelist()
    zip_file.close()
    generated_files = []
    for i in range(0, TEST_FILES + 1):
      generated_files.append(f'in{i:02d}.txt')
      generated_files.append(f'out{i:02d}.txt')
    if sorted(tc_files) != sorted(generated_files):
      assert False

    os.remove(TC_ZIP)


def test_zip_hackerrank():
    # Tests if zipping correctly for HackerRank
    zip_hackerrank()
    zip_file = zipfile.ZipFile(TC_ZIP)
    tc_files = zip_file.namelist()
    zip_file.close()
    generated_files = []
    for i in range(0, TEST_FILES + 1):
      generated_files.append(f'input/input{i:02d}.txt')
      generated_files.append(f'output/output{i:02d}.txt')
    if sorted(tc_files) != sorted(generated_files):
      assert False

    os.remove(TC_ZIP)
