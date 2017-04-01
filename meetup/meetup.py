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
        "last": 4
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

    print("grouped_days: ", grouped_days)

    for i in range(len(grouped_days)):
        for j in grouped_days[i]:
            if j == 0:
                del grouped_days[i][find_index(j)]

    print("deleted: ", grouped_days)

    if spec == "teenth":
        for i in grouped_days[days[weekday]]:
            if i in teenth:
                ex_date = i
    else:
        ex_date = grouped_days[days[weekday]][spec_list[spec]]

    print(ex_date)

    # for i in range(len(b)):
    #     for j in b[i]:
    #         cal[j] = t[0]
    #         del t[0]

    # for i in range(len(b)):
    #     for j in b[i]:
    #         if j > 0:
    #             b_c.append([b[i][find_index(j)]])

    # for h in range(8):
    #     for i in range(len(b)):
    #         for j in b[i]:
    #             if j < 1:
    #                 del b[i][find_index(j)]

    # for i in cal:
    #     if cal[i] == days[weekday] and i in b[spec_list[spec]]:
    #         print(year, month, i)
    #         break
    #     elif cal[i] == days[weekday] and i in b[spec_list[spec] + 1]:
    #         print(year, month, i)
    #         break

    a = date.isocalendar(date.today())

    print("b: ", b)

    return "{0}, {1}, {2}".format(year, month, ex_date)

print(meetup_day(2013, 5, 'Monday', 'teenth'))  # 2013, 5, 13

# teenth : 13 - 17
# Monday : 0; Sunday: 6
