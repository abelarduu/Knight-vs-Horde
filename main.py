from src import *

def input(key):
    """Método de verificação de inputs do jogo."""
    if (not player.is_attacking and 
        key == "right mouse down"):
            player.is_attacking = True
            player.is_defending = False
       
    if (not player.is_defending and 
        key == "left mouse down"):
            player.is_defending = True
            player.is_attacking = False

    # Atualiza as ações do Player a cada interação/click
    player.update()
    if (player.attacked and
        not goblin.defended):
           goblin.hurt(25)
           player.attacked = False

    # Atualiza as ações do Goblin a cada interação/click
    goblin.update()
    if (goblin.attacked and
        not player.defended):
        player.hurt(25)
        goblin.attacked = False
    else:
        player.defended = False

    print(player.life, goblin.life)

# Verificação de execução direta do modulo
if __name__ == "__main__":
    app.run()