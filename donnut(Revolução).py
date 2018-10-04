from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import math
import random
 
 
cores = ( (1,0,0),(1,1,0),(0,1,0),(0,1,1),(0,0,1),(1,0,1),(0.5,1,1),(1,0,0.5) )
 


def donnutRevolucao():
    r = 1.0
    c = 2  
    def s(u,v):
        return ((c + r * math.sin(v)) * math.sin(u), r * math.cos(v), (c + r*math.sin(v)) * math.cos(u))
    
    tet = 0.0
    phi = 0.0
    resolution = math.pi/20
    cor = 0

    while tet <= (math.pi*2):
        glBegin(GL_TRIANGLE_STRIP)
        glColor3f(math.sin(cor),1.0, 1.0)
        cor += resolution
        phi = 0.0
        while phi <= (math.pi*2):
            glVertex3fv(s(tet, phi))
            glVertex3fv(s(tet + resolution, phi))
            phi += resolution
        glVertex3fv(s(tet, 0.0))
        glVertex3fv(s(tet + resolution, 0.0))
        glEnd()
        tet += resolution   
                

def render():
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glRotatef(2,1,3,0)
    donnutRevolucao()
    glutSwapBuffers()
    
def timer(i):
    glutPostRedisplay()
    glutTimerFunc(50,timer,1)
 
# PROGRAMA PRINCIPAL
glutInit(sys.argv)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH | GLUT_MULTISAMPLE)
glutInitWindowSize(800,600)
glutCreateWindow("Donnut")
glutDisplayFunc(render)
glEnable(GL_MULTISAMPLE)
glEnable(GL_DEPTH_TEST)
glClearColor(0.,0.,0.,1.)
gluPerspective(65,800.0/600.0,0.1,50.0)
glTranslatef(0.0,0.0,-8)
glRotatef(45,1,1,1)
glutTimerFunc(50,timer,1)
glutMainLoop()
