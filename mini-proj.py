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
START_LENGTH = 1


#INITIALIZE LISTS
pos_list = []
stamp_list = []
food_pos = []
food_stamps = []

#set up positions
turtle.register_shape("kitty.gif")
snake = turtle.clone()
snake.shape("kitty.gif")

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
    #move around!!!!!!!!!!!!!!!!

UP_ARROW = "Up"
LEFT_ARROW = "Left"
DOWN_ARROW = "Down"
RIGHT_ARROW = "Right"
TIME_STEP = 100
SPACEBAR = "space"
UP = 0
LEFT = 1
DOWN = 2
RIGHT = 3

turtle.register_shape("devile.gif")
food = turtle.clone()
food.shape("devile.gif")



direction = UP

def up():
    global direction #snake direction is global (same everywhere)
    direction=UP #Change direction to up
     #Update the snake drawing <- remember me later
    print("You pressed the up key!")
    
def left(): 
    global direction 
    direction=LEFT
    print("You pressed the left key!")
    
def down(): 
    global direction 
    direction=DOWN
    print("You pressed the down key!")
    
def right():
    global direction 
    direction=RIGHT 
    print("You pressed the right key!")


turtle.onkeypress(down,DOWN_ARROW)
turtle.onkeypress(left,LEFT_ARROW)
turtle.onkeypress(right,RIGHT_ARROW)
turtle.onkeypress(up, UP_ARROW) 
turtle.listen()

def make_food():
    #The screen positions go from -SIZE/2 to +SIZE/2
    #But we need to make food pieces only appear on game squares
    #So we cut up the game board into multiples of SQUARE_SIZE.
    min_x=-int(SIZE_X/2/SQUARE_SIZE)+1
    max_x=int(SIZE_X/2/SQUARE_SIZE)-1
    min_y=-int(SIZE_Y/2/SQUARE_SIZE)+1
    max_y=int(SIZE_Y/2/SQUARE_SIZE)-1
    #Pick a position that is a random multiple of SQUARE_SIZE
    food_x = random.randint(min_x,max_x)*SQUARE_SIZE
    food_y = random.randint(min_y,max_y)*SQUARE_SIZE
    #Make the food turtle go to the randomly-generated position
    random_pos = (food_x, food_y)
    # 1. Make the food turtle go to the random position
    food.goto(food_x, food_y)
    # 2. Add the position to pos_list
    food_pos.append(random_pos)
    # 3. Stamp the food, and add the stamp ID to food_stamps
    stamp_id=food.stamp()
    food_stamps.append(stamp_id)


def move_snake():
    my_pos = snake.pos()
    x_pos = my_pos[0]
    y_pos = my_pos[1]

    if direction==RIGHT:
        snake.goto(x_pos + SQUARE_SIZE, y_pos)
        print("You moved right!")

    elif direction==LEFT:
        snake.goto(x_pos - SQUARE_SIZE, y_pos)
        print("You moved left!")

    elif direction==UP:
        snake.goto(x_pos,y_pos + SQUARE_SIZE)
        print("You moved up!")

    elif direction==DOWN:
        snake.goto(x_pos,y_pos - SQUARE_SIZE)
        print("You moved down!")


    my_pos=snake.pos()
    pos_list.append(my_pos)
    new_stamp = snake.stamp()
    stamp_list.append(new_stamp)


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
        
        # You should write code to check for the left, top, and bottom edg
    global food_stamps, food_pos
    #If snake is on top of food item
    if snake.pos() in food_pos:
        food_ind=food_pos.index(snake.pos()) 
        print(len(food_stamps))
        print(food_ind)
        food.clearstamp(food_stamps[food_ind]) #Remove eaten food stamp
        food_pos.pop(food_ind) #Remove eaten food position
        food_stamps.pop(food_ind) #Remove eaten food stamp
        print("You have eaten the food!")
        make_food()
    else:
        old_stamp = stamp_list.pop(0)
        snake.clearstamp(old_stamp)
        pos_list.pop(0)

    if snake.pos() in pos_list[:-1]:
        print(snake.pos())
        print(pos_list)
        print("Your snake is very depressed")
        print("GAME OVER")
        quit()
        
    turtle.ontimer(move_snake,TIME_STEP)
    
make_food()
move_snake()








######## SPECIAL PLACE - Remember it for Part 5
