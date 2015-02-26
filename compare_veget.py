#!/usr/bin/env python

#2012-11-12
#This is to compare the difference of vegetation type between two stomate_history files.

#Arguments:
#filename1, filename2: the two file names with full path that need to be compared.

import matplotlib as mat
import gnc
import sys
import cons
import matplotlib.pyplot as plt
import g
import bmap

filename1 = sys.argv[1]
filename2 = sys.argv[2]

print "filename1 is {0},filename2 is {1}".format(filename1, filename2)

d1 = gnc.Ncdata(filename1)
d2 = gnc.Ncdata(filename2)

def plot_com_pftnum(d1,d2,pftnum):
    """
    plot the specified number of PFT, pftnum should be 1-based.
    """
    fig, (ax1,ax2,ax3) = plt.subplots(ncols=1,nrows=3,sharex=True,sharey=True)
    bmap.imshowmap(d1.lat, d1.lon, d1.d1.VEGET_MAX[pftnum-1],ax1,cmap=mat.cm.Greens, gridstep=None)
    bmap.imshowmap(d2.lat, d2.lon, d2.d1.VEGET_MAX[pftnum-1],ax2,cmap=mat.cm.Greens, gridstep=None)
    bmap.imshowmap(d2.lat, d2.lon, d1.d1.VEGET_MAX[pftnum-1]-d2.d1.VEGET_MAX[pftnum-1],ax3,gridstep=None)
    g.Set_FigText(fig,'PFT'+str(pftnum)+': '+cons.pftdic[pftnum])
    fig.savefig('com_PFT'+str(pftnum)+'.jpg')
    plt.close(fig)
    print "plot for PFT '{0}' done".format(pftnum)


for pftnum in range(1,14):
    plot_com_pftnum(d1,d2,pftnum)



