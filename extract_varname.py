#!/usr/bin/env python

import sys
import mathex

filename = sys.argv[1]
if filename in ['-h','-help']:
    print """
    Purpose:
    --------
    To extract the spatial (area) sum or (area weighted) mean for variable contained in input netcdf file.
    The netcdf file should ideally contained also the variables of VEGET_MAX and Areas. Output will be a
    text file containing the data. The output file is automatically generated depending the values of the
    flags.

    How to use:
    -----------
    ~/lscetools/extract_varname.py /home/orchidee03/ychao/example.nc TOTAL_M pft_flag:area_flag

    Parameters:
    -----------
    pft_flag: the VEGET_MAX related operation for the varname before spatial operation.
        - none: the variable contains no VEGET_MAX dimension.
        - crop: only the crop PFTs will be extracted.
        - noncrop: the crop PFTs will be excluded.
        - all: all PFTs will be included.
        The default value is 'all'
    area_flag: the area related operation.
        - fsum: simple sum over the spatial scale without being
          multiplied by the area.
        - areasum: the area will be first multiplied with the PFT
          weighted variable and the spatial sum is calculated.
        - areamean: the areasum is first calculated, then is divided
          by the total area.
        The default value is 'fsum'
    """
    sys.exit()

import gnc
import numpy as np

varname = sys.argv[2]
try:
    flags = sys.argv[3]
except IndexError:
    flags = 'all:fsum'

pft_flag,area_flag = flags.split(':')


def get_pftsum(d,varname,pft_flag='all'):
    data = d.d1.__dict__[varname]
    if len(data.shape) != 4:
            raise ValueError("could only handle 4-dim variable in case of veget_max weighted is needed.")
    else:
        if pft_flag == 'noncrop':
            pftsum = np.ma.sum(data[:,0:11,...] * d.d1.VEGET_MAX[:,0:11,...],axis=1)
        elif pft_flag == 'crop':
            pftsum = np.ma.sum(data[:,11:13,...] * d.d1.VEGET_MAX[:,11:13,...],axis=1)
        elif pft_flag == 'all':
            pftsum = np.ma.sum(data * d.d1.VEGET_MAX, axis=1)
        else:
            raise ValueError("Unknown PFT flag")
        return pftsum


def treat_spatial(d,pftsum,area_flag='fsum'):
    if len(pftsum.shape) !=3 :
        raise ValueError("could only handle 3-dim pftsum data or raw data")
    else:
        if area_flag == 'fsum':
            fsum = np.ma.sum(np.ma.sum(pftsum,axis=-1),axis=-1)
            return fsum
        elif area_flag in ['areasum','areamean']:
            areasum = np.ma.sum(np.ma.sum(pftsum*d.d1.Areas,axis=-1),axis=-1)
            if area_flag == 'areasum':
                return areasum
            else:
                total_area = np.ma.sum(d.d1.Areas)
                return areasum/total_area
        else:
            raise ValueError("Unknow area flag")

applymask=False
gnc_china_border = gnc.Ncdata('/homel/ychao/Documents/data/Country_Border/China_mask_halfdegree.nc')
mask=gnc_china_border.d1.land.mask
print "Flag for applymask: ",applymask


if not filename.endswith('.nc'):
    raise TypeError("Input file is not a nc file")
else:
    d = gnc.Ncdata(filename)
    outfilename = filename[:-3]+'_'+varname+'_PFT'+pft_flag+'_SPA'+area_flag+'.txt'

    if pft_flag == 'none':
        pftsum = d.d1.__dict__[varname]
    else:
        pftsum = get_pftsum(d,varname,pft_flag)
    if applymask:
        pftsum = mathex.ndarray_mask_smart_apply(pftsum,mask)

    outdata = treat_spatial(d,pftsum,area_flag)
    np.savetxt(outfilename,outdata)







