import bpy
from random import randint

ob = bpy.data.objects["Sphere"]
frame_number = 0

for i in range(0,50):
    x = randint(-20,20)
    y = randint(-20,20)
    z = 0
    bpy.context.scene.frame_set(frame_number)
    ob.location = (x, y, z)

    frame_number += 5
    