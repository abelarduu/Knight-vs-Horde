from ursina import Animation

class Mob(Animation):
    def __init__(self, animation_paths , *args):
        self.life = 3
        self.is_attacking = False
        self.is_defending = False
        self.attacked = False
        self.defended = False
        self.animation_paths = animation_paths
        self.anim = str(self.animation_paths[0])
        super().__init__(self.anim)
    
    def idle(self):
        """Define a animação do Mob para a posição de descanso."""
        self.anim = str(self.animation_paths[0])
    
    def attack(self):
        """Define a animação de ataque do Mob, se existir."""
        self.anim = str(self.animation_paths[1])
        
    def defense(self):
        """Define a animação de esquiva do Mob, se existir."""
        self.attacked = True
        #self.anim = str(self.animation_paths[2])
        
    def hurt(self):
        """Define a animação de esquiva do Mob, se existir."""
        self.life -= 1
        #self.anim = str(self.animation_paths[3])

    def update(self):
        """Atualiza a animação do Mob conforme seu estado."""
        if self.life > 0:
            if self.is_attacking:
                self.attack()
            elif self.is_defending:
                self.defense()
            else:
                self.idle()