# Assignment 1, Question 20
# Quotient and remainder for packing sensor tags

tag_count = int(input("Number of tags: "))
tags_per_sheet = int(input("Tags per sheet: "))

if tag_count < 0 or tags_per_sheet <= 0:
    print("Use a non-negative tag count and a positive sheet size.")
else:
    full_sheets = tag_count // tags_per_sheet
    leftover_tags = tag_count % tags_per_sheet
    print("Full sheets:", full_sheets)
    print("Tags left over:", leftover_tags)
