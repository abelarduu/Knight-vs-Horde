from ursina import Animation, color
from ursina.prefabs.health_bar import HealthBar

class Mob(Animation):
    def __init__(self, animation_paths , *args):
        self.MAX_LIFE = 50
        self.life = 50
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
        
    def hurt(self, damage):
        """Define a animação de esquiva do Mob, se existir."""
        self.life -= damage
        #self.anim = str(self.animation_paths[3])

    def update(self):
        """Atualiza a animação do Mob conforme seu estado."""
        health_bar = HealthBar(max_value=self.MAX_LIFE,
                               value=self.life,
                               bar_color=color.red,
                               x=-0.25, y=0.25)

        if self.life > 0:
            if self.is_attacking:
                self.attack()
            elif self.is_defending:
                self.defense()
            else:
                self.idle()