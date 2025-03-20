from ursina import Ursina, Entity, mouse, Sky

app = Ursina()
mouse.visible = False
Sky()

# Declarando Entidades
sword = Entity(model="quad",
               texture="assets/sword.png",
               position=(5, -1, 0),
               scale=(3, 7, 0))

shield = Entity(model="quad",
                texture="assets/shield.png",
                position=(-5, -2, 0),
                scale=(6, 6, 0))

goblin = Entity(model="quad",
                texture="assets/goblin.png",
                position=(1, -1, 2),
                scale=(5, 5, 0))
                
def input(key):
    """Método de verificação de inputs do jogo."""
    if (key == "right mouse up" and
        not key == "left mouse up"):
        sword.animate_rotation((-25, -25, -35), duration=0.2)
        sword.animate_position((2, 0, 0), duration=0.2)

    elif (key == "left mouse up" and
        not key == "right mouse up"):
        shield.animate_rotation((-20, -20, 0), duration=0.2)
        shield.animate_position((-2, 0, 0), duration=0.2)

    else:
        sword.animate_rotation((0, 0, 0), duration=0.2)
        sword.animate_position((5, -1, 0), duration=0.2)

        shield.animate_rotation((0, 0, 0), duration=0.2)
        shield.animate_position((-5, -2, 0), duration=0.2)

# Verificação direta do modulo
if __name__ == "__main__":
    app.run()