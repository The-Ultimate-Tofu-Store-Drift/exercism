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

    def find_index(sus):
        for i, lst in enumerate(grouped_days):
            try:
                j = lst.index(sus)
            except ValueError:
                continue
            return j

    b = calendar.monthcalendar(year, month)

    grouped_days = [[], [], [], [], [], [], []]

    for j in range(7):
        for i in range(len(b)):
            grouped_days[j].append(b[i][j])

    for i in range(len(grouped_days)):
        for j in grouped_days[i]:
            if j == 0:
                del grouped_days[i][find_index(j)]

    if spec == "teenth":
        for i in grouped_days[days[weekday]]:
            if i in teenth:
                ex_date = i
    else:
        ex_date = grouped_days[days[weekday]][spec_list[spec]]

    return date(year, month, ex_date)
