from ursina import Entity, SpriteSheetAnimation
from random import randint

class Mob(Entity):
    def __init__(self, spritesheet, animations, *args):
        super().__init__(*args)
        self.MAX_LIFE = 50
        self.life = 50
        self.is_attacking = False
        self.is_defending = False
        self.attacked = False
        self.defended = False
        self.was_hurt = False
        self.position = (0, 0, 0)
        self.scale = (0, 0, 0)
        self.spritesheet = spritesheet
        self.animations = animations
        self.animated_sprite()

    def idle(self):
        """Define a animação do Mob para a posição de descanso."""
        self.anim.loop = True
        self.anim.play_animation('idle')
    
    def attack(self):
        """Define a animação de ataque do Mob."""
        self.anim.loop = False
        self.anim.play_animation('attack')
        
    def defense(self):
        """Define a animação de esquiva do Mob."""
        self.anim.loop = False
        self.anim.play_animation('defense')
        
    def hurt(self, damage):
        """Define a animação de esquiva do Mob."""
        if self.life > 0:
            self.anim.loop = False
            self.anim.play_animation('hit')
            self.life -= damage

    def animated_sprite(self):
        """gera a animação do Mob."""
        self.anim = SpriteSheetAnimation(texture= self.spritesheet,
                                         animations= self.animations,
                                         tileset_size=(6,5),
                                         loop=True,
                                         fps=5,
                                         postion= self.position,
                                         scale= self.scale)

    def change_action(self):
        random_number = randint(0,1)
        if random_number == 0:

            self.is_attacking = True
            self.is_defending = False
        
        elif random_number == 1: 
            self.is_defending = True
            self.is_attacking = False

    def update(self):
        """Atualiza a animação do Mob conforme seu estado."""
        if self.life > 0:
            if self.was_hurt:
                self.change_action()
                self.was_hurt = False

            if self.is_attacking:
                self.attack()
            elif self.is_defending:
                self.defense()
            else:
                self.idle()
        else:
            self.anim.enabled = False