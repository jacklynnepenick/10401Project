#!/bin/sh

# DIRS=$(ls | grep data)
DIRS="data-robotics"
for DIR in $DIRS
do
    cd $DIR
    ../../lda-trial/GibbsLDA++-0.2/src/lda -est -ntopics $(grep $DIR ../numtags | cut -f 2 -d" ") -savestep 500 -twords 20 -dfile *.txt
    cd -
done
