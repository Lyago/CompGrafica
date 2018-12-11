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
CONTROL = 0 #all tetrahedra
# Number of the glut window.
window = 0

# Rotations. 
xrot = [5.0] * 6
yrot = [5.0] * 6
zrot = [5.0] * 6

dx = 5.0
dy = 5.0
dz = 5.0 

#Folding animation duration in frames
duration = 500
frameCount = 1

#Rotation function to build the unfolded tetrahedra 
def roda(cx, cy, px, py, a):

  _px = ((px-cx)*math.cos(a)-(py-cy)*math.sin(a))+cx
  _py = ((px-cx)*math.sin(a)+(py-cy)*math.cos(a))+cy
  return [_px, _py, 0.0]


def foldTetrahedron(edgeLen, frameCount, colors):
	
    
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


    #Base, center triangle
    glColor3fv(colors[0])
    glBegin(GL_POLYGON)
    glVertex3fv((vertex1X, vertex1Y, startHeight))
    glVertex3fv((vertex2X, vertex2Y, startHeight))
    glVertex3fv((vertex3X, vertex3Y, startHeight))
    glEnd()
    
    #First rotation, right triangle  
    glColor3fv(colors[1])
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
    

    #Second rotation, left triangle
    glColor3fv(colors[2])
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
	
    #Third rotation, lower triangle
    glColor3fv(colors[3])
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

    ###############################
    #Up-left corner tetrahedron   #
    ###############################
    glPushMatrix()
    glClearColor(0.5,0.5,0.5,1.0)            
    
    glTranslatef(-3.0,2.0,-10.0)            

    glRotatef(xrot[1],1.0,0.0,0.0)          
    glRotatef(yrot[1],0.0,1.0,0.0)           
    glRotatef(zrot[1],0.0,0.0,1.0) 
    
    foldTetrahedron(2.0, frameCount, ((.99,0,0),(0,0,.99),(0,.99,0),(.99,.99,0)))
    glPopMatrix()

    ###############################
    #Up-right corner tetrahedron  #
    ###############################
    glPushMatrix()
    glClearColor(0.5,0.5,0.5,1.0)            
    
    glTranslatef(3.0,2.0,-10.0)            

    glRotatef(xrot[2],1.0,0.0,0.0)          
    glRotatef(yrot[2],0.0,1.0,0.0)           
    glRotatef(zrot[2],0.0,0.0,1.0)
    foldTetrahedron(2.0, frameCount, ((0,.99,0),(.99,.99,0),(.99,0,0),(0,0,.99)))
    glPopMatrix()  
    
    ###############################
    #Down-left corner tetrahedron #
    ###############################
    glPushMatrix()
    glClearColor(0.5,0.5,0.5,1.0)            
    
    glTranslatef(-3.0,-2.0,-10.0)            

    glRotatef(xrot[3],1.0,0.0,0.0)          
    glRotatef(yrot[3],0.0,1.0,0.0)           
    glRotatef(zrot[3],0.0,0.0,1.0) 
    
    foldTetrahedron(2.0, frameCount, ((.99,.99,0),(0,0,.99),(.99,0,0),(0,.99,0)))
    glPopMatrix()

    ###############################
    #Down-right corner tetrahedron#
    ###############################
    glPushMatrix()
    glClearColor(0.5,0.5,0.5,1.0)            
    
    glTranslatef(3.0,-2.0,-10.0)            

    glRotatef(xrot[4],1.0,0.0,0.0)          
    glRotatef(yrot[4],0.0,1.0,0.0)           
    glRotatef(zrot[4],0.0,0.0,1.0)
    foldTetrahedron(2.0, frameCount, ((.99,0,0),(.99,.99,0),(0,0,.99),(0,.99,0)))
    glPopMatrix()      

    ####################
    #Center tetrahedron#
    ####################
    glPushMatrix()
    glClearColor(0.5,0.5,0.5,1.0)            
    
    glTranslatef(0.0,0.0,-10.0)            

    glRotatef(xrot[5],1.0,0.0,0.0)          
    glRotatef(yrot[5],0.0,1.0,0.0)           
    glRotatef(zrot[5],0.0,0.0,1.0)
    foldTetrahedron(2.0, frameCount, ((0,0,.99),(0,.99,0),(.99,.99,0),(.99,0,0)))
    glPopMatrix()  


    if frameCount < duration:
        frameCount += 1

    if STATE == 'ROTATING':
        #xrot[0] = xrot[0] - .1              # X rotation
        #yrot[0] = yrot[0] + .1                 # Y rotation
        zrot[0] = zrot[0] + .1                 # Z rotation
        for i in range(6):
            zrot[i] = zrot[0]

    if CONTROL == 0:   
        for i in range(6):
            yrot[i] = yrot[0]
            xrot[i] = xrot[0]
            zrot[i] = zrot[0]
            
            

    glutSwapBuffers()


def keyPressed(tecla, x, y):
    global dx, dy, dz, STATE, CONTROL
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
    elif tecla == '1':
        CONTROL = 1
    elif tecla == '2':
        CONTROL = 2
    elif tecla == '3':
        CONTROL = 3
    elif tecla == '4':
        CONTROL = 4
    elif tecla == '5':
        CONTROL = 5
    elif tecla == '0':
        CONTROL = 0
        
    elif tecla == 'r' or tecla == 'R':
        if STATE == 'ROTATING':
            STATE = 'STILL'
        else:
            STATE = 'ROTATING'
                    

def teclaEspecialPressionada(tecla, x, y):
    global xrot, yrot, zrot, dx, dy, dz, CONTROL
    if tecla == GLUT_KEY_LEFT:
        for i in range(6):
            if CONTROL == i:
                xrot[i] -= dx
                yrot[i] -= dy
                zrot[i] -= dz                     
    elif tecla == GLUT_KEY_RIGHT:
        for i in range(6):
            if CONTROL == i:
                xrot[i] += dx
                yrot[i] += dy
                zrot[i] += dz              


def main():
    global window
    glutInit(sys.argv)

    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
    
    # get a 640 x 480 window 
    glutInitWindowSize(640, 480)
    
    # the window starts at the upper left corner of the screen 
    glutInitWindowPosition(0, 0)
    
    window = glutCreateWindow("The Tetrahedron Coloring Problem - Wich one is colored diferently?")

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
    print "Hit 'r' key to stop the rotation and use de 'x', 'y' and 'z' to control the axis with Right and Left Keys. 1, 2, 3, 4 and 5 toogles controls between tetrahedra. Press ESC key to quit."
    main()
