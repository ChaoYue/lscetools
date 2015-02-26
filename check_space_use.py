#!/usr/bin/env python
import pandas as pa
import sys

filename = sys.argv[1]
lower = int(sys.argv[2])
higher = int(sys.argv[3])
df = pa.read_csv(filename,sep='\t',header=None,names=['size','directory'])
dft = df[(df['size']>lower)&(df['size']<higher)&(map(lambda s: len(s.split('/')) < 3,df.directory))]
strlist =  dft['directory'].values
print '\n'
print "The directories are:"
print "----------------------------"
print dft
print '\n'
print "space separated form:"
print "----------------------------"
print ' '.join([s[2:] for s in strlist])
