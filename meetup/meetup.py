from datetime import date
import calendar


def meetup_day(year, month, weekday, spec):

    teenth = [i for i in range(13, 18)]
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
        "teenth":1
    }

    cal = {}

    # if spec == "teenth":

    def find_index(sus):
        for i, lst in enumerate(b):
            try:
                j = lst.index(sus)
            except ValueError:
                continue
            return j

    t = [i for i in range(0, 7)] * 6
    filler = [i for i in range(-10, 0)]

    b = calendar.monthcalendar(year, month)
    print(b)

    for i in range(len(b)):
        for j in b[i]:
            if j == 0:
                b[i][find_index(j)] = filler[0]
                del filler[0]

    for i in range(len(b)):
        for j in b[i]:
            cal[j] = t[0]
            del t[0]

    for i in cal:
        if cal[i] == days[weekday] and i in teenth:
            print(year, month, i)


    a = date.isocalendar(date.today())
    print(teenth)
    print(cal)
    print("t ", t)
    print(filler)

    print("find ", find_index(30))

    return b


print(meetup_day(2013, 5, 'Monday', 'teenth'))  # 2013, 5, 13

# teenth : 13 - 17
# Monday : 0; Sunday: 6
