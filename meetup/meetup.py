from datetime import date
import calendar


def meetup_day(year, month, weekday, spec):

    teenth = [i for i in range(13, 19)]

    days = {
        "Monday": 0,
        "Tuesday": 1,
        "Wednesday": 2,
        "Thursday": 3,
        "Friday": 4,
        "Saturday": 5,
        "Sunday": 6
    }

    spec_list = {
        "1st": 0,
        "2nd": 1,
        "3rd": 2,
        "4th": 3,
        "5th": 4,
        "last": -1
    }

    # thanks to stackoverflow
    def find_index(sus):
        for i, lst in enumerate(grouped_days):
            try:
                j = lst.index(sus)
            except ValueError:
                continue
            return j

    b = calendar.monthcalendar(year, month)

    grouped_days = [[], [], [], [], [], [], []]

    # groups all monday in a list, groups all tuesday in a list and so on
    for j in range(7):
        for i in range(len(b)):
            grouped_days[j].append(b[i][j])

    # a '0' stands for a day outside of the requested month, they must be deleted
    for i in range(len(grouped_days)):
        for j in grouped_days[i]:
            if j == 0:
                del grouped_days[i][find_index(j)]

    # checks if the argument is this weird 'teenth' thing and selects
    # the day with help from the 'teenth' list or the 'spec' list
    if spec == "teenth":
        for i in grouped_days[days[weekday]]:
            if i in teenth:
                extracted_day = i
    else:
        extracted_day = grouped_days[days[weekday]][spec_list[spec]]

    return date(year, month, extracted_day)
