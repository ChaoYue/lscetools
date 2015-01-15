#!/bin/bash

if [[ $1 == "-h" || $1 == "-help" || $1 == "" ]] ; then
  echo "Usage: `basename $0` 4 arguments needed: WORKDIR NC_FILENAME VARNAME TITAL"
  exit 0
fi


WORKDIR=$1
NC_FILENAME=$2
VARNAME=$3
TITAL=$4

cd ${WORKDIR}

python /home/users/ychao/script/map_month.py ${WORKDIR}/${NC_FILENAME} ${VARNAME} "${TITAL[*]}"
convert -delay 80 -loop 0 ${VARNAME}*.png ${VARNAME}_month_ani.gif
rm -fr ${VARNAME}*.png
echo "animation for file --${NC_FILENAME}-- and variable --${VARNAME}-- has been done"


