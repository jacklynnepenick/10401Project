import csv
import sys
from ast import literal_eval

training_set_file = sys.argv[1]

with open(training_set_file) as csvfile:
    reader = csv.DictReader(csvfile)
    tags = set()
    for row in reader:
        for tag in literal_eval(row['tags']):
            tags.add(tag)
    for tag in sorted(tags):
        print(tag)
