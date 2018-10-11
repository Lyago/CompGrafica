from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import math
import random

radius = 1
phi = (math.sqrt(5) + 1) / 2
size = math.sqrt( radius / ( 1 + phi * phi ) )

vertices = (
    ( phi * size,        size,         0.0), #0
    ( phi * size,       -size,         0.0), #1
    (-phi * size,       -size,         0.0), #2
    (-phi * size,        size,         0.0), #3
    (      -size,         0.0,  phi * size), #4
    (       size,         0.0,  phi * size), #5
    (       size,         0.0, -phi * size), #6
    (      -size,         0.0, -phi * size), #7
    (        0.0,  phi * size,        size), #8
    (        0.0,  phi * size,       -size), #9
    (        0.0, -phi * size,       -size), #10
    (        0.0, -phi * size,        size), #11
    )
 
 
faces = (
    [  5,  4, 11,],
    [  5, 11,  1,],
    [  5,  1,  0,],
    [  0,  8,  5,],
    [  5,  8,  4,],
    [  6,  7,  9,],
    [  9,  7,  3,],
    [  3,  7,  2,],
    [  2,  7, 10,],
    [ 10,  7,  6,],
    [  9,  3,  8,],
    [  9,  8,  0,],
    [  9,  0,  6,],
    [  6,  0,  1,],
    [  6,  1, 10,],
    [ 10,  1, 11,],
    [ 10, 11,  2,],
    [  2, 11,  4,],
    [  2,  4,  3,],
    [  3,  4,  8,]
    )


cores = ( (1,0,0),(1,1,0),(0,1,0),(0,1,1),(0,0,1),(1,0,1),(0.5,1,1),(1,0,0.5),(0,1,1),(0,0,1),(1,0,1),(0.5,1,1),(1,0,0.5),(1,0,0),(1,1,0),(0,1,0),(0,1,1),(0,0,1),(1,0,1),(1,0,1) )
 
def icosaedro():
    glBegin(GL_TRIANGLE_STRIP)

    for face in faces:
        for vertex in face:
            glColor3fv(cores[vertex])
            glVertex3fv(vertices[vertex])

    glEnd()

    
                

def render():
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glRotatef(2,1,3,0)
    icosaedro()
    glutSwapBuffers()
    
def timer(i):
    glutPostRedisplay()
    glutTimerFunc(50,timer,1)
 
# PROGRAMA PRINCIPAL
glutInit(sys.argv)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH | GLUT_MULTISAMPLE)
glutInitWindowSize(800,600)
glutCreateWindow("ICOSAEDRO")
glutDisplayFunc(render)
glEnable(GL_MULTISAMPLE)
glEnable(GL_DEPTH_TEST)
glClearColor(0.,0.,0.,1.)
gluPerspective(65,800.0/600.0,0.1,50.0)
glTranslatef(0.0,0.0,-8)
glRotatef(45,1,1,1)
glutTimerFunc(50,timer,1)
glutMainLoop()
