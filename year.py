import months


class Year:
    def __init__(self, number):
        self.number = number
        self.months_tuple = (months.january, months.february, months.march, months.april, months.may)
        self.check_leap_year(number)

    def check_leap_year(self, number):
        if number % 4 == 0:
            self.months_tuple = (months.january, months.leap_year_feb, months.march, months.april, months.may)

    def filter_month_by_holiday(self, holiday_str=""):
        i = 0
        for month in self.months_tuple:
            while len(month.holidays) > i:
                if month.holidays[i] == holiday_str:
                    return month
                else:
                    i += 1

