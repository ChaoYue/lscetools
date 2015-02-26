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
import math

filename1 = sys.argv[1]
filename2 = sys.argv[2]

print "filename1 is {0},filename2 is {1}".format(filename1, filename2)

d1 = gnc.Ncdata(filename1)
d2 = gnc.Ncdata(filename2)

fig, axs = plt.subplots(ncols=3,nrows=4)
axlist = axs.flatten()[:]


def plot_com_pftnum(d1,d2,pftnum,ax):
    """
    plot the specified number of PFT, pftnum should be 1-based.
    """
    #fig, (ax1,ax2) = g.Create_2VAxes()
    #bmap.imshowmap(d1.lat, d1.lon, d1.d1.VEGET_MAX[pftnum-1],ax1,cmap=mat.cm.Greens, gridstep=None)
    #bmap.imshowmap(d2.lat, d2.lon, d2.d1.VEGET_MAX[pftnum-1],ax2,cmap=mat.cm.Greens, gridstep=None)
    absnum = np.ma.max(np.ma.abs(d2.d1.VEGET_MAX[pftnum-1]-d1.d1.VEGET_MAX[pftnum-1]))
    absnum = math.ceil(absnum*10)/10.
    bmap.imshowmap(d2.lat, d2.lon, d2.d1.VEGET_MAX[pftnum-1]-d1.d1.VEGET_MAX[pftnum-1],ax,cmap=g.cm.red2green, gridstep=None,vmin=-1*absnum,vmax=absnum)
    ax.set_aspect('auto')
    g.Set_AxText(ax,'PFT'+str(pftnum)+': '+cons.pftdic[pftnum],pos=(0,1.05),ftdic={'size':10})
    print "plot for PFT '{0}' done".format(pftnum)


for pftnum in range(2,14):
    plot_com_pftnum(d1,d2,pftnum,axlist[pftnum-2])

g.Set_FigText(fig,"ORCHIDEE minus Ben's PFT map")
g.Set_Axes_Cross_Line(axlist[-1])
g.Set_Axes_Cross_Line(axlist[-2])

