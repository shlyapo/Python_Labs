
def count_word(sentence): #первый метод
    count_of_words = dict()

    for value in sentence.values():
        for word in value:
            if word in count_of_words.keys():
                count_of_words[word] += 1
            else:
                count_of_words[word] = 1

    return count_of_words


def medium_word(sentence): #второй метод
    count = 0
    count_of_sentence = len(sentence)

    for value in sentence.values():
        n = len(value)
        count += n

    return count / count_of_sentence


def median_word(sentence): #третий метод
    count = []

    for value in sentence.values():
        length = len(value)
        count.append(length)

    n = len(count)
    index = n // 2

    if n % 2:
        return sorted(count)[index]

    return sum(sorted(count)[index - 1:index + 1]) / 2


def n_gram(sentence, N):
    temp = []


    for value in sentence.values():
        for el in value:
            for letter in el:
                temp.append(letter)
            general = []
            for i in range(N):
                general.append(temp[i:])

    n_gram = list(zip(*general))
    n_gram_dic = {}

    for el in n_gram:
        if el in n_gram_dic:
            n_gram_dic[el] += 1
        else:
            n_gram_dic[el] = 1

    return n_gram_dic
