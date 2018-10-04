from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import math
import random
 

def esferaRevolucao(radius, resolution):
    r = radius 
    def s(u,v):
        return ((r * math.cos(u)) * math.cos(v), r * math.sin(u), (r*math.cos(u)) * math.sin(v))
    
    tet = -math.pi/2
    phi = 0.0

#incremento eh pi dividido por uma resolucao. A resolucao determina o numero de "gomos" que serao renderizados na esfera e a discretizacao dos       triangulos(do Triangle Strip) que compoem esses gomos.
    inc = math.pi/resolution

    cor = 0
    while tet < (math.pi/2):
        glBegin(GL_TRIANGLE_STRIP)
        
        phi = 0
        #while ate 2pi + o incremento para completar a esfera no final
        while phi < (math.pi*2 + inc):
            glColor3f(math.cos(cor),math.sin(cor), 1.0)
            cor += math.pi/resolution
            glVertex3fv(s(tet, phi))
            glVertex3fv(s(tet + inc, phi))
            phi += inc
        glEnd()
        tet += inc
        

def render():
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glRotatef(2,1,3,0)
    esferaRevolucao(2, 20)
    glutSwapBuffers()
    
def timer(i):
    glutPostRedisplay()
    glutTimerFunc(50,timer,1)
 
# PROGRAMA PRINCIPAL
glutInit(sys.argv)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH | GLUT_MULTISAMPLE)
glutInitWindowSize(800,600)
glutCreateWindow("ESFERA")
glutDisplayFunc(render)
glEnable(GL_MULTISAMPLE)
glEnable(GL_DEPTH_TEST)
glClearColor(0.,0.,0.,1.)
gluPerspective(65,800.0/600.0,0.1,50.0)
glTranslatef(0.0,0.0,-8)
glRotatef(45,1,1,1)
glutTimerFunc(50,timer,1)
glutMainLoop()
