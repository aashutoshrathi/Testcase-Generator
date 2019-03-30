f=open('output/output%02d.txt' % 3,'rt')
try:
    if f.read() is '' :
        raise Exception ('blank output file')
except Exception as error :
    print(repr(error))
f.close()
    
