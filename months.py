import calendar

# calendar.month_name contains an empty string at index 0, so we slice from index 1
for month_id in range(1, 13):
    print(calendar.month_name[month_id])
