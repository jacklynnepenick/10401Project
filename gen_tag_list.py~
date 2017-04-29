import csv
import sys

training_set_file = sys.argv[1]

with open(training_set_file) as csvfile:
    reader = csv.DictReader(csvfile)
    tags = set()
    for row in reader:
        for tag in eval(row['tags']):
            tags.add(tag)
    for tag in sorted(tags):
        print(tag)
