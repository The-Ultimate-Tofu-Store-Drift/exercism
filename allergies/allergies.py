
class Allergies(object):

    def __init__(self, points):
        self.points = points
        self.lst = list(i for i in self.list_of_items if self.is_allergic_to(i))

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

    def is_allergic_to(self, item):
        return self.list_of_items[item] & self.points
