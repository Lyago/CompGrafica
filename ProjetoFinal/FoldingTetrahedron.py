from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import time
import math
import random

# Some api in the chain is translating the keystrokes to this octal string
# so instead of saying: ESCAPE = 27, we use the following.
ESCAPE = '\033'
STATE = 'ROTATING'
# Number of the glut window.
window = 0

# Rotations. 
xrot = 5.0
yrot = 5.0
zrot = 5.0
dx = 5.0
dy = 5.0
dz = 5.0 

#Folding animation duration in frames
duration = 5000
frameCount = 1
 
cores = ( (.99,0,0),(.99,.99,0),(0,.99,0),(0,.99,.99),(0,0,.99),(1,0,1),(0.5,1,1),(1,0,0.5) )

def roda(cx, cy, px, py, a):

  _px = ((px-cx)*math.cos(a)-(py-cy)*math.sin(a))+cx
  _py = ((px-cx)*math.sin(a)+(py-cy)*math.cos(a))+cy
  return [_px, _py, 0.0]


def foldTetrahedron(edgeLen, frameCount):
	
    
    apothem = edgeLen * math.sqrt(3.0)/2.0
    
    finalHeight = 2.0/3.0 * edgeLen * math.sqrt(6.0)/3.0
    startHeight = -1.0/3.0 * edgeLen * math.sqrt(6.0)/3.0 
    height = finalHeight * frameCount/duration 
    
    vertex1X = -edgeLen/2.0 
    vertex1Y = -apothem/3.0 
    vertex1 = [vertex1X, vertex1Y, startHeight]
    
    vertex2X = edgeLen/2.0 
    vertex2Y = -apothem/3.0
    vertex2 = [vertex2X, vertex2Y, startHeight]
 
    vertex3X = (vertex1X + vertex2X)/2.0
    vertex3Y = 2.0*apothem/3.0
    vertex3 = [vertex3X, vertex3Y, startHeight]

    centerOffsetX = edgeLen
    centerOffsetY = 2.0*apothem/3.0

    
    glColor3fv(cores[1])
    glBegin(GL_POLYGON)
    glVertex3fv((vertex1X, vertex1Y, startHeight))
    glVertex3fv((vertex2X, vertex2Y, startHeight))
    glVertex3fv((vertex3X, vertex3Y, startHeight))
    glEnd()
      
    glColor3fv(cores[0])
    glBegin(GL_POLYGON)
    rotated = roda(vertex3X, vertex3Y, vertex2X, vertex2Y, math.pi/3)
    startX = rotated[0]
    startY = rotated[1]
    x = startX - frameCount * centerOffsetX/duration
    y = startY - frameCount * centerOffsetY/duration
    rotated = (x,y,height)
    glVertex3fv(rotated)
    glVertex3fv((vertex2X, vertex2Y, startHeight))
    glVertex3fv((vertex3X, vertex3Y, startHeight))
    glEnd()
    
    glColor3fv(cores[2])
    glBegin(GL_POLYGON)
    rotated = roda(vertex3X, vertex3Y, vertex1X, vertex1Y, -math.pi/3)
    startX = rotated[0]
    startY = rotated[1]
    x = startX + frameCount * centerOffsetX/duration
    y = startY - frameCount * centerOffsetY/duration
    rotated = (x,y,height)
    glVertex3fv(rotated)
    glVertex3fv((vertex1X, vertex1Y, startHeight))
    glVertex3fv((vertex3X, vertex3Y, startHeight))
    glEnd()
	
    glColor3fv(cores[3])
    glBegin(GL_POLYGON)
    rotated = roda(vertex1X, vertex1Y, vertex2X, vertex2Y, -math.pi/3)
    startX = rotated[0]
    startY = rotated[1]    
    x = startX 
    y = startY + 2.0*frameCount * centerOffsetY/duration
    rotated = (x,y,height)
    glVertex3fv(rotated)
    glVertex3fv((vertex1X, vertex1Y, startHeight))
    glVertex3fv((vertex2X, vertex2Y, startHeight))
    glEnd()


def InitGL(Width, Height):             
    glClearColor(0.0, 0.0, 0.0, 0.0)    
    glClearDepth(1.0)                  
    glDepthFunc(GL_LESS)               
    glEnable(GL_DEPTH_TEST)            
    glShadeModel(GL_SMOOTH)            
    
    glMatrixMode(GL_PROJECTION)
    gluPerspective(45.0, float(Width)/float(Height), 0.1, 100.0)
    glRotatef(-180.0,1.0,.0,0.0)

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

    glRotatef(xrot,1.0,0.0,0.0)          
    glRotatef(yrot,0.0,1.0,0.0)           
    glRotatef(zrot,0.0,0.0,1.0) 
    
    foldTetrahedron(2.0, frameCount)
    if frameCount < duration:
        frameCount += 1

    if STATE == 'ROTATING':
        #xrot = xrot - .1              # X rotation
        #yrot = yrot + .1                 # Y rotation
        zrot = zrot + .1                 # Z rotation

    glutSwapBuffers()


def keyPressed(tecla, x, y):
    global dx, dy, dz, STATE
    if tecla == ESCAPE:
        glutLeaveMainLoop()
    elif tecla == 'x' or tecla == 'X':
        dx = 5.0
        dy = 0
        dz = 0   
    elif tecla == 'y' or tecla == 'Y':
        dx = 0
        dy = 5.0
        dz = 0   
    elif tecla == 'z' or tecla == 'Z':
        dx = 0
        dy = 0
        dz = 5.0
    elif tecla == 'r' or tecla == 'R':
        if STATE == 'ROTATING':
            STATE = 'STILL'
        else:
            STATE = 'ROTATING'
                    

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
    
    window = glutCreateWindow("Tetraedro")

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
    print "Hit 'r' key to stop the rotation and use use de 'x', 'y' and 'z' to control the axis with Right and Left Keys. Press ESC key to quit."
    main()
