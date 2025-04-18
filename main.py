from src import *

def input(key):
    """Método de verificação de inputs do jogo."""
    if (not player.is_attacking and 
        key == "right mouse down"):
            player.is_attacking = True
            goblin.was_hurt= True

    elif (not player.is_defending and 
        key == "left mouse down"):
            player.is_defending = True
            goblin.was_hurt= True

    # Atualiza as ações do Player a cada interação/click
    player.update()
    if (player.attacked and
        not goblin.defended):
        goblin.hurt(damage=10)
        player.hurt(damage=55)
        player.attacked = False

def update():
    # Atualiza as ações do Goblin a cada interação/click
    goblin.update()
    if (goblin.attacked and
        not player.defended):
        player.hurt(damage=25)
        goblin.attacked = False
    else:
        player.defended = False

    #print(goblin.is_attacking, goblin.is_defending)
    print(goblin.life)

# Verificação de execução direta do módulo
if __name__ == "__main__":
    app.run()