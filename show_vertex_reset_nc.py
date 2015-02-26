#!/usr/bin/env python

#Purpose:
#    This script is to show the vertex of lat/lon for a nc file.

import sys
import pb

filename=sys.argv[1]

lat_lon_pairlist=[('nav_lat','nav_lon')]

if filename=='-h':
    print "This script is to show the vertex of lat/lon for a nc file. \n how to call: show_vertex_nc.py filename.nc"
else:
    d0,d1 =pb.ncreadg(filename)
    print "filename:  {0}".format(filename)
    print "lonlim:"
    lonvar = d1.nav_lon
    if lonvar.ndim == 2:
        print d1.nav_lon[0][0]
        print d1.nav_lon[0][-1]
    elif lonvar.ndim == 1:
        print d1.nav_lon[0]
        print d1.nav_lon[-1]
    elif lonvar.ndim == 0:
        print d1.nav_lon
        print d1.nav_lon
    else:
        raise ValueError("nav_lon has {0} dimensions!").format(lonvar.ndim)


    print "latlim:"
    latvar = d1.nav_lat
    if latvar.ndim == 2:
        print "latlim ndim is 2"
        print d1.nav_lat[:,0][0]
        print d1.nav_lat[:,0][-1]
    elif latvar.ndim == 1:
        print "latlim ndim is 1"
        print d1.nav_lat[0]
        print d1.nav_lat[-1]
    elif latvar.ndim == 0:
        print d1.nav_lat
        print d1.nav_lat
    else:
        raise ValueError("nav_lat has {0} dimensions!").format(latvar.ndim)
