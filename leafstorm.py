#!/usr/bin/python
import sys
import re

def main():
    f = open(sys.argv[2])
    s = f.read()

    s = re.sub('//[^\n]*', '', s)
    s = re.sub('[\n\t]+', '', s)
    s = re.sub('/\*.*?\*/', '', s)

    n = 1
    d = {}
    output = []
    ss = s.split(';')
    for line in ss:
        if line[0] == '#':
            output.append('\n#'.join(line.split('#')))
        else:
            if line not in d:
                d[line] = sys.argv[1]*n
                output.insert(0, '#define %s %s;' % (d[line], line))
                n+=1
            output.append(d[line])
    print '\n'.join(output)

def usage():
    print 'usage: leafstorm word file.c'

if __name__ == "__main__":
    if len(sys.argv) != 3:
        usage()
    else:
        main()
