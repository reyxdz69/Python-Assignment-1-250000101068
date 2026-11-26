# Assignment 1, Question 10
# Swap variables with tuple unpacking

first_stop = "Hostel Gate"
second_stop = "Central Library"
print("Original shuttle order:", first_stop, "then", second_stop)

first_stop, second_stop = second_stop, first_stop
print("Revised shuttle order:", first_stop, "then", second_stop)
