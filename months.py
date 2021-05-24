class Months:
    def __init__(self, name, num_days, holidays_list):
        self.name = name
        self.days = num_days
        self.holidays = holidays_list


january = Months("January", 31, ["New Year's Day"])
february = Months("February", 28, ["Valentine's Day"])
leap_year_feb = Months("February", 29, ["Valentine's Day"])
march = Months("March", 31, ["St. Patrick's Day", "Pi Day"])
april = Months("April", 30, ["April Fool's Day"])
may = Months("May", 31, ["Star Wars Day"])

