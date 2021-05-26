from year import *
from sweepstakes import *
from immediate_family import *
from linkedlist import *
from node2 import *
"""Store the months of the year, grab month which Pi Day exists"""

current_year = Year(2021)
month_contains_pi_day = current_year.filter_month_by_holiday("Pi Day")
print(month_contains_pi_day.name)

"""Store placed you've celebrated a birthday. Add 3 locations. Print each location"""
vacation_places = {"Miami", "Savannah", "Atlanta"}
vacation_places.update(["Los Angeles", "Cancun", "Alaska"])

for place in vacation_places:
    print(place)

"""Create sweepstakes object, add 5 contestants, pick random winner"""
sweepstakes = Sweepstakes()
sweepstakes.add_contestant("Jon", "Cena", 37461)
sweepstakes.add_contestant("Jerry", "McGuire", 4578)
sweepstakes.add_contestant("Mary", "Poppins", 6521)
sweepstakes.add_contestant("Rocky", "Balboa", 7623)
sweepstakes.add_contestant("Demolition", "Man", 8964)
sweepstakes.random_winner()

"""create immediate family dictionary list"""
immediate_family = [ImmediateFamily("Amanda", "Farrell", "Spouse"), ImmediateFamily("Mary", "Myers", "Mother"), ImmediateFamily("Finlee", "Farrell", "Daughter")]
print(immediate_family)

"""Linked list"""
linked_list = LinkedList()
linked_list.append_node(55)
linked_list.append_node(60)
linked_list.append_node(65)
linked_list.add_to_beginning(50)
if linked_list.contains_node(60):
    print("yes")
else:
    print("No")


node = Node(50)
insert_node(node, 47)
insert_node(node, 65)
insert_node(node, 32)
insert_node(node, 52)

if search_for_node(node, 65):
    print('yes')
else:
    print('no')

in_order(node)
pre_order(node)
