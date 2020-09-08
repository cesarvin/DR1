from gl import Raytracer, color, V2, V3
from obj import Obj, Texture
from sphere import Sphere, Material
import random

brick = Material(diffuse = color(0.8, 0.25, 0.25 ))
stone = Material(diffuse = color(0.4, 0.4, 0.4 ))
grass = Material(diffuse = color(0.5, 1, 0))

snowman = Material(diffuse = color(1, 1, 1))
button = Material(diffuse = color(0, 0, 0))
nose = Material(diffuse = color(1, 0.5, 0))

width = 960
height = 1280
r = Raytracer(width,height)
#r.glCreateWindow(500,300)

r.glClearColor(0.3,0.5,0.8)

r.scene.append( Sphere(V3(0.15, 1.5,  -4), 0.05, button) )
r.scene.append( Sphere(V3(-0.15, 1.5,  -4), 0.05, button) )
r.scene.append( Sphere(V3(0, 1.3,  -4), 0.10, nose) )

r.scene.append( Sphere(V3(0.20, 1.10,  -4), 0.04, button) )
r.scene.append( Sphere(V3(-0.10, 1.15,  -4), 0.04, button) )
r.scene.append( Sphere(V3(0.10, 1.15,  -4), 0.04, button) )
r.scene.append( Sphere(V3(-0.20, 1.10,  -4), 0.04, button) )

r.scene.append( Sphere(V3(0, 1.1,  -6), 0.18, button) )
r.scene.append( Sphere(V3(0, 0.2,  -6), 0.20, button) )
r.scene.append( Sphere(V3(0, -0.8,  -6), 0.22, button) )

r.scene.append( Sphere(V3(0, 2.6,  -8), 0.90, snowman) )
r.scene.append( Sphere(V3(0, 1,  -8), 1.25, snowman) )
r.scene.append( Sphere(V3(0, -1.1,  -8), 1.6, snowman) )
 
r.rtRender()

r.glFinish('output8.bmp')