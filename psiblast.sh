#!/bin/bash
for i in *.fasta
do
    psiblast -query $i -db uniprot_sprot -evalue 0.01 -num_iterations 3 -out_ascii_pssm $i_.pssm -out $i_.alns.blast
done

