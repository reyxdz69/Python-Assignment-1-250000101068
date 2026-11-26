# Assignment 1, Question 28
# Use abs(), round() and pow()

target_temperature = 32.0
reading = 29.647
temperature_gap = abs(reading - target_temperature)
side = 7

print(f"Temperature gap: {round(temperature_gap, 2):.2f} C")
print(f"Area of a model tile: {pow(side, 2)} cm^2")
