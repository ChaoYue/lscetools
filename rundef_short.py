#!/usr/bin/env python

import sys

infile = 'run.def'
outfile = 'run.def.mod'
outfile2 = 'copy_file.sh'

def convert_rundef_to_dict(filename):
    '''
    Convert all the '='s to python dictionary.
    '''
    fob = open(filename)
    flist1 = fob.readlines()
    uniflist1 = list(set(flist1))
    uniflist1 = [s.strip(' ') for s in uniflist1]
    uniflist1 = [s[:-1] for s in uniflist1 if s[:-1].strip() and s[0]!='#']
    tuple_list = []
    for s in uniflist1:
        try:
            s1,s2 = s.split('=')
        except ValueError:
            print """Warning! please check: there are lines that are neither
            commented nor contain an equation mark!"""
            print s
        tuple_list.append((s1.strip(),s2.strip()))
    f1dic = OrderedDict(tuple_list)
    return f1dic

dic = convert_rundef_to_dict(infile)

fob1 = open(infile)
lines = fob1.readlines()
fob2 = open(outfile,'w')
fob3 = open(outfile2,'w')

for line in lines:
    if line.strip().startswith('#'):
        fob2.write(line)
    else:
        # empty or only whiteblanks
        if line=='\n' or len(line.strip())==0:
            fob2.write(line)
        else:
            if '=' in line:
                key = line.split('=')[0].strip()
                val = dic[key]
                if '/' in val:
                    fob2.write(line.split('=')[0]+'= '+val.split('/')[-1]+'\n')
                    fob3.write('cp '+val+' .\n')
                else:
                    fob2.write(line)
                    
            # line is not empty, not commented, does not contain '=', we will comment it.
            else:
                fob2.write('#'+line)
fob2.close()
fob3.close()
