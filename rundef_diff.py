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
    outfile1,outfile2 = sys.argv[3:5]
except ValueError:
    outfile1 = infile1+'_com'
    outfile2 = infile2+'_com'


def convert_rundef_to_dict(filename):
    '''
    Convert all the '='s to python dictionary.
    '''
    fob = open(filename)
    flist1 = fob.readlines()
    uniflist1 = list(set(flist1))
    uniflist1 = [s[:-1] for s in uniflist1 if s[:-1].strip() and s[0]!='#']
    tuple_list = []
    for s in uniflist1:
        s1,s2 = s.split('=')
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

write_to_outfile(outfile1,comlist,diffA,onlyA)
write_to_outfile(outfile2,comlist,diffB,onlyB)


