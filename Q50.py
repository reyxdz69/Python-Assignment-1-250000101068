# Assignment 1, Question 50
# Formatted student profile from separate variables

name = input("Full name: ").strip()
roll_number = input("Roll number: ").strip()
branch = input("Branch: ").strip()
university = "Veer Madho Singh Bhandari Uttarakhand Technical University, Dehradun"

print("\nStudent profile")
print("-" * 26)
print(f"{'Name':<12} {name}")
print(f"{'Roll number':<12} {roll_number}")
print(f"{'Branch':<12} {branch}")
print(f"{'University':<12} {university}")
