# Assignment 1, Question 5
# Valid and invalid Python identifiers

import keyword

lab_room = "B-204"
_lab_helper = "Meera"
seat2 = 2
print("Values of valid variables:", lab_room, _lab_helper, seat2)

examples = ["lab_room", "_lab_helper", "seat2", "2seat", "lab-room", "for"]
for name in examples:
    if name.isidentifier() and not keyword.iskeyword(name):
        print(f"{name}: valid")
    else:
        print(f"{name}: invalid")
