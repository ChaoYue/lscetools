#!/bin/bash
#set -vx

#Purpose:
#   Used to merge several NetCDF files into one 

#How to use:
#   ./merge_ncfile.sh working_directory var1.nc var2.nc var3.nc var4.nc allvar.nc
#   1. the first argument is the working directory.
#   2. the last one is output file, files before last one are input files.


#read all the input into an shell array
ARGS=("$@")
#get the 1st argument as working_directory
WD=${ARGS[0]}
#give the last element(outputfile)
outputfile=${ARGS[$((${#ARGS[@]}-1))]}

if [ -f ${outputfile} ] ; then
  echo ${outputfile} exists and will be deleted!!
  rm -fr ${outputfile}
fi

cd $WD
cp ${ARGS[1]} ${outputfile}
echo ${ARGS[1]} has been copied as the final outputfile: ${outputfile}

for FILENAME in ${ARGS[*]:2:$((${#ARGS[@]}-3))} #slice begining the 2nd one, with length of $((total_length-3))
 do
  ncks -A ${FILENAME} ${outputfile}
  echo input file --${FILENAME}-- has been included!
 done

