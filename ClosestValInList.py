# Given List, and an integer X,
# Find the closest value for X in the list


given_value = -4
a_list = [10, 2, 8, -5, 4, -5]
closest_value = min(a_list, key=lambda a_list: abs(a_list - given_value))
print(closest_value)
