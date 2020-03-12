import os

DIRNAME = os.path.dirname(__file__) # Absolute path of the file
CMD = os.path.join(DIRNAME, 'logic') # Command to run the logic file


LANGS = [{'req': 'gcc',
          'command': CMD,
          'link': 'https://gcc.gnu.org/install/',
          'compile': f'gcc -o {CMD} {CMD}.c'},
         {'req': 'g++',
          'command': CMD,
          'link': 'https://www.cs.odu.edu/~zeil/cs250PreTest/latest/Public/installingACompiler/',
          'compile': f'g++ -o {CMD} {CMD}.cpp'},
         {'req': 'Java',
          'command': f'java -cp {DIRNAME} logic',
          'link': 'https://introcs.cs.princeton.edu/java/15inout/windows-CMD.html',
          'compile': f'javac {CMD}.java'},
         {'req': 'Python',
          'command': f'python {CMD}.py',
          'link': 'https://www.python.org/downloads/',
          'compile': ''},
         {'req': 'C#',
          'command': f'mono {CMD}',
          'link': 'https://www.mono-project.com/docs/about-mono/languages/csharp/',
          'compile': f'msc {CMD}.cs'},
         {'req': 'Golang',
          'command': CMD,
          'link': 'https://golang.org/doc/install',
          'compile': f'go build -o {CMD} {CMD}.go'},
         ]
