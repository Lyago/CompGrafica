from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import time
import math
import random
 
 
cores = ( (1,0,0),(1,1,0),(0,1,0),(0,1,1),(0,0,1),(1,0,1),(0.5,1,1),(1,0,0.5) )

def roda(cx, cy, px, py, a):

  _px = ((px-cx)*math.cos(a)-(py-cy)*math.sin(a))+cx
  _py = ((px-cx)*math.sin(a)+(py-cy)*math.cos(a))+cy
  return [_px, _py, 0]



def foldTetrahedron(edgeLen, height):
	
    apothem = edgeLen * math.sqrt(3)/2
    glColor3fv(cores[1])
    glBegin(GL_POLYGON)
    glVertex3fv((-edgeLen/2, -apothem/2, -height/2))
    glVertex3fv((edgeLen/2, -apothem/2, -height/2))
    glVertex3fv((edgeLen/4, apothem/2, -height/2))
    glEnd()

    glColor3fv(cores[0])
    glBegin(GL_POLYGON)
    rotated = roda(edgeLen/4, apothem/2, edgeLen/2, -apothem/2, math.pi/3)
    rotated[2] = -height/2
    glVertex3fv(rotated)
    glVertex3fv((edgeLen/2, -apothem/2, -height/2))
    glVertex3fv((edgeLen/4, apothem/2, -height/2))
    glEnd()
    
    glColor3fv(cores[2])
    glBegin(GL_POLYGON)
    rotated = roda(edgeLen/4, apothem/2, -edgeLen/2, -apothem/2, -math.pi/3)
    rotated[2] = -height/2
    glVertex3fv(rotated)
    glVertex3fv((-edgeLen/2, -apothem/2, -height/2))
    glVertex3fv((edgeLen/4, apothem/2, -height/2))
    glEnd()
	
    glColor3fv(cores[3])
    glBegin(GL_POLYGON)
    rotated = roda(-edgeLen/2, -apothem/2, edgeLen/2, -apothem/2, -math.pi/3)
    rotated[2] = -height/2
    glVertex3fv(rotated)
    glVertex3fv((-edgeLen/2, -apothem/2, -height/2))
    glVertex3fv((edgeLen/2, -apothem/2, -height/2))
    glEnd()

def piramidePoligono(rBase, nBase ,altura):
    
    glColor3fv(cores[3])     
    glBegin(GL_POLYGON)

#Chamei de resolution pq esse algoritmo tmb pode gerar a aprox. de um cone conforme nBase aumenta    
    resolution = nBase
    height = [0,altura,0]
    radius = rBase

    for vertex in range(0, resolution):     
        glVertex3fv([math.cos(2* math.pi * vertex/resolution * radius), -1 , math.sin(2 * math.pi * vertex/resolution * radius)])

    glEnd()


    glVertex3fv(height)    

    for vertex in range(0, resolution):
        
        glColor3fv(cores[vertex%len(cores)])
        
        glBegin(GL_TRIANGLES)
             
        glVertex3fv([math.cos(2* math.pi * (vertex%(resolution))/resolution * radius), -1 , math.sin(2 * math.pi * (vertex%(resolution))/resolution) * radius])
        glVertex3fv([math.cos(2* math.pi * ((vertex+1)%(resolution))/resolution * radius), -1 , math.sin(2 * math.pi * ((vertex+1)%(resolution))/resolution) * radius])
        glVertex3fv(height)

        glEnd()

                

def render():
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glRotatef(2,3,3,0)
    #piramidePoligono(1, 3, .5)
    foldTetrahedron(3, 0)
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
gluPerspective(60,800.0/600.0,0.1,50.0)
glTranslatef(0.0,0.0,-8)
#glRotatef(45,1,1,1)
glutTimerFunc(50,timer,1)
glutMainLoop()
