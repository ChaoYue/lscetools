#!/usr/bin/python

import sys
import re


infile = sys.argv[1]

if infile in ['-h','-help','help','--help']:
    print """
    ************************************************************************
    This script is used to change many histdef variables to the same history
        output level, could be used to reduce the number of variables in
        stomate_history.nc and sechiba_history.nc
    ************************************************************************

    How to use:
    -----------
    First make the script exectuable, then

    $ change_histdef_level.py intersurf.f90 new_intersurf.f90 varnames.txt 9

    Notes:
    ------
    Above command will change the output level of all variables as listed in
    varname.txt to the same level of 9. In varnames.txt, each variable name
    takes a single line, eg.,

    $ cat varnames.txt
    CO2_TAKEN
    CO2_FIRE
    flood_frac
    SAP_M_AB
    ROOT_BM_LITTER

    The 5 variables above will be changed to have output level as 9.
    """
    sys.exit()

outfile = sys.argv[2]
varfile = sys.argv[3]

try:
    newlevel = int(sys.argv[4])
except IndexError:
    print "Error: New history level is not provided!"
    sys.exit()


if outfile == infile:
    print "Error: output file could not be the same as input file!"
    sys.exit()

def check_var_in_linelist(var,linelist):
    '''
    check if the linelist block contains the var
    '''
    for line in linelist:
        line = line.replace('"',"'")
        linesplit = [s.strip() for s in line.split("'")]
        if var in linesplit:
            return True

def find_block_by_var(var,lines):
    '''
    Rreturn the block of lines defining the var and line number.
    Returns:
    --------
    code_block_list: a list of code_blocks(line list) which forms
        histdef definition.
    num_tuple_list: a list of 2-len tuples, the 2-len tuples contains
        the beginning and end line number (not python index) for the
        block of code of histdef.
    '''
    newblock = False
    detect = False
    code_block_list = []
    num_tuple_list = []
    for i,line in enumerate(lines):
        if 'CALL' in line and 'histdef' in line:
            newblock = True
            d=[]
            begin_num = i+1
        if newblock:
            if line.strip().endswith('&'):
                d.append(line)
            elif line.strip().endswith(')'):
                d.append(line)
                newblock = False
                end_num = i+1
                if check_var_in_linelist(var,d):
                    code_block_list.append(d)
                    num_tuple_list.append((begin_num,end_num))
    return code_block_list,num_tuple_list

def replace_block_level(level,blockline):
    return [re.sub(r'\(\d?\d\)','('+str(level)+')',d) for d in blockline]

def change_lines_in_place(lines,new_line_block,num_tuple):
    line_num_list = range(num_tuple[0]-1,num_tuple[1])
    for num,line in zip(line_num_list,new_line_block):
        lines[num] = line

def change_lines_by_varlist(level,varlist,lines):
    for var in varlist:
        code_block_list, num_tuple_list = find_block_by_var(var,lines)
        #code_block means a list of lines
        for code_block,num_tuple in zip(code_block_list,num_tuple_list):
            new_line_block = replace_block_level(level,code_block)
            change_lines_in_place(lines,new_line_block,num_tuple)




with open(varfile) as fob:
    varlist = [s[:-1].strip() for s in fob.readlines() if s.endswith('\n')]

with open(infile) as fob:
    lines = [s[:-1] for s in fob.readlines() if s.endswith('\n')]

change_lines_by_varlist(newlevel, varlist, lines)
newlines = [line+'\n' for line in lines]
with open(outfile,'w') as fob:
    fob.writelines(newlines)


