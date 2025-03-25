from ursina import *
from src.player import Player

app = Ursina()
mouse.visible = False
Sky()

ground = Entity(model="quad",
                color= "#70c6a9",
                scale=(650, 650),
                rotation_x=90,
                position=(0, -7, 0))
                
grass = Entity(model="quad",
                texture="src/assets/grass.png",
                position=(0, -2.5, 1),
                scale=(17, 5, 0))

# Declarando Entidades
player = Player()

goblin = Entity(model="quad",
                texture="src/assets/goblin.png",
                position=(0, -1, 2),
                scale=(5, 5, 0))
                
                                

