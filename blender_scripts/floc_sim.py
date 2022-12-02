import bpy
import random

try: 
    object_to_delete = bpy.data.objects['MetaBallObject']
    bpy.data.objects.remove(object_to_delete, do_unlink=True)
except:
    print("lol")

for material in bpy.data.materials:
    material.user_clear()
    bpy.data.materials.remove(material)

def shader():

    material_basic = bpy.data.materials.new(name = "BacteriaFinal")
    material_basic.use_nodes = True


    principled_node = material_basic.node_tree.nodes.get('Principled BSDF')

    principled_node.inputs[0].default_value = (0, 0, 0, 1)
    principled_node.inputs[9].default_value = 1
    l = principled_node.outputs[0].links[0]
    material_basic.node_tree.links.remove(l)

    #Mix Shader

    mix_shader = material_basic.node_tree.nodes.new("ShaderNodeMixShader")
    mix_shader.location = (260, 0)


    #material output

    material_output = material_basic.node_tree.nodes.get("Material Output")

    #link

    link = material_basic.node_tree.links.new

    link(mix_shader.outputs[0], material_output.inputs[0])
    link(principled_node.outputs[0], mix_shader.inputs[1])


    #emission

    emission = material_basic.node_tree.nodes.new("ShaderNodeEmission")
    link(emission.outputs[0], mix_shader.inputs[2])

    #layer weight

    weight = material_basic.node_tree.nodes.new("ShaderNodeLayerWeight")
    weight.inputs[0].default_value = 0.300
    link(weight.outputs[0], mix_shader.inputs[0])
    
    return material_basic
    
def groups(offset):
    
    for i in range(random.choice(range(6,20))):
        x,y,z = tuple(random.uniform(random.choice(range(-10,0)) + offset,random.choice(range(0, 10)) + offset) for i in range(3))
        element = mball.elements.new()
        element.co = (x + offset,y + offset,z + offset)
        element.radius = 2.0
    
scene = bpy.context.scene

# add metaball object

mball = bpy.data.metaballs.new("MetaBall")
obj = bpy.data.objects.new("MetaBallObject", mball)
scene.collection.objects.link(obj)
balls = bpy.context.active_object
mball.resolution = 0.2   # View resolution
mball.render_resolution = 0.02

amount = random.choice(range(1,3))

for i in range(amount):
    groups(0)
    groups(random.choice(range(10,20)))


obj.data.materials.append(shader())
obj.active_material_index = 0


