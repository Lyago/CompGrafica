from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import math
import random
 
 
cores = ( (1,0,0),(1,1,0),(0,1,0),(0,1,1),(0,0,1),(1,0,1),(0.5,1,1),(1,0,0.5) )

def troncoPiramidePoligono(rBase, rTopo, nBase ,altura):
    #Chamei de resolution pq esse algoritmo tmb pode gerar a aprox. de um cone conforme nBase aumenta    
    resolution = nBase
    height = altura
    radius = rBase
    topRadius = rTopo    

    glBegin(GL_POLYGON)

    for vertex in range(0, resolution):     
        glVertex3fv([math.cos(2* math.pi * vertex/resolution * radius), -1, math.sin(2 * math.pi * vertex/resolution * radius)])

    glEnd()
    
    glBegin(GL_QUADS)
   

    for vertex in range(0, resolution+1):
        glColor3fv(cores[vertex%len(cores)])     
        glVertex3fv([math.cos(2* math.pi * vertex/resolution * radius), -1, math.sin(2 * math.pi * vertex/resolution) * radius])
        glVertex3fv([math.cos(2* math.pi * vertex/resolution * topRadius), height , math.sin(2 * math.pi * vertex/resolution) * topRadius])

    glEnd()

    glBegin(GL_POLYGON)

    for vertex in range(0, resolution):     
        glVertex3fv([math.cos(2* math.pi * vertex/resolution * topRadius), height , math.sin(2 * math.pi * vertex/resolution * topRadius)])

    glEnd()     

def render():
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glRotatef(2,1,3,0)
    troncoPiramidePoligono(2, 1, 5, 1)
    glutSwapBuffers()
    
def timer(i):
    glutPostRedisplay()
    glutTimerFunc(50,timer,1)
 
# PROGRAMA PRINCIPAL
glutInit(sys.argv)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH | GLUT_MULTISAMPLE)
glutInitWindowSize(800,600)
glutCreateWindow("PIRAMIDENBASE")
glutDisplayFunc(render)
glEnable(GL_MULTISAMPLE)
glEnable(GL_DEPTH_TEST)
glClearColor(0.,0.,0.,1.)
gluPerspective(80,800.0/600.0,0.1,50.0)
glTranslatef(0.0,0.0,-8)
glRotatef(45,1,1,1)
glutTimerFunc(50,timer,1)
glutMainLoop()
