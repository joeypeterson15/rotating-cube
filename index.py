from graphics import *
import numpy

def main():
    xLength = 400
    yLength = 400
    xCenter = xLength / 2
    yCenter = yLength / 2
    win = GraphWin("Cube", 400, 400, autoflush=False)
    vertices = [[xCenter + 20, yCenter - 20], [xCenter - 20, yCenter - 20], [xCenter - 20, yCenter + 20], [xCenter + 20, yCenter + 20]]
    edges = [(0,1), (1,2), (2,3), (0,3)] 

    lines = []
    for edge in edges:
        line = Line(Point(*vertices[edge[0]]), Point(*vertices[edge[1]])) #unpack with '*'
        line.draw(win)
        lines.append(line)

    def rotateVertices(angle):
        for i in range(len(vertices)):
            # lastx = vertices[i][0] - xOrigin
            # lasty = vertices[i][1] - yOrigin

            # # Apply the rotation transformation
            # rotatedX = lastx * numpy.cos(angle) - lasty * numpy.sin(angle)
            # rotatedY = lastx * numpy.sin(angle) + lasty * numpy.cos(angle)

            # # Update the vertex positions, translating back relative to the origin
            # vertices[i][0] = rotatedX + xOrigin
            # vertices[i][1] = rotatedY + yOrigin

            # SAME AS ABOVE BUT MATRIX VERSION
            lastx = vertices[i][0]
            lasty = vertices[i][1]
            v = [lastx, lasty, 1]

            translateToOriginM = [
                [1, 0, 0],
                [0, 1, 0],
                [-xCenter, -yCenter, 1]
            ]

            rotationM = [
                [numpy.cos(angle), -numpy.sin(angle), 0],
                [numpy.sin(angle), numpy.cos(angle), 0],
                [0, 0, 1] 
            ]

            translateToCenterM = [
                [1, 0, 0],
                [0, 1, 0],
                [xCenter, yCenter, 1]
            ]
            
            originV = numpy.dot(v, translateToOriginM) #translate square to the top left window origin
            rotateV = numpy.dot(originV, rotationM) #apply rotation to square 
            finalV = numpy.dot(rotateV, translateToCenterM) #translate back to center of window

            vertices[i][0] = finalV[0]
            vertices[i][1] = finalV[1]

    angle_offset = numpy.pi / 35
    angle = angle_offset
    running = True
    while running:
        # angle += angle_offset
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
        time.sleep(0.05)
        # win.update()
main()