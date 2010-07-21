#!/usr/bin/python
import sys
import re

def main():
    # read file
    f = open(sys.argv[2])
    s = f.read()

    # remove comments
    s = re.sub('(/\*(.|\s)*?\*/|//[^\n]*)', '', s)

    # hash record of macros we've made
    n = 1
    d = {}
    output = []

    # loop through chunks of code
    blocks = s.split('\n')
    for block in blocks:
        if len(block) < 1:
            continue

        if block[0] == '#':
            # preserve preprocessor instructions
            output.append(block)
        else:
            # add line
            line = re.sub('[\t]+', '', block).strip()
            if len(line) > 0:
                if line not in d:
                    d[line] = sys.argv[1]*n
                    output.insert(0, '#define %s %s' % (d[line], line))
                output.append(d[line])
                n+=1

    # ouput
    print '\n'.join(output)

def usage():
    print 'usage: leafstorm word file.c'

if __name__ == "__main__":
    if len(sys.argv) != 3:
        usage()
    else:
        main()
