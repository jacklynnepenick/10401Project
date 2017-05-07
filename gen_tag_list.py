import csv
import sys
from ast import literal_eval
from os import listdir
from os.path import isdir

#training_set_file = sys.argv[1]

for partial_data_folder in listdir("./preprocessed-input"):
    if not isdir("./preprocessed-input/" + partial_data_folder):
        continue
    data_folder = "./preprocessed-input/" + partial_data_folder
    training_set_file = None
    for file_name in listdir(data_folder):
        if file_name[-len(".csv"):] == ".csv":
            training_set_file = data_folder + "/" + file_name
            break
    else:
        print("Could not find csv for data folder " + partial_data_folder)
    tag_list_file_name = data_folder + "/tag_list.txt"

    with open(training_set_file) as csvfile, \
            open(tag_list_file_name, "w") as tag_list_file:
        reader = csv.DictReader(csvfile)
        tags = set()
        for row in reader:
            for tag in literal_eval(row['tags']):
                tags.add(tag)
        for tag in sorted(tags):
            tag_list_file.write(tag + "\n")
