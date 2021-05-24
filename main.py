from year import *
from sweepstakes import *
"""Store the months of the year, grab month which Pi Day exists"""

current_year = Year(2021)
month_contains_pi_day = current_year.filter_month_by_holiday("Pi Day")
print(month_contains_pi_day.name)

vacation_places = {"Miami", "Savannah", "Atlanta"}
vacation_places.update(["Los Angeles", "Cancun", "Alaska"])

for place in vacation_places:
    print(place)

sweepstakes = Sweepstakes()
sweepstakes.add_contestant("Jon", "Cena", 37461)
sweepstakes.add_contestant("Jerry", "McGuire", 4578)
sweepstakes.add_contestant("Mary", "Poppins", 6521)
sweepstakes.add_contestant("Rocky", "Balboa", 7623)
sweepstakes.add_contestant("Demolition", "Man", 8964)
sweepstakes.random_winner()
