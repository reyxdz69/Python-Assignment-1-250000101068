# Assignment 1, Question 45
# Read dimensions and calculate rectangle area

length = float(input("Poster board length (cm): "))
breadth = float(input("Poster board breadth (cm): "))
if length > 0 and breadth > 0:
    print(f"Poster board area: {length * breadth:.2f} cm^2")
else:
    print("Both dimensions must be positive.")
