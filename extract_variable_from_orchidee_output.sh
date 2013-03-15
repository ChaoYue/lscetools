#!/bin/bash

##Purpose:
#This is especially for extracting varialbe values from the orchidee output file and useful for debugging purpose.

##Arguments:
#infile --> file from which string will be extract.
#outfile --> final output data file, containing data sperated by blank spaces or tab.
#search_string_and_remove --> string searched and will be removed in the data file to have only numeric data separated by blank space or tab
#line_number how many lines including the matching line to be extracted in occurrence of a match.

##Notes:
#The script can handle flexibly the cases when line_number==1

infile=$1
outfile=$2
search_string_and_remove=$3
line_number=$4

echo ${search_string_and_remove}

rm -fr tempfile.txt

if [ ${line_number} -eq 1 ] ; then
  grep "${search_string_and_remove}" ${infile} > tempfile.txt
  python /home/users/ychao/python/script/remove_string_each_line.py tempfile.txt ${outfile} "${search_string_and_remove}"
  rm -fr tempfile*.txt
else
  grep "${search_string_and_remove}" -A $((line_number-1)) ${infile} > tempfile.txt
  python /home/users/ychao/python/script/mergeline.py tempfile.txt tempfile1.txt $((line_number+1))  #line_number needs to be added 1 because after each pattern matching, 											           #grep command add another "--" afterwards.
  python /home/users/ychao/python/script/remove_string_each_line.py tempfile1.txt tempfile2.txt "${search_string_and_remove}"
  python /home/users/ychao/python/script/remove_string_each_line.py tempfile2.txt ${outfile} "--"  #we have to remove the "--" that's introduced when using grep command
  rm -fr tempfile*.txt
fi
