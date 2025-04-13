from ursina import Entity, SpriteSheetAnimation

class Mob:
    def __init__(self, spritesheet, animations):
        self.MAX_LIFE = 50
        self.life = 50
        self.is_attacking = False
        self.is_defending = False
        self.attacked = False
        self.defended = False
        self.position = (0, 0, 0)
        self.scale = (0, 0, 0)
        self.spritesheet = spritesheet
        self.animations = animations
        self.animated_sprite()
        self.idle()

    def idle(self):
        """Define a animação do Mob para a posição de descanso."""
        self.anim.play_animation('idle')
    
    def attack(self):
        """Define a animação de ataque do Mob."""
        self.anim.play_animation('attack')
        
    def defense(self):
        """Define a animação de esquiva do Mob."""
        self.anim.play_animation('defense')
        
    def hurt(self, damage):
        """Define a animação de esquiva do Mob."""
        self.anim.play_animation('hit')
        self.life -= damage

    def animated_sprite(self):
        """gera a animação do Mob."""
        self.anim = SpriteSheetAnimation(texture= self.spritesheet,
                                        animations= self.animations,
                                        tileset_size=(6,5),
                                        fps=6,
                                        loop=True)

    def update(self):
        """Atualiza a animação do Mob conforme seu estado."""
        if self.life > 0:
            if self.is_attacking:
                self.attack()
            elif self.is_defending:
                self.defense()
            else:
                self.idle()