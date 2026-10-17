import turtle
turtle.speed(10)

def draw_triagnel(side_length):
    for i in range(3):
        turtle.forward(side_length)
        turtle.left(120)

def draw_square(side_length):
    for i in range(4): 
        turtle.forward(side_length)
        turtle.left(90)


def draw_pattern(shape):
     
     counter = 0
     c = 0
     
     while counter < 90:
        turtle.color(colors[c])
        if shape == "square": 
            draw_square(200)
            r = 4

        elif shape == "triangle":
            draw_triagnel(200)
            r = 6
        
        turtle.right(r)
        counter+= 1
        c+=1
        if c == 3: c = 0
    
   


colors = ["red", "green", "blue"]



while True:
    shape = input("enter shape tringle/square/pattern/quite : ")
    if shape == "triangle":
        draw_triagnel(100)
       
    elif shape == "square": 
        draw_square(100)
   
    elif shape == "pattern": 
        draw_pattern(input("enter shape for pattern: "))
     
    elif shape == "quit": 
        break 
    
 
       
        

