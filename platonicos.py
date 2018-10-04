from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import math
import random

phi = (1 + 5 ** 0.5) / 2

vertices = (
 
    )
 

 
faces = (

    )
 
cores = ( (1,0,0),(1,1,0),(0,1,0),(0,1,1),(0,0,1),(1,0,1),(0.5,1,1),(1,0,0.5),(0,1,1),(0,0,1),(1,0,1),(0.5,1,1),(1,0,0.5),(1,0,0),(1,1,0),(0,1,0),(0,1,1),(0,0,1),(1,0,1),(1,0,1) )
 
def tetraedro():
    glBegin(GL_LINES)
    i = 0
    for face in faces:
        glColor3fv(cores[i])
        for vertex in face:
            glColor3fv(cores[vertex])
            glVertex3fv(vertices[vertex])
        i = i+1
    glEnd()
 
#    glColor3fv((0,0.5,0))
#    glBegin(GL_LINES)
#    for linha in linhas:
#        for vertice in linha:
#            glVertex3fv(vertices[vertice])
#    glEnd()

    
                

def render():
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glRotatef(2,1,3,0)
    tetraedro()
    glutSwapBuffers()
    
def timer(i):
    glutPostRedisplay()
    glutTimerFunc(50,timer,1)
 
# PROGRAMA PRINCIPAL
glutInit(sys.argv)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH | GLUT_MULTISAMPLE)
glutInitWindowSize(800,600)
glutCreateWindow("TETRAEDRO")
glutDisplayFunc(render)
glEnable(GL_MULTISAMPLE)
glEnable(GL_DEPTH_TEST)
glClearColor(0.,0.,0.,1.)
gluPerspective(65,800.0/600.0,0.1,50.0)
glTranslatef(0.0,0.0,-8)
glRotatef(45,1,1,1)
glutTimerFunc(50,timer,1)
glutMainLoop()
