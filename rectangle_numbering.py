
'''
Task 1: Assign the number (1 to 4) below the image of the rectangle with respect to its length
inside the rectangle. The shorter the line lower the number (No need to reorder the image of the
rectangle, only give numbering)
'''



class Rectangle:
    def __init__(self, length, number=None):
        self.length = length
        self.number = number


# assuming length of line insides rectangle
line_length = [3, 2, 5, 1]

#creating rectangle with line lengths
rectangles = [Rectangle(line_length) for line_length in line_length]

#Assigning number based on the length of the line
sorted_rectangles = sorted(rectangles, key=lambda rect:rect.length)

number = 1
for rect in sorted_rectangles:
    rect.number = number
    number += 1

#printing assigned numbers for each rectangle
for rect in rectangles:
    print(f"Rectangle (Line Length: {rect.length}) - Number: {rect.number}")



