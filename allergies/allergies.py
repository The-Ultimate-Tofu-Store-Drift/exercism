
class Allergies(object):

    def __init__(self, points):
        self.points = points

    list_of_items = {
        "eggs": 1,
        "peanuts": 2,
        "shellfish": 4,
        "strawberries": 8,
        "tomatoes": 16,
        "chocolate": 32,
        "pollen": 64,
        "cats": 128
    }

    order = ["cats", "pollen", "chocolate", "tomatoes", "strawberries", "shellfish", "peanuts", "eggs"]
    lst_results = []

    def is_allergic_to(self, item):
        if self.list_of_items[item] <= self.points:
            return True
        else:
            return False

    def lst(self):
        while self.points > 256:
            self.points -= 256

        for i in self.order:
            if self.list_of_items[i] <= self.points:
                self.lst_results.append(i)
                self.points -= self.list_of_items[i]

        return self.lst_results[::-1]

if __name__ == "__main__":
    print(Allergies(2).lst())
