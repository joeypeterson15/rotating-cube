from graphics import *
import numpy

def main():
    xLength = 400
    yLength = 400
    xOrigin = xLength / 2
    yOrigin = yLength / 2
    win = GraphWin("Cube", 400, 400)
    vertices = [(xOrigin + 20, yOrigin - 20), (xOrigin - 20, yOrigin - 20), (xOrigin - 20, yOrigin + 20), (xOrigin + 20, yOrigin + 20)]
    edges = [(0,1), (1,2), (2,3), (0,3)]

    lines = []
    for edge in edges:
        line = Line(Point(*vertices[edge[0]]), Point(*vertices[edge[1]])) #unpack the tuple with '*'
        line.draw(win)
        lines.append(line)

    if win.getMouse(): # pause for click in window
        win.close()

    def rotateLines(lines, angle):
        rotationMatrix = [
            [numpy.cos(angle), -numpy.sin(angle)],
            [numpy.sin(angle), numpy.cos(angle)] 
        ]
        

    angle = 0
    while True:
        angle += 0.1
        # undraw lines
        for line in lines:
            line.undraw()
            
        rotateLines(lines, angle)

main()