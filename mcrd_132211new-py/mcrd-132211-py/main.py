from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
import random
from ursina import time

app = Ursina()
player = FirstPersonController()
player.position = (25, 2, 25)

window.icon = "icon.png"
window.title = "Minecraft rd-132211"
window.fullscreen = True
window.editor_ui.visible = False

gokyuzu = load_texture("gökyüzü.png")
cursortexture = load_texture("cursortexture.png")
Sky(texture=gokyuzu)

player.cursor.visible = True
player.cursor.texture = cursortexture
player.cursor.color = color.white

mouse.visible = False

taban = []
for i in range(50):
    for j in range(50):
        cimen = Button(
            color=color.white,
            model='cube',
            position=(j, 0, i),
            texture='çimen.png',
            parent=scene,
            origin_y=0.5,
            collider='box' 
        )
        taban.append(cimen)

yapibloklari = []


cimen_tusu_basildi = False
tas_tusu_basildi = False
tahta_tusu_basildi = False
tugla_tusu_basildi = False


grasswalk1 = Audio('grasswalk1.wav', autoplay=False, loop=False)
grasswalk2 = Audio('grasswalk2.wav', autoplay=False, loop=False)
grasswalk3 = Audio('grasswalk3.wav', autoplay=False, loop=False)
grasswalksounds = [grasswalk1, grasswalk2, grasswalk3]

step_timer = 0
step_interval = 0.4

def input(key):
    global cimen_tusu_basildi 
    global tas_tusu_basildi 
    global tahta_tusu_basildi
    global tugla_tusu_basildi

    if key == 'escape':
        application.quit()
    if key == 'f11':
        window.fullscreen = True


    if key == '1':
        cimen_tusu_basildi = True
        tas_tusu_basildi = False
        tahta_tusu_basildi = False
        tugla_tusu_basildi = False
    if key == '2':
        tas_tusu_basildi = True
        cimen_tusu_basildi = False
        tahta_tusu_basildi = False
        tugla_tusu_basildi = False
    if key == '3':
        tahta_tusu_basildi = True
        cimen_tusu_basildi = False
        tas_tusu_basildi = False
        tugla_tusu_basildi = False
    if key == '4':
        tugla_tusu_basildi = True
        cimen_tusu_basildi = False
        tas_tusu_basildi = False
        tahta_tusu_basildi = False

    if key == 'left mouse down' and mouse.hovered_entity:
        pos = mouse.hovered_entity.position + mouse.normal

        if cimen_tusu_basildi:
            texture_path = 'çimen.png'
        elif tas_tusu_basildi:
            texture_path = 'tas.png'
        elif tahta_tusu_basildi:
            texture_path = 'tahta.png'
        elif tugla_tusu_basildi:
            texture_path = 'tuğla.png'
        else:
            return

        yeni_blok = Button(
            model='cube',
            color=color.white,
            texture=texture_path,
            position=pos,
            parent=scene,
            origin_y=0.5,
            collider='box'
        )
        yapibloklari.append(yeni_blok)

    if key == 'right mouse down' and mouse.hovered_entity:
        if mouse.hovered_entity in yapibloklari:
            yapibloklari.remove(mouse.hovered_entity)
            destroy(mouse.hovered_entity)

def update():
    global step_timer
    step_timer -= time.dt

    if (held_keys['w'] or held_keys['a'] or held_keys['s'] or held_keys['d']) and step_timer <= 0:
        random.choice(grasswalksounds).play()
        step_timer = step_interval

app.run()
