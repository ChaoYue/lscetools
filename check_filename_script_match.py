#!/usr/bin/python

import sys

filename_file = sys.argv[1]

if filename_file in ['-h','-help','--help']:
    print """
    This script checks which file in the filename.txt are used in the scripts
        as list in scriptfile.txt, and print the result in result.txt.

    How to use:
    -----------
    ./check_filename_script_match.py filename.txt scriptfile.txt result.txt
    """
    sys.exit()

scriptname_file = sys.argv[2]
resfile = sys.argv[3]


with open(filename_file) as fob:
    filename_list = [s[:-1].strip() for s in fob.readlines() if s.endswith('\n')]

with open(scriptname_file) as fob:
    scriptname_list =[s[:-1].strip() for s in fob.readlines() if s.endswith('\n')]


def check_filename_used(filename):
    '''
    If whether single filename is used in any of the scripts. return the
        filename and script list.
    '''
    fileused = False
    detect_list = []
    for scriptname in scriptname_list:
        fob = open(scriptname)
        if filename in fob.read():
            detect_list.append(scriptname)
            fileused = True
    if fileused == True:
        return detect_list

filename_not_used_list = []
filename_used_list = []
filename_script_used_dict = {}
for filename in filename_list:
    detect_list = check_filename_used(filename)
    if detect_list != None:
        filename_used_list.append(filename)
        filename_script_used_dict[filename] = detect_list
    else:
        filename_not_used_list.append(filename)




with open(resfile,'w') as fob:
    if filename_not_used_list != []:
        filename_not_used_list = [s+'\n' for s in filename_not_used_list]
        fob.write('**************************************************\n')
        fob.write('The files that are not used in any of the scripts:\n')
        fob.write('**************************************************\n')
        fob.writelines(filename_not_used_list)
    if filename_used_list == []:
        fob.write('No filename is used in one of the scripts')
    else:
        fob.write('\n\n')
        fob.write('**********************************\n')
        fob.write('filenames used in the scripts are:\n')
        fob.write('**********************************\n')
        for filename in filename_used_list:
            script_list = filename_script_used_dict[filename]
            script_list = ['        '+s+'\n' for s in script_list]
            fob.write('    '+filename+':\n')
            fob.writelines(script_list)
            fob.write('\n')








