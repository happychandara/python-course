# Import
import turtle as t

# Settings*
t.shape('turtle')
t.speed(0)

def spiral():
    colors = ['red', 'orange', 'yellow', 'green', 'cyan', 'blue', 'purple', 'pink']
    t.bgcolor('black')
    t.pensize(2)

    for k in range(1,1001):
        t.color(colors[k % 8])
        t.forward(k)
        t.left(46)

spiral()

t.hideturtle()
t.done()