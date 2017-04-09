
def detect_anagrams(word, list_with_words):

    counter = 0
    results = []

    for i in range(len(list_with_words)):

        if len(word) == len(list_with_words[i]) and word.lower() != list_with_words[i].lower():

            for letter in list_with_words[i]:

                if list_with_words[i].lower().count(letter) == word.lower().count(letter):

                    counter += 1

                    if counter == len(word):
                        results.append(list_with_words[i])
                        counter = 0

                else:
                    counter = 0
                    break

    return results
