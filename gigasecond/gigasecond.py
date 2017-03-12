from datetime import timedelta
# 11574 days, 1:46:40


def add_gigasecond(date):

    d = date
    gigasecond = timedelta(0, 10**9)

    moment = d + gigasecond

    return moment
