import turtle

import random

UP_EDGE = 250
DOWN_EDGE = -250
RIGHT_EDGE = 400
LEFT_EDGE = -400
    
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
     #Update the snake drawing <- remember me later
    print("You pressed the up key!")
    
def left(): 
    global direction 
    direction=left  
    print("You pressed the left key!")
    
def down(): 
    global direction 
    direction=down 
    print("You pressed the down key!")
    
def right():
    global direction 
    direction=right 
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

    elif direction==up:
        snake.goto(x_pos,y_pos + SQUARE_SIZE)
        print("You moved up!")

    elif direction==down:
        snake.goto(x_pos,y_pos - SQUARE_SIZE)
        print("You moved down!")


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

    #Now go add code to the end of your move_snake() function
    #Add new lines to the end of the function
    #Grab position of snake
    new_pos = snake.pos()
    new_x_pos = new_pos[0]
    new_y_pos = new_pos[1]
    # The next three lines check if the snake is hitting the
    # right edge.
    if new_x_pos >= RIGHT_EDGE:
        print("You hit the right edge! Game over!")
        quit()
        #left edge.
    if new_x_pos <= LEFT_EDGE:
        print("You hit the left edge! Game over!")
        quit()
        #down adge
    if new_y_pos <= DOWN_EDGE:
        print("You hit the bottom edge! Game over!")
        quit()
    if new_y_pos >= UP_EDGE:
        print("You hit the top edge! Game over!")
        quit()
        # You should write code to check for the left, top, and bottom edges.
        #####WRITE YOUR CODE HERE
        global food_stamps, food_pos
    #If snake is on top of food item
    if snake.pos() in food_pos:
        food_ind=food_pos.index(snake.pos()) #What does this do?
        food.clearstamp(food_stamps[food_ind]) #Remove eaten food
         #stamp
        food_pos.pop(food_ind) #Remove eaten food position
        food_stamps.pop(food_ind) #Remove eaten food stamp
        print("You have eaten the food!")
        
    turtle.ontimer(move_snake,TIME_STEP)
move_snake()
turtle.register_shape("trash.gif")
food = turtle.clone()
food.shape("trash.gif")
#locations of food
food_pos = [(100,100), (-100,100), (-100,-100), (100,-100)]
food_stamps = []

for this_food_pos in food_pos:
    food.goto(this_food_pos[0],this_food_pos[1])
    food.stamp()
    food_pos=(x_pos,y_pos)
    food.goto(x_pos,y_pos)
    pos_list.append(food_pos)
    #save the stamp id
    stamp_list.append(food.stamp())
    stamp_list.append(food_pos)

######## SPECIAL PLACE - Remember it for Part 5
    
        

    
    





















