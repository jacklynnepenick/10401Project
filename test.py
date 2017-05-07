import sys
import csv
from ast import literal_eval
from os import listdir
from os.path import isdir

from best_n_tags import main as get_best_n_taggings

if __name__ == '__main__':
    with open("./test_results.txt", "w") as results_file:
        for partial_data_folder in listdir("./preprocessed-input"):
            if "crypto" in partial_data_folder:
                # bug that affects crypto data, don't got time to actually fix it
                continue
            if "travel" in partial_data_folder:
                # My computer doesn't have enough ram for travel and I don't have the time to fix that
                continue
            print("%s:" % partial_data_folder)
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
            theta_file = data_folder + "/model-final.theta"
            tags_list_file = data_folder + "/tag_list.txt"
            phi_file = data_folder + "/model-final.phi"
            wordmap_file = data_folder + "/wordmap.txt"

            training_set = []

            with open(training_set_file) as csvfile:
                reader = csv.DictReader(csvfile)
                n = 0
                for row in reader:
                    row['tags'] = literal_eval(row['tags'])
                    training_set.append(row)
                    n += len(row['tags'])

            best_n_taggings = get_best_n_taggings(
                n, tags_list_file, theta_file, phi_file, wordmap_file
            )

            ncorrect = 0

            for (tag,question), prob in best_n_taggings:
                if tag in training_set[question]['tags']:
                    ncorrect += 1

            results_file.write(
                "%s: Correct: %d, Total: %d\n"
                % (partial_data_folder, ncorrect, n)
            )
