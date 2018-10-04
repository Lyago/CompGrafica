from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import math
import random
 
	
def funcaoMalha(resolution, minX, maxX, minY, maxY):

    def MathFunctionXYParaboloid(x, y):
        return 0.1*(-pow(x, 2) + pow(y, 2))    
    
    def FunctionPlaneVertexAt(x, y, resolution, minX, maxX, minY, maxY):
        glVertex3f(1.0*x / resolution, MathFunctionXYParaboloid( minX + (maxX - minX) * x / resolution, minY + (maxY - minY) * y / resolution), 1.0*y / resolution)    

    

    for y in range(0, resolution):
        glBegin(GL_TRIANGLE_STRIP)
        FunctionPlaneVertexAt(0 , y , resolution, minX, maxX, minY, maxY)
        FunctionPlaneVertexAt(0 , y+1, resolution, minX, maxX, minY, maxY)
        for x in range(0, resolution):
            glColor3f(math.cos(x),0.1*math.sin(x),math.cos(y))
            
            FunctionPlaneVertexAt(x+1, y  , resolution, minX, maxX, minY, maxY)
            FunctionPlaneVertexAt(x+1, y+1, resolution, minX, maxX, minY, maxY)
            
        glEnd()    
                

def abacaxi():
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glRotatef(1,1,3,0)
    funcaoMalha(50, -2.0, 2.0, -2.0, 2.0)
    glutSwapBuffers()
    
def timer(i):
    glutPostRedisplay()
    glutTimerFunc(50,timer,1)
 
# PROGRAMA PRINCIPAL
glutInit(sys.argv)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH | GLUT_MULTISAMPLE)
glutInitWindowSize(800,600)
glutCreateWindow("SELA")
glutDisplayFunc(abacaxi)
glEnable(GL_MULTISAMPLE)
glEnable(GL_DEPTH_TEST)
glClearColor(0.,0.,0.,1.)
gluPerspective(40,800.0/600.0,0.1,50.0)
glTranslatef(0.0,0.0,-4)
glRotatef(45,1,1,1)
glutTimerFunc(50,timer,1)
glutMainLoop()
