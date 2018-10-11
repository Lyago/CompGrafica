from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import math
import random
 
 
cores = ( (1,0,0),(1,1,0),(0,1,0),(0,1,1),(0,0,1),(1,0,1),(0.5,1,1),(1,0,0.5) )
 

#produz um tronco de cone oco (como um abajur) atraves da revolucao da funcao da reta -2x + 2 em um raio base e um raio de topo.
#se o raio do topo for = 0, a funcao produz um cone
def troncoConeRevolucao(baseRadius, resolution, topRadius=0):
    
    def mathFunctionXLine(x):
        return (-2*x + 3)
    
    def s(x,v):
        return (x * math.cos(v), mathFunctionXLine(x), x * math.sin(v))
    
    inc = math.pi/resolution
    cor = 0.0
    phi = 0.0
    x = 0.0

    glBegin(GL_TRIANGLE_STRIP)
    
    phi = 0.0
    while phi <= (math.pi*2 + inc):
        glColor3f(math.cos(cor),math.sin(cor), 1.0)
        cor += inc 
        glVertex3fv(s(x+topRadius, phi))
        glVertex3fv(s(x+baseRadius, phi))
        phi += inc
    glEnd()


def render():
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glRotatef(2,2,3,0)
    troncoConeRevolucao(2, 100, 1)
    #troncoConeRevolucao(2, 100)
    glutSwapBuffers()
    
def timer(i):
    glutPostRedisplay()
    glutTimerFunc(50,timer,1)
 
# PROGRAMA PRINCIPAL
glutInit(sys.argv)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH | GLUT_MULTISAMPLE)
glutInitWindowSize(800,600)
glutCreateWindow("CONE")
glutDisplayFunc(render)
glEnable(GL_MULTISAMPLE)
glEnable(GL_DEPTH_TEST)
glClearColor(0.,0.,0.,1.)
gluPerspective(60,800.0/600.0,0.1,50.0)
glTranslatef(0.0,0.0,-8)
glRotatef(45,1,1,1)
glutTimerFunc(50,timer,1)
glutMainLoop()
