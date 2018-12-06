from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import time
import math
import random

# Some api in the chain is translating the keystrokes to this octal string
# so instead of saying: ESCAPE = 27, we use the following.
ESCAPE = '\033'
# Number of the glut window.
window = 0

# Rotations for cube. 
xrot = 10.0
yrot = 0.0
zrot = 5.0
dx = 5.0
dy = 5.0
dz = 5.0 

slowness = 300
frameCount = 1
 
cores = ( (1,0,0),(1,1,0),(0,1,0),(0,1,1),(0,0,1),(1,0,1),(0.5,1,1),(1,0,0.5) )

def roda(cx, cy, px, py, a):

  _px = ((px-cx)*math.cos(a)-(py-cy)*math.sin(a))+cx
  _py = ((px-cx)*math.sin(a)+(py-cy)*math.cos(a))+cy
  return [_px, _py, 0.0]


def foldTetrahedron(edgeLen, frameCount):
	
    
    apothem = edgeLen * math.sqrt(3.0)/2.0
    finalHeight = edgeLen * math.sqrt(6.0)/3.0
    startHeight = 0.0
    height = finalHeight * frameCount/slowness 
    finalX = 0.0
    finalY = 0.0


    glColor3fv(cores[1])
    glBegin(GL_POLYGON)
    glVertex3fv((-edgeLen/2, -apothem/2, startHeight))
    glVertex3fv((edgeLen/2, -apothem/2, startHeight))
    glVertex3fv((0.0, apothem/2, -startHeight))
    glEnd()
      
    glColor3fv(cores[0])
    glBegin(GL_POLYGON)
    rotated = roda(0.0, apothem/2, edgeLen/2, -apothem/2, math.pi/3)
    startX = rotated[0]
    startY = rotated[1]
    x = frameCount * finalX/slowness
    y = frameCount * finalY/slowness
    rotated = (x,y,height)
    glVertex3fv(rotated)
    glVertex3fv((edgeLen/2, -apothem/2, startHeight))
    glVertex3fv((0.0, apothem/2, startHeight))
    glEnd()
    
    glColor3fv(cores[2])
    glBegin(GL_POLYGON)
    rotated = roda(0.0, apothem/2, -edgeLen/2, -apothem/2, -math.pi/3)
    rotated[2] = height
    glVertex3fv(rotated)
    glVertex3fv((-edgeLen/2, -apothem/2, startHeight))
    glVertex3fv((0.0, apothem/2, startHeight))
    glEnd()
	
    glColor3fv(cores[3])
    glBegin(GL_POLYGON)
    rotated = roda(-edgeLen/2, -apothem/2, edgeLen/2, -apothem/2, -math.pi/3)
    rotated[2] = height
    glVertex3fv(rotated)
    glVertex3fv((-edgeLen/2, -apothem/2, startHeight))
    glVertex3fv((edgeLen/2, -apothem/2, startHeight))
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

                



def InitGL(Width, Height):             
    glClearColor(0.0, 0.0, 0.0, 0.0)    
    glClearDepth(1.0)                  
    glDepthFunc(GL_LESS)               
    glEnable(GL_DEPTH_TEST)            
    glShadeModel(GL_SMOOTH)            
    
    glMatrixMode(GL_PROJECTION)
    gluPerspective(45.0, float(Width)/float(Height), 0.1, 100.0)

    glMatrixMode(GL_MODELVIEW)

def ReSizeGLScene(Width, Height):
    if Height == 0:                        
        Height = 1

    glViewport(0, 0, Width, Height)      
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45.0, float(Width)/float(Height), 0.1, 100.0)
    glMatrixMode(GL_MODELVIEW)

def DrawGLScene():
    global xrot, yrot, zrot, frameCount

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)    
    glLoadIdentity()                   

    glClearColor(0.5,0.5,0.5,1.0)            
    
    glTranslatef(0.0,0.0,-5.0)            

    glRotatef(xrot,10.0,0.0,0.0)          
    glRotatef(yrot,0.0,1.0,0.0)           
    glRotatef(zrot,0.0,0.0,5.0) 
    
    foldTetrahedron(1.0, frameCount)
    if frameCount < slowness:
        frameCount += 1


    #xrot = xrot + 5                # X rotation
    #yrot = yrot + 1.0                 # Y rotation
    #zrot = zrot + 5                 # Z rotation

    glutSwapBuffers()


def keyPressed(tecla, x, y):
    global dx, dy, dz
    if tecla == ESCAPE:
        glutLeaveMainLoop()
    elif tecla == 'x' or tecla == 'X':
        dx = 5.0
        dy = 0
        dz = 0   
    elif tecla == 'y' or tecla == 'Y':
        dx = 0
        dy = 5
        dz = 0   
    elif tecla == 'z' or tecla == 'Z':
        dx = 0
        dy = 0
        dz = 5

def teclaEspecialPressionada(tecla, x, y):
    global xrot, yrot, zrot, dx, dy, dz
    if tecla == GLUT_KEY_LEFT:
        print "ESQUERDA"
        xrot -= dx                # X rotation
        yrot -= dy                 # Y rotation
        zrot -= dz                     
    elif tecla == GLUT_KEY_RIGHT:
        print "DIREITA"
        xrot += dx                # X rotation
        yrot += dy                 # Y rotation
        zrot += dz                     
    elif tecla == GLUT_KEY_UP:
        print "CIMA"
    elif tecla == GLUT_KEY_DOWN:
        print "BAIXO"

def main():
    global window
    glutInit(sys.argv)

    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
    
    # get a 640 x 480 window 
    glutInitWindowSize(640, 480)
    
    # the window starts at the upper left corner of the screen 
    glutInitWindowPosition(0, 0)
    
    window = glutCreateWindow("Textura")

    glutDisplayFunc(DrawGLScene)
    
    # When we are doing nothing, redraw the scene.
    glutIdleFunc(DrawGLScene)
    
    # Register the function called when our window is resized.
    glutReshapeFunc(ReSizeGLScene)
    
    # Register the function called when the keyboard is pressed.  
    glutKeyboardFunc(keyPressed)

    glutSpecialFunc(teclaEspecialPressionada)

    # Initialize our window. 
    InitGL(640, 480)

    # Start Event Processing Engine    
    glutMainLoop()

# Print message to console, and kick off the main to get it rolling.
if __name__ == "__main__":
    print "Hit ESC key to quit."
    main()
