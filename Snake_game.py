from tkinter import *
import random

#We are going to declare a constant variable and values that we are going to use
#if we want we can also change the value for this constant values
Gamebox_width = 500            #width of canvas box
Gamebox_height = 500            #height of canvas box
Game_speed = 110                        #speeed for snake
space_size = 50                   #how large the item for snake and food
body_parts = 3                        # body parts for snake when we begin
snake_color = "green"                 #snake color
food_color =  "red"             #food color
background_color="black"        #canvas box background color

class snake():
# creating a snake
    def __init__(self):
        self.body_size = body_parts     #body parts value self.body_size la store panrom
        self.coordinates = []   # empty list  ha erkum we are going to append
        self.square=[]          # empty list  ha erkum we are going to append

        #using for loop we are going to append the coordinates value of x,y
        for i in range(0,body_parts):
            self.coordinates.append([0,0])      #coordinates x,y value append panrom
        #print(self.coordinates) #output is  [[0, 0], [0, 0], [0, 0]]
        for x,y in self.coordinates:
            squares=canvas.create_rectangle(x,y,x+space_size,y+space_size,fill=snake_color,tag="snake")
            self.square.append(squares) #creating canvas rectangle in squares la athu append panrom self.square la



class Food():
    def __init__(self):
        #It will create a food at random place when we run
        x=random.randint(0, (Gamebox_width // space_size)-1) * space_size #when we multiply with space_size
                                                                       #It will convert into 'x' pixels
        y=random.randint(0, (Gamebox_height // space_size)-1) * space_size #when we multiply with space_size
                                                                        # It will convert into 'y' pixels

        self.coordinates=[x,y] #x,y oda coordinates than list la vekrom
        canvas.create_oval(x, y, x + space_size , y + space_size , fill=food_color ,tag="food")




def next_turn(snake,food):
    x,y= snake.coordinates[0]

    if direction=="up":
        y = y - space_size
    elif direction == "down":
        y = y + space_size
    elif direction == "left":
        x = x-space_size
    elif direction == "right":
        x = x + space_size

    snake.coordinates.insert(0,(x,y))
    squares = canvas.create_rectangle(x,y, x+space_size , y + space_size , fill=snake_color)
    snake.square.insert(0,squares)
    if x==food.coordinates[0] and y == food.coordinates[1]:
        global score

        score = score + 1

        score_label.config(text="Score : {}".format(score))

        canvas.delete("food")#->enga potuerka food vanthu namba tag = food nu mention pani erkom
        #delete panitu new food object create panrom
        food = Food()
    else:
        # delete last position of snake using del command
        del snake.coordinates[-1]
        canvas.delete(snake.square[-1])
        del snake.square[-1]
        # up to this deleting the last position
    #calling check_collection is checking
    if collision(snake):
        game_over()
    else:
         window.after(Game_speed,next_turn,snake,food)#after syntax-> after(event,function)->event is game_speed,
                                                 # function we want to call new turn function every game speed and
                                                 # we are passing argument food and snake

def change_direction(new_direction):
    global direction

    if new_direction == "left":
        if direction != "right":
            direction = new_direction
    elif new_direction == "right":
        if direction != "left":
            direction = new_direction
    elif new_direction == "up":
        if direction != "down":
            direction = new_direction
    elif new_direction == "down":
        if direction != "up":
            direction = new_direction

def collision(snake):#meaning ->crash
    x,y = snake.coordinates[0]

    if x < 0 or x >= Gamebox_width:
        return True
    elif y < 0 or y >= Gamebox_height:
        return True

    for body_parts in snake.coordinates[1:]:
        if x == body_parts[0] and y == body_parts[1]:
            return True

    return False


def game_over():
    canvas.delete(ALL)
    canvas.create_text(canvas.winfo_width()/2,canvas.winfo_height()/2,
                       font=("Arial black",50),text="Game Over",fill="red",tag="gameover")


window=Tk()

window.title("Snake Game")
window.resizable(False,False)#we cannot resize our window

score = 0 # default value for score
direction = "right" # defaultly it will move left side

# creation score_label to display score
score_label = Label(window,text="score : {}".format(score),font=("Arial black",20),fg="red",
                  bg="black")
score_label.pack()

#creating canvas

canvas=Canvas(window,height=Gamebox_height,width=Gamebox_width,bg=background_color,relief=RAISED,bd=5)
canvas.pack()

window.update()
#This code for put our output window to display in center of our main window
window_height=window.winfo_height()         #Calculating window height
window_width=window.winfo_width()           #calculation window width
screen_height=window.winfo_screenheight()   #calculating our scrren height
screen_width=window.winfo_screenwidth()     #calculating our screen width

x=int((screen_width/2)-(window_width/2))    # x axis is width
y=int((screen_height/2)-(window_height/2))  # y axis is height

window.geometry("{}x{}+{}+{}".format(window_width,window_height,x,y))
#creating left right top down button
window.bind("<Left>",lambda x: change_direction("left"))
window.bind("<Right>",lambda x: change_direction("right"))
window.bind("<Up>",lambda x: change_direction("up"))
window.bind("<Down>",lambda x: change_direction("down"))

snake=snake()#creating object for class snake
food=Food()#creating object for class food
#calling next function
next_turn(snake,food)
window.mainloop()