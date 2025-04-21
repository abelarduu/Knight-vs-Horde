from src import *

def input(key):
    """Método de verificação de inputs do jogo."""
    if (not player.is_attacking and 
        key == "right mouse down"):
            player.is_attacking = True
            goblin.was_hurt= True

    if (not player.is_defending and 
          key == "left mouse down"):
            player.is_defending = True
            goblin.was_hurt= True

    if (player.is_attacking and 
        key == "right mouse up"):
            player.is_attacking = False

    if (player.is_defending and 
        key == "left mouse up"):
            player.is_defending = False

def update():
    """Metodo de atualização da interface a cada quadro/frame"""

    # Atualizando as ações do Player
    player.update()
    if (player.attacked and
        not goblin.defended):
        goblin.hurt(damage=10)
        #player.hurt(damage=55) #Testando do player.die()
        player.attacked = False

    # Atualizando as ações do Goblin
    goblin.update()
    if (goblin.attacked and
        not player.defended):
        player.hurt(damage=25)
        goblin.attacked = False
    else:
        player.defended = False

    if player.life < 0:
        Text(parent= camera, text="GAME OVER", scale=6, position= 0)

# Verificação de execução direta do módulo
if __name__ == "__main__":
    app.run()