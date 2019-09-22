#!/usr/bin/python
import sys

def get_list_fasta(lid,fasta):
    f=open(fasta)
    c=0
    for line in f:
        line=line.rstrip()
        if line[0]=='>':
            tid=line.split('|')[0][1:]

        if lid.get(tid,False)==1:
            #you go here only if the statement is true and so c=1 and it will print the value
            #in the case the id is not present in line it will return false and it will pass in the else statement
            c=1
        else:
            c=0
        if c==1 :
            print(line)


if __name__=="__main__":
    fid=sys.argv[1]
    fasta= sys.argv[2]
    lid=dict([(i,True) for i in open(fid).read().split('\n')])
              #here i generate a set of touples where each key
    get_list_fasta(lid,fasta)
