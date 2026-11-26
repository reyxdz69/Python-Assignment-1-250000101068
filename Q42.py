# Assignment 1, Question 42
# Object identity with id()

active_orders = ["ORD-207", "ORD-215"]
same_orders = active_orders
separate_orders = active_orders.copy()

print("Active list ID:", id(active_orders))
print("Alias ID:", id(same_orders))
print("Copy ID:", id(separate_orders))
print("Alias and original share an ID:", id(same_orders) == id(active_orders))
