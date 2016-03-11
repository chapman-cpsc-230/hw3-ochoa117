"""
File: <turtlestar.py>

Copyright (c) 2016 <William Ochoa>

License MIT

<This code produces a star with five points. Add 360 to the value of n every time you add 2 to num_sides to get stars with more points (that was the best I could do)>
"""

import turtle
t = turtle.Pen()

num_sides_inp = raw_input("Enter odd number of sides (at least 5): ")
num_sides = int(num_sides_inp)

side_len_inp = raw_input("Enter length of each side: ")
side_len = int(side_len_inp)

n = 720.0
for i in range(num_sides):
    t.forward(side_len)
    t.left(n/num_sides)

stopper = raw_input("Hit <enter> to quit.")

turtle.bye()
