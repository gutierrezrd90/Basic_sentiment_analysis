def strip_punctuation(word):
    for char in word:
        if char in punctuation_chars:
            word = word.replace(char,"")
    return word

def get_pos(sentence):
    count = 0
    sentence = strip_punctuation(sentence.lower())
    for word in sentence.split():
        if word in positive_words:
            count = count + 1
    return count

def get_neg(sentence):
    count = 0
    sentence = strip_punctuation(sentence.lower())
    for word in sentence.split():
        if word in negative_words:
            count = count + 1
    return count

punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']

positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())

negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())

file_input = open("project_twitter_data.csv", "r")
file_output = open("resulting_data.csv", "w")
file_output.write("Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score\n")
for line in file_input.readlines()[1:]:
    items = line.strip().split(",")
    pos_score = get_pos(items[0])
    neg_score = get_neg(items[0])
    net_score = pos_score - neg_score
    file_output.write("{},{},{},{},{}\n".format(items[1], items[2], pos_score, neg_score, net_score))
file_input.close()
file_output.close()