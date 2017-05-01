import sys
from operator import itemgetter

import pair_tags

def main(n, tags_list_file, theta_file, phi_file, wordmap_file):
    topic_tag_dict, tag_topic_dict = pair_tags.main(
            tags_list_file, phi_file, wordmap_file
        )

    # topic_questions_probs_dict[tag, question] = prob
    tag_questions_probs_dict = {}

    with open(theta_file, "r") as f:
        for question, line in enumerate(f):
            for topic, sprob  in enumerate(line.split()):
                if topic not in topic_tag_dict: continue
                prob = float(sprob)
                tag = topic_tag_dict[topic]
                tag_questions_probs_dict[tag, question] = prob

    best_n_taggings = sorted(
            tag_questions_probs_dict.items(),
            key=itemgetter(1),
            reverse=True
        )[:n]

    return best_n_taggings



if __name__ == '__main__':
    n = int(sys.argv[1])
    tags_list_file = sys.argv[2]
    theta_file = sys.argv[3]
    phi_file = sys.argv[4]
    wordmap_file = sys.argv[5]

    print(main(n, tags_list_file, theta_file, phi_file, wordmap_file))
