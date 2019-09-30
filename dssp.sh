#!/bin/bash
for m in `cat blindsetnames`
do
#	echo $m
   mkdssp -i $m.pdb -o $m.dssp
done
