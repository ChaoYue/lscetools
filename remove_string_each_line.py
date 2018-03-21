#!/home/orchidee03/ychao/anaconda/bin/python

"""
This script is to remove the specified string from each line of a file and write into a new file.
How to use:
./remove_string_each_line.py infile outfile string_to_remove
"""

import sys

infile=sys.argv[1]
outfile=sys.argv[2]
string_to_remove=sys.argv[3]

fob=open(infile,'r')
fob2=file(outfile,'w')

while True:
    line=fob.readline()
    if line=='':
        break
    else:
        newline = line.replace(string_to_remove,'')
    fob2.write(newline)
fob.close()
fob2.close()

