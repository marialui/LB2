for i in *.pssm
do
cat $i| tail -n +3|head -n -6 |tr -s " "|sed "s/\s/\t/g"> ../profile/${i%.*.*}.pssm
python3 pssm_parsing.py ../profile/${i%.*.*}.pssm  ../profile/${i%.*.*}.profile
done

