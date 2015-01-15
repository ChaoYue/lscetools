#!/usr/bin/python

import glob
import sys
import os
from subprocess import call
import datetime

pattern = sys.argv[1]
if pattern in ['-h','-help']:
    print '''
    Script to make backup for files.

    #How to call:
    #   ./backup_local.py '*py'
    '''
    sys.exit()


try:
    newdir_name = sys.argv[2]
except IndexError:
    newdir_name = 'backup'

pwd = os.getcwd()
backdir = pwd+'/'+newdir_name
if not os.path.exists(backdir):
    os.makedirs(backdir)
else:
    pass

#print 'patter:',pattern,type(pattern)

filelist = glob.glob(pattern)
#print pattern
#print filelist

now = datetime.datetime.today()
date_string = str(now.date()).replace('-','')

def change_oldname_to_newname(filename):
    try:
        name,surfix = filename.split('.')
        newname = name+'_'+date_string+'.'+surfix
    except ValueError:
        name = filename
        newname = name+'_'+date_string
    return newname


for filename in filelist:
    newname = change_oldname_to_newname(filename)
    full_oldname = pwd+'/'+filename
    full_newname = backdir+'/'+newname
    call(['cp',full_oldname,full_newname])
    print "backup done for --{0}--".format(filename)


