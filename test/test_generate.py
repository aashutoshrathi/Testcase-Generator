import os
import sys
import shutil
import math
from random import randint
import pytest

from tc_generator.tc_gen import generate, IN_SOURCE, OUT_SOURCE


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

    yield

    shutil.rmtree(IN_SOURCE)
    shutil.rmtree(OUT_SOURCE)


def test_generate():
    # Tests if generate() runs successfuly
    for i in range(0, 4 + 1):
        assert(generate(4, i) == 0)

    # Tests if generate() throws error
    for i in range(5, 6 + 1):
        with pytest.raises(SystemExit) as se:
            generate(4, i)
        assert(se.value.code == 1)


def test_blank():
    # Tests if the logic is not generating blank files
    for i in range(0, 4 + 1):
        generate(4, i)
        out_file = os.path.join(OUT_SOURCE, f'output{i:02d}.txt')
        assert(os.stat(out_file).st_size != 0)
    # Tests if correctly identifies blank files
    for i in range(5, 6 + 1):
        out_file = os.path.join(OUT_SOURCE, f'output{i:02d}.txt')
        file = open(out_file, 'w')
        file.close()
        assert(os.stat(out_file).st_size == 0)
