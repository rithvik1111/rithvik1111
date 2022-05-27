import turtle
t=turtle.Turtle()
s=turtle.Screen ()

s.bgcolor ("black")
t. speed (0)

color = ('cyan', 'yellow', 'pink', 'red', 'light green', 'blue')

for i in range (120) :
 t.pencolor (color[i%6] )
 t.circle (190-i/2,90)
 t.lt (90)
 t.circle(190-i/3,90)
 t.lt(60)

s.exitonclick()
