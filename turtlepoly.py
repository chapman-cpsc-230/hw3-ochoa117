"""
File: <turtlestar.py>

Copyright (c) 2016 <William Ochoa>

License MIT

<This code produces a polygon with any number of sides given that it is a natural number.>
"""

import turtle
bob = turtle.Pen()

num_sides_inp = raw_input("Enter number of sides: ")
num_sides = int(num_sides_inp)

side_len_inp = raw_input("Enter length of each side: ")
side_len = int(side_len_inp)

for side in range(num_sides):
    bob.forward(side_len)
    bob.left(360.0/num_sides)

stopper = raw_input("Hit <enter> to quit.")

turtle.bye()
