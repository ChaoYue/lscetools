#!/usr/bin/python

#how to use:
# ./insert_line.py filein fileout linenumber string

import sys
import subprocess

input_filename = sys.argv[1]
if input_filename in ['-h','-help']:
    print """
    how to use:
    -----------
    replace_line.py filein fileout linenumber string

    Parameters:
    -----------
    1. string could contain multiple whitespaces.

    Notes:
    ------
    1. filein and fileout could be the same file name, in this case filein
        will be overwritten.

    """
    sys.exit()
output_filename = sys.argv[2]
insert_line_number = int(sys.argv[3])
insert_string = sys.argv[4:]
insert_string = ' '.join(insert_string)

overwrite = False
if input_filename == output_filename:
    overwrite = True
    input_filename_temp = input_filename+'_testtemp'
    #subprocess.Popen(["cp",input_filename,input_filename_temp])
    subprocess.call(["cp",input_filename,input_filename_temp])
    input_filename = input_filename_temp

fob = open(input_filename,'r')
fob2 = open(output_filename,'w')

for lnum, line in enumerate(fob):
    if lnum != insert_line_number-1:
        fob2.write(line)
    else:
        fob2.write(insert_string+'\n')

fob.close()
fob2.close()

if overwrite:
    subprocess.Popen(['rm','-f',input_filename])
