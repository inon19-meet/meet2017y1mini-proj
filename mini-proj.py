import turtle

import random 

turtle.tracer(1,0) #help python move more smoothly

SIZE_X = 800

SIZE_Y = 500

turtle.setup(SIZE_X, SIZE_Y)

turtle.penup()

SQUARE_SIZE = 20
START_LENGTH = 7

#INITIALIZE LISTS
pos_list = []
stamp_list = []
food_pos = []
food_stamps = []

#set up positions
snake = turtle.clone()
snake.shape("square")

#hide the turtle object
turtle.hideturtle()

#dtaw the snake at the start of the game
for i in range(START_LENGTH):
    x_pos=snake.pos()[0]
    y_pos=snake.pos()[1]

    #add square size
    x_pos+=SQUARE_SIZE

    #kkk
    my_pos=(x_pos,y_pos)
    snake.goto(x_pos,y_pos)
    pos_list.append(my_pos)
    #save the stamp id
    stamp_list.append(snake.stamp())
    stamp_list.append(my_pos)
    #move around!!!!!!!!!!!!!!!!

UP_ARROW = "Up"
LEFT_ARROW = "Left"
DOWN_ARROW = "Down"
RIGHT_ARROW = "Right"
TIME_STEP = 100
SPACEBAR = "space"
up = 0
left = 1
down = 2
right = 3

direction = up

def up():
    global direction #snake direction is global (same everywhere)
    direction=up #Change direction to up
    move_snake() #Update the snake drawing <- remember me later
    print("You pressed the up key!")
    
def left(): 
    global direction 
    direction=left 
    move_snake() 
    print("You pressed the left key!")
    
def down(): 
    global direction 
    direction=down 
    move_snake() 
    print("You pressed the down key!")
    
def right():
    global direction 
    direction=right
    move_snake() 
    print("You pressed the right key!")
    
turtle.onkeypress(down,DOWN_ARROW)
turtle.onkeypress(left,LEFT_ARROW)
turtle.onkeypress(right,RIGHT_ARROW)
turtle.onkeypress(up, UP_ARROW) 
turtle.listen()
def move_snake():
    my_pos = snake.pos()
    x_pos = my_pos[0]
    y_pos = my_pos[1]
if direction==right:
    snake.goto(x_pos + SQUARE_SIZE, y_pos)
    print("You moved right!")
elif direction==left:
    snake.goto(x_pos - SQUARE_SIZE, y_pos)
    print("You moved left!")
    #4. Write the conditions for UP and DOWN on your own
    ##### YOUR CODE HERE
    #Stamp new element and append new stamp in list
    #Remember: The snake position changed - update my_pos()
    my_pos=snake.pos()
    pos_list.append(my_pos)
    new_stamp = snake.stamp()
    stamp_list.append(new_stamp)
    ######## SPECIAL PLACE - Remember it for Part 5
    #pop zeroth element in pos_list to get rid of last the last
    #piece of the tail
    old_stamp = stamp_list.pop(0)
    snake.clearstamp(old_stamp)
    pos_list.pop(0)
    
    
    





















