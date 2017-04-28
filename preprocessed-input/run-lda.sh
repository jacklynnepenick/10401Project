#!/bin/sh

DIRS=$(ls | grep data)
for DIR in $DIRS
do
    cd $DIR
    ../../lda-trial/GibbsLDA++-0.2/src/lda -est -savestep 500 -twords 20 -dfile *.txt
    cd -
done
