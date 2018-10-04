from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import math
import random
 
 
cores = ( (1,0,0),(0,1,0))

def piramide():
    glBegin(GL_QUADS)
    
    glColor3fv([1,0,0])
    glVertex3fv([-1,-1,1])
    
    glColor3fv([0,1,0])
    glVertex3fv([-1,-1,-1])
    
    glColor3fv([0,0,1])
    glVertex3fv([1,-1,-1])
    
    glColor3fv([1,1,0])
    glVertex3fv([1,-1,1])
    glEnd()

    glBegin(GL_TRIANGLE_FAN)
    
    glColor3fv([1,0,0])
    glVertex3fv([0,1,0])
    
    glColor3fv([0,1,0])
    glVertex3fv([-1,-1,-1])
    
    glColor3fv([0,0,1])
    glVertex3fv([1,-1,-1])
    
    glColor3fv([1,1,0])
    glVertex3fv([1,-1,1])
    
    glColor3fv([1,1,0])
    glVertex3fv([-1,-1,1])
    
    glColor3fv([0,1,1])
    glVertex3fv([-1,-1,-1])
    glEnd()
    
                

def render():
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glRotatef(2,1,3,0)
    piramide()
    glutSwapBuffers()
    
def timer(i):
    glutPostRedisplay()
    glutTimerFunc(50,timer,1)
 
# PROGRAMA PRINCIPAL
glutInit(sys.argv)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH | GLUT_MULTISAMPLE)
glutInitWindowSize(800,600)
glutCreateWindow("PIRAMIDE")
glutDisplayFunc(render)
glEnable(GL_MULTISAMPLE)
glEnable(GL_DEPTH_TEST)
glClearColor(0.,0.,0.,1.)
gluPerspective(40,800.0/600.0,0.1,50.0)
glTranslatef(0.0,0.0,-8)
glRotatef(45,1,1,1)
glutTimerFunc(50,timer,1)
glutMainLoop()
