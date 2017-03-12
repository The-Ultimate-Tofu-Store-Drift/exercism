

def clock(hours, minutes):

    hh = 0
    mm = 0

    while minutes < 0:
        minutes += 60
        hours -= 1

    while hours < 0:
        hours += 24

    while minutes >= 60:
        minutes -= 60
        hours += 1
    else:
        mm = minutes

    while hours >= 24:
        hours -= 24
        if hours == 24:
            hh = 0
    else:
        hh = hours

    # if hh < 10:
    #    hh = str(0) + str(hh)

    # if mm < 10:
    #    mm = str(0) + str(mm)

    return "{0:02d}:{1:02d}".format(hh, mm)

print(clock(11, 9))
