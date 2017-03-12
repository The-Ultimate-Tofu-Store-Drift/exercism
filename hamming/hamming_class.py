
class Hamming:

    def __init__(self):
        pass

    def distance(self, dna_string_1, dna_string_2):

        if len(dna_string_1) != len(dna_string_2):
            return False

        dna_list_1 = list(dna_string_1)
        dna_list_2 = list(dna_string_2)
        hamming_counter = 0

        for i in range(len(dna_string_1)):
            if dna_list_1[i] != dna_list_2[i]:
                hamming_counter += 1

        return hamming_counter

hamming = Hamming()

