from statistics import median
import func
import constant


def main():
    print("Input text ")
    text = input()

    text = text.replace(",", "").replace(":", "").replace(";", "")
    text = text.replace("?", ".").replace("!", ".").lower()


    #mr = ['mr.', 'ms.', 'mrs.', 'dr.', 'ex.', 'etc.', 'co.',  'st.', 'ave.', 'jr.', 'sr.', 'in', 'cm.', 'kg.']

    #for elem in text:
        #if elem is mr:
            #elem = elem[:(len(elem)-1)]

    text = text.split(".")
    sentence = dict()

    #sentence in dictionary
    for val in text:
        sentence[text.index(val)+1] = val.split()

    count_of_words = func.count_word(sentence)
    for key in count_of_words:
      print(f"{key}:{count_of_words[key]}")

    medium = func.medium_word(sentence)
    print(medium)

    a = func.median_word(sentence)
    print(a)

    #NGRAM
    K = input("Input k")

    try:
        K = int(K)
        print("It's correct input!")
    except ValueError:
        print("Wrong input!  K is 10")
        K = constant.CONST_K

    N = input("Input N")

    try:
        N = int(N)
        print("It's correct input!")
    except ValueError:
        print("Wrong input! N is 4")
        N = constant.CONST_N

    grams = func.n_gram(sentence, N)

    grams_fin = dict(sorted(grams.items(), key=lambda item: item[1], reverse=True))
    print(f"Top-{K}  {N}-grams:")

    for t in grams_fin:
        K -= 1
        if K == -1:
            return
        for el in t:
            print(f"{el}", end=" ")
        print(f":{grams_fin[t]}")


if __name__ == "__main__":
    main()
















