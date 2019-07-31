import turtle
import random 

turtle.tracer(1,0) 

SIZE_X=800
SIZE_Y=500
turtle.setup(SIZE_X, SIZE_Y) 
                                 
turtle.penup()

SQUARE_SIZE = 20
START_LENGTH = 10
TIME_STEP = 100

pos_list = []
stamp_list = []
food_pos = []
food_stamps = []

snake = turtle.clone()
snake.shape("square")

turtle.hideturtle()

def new_stamp():
    snake_pos = snake.pos() 
    pos_list.append(snake_pos)          
    ID1 = snake.stamp()    
    stamp_list.append(ID1)

for counter in range(START_LENGTH):
    x_pos=snake.pos()[0]
    y_pos=snake.pos()[1]

    x_pos+=SQUARE_SIZE 

    snake.goto(x_pos,y_pos) 
   
    new_stamp()
def remove_tail():
    old_stamp = stamp_list.pop(0) 
    snake.clearstamp(old_stamp) 
    pos_list.pop(0) 

snake.direction = "Up"

UP_EDGE = 250
DOWN_EDGE = -250
RIGHT_EDGE = 400
LEFT_EDGE = -400


def up():
    snake.direction="Up" 
    print("You pressed the up key!")
turtle.onkeypress(up, "Up")

def down():
    snake.direction="Down"
    print("You pressed the down key!")
turtle.onkeypress(down,"Down")



def right():
    snake.direction="Right"
    print("You pressed the right key!")
turtle.onkeypress(right,"Right")

def left():
    snake.direction="left"
    print("You pressed the left key!")
turtle.onkeypress(left,"Left")


turtle.register_shape("trash.gif")
food = turtle.clone()
food.shape("trash.gif")
food_pos = [(100,100), (-100,100), (-100,-100), (100,-100)]
food_stamps = []
for this_food_pos in food_pos :
    food_x=(food.xcor)
    food_y=(food.ycor)
    food.goto(food_x,food_y)



def move_snake():
    my_pos = snake.pos()
    x_pos = my_pos[0]
    y_pos = my_pos[1]

    if snake.direction == "Up":
        snake.goto(x_pos, y_pos + SQUARE_SIZE)
        print("You moved up!")
        
    elif snake.direction=="Down":
        snake.goto(x_pos, y_pos - SQUARE_SIZE)
        print("You moved down!")

    elif snake.direction=="Right":
        snake.goto(x_pos + SQUARE_SIZE, y_pos)
        print("You moved right!")

    elif snake.direction=="left":
        snake.goto(x_pos- SQUARE_SIZE, y_pos)
        print("You moved left!")
        
    new_stamp()

    ######## SPECIAL PLACE - Remember it for Part 5
    remove_tail()

    new_pos = snake.pos()
    new_x_pos = new_pos[0]
    new_y_pos = new_pos[1]

    # The next three lines check if the snake is hitting the 
    # right edge.
    if new_x_pos >= RIGHT_EDGE:
         print("You hit the right edge! Game over!")
         quit()
         
    if new_x_pos<= LEFT_EDGE:
        print("You hit the left edge! Game over!")
        quit()
        
    if new_y_pos >= UP_EDGE:
        print("You hit the left edge! Game over!")
        quit()

    if new_y_pos <= DOWN_EDGE:
        print("You hit the left edge! Game over!")
        quit()

    turtle.ontimer(move_snake,TIME_STEP)

move_snake()    
turtle.listen()
turtle.mainloop()
