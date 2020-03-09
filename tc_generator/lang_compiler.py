import sys

cmd = 'logic'
if sys.platform[0].lower() == 'w':
    cmd = cmd + '.exe'
else:
    cmd = './' + cmd


LANGS = [{'req': 'gcc',
          'command': cmd,
          'link': 'https://gcc.gnu.org/install/',
          'compile': 'gcc -o logic logic.c'},
         {'req': 'g++',
          'command': cmd,
          'link': 'https://www.cs.odu.edu/~zeil/cs250PreTest/latest/Public/installingACompiler/',
          'compile': 'g++ -o logic logic.cpp'},
         {'req': 'Java',
          'command': 'java logic',
          'link': 'https://introcs.cs.princeton.edu/java/15inout/windows-cmd.html',
          'compile': 'javac logic.java'},
         {'req': 'Python',
          'command': 'python logic.py',
          'link': 'https://www.python.org/downloads/',
          'compile': ''},
         {'req': 'C#',
          'command': 'mono logic',
          'link': 'https://www.mono-project.com/docs/about-mono/languages/csharp/',
          'compile': 'msc logic.cs'},
         {'req': 'Golang',
          'command': cmd,
          'link': 'https://golang.org/doc/install',
          'compile': 'go build -o logic logic.go'},
         ]
