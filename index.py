from graphics import *
import numpy

def main():
    xLength = 400
    yLength = 400
    xOrigin = xLength / 2
    yOrigin = yLength / 2
    win = GraphWin("Cube", 400, 400, autoflush=False)
    vertices = [[xOrigin + 20, yOrigin - 20], [xOrigin - 20, yOrigin - 20], [xOrigin - 20, yOrigin + 20], [xOrigin + 20, yOrigin + 20]]
    edges = [(0,1), (1,2), (2,3), (0,3)] 

    lines = []
    for edge in edges:
        line = Line(Point(*vertices[edge[0]]), Point(*vertices[edge[1]])) #unpack with '*'
        line.draw(win)
        lines.append(line)

    def rotateVertices(angle):
        for i in range(len(vertices)):
            # # SAME AS MATRIX VERSION BELOW
            # lastx = vertices[i][0] - xOrigin
            # lasty = vertices[i][1] - yOrigin

            # # Apply the rotation transformation
            # rotatedX = lastx * numpy.cos(angle) - lasty * numpy.sin(angle)
            # rotatedY = lastx * numpy.sin(angle) + lasty * numpy.cos(angle)

            # # Update the vertex positions, translating back relative to the origin
            # vertices[i][0] = rotatedX + xOrigin
            # vertices[i][1] = rotatedY + yOrigin

            lastx = vertices[i][0]
            lasty = vertices[i][1]
            v = [lastx, lasty, 1]

            translateFromOriginM = [
                [1, 0, 0],
                [0, 1, 0],
                [-xOrigin, -yOrigin, 1]
            ]

            rotationMatrix = [
                [numpy.cos(angle), -numpy.sin(angle), 0],
                [numpy.sin(angle), numpy.cos(angle), 0],
                [0, 0, 1] 
            ]

            translateToOriginM = [
                [1, 0, 0],
                [0, 1, 0],
                [xOrigin, yOrigin, 1]
            ]
            
            FromOriginv = numpy.dot(v, translateFromOriginM)
            rotateV = numpy.dot(FromOriginv, rotationMatrix)
            finalV = numpy.dot(rotateV, translateToOriginM)

            vertices[i][0] = finalV[0]
            vertices[i][1] = finalV[1]

    # angle = numpy.pi / 3
    # rotateVertices(angle)
    angle = 0
    while True:
        angle += numpy.pi / 6
        for line in lines:
            line.undraw()
        lines = []
        rotateVertices(angle)
        for edge in edges:
            line = Line(Point(*vertices[edge[0]]), Point(*vertices[edge[1]])) #unpack with '*'
            line.draw(win)
            lines.append(line)

        if win.checkMouse():
            break
        win.update()
        time.sleep(0.2)
main()