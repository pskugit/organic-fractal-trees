from tkinter import *
import random
import math

#init
minlen = 5
stemsize = 100
width = 900
height = 600

def branch(len, level, x, y, angle):
    if (len > minlen):
        rlength = random.random() *len + len / 2
        rangle = random.random() * 2 * math.pi * 0.03 + 2 * math.pi * 0.03
        ramount = random.random() * 100
        rside = random.random() * 100
        if (rside > 50):
            rside = 1
        else:
            rside = -1

        scale = 0.78

        thickness = 2*len/(level+12)

        x_to = x + math.sin(angle) * rlength
        y_to = y + math.cos(angle) * rlength

        rgb = (30, 210*(minlen/len), 80)

        # ANTI ALIASING
        if (thickness > 1):
            l = c.create_line(x, y, x_to, y_to, width=thickness+0.5, fill=_from_rgb(tuple((int(v + 30) for v in rgb))))

        #LINIE
        l = c.create_line(x, y, x_to, y_to, width=thickness, fill=_from_rgb(tuple((int(v) for v in rgb))))



        #AUFRUF1
        branch(len*scale, level+1, x_to, y_to, angle + rangle)
        #AUFRUF2
        branch(len * scale, level + 1, x_to, y_to, angle - rangle)
        #AUFRUF3
        if (ramount > 60):
            branch(len * scale, level + 1, x_to, y_to, angle + rside*2.5*rangle)

def _from_rgb(rgb):
    return "#%02x%02x%02x" % rgb

root = Tk()
root.geometry('900x600')

c = Canvas(root, width=width, height=height, bg="white")

branch(stemsize, 1, width/2 , height, math.pi)







c.pack()
root.mainloop()


