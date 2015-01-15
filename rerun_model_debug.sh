#!/bin/bash

###Arguments:
#working_directory

wd=$1

echo "----------------begining to run the model for test--------"
echo "----------------------------------------------------------"

cd ${wd}
echo "enter into working directory:"
echo ${wd}

echo "----------------remove restart files-----------------"
rm -fr driver_restart.nc
rm -fr sechiba_restart.nc
rm -fr stomate_restart.nc
echo "----------------copy orchidee_ol---------------------"
cp /home/orchidee01/ychao/TRUNK_SPITFIRE/modipsl/bin/orchidee_ol .
echo "--------run the model and write to out.txt------------"
./orchidee_ol > out.txt

