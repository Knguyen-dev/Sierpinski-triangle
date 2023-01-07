import turtle
# Sets direction and cartesian positions for next turtles
def style_turtle(t, x, y):
  t.hideturtle()
  t.setheading(60)
  t.penup()
  t.setpos(x,y)
  t.pendown()
  t.speed(0)
  t.color('white')
  return t

def drawMain(t, l):
  t.left(60)
  t.forward(l)
  t.right(120)
  t.forward(l)
  t.right(120)
  t.forward(l)

def drawInverted(t, l, colorIndex):
  # given a triangle any triangle
  # draw an inverted triangle within it
  # to get the inverted triangle within others you must use recursion
  # I idea I have is to create 3 turtles at 3 key points to continue the drawing. Since recursion we should set a limit
  # Until the recursion stack stops, this base case will be when the turtles will stop
  arr = ['blue','red','yellow']
  if (l <= 5):
    return
  else:
    # set turtle directions in the same directions
    # Set the positions of the next turtles at key places
    # Place bottom left turtle here
    a = turtle.Turtle()
    a = style_turtle(a, t.xcor(), t.ycor())
    t.forward(l)

    if (colorIndex > len(arr) - 1):
      colorIndex = 0
    t.color(arr[colorIndex])


    #Place top turtle here
    b = turtle.Turtle()
    b = style_turtle(b, t.xcor(), t.ycor())
    t.right(60)
    t.forward(l)
    t.right(120)
    t.forward(l)
    
    #Place bottom right turtle
    c = turtle.Turtle()
    c = style_turtle(c, t.xcor(), t.ycor())
    t.right(120)
    t.forward(l)
    
    # Probably have to finished the drawing, and then multiplication can begin; though test first
    # Hides current turtle and gives show to the next turtles
    # Start stack for bottom left
    print("Drawing Bottom left")
    drawInverted(a, l/2, colorIndex + 1)

    print("Drawing top")
    drawInverted(b, l/2, colorIndex + 1)
    print("Drawing bottom right")
    drawInverted(c, l/2, colorIndex + 1)
    return

def main():
  # Turtle setup  
  wn = turtle.Screen()
  wn.bgcolor('black')
  length = 700
  wn.setup(length * 2, length * 1.5)
  # Sets the speed
  wn.delay(0)
  alyx = turtle.Turtle()
  alyx.color('white')
  alyx.hideturtle
  # Turtle positioning
  alyx.penup()
  alyx.setpos(-length / 2, -length / 2.5)
  alyx.pendown()

  # Draws the main triangle and positions turtle
  drawMain(alyx, length)
  alyx.setheading(60)
  
  drawInverted(alyx, length/2, 0)
  wn.exitonclick()
main()