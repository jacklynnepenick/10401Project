import sys
import csv
from ast import literal_eval

from best_n_tags import main as get_best_n_taggings

if __name__ == '__main__':
    training_set_file = sys.argv[1]
    theta_file = sys.argv[2]
    tags_list_file = sys.argv[3]
    phi_file = sys.argv[4]
    wordmap_file = sys.argv[5]

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

    print(ncorrect, n)

