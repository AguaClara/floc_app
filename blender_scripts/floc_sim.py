import random
import bpy


scene = bpy.context.scene

# add metaball object

mball = bpy.data.metaballs.new("MetaBall")
obj = bpy.data.objects.new("MetaBallObject", mball)
scene.collection.objects.link(obj)

mball.resolution = 0.2   # View resolution
mball.render_resolution = 0.02

random.choice(range(1,20));

for i in range(random.choice(range(1,20))):
    coordinate = tuple(random.uniform(-5,5) for i in range(3))

    element = mball.elements.new()
    element.co = coordinate
    element.radius = 2.0
    
# add camera object
    
camera_data = bpy.data.cameras.new(name='Camera')
camera_object = bpy.data.objects.new('Camera', camera_data)
bpy.context.scene.collection.objects.link(camera_object)