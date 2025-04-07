from ursina import *
from src.player import Player
from src.mob import Mob

app = Ursina()
window.title = "Knight Vs Horde"
#window.fullscreen = True
mouse.visible = False
Sky()

ground = Sprite(color= "#70c6a9",
                position=(0, -8, 0),
                scale=(650, 650),
                rotation_x=90)

grass = Sprite(texture="src/assets/images/grass.png",
               position=(0, -2.5, 1),
               scale=(18, 6, 0))

# Declarando Entidades
player = Player()
goblin = Mob(animation_paths=["src/assets/images/goblin.gif"])
goblin.position=(0, -1, 2)
goblin.scale=(5, 5, 0)