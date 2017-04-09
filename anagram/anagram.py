
def detect_anagrams(word, list_with_words):

    counter = 0
    results = []

    while counter != len(word):

        for i in range(len(list_with_words)):
            if len(word) == len(list_with_words[i]):
                for letter in list_with_words[i]:
                    if list_with_words.count(letter).lower == word.lower.count(letter):
                        counter += 1
                    else:
                        break
            else:
                break
    else:
        results.append(list_with_words[i])

    return results


if __name__ == "__main__":
    print(detect_anagrams("ant", ["tan", "stand", "at"]))
