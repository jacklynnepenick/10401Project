import sys
import os
import itertools
import operator

question = 0
with open(sys.argv[1], "r") as f:
    for line in f:
        words = [ (i,float(x)) for (i,x) in enumerate(line.split(" ")) if x.strip() is not "" ]
        print(str(question) + ":\t" + str(sorted(words, key=operator.itemgetter(1), reverse=True)[:5]))
        question += 1
