# Assignment 1, Question 46
# Read five subject marks and total them

subjects = ("Python", "Mathematics", "Physics", "English", "Engineering Drawing")
marks = []
for subject in subjects:
    marks.append(float(input(f"{subject} marks: ")))

print(f"Total for five subjects: {sum(marks):g}")
