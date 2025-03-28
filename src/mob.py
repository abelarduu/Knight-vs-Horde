from ursina import Animation

class Mob(Animation):
    def __init__(self, animation_paths , *args):
        self.life = 3
        self.is_attacking = False
        self.is_defending = False
        self.animation_paths = animation_paths
        self.anim = str(self.animation_paths[0])
        super().__init__(self.anim)
    
    def idle(self):
        """Define a animação do Mob para a posição de descanso."""
        self.anim = str(self.animation_paths[0])
    
    def attack(self):
        """Define a animação de ataque do Mob, se existir."""
        self.anim = str(self.animation_paths[1])
        
    def dodge(self):
        """Define a animação de esquiva do Mob, se existir."""
        self.anim = str(self.animation_paths[2])

    def update(self):
        """Atualiza a animação do Mob conforme seu estado."""
        self.idle()
