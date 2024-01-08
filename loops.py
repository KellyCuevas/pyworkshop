colors = ["red", "green", "blue", "orange"]

for color in colors:
  print(f"The color is: {color}")

print("outside of the loop", color)

for index, color in enumerate(colors):
  print(f"{index} color at: {color}")