import turtle


# class contains information about the turtle (blueprint)
# create multiple instances of the class turtle (instances of the blueprint)


def draw_square(some_turtle) : #some_turtle is the argument that draw_square takes
    for i in range(1,5): 
        some_turtle.forward(100)
        some_turtle.right(90)

def draw_art():
    window = turtle.Screen()
    window.bgcolor("red")
    #create the turtle that draws a square
    brad = turtle.Turtle() #create an instance of the class turtle called brad
    brad.shape("turtle")
    brad.color("blue")
    brad.speed(0.1)

    charlesschwein = turtle.Turtle()
    charlesschwein.shape("turtle")
    charlesschwein.color("green")
    charlesschwein.speed(0.1)


    for i in range(1,73):
        draw_square(brad)
        charlesschwein.right(10)
        draw_square(charlesschwein)
        brad.right(10)
 

   # angie = turtle.Turtle()
 #   angie.circle(100)
 #   angie.shape("turtle")
 #   angie.color("yellow")

    window.exitonclick()
     


draw_art()

