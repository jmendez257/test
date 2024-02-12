import math

radius = int(input('Enter the radius of your circle: '))
circumference = 2 * math.pi * radius
area = math.pi * radius ** 2
print(f'The circumference is {round(circumference, 2)}, the area is {round(area, 2)} '
      f'For the radius {radius}')

