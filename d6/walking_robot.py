def jump():
    print("I'm jumping.")
def front_is_clear():
    print("Front is clear")
def wall_in_front():
    print("Wall im front")
def move():
    print("Move")
def at_goal():
    print("At goal")
def right_is_clear():
    print("Right is clear")
def turn_left():
    print("Turn left") 
def turn_right():
    turn_left()
    turn_left()
    turn_left()



while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()

# What you need to know
# The functions move() and turn_left().
# The conditions front_is_clear() or wall_in_front(), at_goal(), and their negation.
# How to use a while loop and an if statement.
# Your program should also be valid for worlds Hurdles 1 and Hurdles 2.
