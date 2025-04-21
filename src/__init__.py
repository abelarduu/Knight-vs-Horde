from ursina import *
from src.player import Player
from src.mob import Mob
DIR_ASSETS= "src/assets/images"

app = Ursina()
window.title = "Knight Vs Horde"
mouse.visible = False

ground = Sprite(color= "#70c6a9",
                position=(0, -5, 15),
                scale=(30, 15, 0))

grass = Sprite(texture=f"{DIR_ASSETS}/grass.png",
               position=(0, -2.5, 1),
               scale=(18, 6, 0))

# Declarando Entidades
player = Player()

goblin = Mob(spritesheet=f"{DIR_ASSETS}/goblin.png",
             animations={'idle': ((0, 0), (5, 1)),
                         'attack': ((0, 2), (5, 4)),
                         'defense': ((0, 2), (5, 4)),
                         'hit': ((0, 2), (5, 4))})

goblin.position=(0, -1, 2)
goblin.scale=(5, 5, 0)