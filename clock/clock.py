
class Clock:
    """They wanted a class. So here it is!"""

    def __init__(self, hours, minutes):

        while minutes < 0:
            minutes += 60
            hours -= 1

        while hours < 0:
            hours += 24

        while minutes >= 60:
            minutes -= 60
            hours += 1

        while hours >= 24:
            hours -= 24
            if hours == 24:
                hours = 0

        self.hours = hours
        self.minutes = minutes

    # I guess it changes the way the original 'add' function works
    # instead of 'adding', it adds only to our variable 'minutes'
    def add(self, added_minutes):
        return Clock(self.hours, self.minutes + added_minutes)

    # This one overrides the 'str' function and let's it print
    # out the special format we are looking for.
    def __str__(self):
        return "{0:02d}:{1:02d}".format(self.hours, self.minutes)

    # I'll be honest, I don't how this actually works. It is indeed necessary
    # for unitesting, but I can't figure out how it resolves the following problem.
    # Some test of the unitest compare two clocks with the same time but different arguments
    # without this method it compares two shits like: <function Clock.add at 0x7f0a3774f950>
    # with each other. So this part must be some sort of python magic.
    def __eq__(self, other):
        if str(self) == str(other):
            return True
        else:
            return False
