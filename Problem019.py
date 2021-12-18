year = 1901
month = 1
day = 1

end_year = 2000
end_month = 12
end_day = 30

week_day = 1
sunday_counter = 0

while not (year == end_year and month == end_month and day == end_day):
    day += 1
    week_day = week_day % 7
    week_day += 1
    print(f"{day}/{month}/{year} {week_day}")
    if day == 1 and week_day == 7:
        sunday_counter += 1
    if day == 28 and month == 2:
        if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
            pass
        else:
            day = 0
            month += 1
    elif day == 29 and month == 2:
        day = 0
        month += 1
    elif day == 30 and (month == 4 or month == 6 or month == 9 or month == 11):
        day = 0
        month += 1
    elif day == 31:
        day = 0
        if month == 12:
            month = 1
            year += 1
        else:
            month += 1
    else:
        pass
print(f"Number of Sundays is: {sunday_counter}")