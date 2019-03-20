import os
import random
import shutil
import sys
import timeit
import zipfile
import subprocess
import math

from lang_compiler import LANGS

if sys.version[0] == '3':
    INPUT = input
    XRange = range

try:
    os.mkdir('input')
    os.mkdir('output')
except OSError:
    pass


def user(choice, i):
    #add code to execute users program
    '''try:

        pass   #users program has to be executed

    except Exception:
        print("Looks like you don't have {0} :/ \nYou can refer to {1} for help.".format(
            LANGS[choice - 1]['req'], LANGS[choice - 1]['link']))
   '''



def generate(choice, i):
    try:
        return (subprocess.check_output('%s < input/input%02d.txt' %
                  (LANGS[3]['command'], 2),shell=True))

    except Exception:
        print("Looks like you don't have {0} :/ \nYou can refer to {1} for help.".format(
            LANGS[choice - 1]['req'], LANGS[choice - 1]['link']))



'''
def main():
    # Get input from Input Test Files
    N = int(raw_input()
    assert(N >= 1 and N <= 1000000)
    s = map(int, raw_input().split())
    assert(len(s) == N)

    # Get output produced by User's code
    user_result = int(raw_input()

    # Write your logic to check if user's result is correct. Assert false if not.
    score = 10 # Score for this test file
    print score
'''
def main():
    #f=open('input2/input01.txt', 'r')
    t=10
    score=10
    res=0
    for i in range(0,t+1):
        m=generate(4,i)

        n=user(4,i)  #this function will execute users logic.

        

        if m==n:res+=score
     # if assertion failed it will fail for the given testcase
     #f.close()
    print(res)


# Always invoke by main. It is necessary for checker to be invoked by main()
if __name__ == '__main__':
    main()
