from tkinter import *
import random
import math

#Initialization parameters
MIN_LEN = 5
STEM_SIZE = 100
WIN_WIDTH = 900
WIN_HEIGHT = 600

def branch(len, level, x, y, angle):
    '''
    Generates and draws a new branch to the current tree.
    Is calles recursively to build the full tree.

    :param len: int
        specifies the length of the branch
    :param level: int
        keeps track of the level of the branch within the tree
    :param x: int
        spawn position x
    :param y: int
        spawn position y
    :param angle:
        angle of the branch relative to the tree
    '''

    #recursion termination when branches get too small
    if (len > MIN_LEN):
        #GET BRACH PROPERTIES
        #length
        rlength = random.random() *len + len / 2
        #angle
        rangle = random.random() * 2 * math.pi * 0.03 + 2 * math.pi * 0.03
        #thickness
        thickness = 2*len/(level+12)
        #color (based on length)
        rgb = (30, 210 * (MIN_LEN / len), 80)
        #destination point
        x_to = x + math.sin(angle) * rlength
        y_to = y + math.cos(angle) * rlength

        #this block defines if three instead of two branches will be created and on which side the third branch will be attached
        ramount = random.random() * 100
        rside = random.random() * 100
        if (rside > 50):
            rside = 1
        else:
            rside = -1

        #DRAWING THE BRANCH
        # additional line for anti aliasing
        if (thickness > 1):
            l = c.create_line(x, y, x_to, y_to, width=thickness+0.5, fill=_from_rgb(tuple((int(v + 30) for v in rgb))))
        # main line
        l = c.create_line(x, y, x_to, y_to, width=thickness, fill=_from_rgb(tuple((int(v) for v in rgb))))

        # RECURSION
        # scaling factor for the next level of branches
        scale = 0.78
        # recursive call 1 (positive angle)
        branch(len*scale, level+1, x_to, y_to, angle + rangle)
        # recursive call 2 (negative angle)
        branch(len * scale, level + 1, x_to, y_to, angle - rangle)
        # recursive call 3 (random angle)
        if (ramount > 60):
            branch(len * scale, level + 1, x_to, y_to, angle + rside*2.5*rangle)

def _from_rgb(rgb):
    return "#%02x%02x%02x" % rgb

if __name__ == '__main__':
    root = Tk()
    root.geometry('%dx%d'%(WIN_WIDTH,WIN_HEIGHT))
    c = Canvas(root, width=WIN_WIDTH, height=WIN_HEIGHT, bg="white")
    branch(STEM_SIZE, 1, WIN_WIDTH / 2, WIN_HEIGHT, math.pi)
    c.pack()
    root.mainloop()
