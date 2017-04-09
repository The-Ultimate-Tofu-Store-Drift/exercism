
def detect_anagrams(word, list_with_words):

    counter = 0
    results = []

    while counter != len(word):

        for i in list_with_words:
            if len(word) == len(i):
                for letter in list_with_words[i]:
                    if list_with_words.lower.count(letter) == word.lower.count(letter):
                        counter += 1
                    else:
                        break
            else:
                break
    else:
        results.append(list_with_words[i])


if __name__ == "__main__":
    print(detect_anagrams())
