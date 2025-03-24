from ursina import Ursina, Entity, mouse, Sky
from src.player import Player

app = Ursina()
mouse.visible = False
Sky()

# Declarando Entidades
player = Player()
goblin = Entity(model="quad",
                texture="src/assets/goblin.png",
                position=(1, -1, 2),
                scale=(5, 5, 0))