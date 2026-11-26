# Assignment 1, Question 9
# Swap variables with a temporary variable

monday_room = "Lab 302"
wednesday_room = "Lab 105"
print("Before:", monday_room, wednesday_room)

previous_monday_room = monday_room
monday_room = wednesday_room
wednesday_room = previous_monday_room
print("After:", monday_room, wednesday_room)
