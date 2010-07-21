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
    def record(chunk):
        if chunk not in d:
            d[chunk] = sys.argv[1]*n
            output.insert(0, '#define %s %s' % (d[chunk], chunk))
        output.append(d[chunk])

    # loop through chunks of code
    blocks = s.split('\([.\n]*?\)')
    for block in blocks:
        if len(block) < 1:
            continue

        if block[0] == '#':
            # preserve preprocessor instructions
            lines = block.split('\n')
            for line in lines:
                line = line.strip()
                if len(line) > 0 and line[0] == '#':
                    output.append(line)
                elif len(line) > 0:
                    record(line)
                    n+=1
        else:
            # add line
            line = re.sub('[\t\n]+', '', block).strip()
            if len(line) > 0:
                record('(' + line + ')')
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
