#!/home/orchidee03/ychao/anaconda/bin/python

import sys
import numpy as np

time_axis = sys.argv[1]
if time_axis in ['-h','-help']:
    print '''
    Return the 0-based slice index for intervals:

    How to use:
    -----------
    find_index.py start:end[:step] slice1:slice2

    Example:
    --------
    find_index.py 1946:2012 2000:2009

    Notes:
    ------
    step default is 1.

    Returns:
    --------
    0-based based slice index for interval of (slice1,slice2)
    '''
    sys.exit()

slice_axis = sys.argv[2]


time_axis_list = map(float,time_axis.split(':'))
slice_axis_list = map(float,slice_axis.split(':'))

if len(time_axis_list) == 2:
    time_axis_list = time_axis_list + [1]

start,end,step = time_axis_list
time_axis = np.arange(start,end+step/5.,step)

if len(time_axis) == 0:
    raise ValueError("""Please check the parent sequnce input,
                        empty array generated!""")



if time_axis[0] > time_axis[1]:
    decrease = True
else:
    decrease = False

slice1,slice2 = slice_axis_list
if decrease:
    if slice1 < slice2:
        raise ValueError("""parent sequence decrease but
                            the subslice is increasing""")
    else:
        index_list = np.nonzero((time_axis<=slice1)&(time_axis>=slice2))[0]
else:
    if slice1 > slice2:
        raise ValueError("""parent sequence increase but
                            the subslice is decreasing""")
    else:
        index_list = np.nonzero((time_axis>=slice1)&(time_axis<=slice2))[0]

print (index_list[0],index_list[-1])






