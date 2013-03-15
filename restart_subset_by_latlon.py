#!/usr/bin/python

#Purpose:
#    Use ncks to subset the restart file according to lat1,lat2 lon1,lon2

#How to call:
#   restart_subset_by_latlon.py $PWD driver_restart.nc lat1,lat2 lon1,lon2 output_file_name[optional]

import sys
import pb
import gnc
import os
from subprocess import call

wd = sys.argv[1]
if wd in ['-h','-help']:
    print '''
    #How to call:
    #   restart_subset_by_latlon.py $PWD driver_restart.nc lat1,lat2 lon1,lon2 output_file_name[optional]
    '''
    sys.exit()
infile = sys.argv[2]
latr = sys.argv[3]
lonr = sys.argv[4]
try:
    force_output_file = sys.argv[5]
except IndexError:
    force_output_file = None

os.chdir(wd)
print "---------------------------------------------------------------------------------"
print "start extract, working directory is: \n"
print wd

#if 'start' not in infile and 'restart' not in infile:
#    raise ValueError("check the input file name, it's supposed to be orchidee restart or start files.")
#else:
#    pass

#get the lat/lon range
[lat1,lat2] = [float(i) for i in latr.split(',')]
[lon1,lon2] = [float(i) for i in lonr.split(',')]

#construct output file name
if force_output_file == None:
    outfile = ''.join([infile[:-3],'_lat',latr.replace(',','_'),'_lon',lonr.replace(',','_'),'.nc'])
    #if infile is a full path file, then we always want to put outfile in wd rather than the same directory with inputfile.
    if infile[0] == '/':
        outfile = os.path.join(wd,outfile.split('/')[-1])
else:
    outfile = os.path.join(wd,force_output_file)
print "output file is: {0}".format(outfile)

d = gnc.Ncdata(os.path.join(wd,infile),('x','y'))
#note x1,x2 is actually the horizontal axis and therefore longitude
(x1,x2,y1,y2) = d.find_index_by_vertex((lat1,lat2),(lon1,lon2))

par3 = ','.join(['x',str(x1),str(x2)])  #get something like "x,98,99"
par4 = ','.join(['y',str(y1),str(y2)])  #get soemthing like "y,70,71"
call(["ncks","-d",par3,"-d",par4,infile,outfile])



