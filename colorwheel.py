import turtle

# this in a pratical trial on using turtle to create
# something colorful

def colorWheel():
    def drawOuterCircle(radius):
        turtle.penup()
        turtle.setpos(0,-radius)
        turtle.color("black")
        turtle.pendown()
        turtle.begin_fill()
        turtle.circle(radius)
        turtle.end_fill()
        return

    def drawInnerCircle(radius):
        turtle.penup()
        turtle.setpos(0,-radius)
        turtle.color("white")
        turtle.pendown()
        turtle.begin_fill()
        turtle.circle(radius)
        turtle.end_fill()
        turtle.color('black')
        turtle.width(2)
        turtle.circle(radius)
        return

    def drawRing(colorList, radius):
        angle= 360/len(colorList)
        turtle.penup()
        turtle.setpos(0, 0)
        xpos=turtle.xcor()
        ypos=turtle.ycor()

        for color in colorList:
            turtle.pendown()
            turtle.color(color)
            turtle.begin_fill()
            turtle.pencolor('black')
            turtle.forward(radius)
            turtle.left(90)
            turtle.circle(radius, angle)
            turtle.left(90)
            turtle.pencolor('black')
            turtle.forward(radius)
            turtle.end_fill()
            turtle.color('black')
            turtle.width(2)
            turtle.left(180-angle)
            turtle.left(angle)
        return


    darkList = ["#880000",\
                "#884400",\
                "#888800",\
                "#008800",\
                "#008888",\
                "#000088",\
                "#440088",\
                "#880088"]
    mediumList=["#FF0000",\
                "#FF8800",\
                "#FFFF00",\
                "#00FF00",\
                "#00FFFF",\
                "#0000FF",\
                "#8800FF",\
                "#FF00FF"]
    lightList = ["#FF8888",\
                 "#FFCC88",\
                 "#FFFF88",\
                 "#88FF88",\
                 "#88FFFF",\
                 "#8888FF",\
                 "#CC88FF",\
                 "#FF88FF"]
    turtle.hideturtle()
    turtle.speed(0)
    drawOuterCircle(250)
    drawRing(darkList, 200)
    drawRing(mediumList, 150)
    drawRing(lightList, 100)
    drawInnerCircle(50)
    turtle.exitonclick()


colorWheel()
