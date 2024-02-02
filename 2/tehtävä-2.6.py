from datetime import date

def list_years(date1, date2, date3):
    years = ""
    dates = [date1, date2, date3]
    years = sorted(d.year for d in dates)
    return years






date1 = date(2019, 2, 3)
date2 = date(2006, 10, 10)
date3 = date(1993, 5, 9)

years = list_years(date1, date2, date3)
print (years)