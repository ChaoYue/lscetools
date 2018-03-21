#!/usr/bin/env python

import sys

infile1 = sys.argv[1]
if infile1 in ['-h','-help']:
    print """
    Compare two run.def files, four parts will be distinguished:
        keys with the same values in both files, keys appearing
        in both files but with differnt values, and keys appearing in only
        one of the two files.

    How to use:
    -----------
    ./rundef_diff.py run.def.A run.def.B

    It will generate another two files: run.def.A_com and run.def.B_com,
        in which comparing results will be presented.

    Notes:
    ------
    1. For flags that appear more than once in the run.def, the last value will be used.
    """
    sys.exit()

infile2 = sys.argv[2]

try:
    outfile1,outfile2,outfile3,outfile4 = sys.argv[3:7]
except ValueError:
    outfile1 = infile1+'_com'
    outfile2 = infile2+'_com'
    outfile3 = infile1+'_mark'
    outfile4 = infile2+'_mark'


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
    f1dic = dict(tuple_list)
    return f1dic

rundic1 = convert_rundef_to_dict(infile1)
rundic2 = convert_rundef_to_dict(infile2)

comdic = {} #same key/value pairs in both files.
diffA = {} #same key but unequal value
diffB = {}
onlyA = {} #key only in file1
onlyB = {} #key only in file2
for key in rundic1:
    if key in rundic2:
        if rundic1[key] == rundic2[key]:
            comdic[key] = rundic1[key]
        else:
            diffA[key] = rundic1[key]
            diffB[key] = rundic2[key]
    else:
        onlyA[key] = rundic1[key]
for key in rundic2.keys():
    if key not in rundic1:
        onlyB[key] = rundic2[key]

## write the marked file:
## keys with different values start with '!'
## keys appearing in one file start with '+'
def write_mark_file(infile1,outfile3,comdic,diffA,onlyA):
    fob1 = open(infile1)
    lines = fob1.readlines()
    fob2 = open(outfile3,'w')
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
                    if key in comdic:
                        fob2.write(line)
                    elif key in diffA:
                        fob2.write('!'+line)
                    elif key in onlyA:
                        fob2.write('+'+line)
                    else:
                        raise Error("""key {0} does not fall in any of the three group""".format(key))
                # line is not empty, not commented, does not contain '=', we will comment it.
                else:
                    fob2.write('#'+line)
    fob2.close()

print outfile3
print outfile4
write_mark_file(infile1,outfile3,comdic,diffA,onlyA)
write_mark_file(infile2,outfile4,comdic,diffB,onlyB)

## Write re-arranged comparison files
#convert dict to list for easy writing.
def convert_dict_to_list(dic):
    return [key+' = '+dic[key]+'\n' for key in sorted(dic.keys())]

comlist,diffA,diffB,onlyA,onlyB = \
    map(convert_dict_to_list,[comdic,diffA,diffB,onlyA,onlyB])

def write_to_outfile(filename,comlist,diffA,onlyA):
    with open(filename,'w') as fob:
        fob.write("equal rundef value in both files:\n")
        fob.writelines(comlist)
        fob.write('\n'*2)
        fob.write('rundef value not equal:\n')
        fob.writelines(diffA)
        fob.write('\n'*2)
        fob.write('rundef keys only appear in this one:\n')
        fob.writelines(onlyA)

print outfile1
print outfile2
write_to_outfile(outfile1,comlist,diffA,onlyA)
write_to_outfile(outfile2,comlist,diffB,onlyB)


