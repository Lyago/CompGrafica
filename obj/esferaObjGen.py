import math
import random
 
def sphere(radius, resolution):
    r = radius 
    def s(u,v):
        return ((r * math.cos(u)) * math.cos(v), r * math.sin(u), (r*math.cos(u)) * math.sin(v))
    
    tet = -math.pi/2.0
    phi = 0.0

#incremento eh pi dividido por uma resolucao. A resolucao determina o numero de "gomos" que serao renderizados na esfera e a discretizacao dos       triangulos(do Triangle Strip) que compoem esses gomos.
    
    inc = math.pi/resolution
    f = open("esfera.obj", 'w')
    vertexCount = 0
    faceCount = 0
    
    for i in range(0,resolution):
        phi = 0
        for j in range(0,resolution*2+1):
            writeVertexObj(f, s(tet, phi))
            writeVertexObj(f, s(tet + inc, phi))
            vertexCount += 2
            phi += inc
        tet += inc

    for i in range(1,vertexCount,3):
        writeFaceObj(f, (i, i+1, i+2))
        #if (i < vertexCount-1):
        #    writeFaceObj(f, (i+3, i+1, i+2))        

def writeVertexObj(f, vertex):    
    line = "v "+ str(vertex[0]) + " " + str(vertex[1]) + " " + str(vertex[2])+ "\n"
    f.write(line)
    

def writeFaceObj(f, face):
    line = "f "+ str(face[0]) + " " + str(face[1]) + " " + str(face[2])+ "\n"
    f.write(line)   

sphere(1, 15)
