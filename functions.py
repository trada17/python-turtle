import turtle
# creating canvas
turtle.Screen().bgcolor("Cyan")

sc = turtle.Screen()
sc.setup(400, 300)

turtle.title("Welcome to Turtle Window")

#turtle object creation
board = turtle.Turtle()

#creating a square
for i in range(5):
    board.forward(100)
    board.left(90)
    i = i+1
sc.mainloop()
