import sys

def tags_to_topics(topic_tag_probabilities):
    #topic_tag_probabilities[topic, tag] = avg(P(tag_word | topic) for tag_word in tag)
    if len(topic_tag_probabilities) == 0:
        #base case
        return ({}, {})

    best_topic = None
    best_tag = None
    best_prob = -1.0
    for (topic,tag) in topic_tag_probabilities:
        prob = topic_tag_probabilities[topic,tag]
        if prob > best_prob:
            best_topic = topic
            best_tag = tag
            best_prob = prob

    topic_tag_probabilities_ = {
            (topic, tag) : topic_tag_probabilities[topic,tag]
            for topic, tag in topic_tag_probabilities
            if topic != best_topic and tag != best_tag
        }

    best_tag_s = "-".join(best_tag)

    topic_tag_dict, tag_topic_dict = tags_to_topics(topic_tag_probabilities_)
    topic_tag_dict[best_topic] = best_tag_s
    tag_topic_dict[best_tag_s] = best_topic

    return (topic_tag_dict, tag_topic_dict)


def get_topic_tag_probabilities(tags_list_file, phi_file, wordmap_file):
    tags_list = []
    with open(tags_list_file) as f:
        tags_list = [tuple(line[:-1].split('-')) for line in f]

    #relevant_words = set.union(*(set(tag) for tag in tags_list))

    words_to_idx = {}
    idx_to_words = {}
    with open(wordmap_file) as f:
        for line in f:
            word = line[:-1].split()[0]
            idx = int(line[:-1].split()[-1])
            #if word not in relevant_words: continue
            words_to_idx[word] = idx
            idx_to_words[idx] = word

    topic_word_probabilities = {}

    topics = None

    with open(phi_file) as f:
        for topic, line in enumerate(f):
            probs = [float(sprob) for sprob in line.split()]
            for word_idx, prob in enumerate(probs):
                #if idx not in idx_to_words: continue
                word = idx_to_words[word_idx]
                topic_word_probabilities[topic, word] = prob
        topics = range(topic+1)

    topic_tag_probabilities = {
        (topic, tag): sum(
                (topic_word_probabilities[topic, word]
                 if (topic, word) in topic_word_probabilities
                 else 0.0)
                for word in tag
            ) / len(tag)
        for tag in tags_list
        for topic in topics
    }

    return topic_tag_probabilities, topics, tags_list

def main(tags_list_file, phi_file, wordmap_file):
    return tags_to_topics(get_topic_tag_probabilities(tags_list_file, phi_file, wordmap_file)[0])



if __name__ == '__main__':
    tags_list_file = sys.argv[1]
    phi_file = sys.argv[2]
    wordmap_file = sys.argv[3]

    print(main(tags_list_file, phi_file, wordmap_file))

