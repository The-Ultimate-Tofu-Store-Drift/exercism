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

    # if spec == "teenth":

    t = []

    b = calendar.monthcalendar(year, month)

    for i in range(len(b)):
        for j in b[i]:
            print(j)

    a = date.isocalendar(date.today())
    print(teenth)
    print(t)

    return b


print(meetup_day(2013, 5, 'Monday', 'teenth'))  # 2013, 5, 13

# teenth : 13 - 17
# Monday : 0; Sunday: 6
