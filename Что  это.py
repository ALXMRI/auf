import turtle


a = []
for i in range(0,10) :
    a.append(int(input()))
print(*a)
# t = turtle.Turtle()
turtle.speed(0)
for i in a:
    turtle.circle(i)
turtle.exitonclick()

