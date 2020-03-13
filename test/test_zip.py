import os
import sys
import shutil
import math
from random import randint
import pytest

from tc_generator.tc_gen import *


@pytest.fixture(autouse=True)
def make_input_files():
    # Generate input files for testing
    if not os.path.exists(IN_SOURCE):
        os.mkdir(IN_SOURCE)
    if not os.path.exists(OUT_SOURCE):
        os.mkdir(OUT_SOURCE)
    for i in range(0, 4 + 1):
        sys.stdout = open(os.path.join(IN_SOURCE, 'input%02d.txt' % i), 'w')

        required_input = randint(5, math.pow(10, (i // 2) + 1))
        print(required_input)  # Prints x into input file
        for _ in range(required_input):
            print(randint(1, math.pow(10, min(4, max(i // 2, 2)))))

        sys.stdout.close()
        generate(4, i)

    yield

    shutil.rmtree(IN_SOURCE)
    shutil.rmtree(OUT_SOURCE)


def test_zip_codechef():
    # Tests if zipping correctly for CodeChef
    assert(zip_codechef() == 0)
    shutil.rmtree(TC_SOURCE)


def test_zip_hackerearth():
    # Tests if zipping correctly for HackerEarth
    assert(zip_hackerearth() == 0)
    zip_file = os.path.join(DIRNAME, 'test-cases.zip')
    os.remove(zip_file)


def test_zip_hackerrank():
    # Tests if zipping correctly for HackerRank
    assert(zip_hackerrank() == 0)
    zip_file = os.path.join(DIRNAME, 'test-cases.zip')
    os.remove(zip_file)
