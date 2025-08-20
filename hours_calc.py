import datetime
def working_hours_calc(
    time1: datetime.datetime,
    time2: datetime.datetime,
    special_days: list[datetime.date] = None):
    
    """
    Returns a list of datetimes between time1 and time2:
    - time1 and time2 are always included with their exact time
    - intermediate days are included at midnight (00:00)
    - weekends (Sat, Sun) are excluded
    - special_days (list of datetime.date) are excluded
    """

    if special_days is None:
        special_days = []

    days_list = [time1]

    for i in range(1, (time2.date() - time1.date()).days):
        d = time1.date() + datetime.timedelta(days=i)
        if d.weekday() < 5 and d not in special_days:
            days_list.append(datetime.datetime.combine(d, datetime.time()))

    days_list.append(time2)

    end_of_working_hours = 16
    hours = 0
    hours += round(end_of_working_hours - (time1.hour + time1.minute / 60), 2)
    hours += round(end_of_working_hours - (time2.hour + time2.minute / 60), 2)
    hours += (len(days_list) - 2 ) * 8

    return hours