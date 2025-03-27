from src import *

def input(key):
    """Método de verificação de inputs do jogo."""
    if (not player.is_attacking and 
        player.sword.position == (5, -1, 0)):
        
        if (key == "right mouse down" and
            not key == "left mouse down"):
            player.is_attacking = True
            player.is_defending = False
       
    if (not player.is_defending and 
        player.shield.position == (-5, -2, 0)):
        
        if (key == "left mouse down" and
            not key == "right mouse down"):
            player.is_defending = True
            player.is_attacking = False
    
    # Atualiza as ações do player a cada interação/Click
    player.update()
    
# Verificação de execução direta do modulo
if __name__ == "__main__":
    app.run()
