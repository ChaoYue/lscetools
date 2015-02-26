#!/usr/bin/env python

"""
This script is for merging multiple lines from one file and write to another file.
How to use:
./mergeline.py infile outfile line_number_for_merge

Note:
    1. If the number of lines of the original file is not the product of line_number for merge, it will sum the remaining lines as the last line.
"""
import sys

infile=sys.argv[1]
outfile=sys.argv[2]
line_number=int(sys.argv[3])

if line_number == 1:
    pass
else:
    fob=open(infile,'r')
    fob2=file(outfile,'w')
    endfile=False
    while(not endfile):
        mergelines=''
        for i in range(line_number):
            line=fob.readline()
            #print "line is,{0}".format(line)
            if line=='':
                endfile=True
                break
            else:
                if i<line_number-1:
                    mergelines+=line.strip('\n')+' '  #remove the \n but add a new space to separate
                else:
                    mergelines+=line
        fob2.write(mergelines)
    fob.close()
    fob2.close()


