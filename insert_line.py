#!/usr/bin/python

#how to use:
# ./insert_line.py filein fileout linenumber string

import sys
import subprocess

input_filename = sys.argv[1]
output_filename = sys.argv[2]
insert_line_number = int(sys.argv[3])
insert_string = sys.argv[4]

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
    fob2.write(line)
    if lnum == insert_line_number-1:
        insert_string_list = insert_string.split('\n')
        for substr in insert_string_list:
            fob2.write(substr+'\n')

fob.close()
fob2.close()

if overwrite:
    subprocess.Popen(['rm','-f',input_filename])
