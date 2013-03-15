#!/bin/bash

#Purpose:
#   Used to merge several csv files

#How to use:
#   ./csv_merge f1.csv f2.csv f3.csv all.csv
#   1. the last one is output file, files before last one are input files.
#   2. the first line of the first file will be copied into output file, the first lines of other input files will be skiped.



#read all the input into an shell array
ARGS=("$@")
echo "ARGS: ${ARGS[*]}"
echo "Number of ARGS: ${#ARGS[*]}"
#give the last element(outputfile)
#outputfile=${ARGS[-1]}
outputfile=${ARGS[${#ARGS[@]}-1]}

echo "the one before output: ${ARGS[5-2]}"
echo "outputfile: ${outputfile}"

#remove the last one (in place operation) from the array
unset ARGS[${#ARGS[@]}-1]
echo "ARGS after removing last element: ${ARGS[*]}"
#use sed to write header of the first input file to output file
#sed -n 1p ${ARGS[0]} > ${outputfile}

#use sed to write 1-->end lines of other input files to output file
#for input_file_name in ${ARGS[*]}
#do 
#  sed 1d ${input_file_name} >> ${outputfile}
#done


