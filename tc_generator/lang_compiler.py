import os

dirname = os.path.dirname(__file__) # Absolute path of the file
cmd = os.path.join(dirname, 'logic') # Command to run the logic file


LANGS = [{'req': 'gcc',
          'command': cmd,
          'link': 'https://gcc.gnu.org/install/',
          'compile': 'gcc -o ' + cmd + ' ' + cmd + '.c'},
         {'req': 'g++',
          'command': cmd,
          'link': 'https://www.cs.odu.edu/~zeil/cs250PreTest/latest/Public/installingACompiler/',
          'compile': 'g++ -o ' + cmd + ' ' + cmd + '.cpp'},
         {'req': 'Java',
          'command': 'java -cp ' + dirname + ' ' + 'logic',
          'link': 'https://introcs.cs.princeton.edu/java/15inout/windows-cmd.html',
          'compile': 'javac ' + cmd + '.java'},
         {'req': 'Python',
          'command': 'python ' + cmd + '.py',
          'link': 'https://www.python.org/downloads/',
          'compile': ''},
         {'req': 'C#',
          'command': 'mono ' + cmd,
          'link': 'https://www.mono-project.com/docs/about-mono/languages/csharp/',
          'compile': 'msc ' + cmd + '.cs'},
         {'req': 'Golang',
          'command': cmd,
          'link': 'https://golang.org/doc/install',
          'compile': 'go build -o ' + cmd + ' ' + cmd + '.go'},
         ]
