import random

r = 0
last_way_y = 0
last_way_x = 0
MINUTES = 10
my_way_y = 0
my_way_x = 0
while r == 0:
    temp = 0

    while temp <= MINUTES:
        rand = random.randint(0, 3)

        if rand == 0:
            my_way_y = 1
            print("N")

        elif rand == 1:
            my_way_y = -1
            print("S")

        elif rand == 2:
            my_way_x = -1
            print("W")

        elif rand == 3:
            my_way_x = 1
            print("E")

        last_way_y += my_way_y

        last_way_x += my_way_x

        temp += 1
    if last_way_y == 0 and last_way_x == 0:
        print("Congratulations! You finished your way to work!")
        r = 1
    else:
        print("-----------Next try------------")
