#!/usr/bin/env python

import sys
import gnc
import matplotlib as mat
import matplotlib.pyplot as plt

filename=sys.argv[1]
varname=sys.argv[2]
try:
    title=sys.argv[3]
except:
    title=''

print "title is {0}".format(title)

d=gnc.Ncdata(filename)
for month in range(0,12):
    d.map(mapvarname=varname, mapdim=month,
                                 title=title+'['+str(month+1).zfill(2)+']',unit=False)

    fig = d.m.ax.figure
    fig.savefig(varname+str(month+1).zfill(2)+'.png')
    plt.close(fig)
    print '{0} finished'.format(month+1)



