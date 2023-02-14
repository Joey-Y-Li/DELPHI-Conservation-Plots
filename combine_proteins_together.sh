#!/bin/bash

for file in dataset/*.fasta
do
	cat $file >> sh2_DELPHI_format.fasta
	printf "\n" >> sh2_DELPHI_format.fasta
done
