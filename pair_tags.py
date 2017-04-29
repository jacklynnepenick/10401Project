import sys

def tags_to_topics(topic_word_probabilities):
    #topic_word_probabilities[topic, word] = P(word | topic)
    # topic_word_probabilities undefined for word not in tags
    if len(topic_word_probabilities) == 0:
        #base case
        return ({}, {})

    best_topic = None
    best_tag = None
    best_prob = -1.0
    for (topic,tag) in topic_word_probabilities:
        prob = topic_word_probabilities[topic,tag]
        if prob > best_prob:
            best_topic = topic
            best_tag = tag
            best_prob = prob

    topic_word_probabilities_ = {
            (topic, word) : topic_word_probabilities[topic,word]
            for topic, word in topic_word_probabilities
            if topic != best_topic and word != best_tag
        }

    topic_tag_dict, tag_topic_dict = tags_to_topics(topic_word_probabilities_)
    topic_tag_dict[best_topic] = best_tag
    tag_topic_dict[best_tag] = best_topic

    return (topic_tag_dict, tag_topic_dict)

if __name__ == '__main__':
    tags_list_file = sys.argv[1]
    phi_file = sys.argv[2]
    wordmap_file = sys.argv[3]

    tags_list = []
    with open(tags_list_file) as f:
        tags_list = [line[:-1] for line in f]
    tags_set = set(tags_list)

    tags_to_idx = {}
    idx_to_tags = {}
    with open(wordmap_file) as f:
        for line in f:
            tag = line[:-1].split()[0]
            idx = int(line[:-1].split()[-1])
            if tag in tags_set:
                tags_to_idx[tag] = idx
                idx_to_tags[idx] = tag
    #note: domain(tags_to_idx) != tags_set

    topic_word_probabilities = {}

    with open(phi_file) as f:
        for topic, line in enumerate(f):
            probs = [float(sprob) for sprob in line.split()]
            for tag_idx, prob in enumerate(probs):
                if tag_idx not in idx_to_tags:
                    continue
                tag = idx_to_tags[tag_idx]
                topic_word_probabilities[topic, tag] = prob


    print(tags_to_topics(topic_word_probabilities))

