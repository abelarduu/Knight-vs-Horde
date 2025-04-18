from ursina import Entity, Sprite, camera, Vec3, curve
from ursina.ursinamath import distance

INITIAL_SWORD_POSITION = camera.position + (5, -1, 0)
INITIAL_SHIELD_POSITION = camera.position + (-5, -2, 0)

class Player:
    def __init__(self):
        self.MAX_LIFE = 100
        self.life = 100
        self.scores = 0
        self.is_attacking = False
        self.is_defending = False
        self.attacked = False
        self.defended = False
        self.was_hurt = False

        self.sword = Sprite(texture="src/assets/images/sword.png",
                            position= INITIAL_SWORD_POSITION,
                            scale=(5, 9, 0))

        self.shield = Sprite(texture="src/assets/images/shield.png",
                             position= INITIAL_SHIELD_POSITION,
                             scale=(11, 11, 0))

    def idle_sword(self):
        """Restaura a posição e rotação da espada."""
        camera.animate_rotation((0, 0, 0), duration=0.4)
        self.sword.animate_rotation((0, 0, 0), duration=0.2)
        self.sword.animate_position(INITIAL_SWORD_POSITION, duration=0.2)
        self.is_attacking = False

    def idle_shield(self):
        """Restaura a posição e rotação do escudo."""
        camera.animate_rotation((0, 0, 0), duration=0.4)
        self.shield.animate_rotation((0, 0, 0), duration=0.2)
        self.shield.animate_position(INITIAL_SHIELD_POSITION, duration=0.2)
        self.defended = False
        self.is_defending = False

    def attack(self):
        """Executa a animação de ataque com espada e rotação da câmera."""
        self.is_attacking = True
        camera.animate_rotation((2, -2, 0), duration=0.4)
        self.sword.animate_rotation((-25, 35, -25), duration=0.2)
        self.sword.animate_position((2, 0, 0), duration=0.2)
        
        # Verifica o fim da animação
        if (distance(self.sword.rotation, Vec3(-25, 35, -25)) < 1.0 and
            distance(self.sword.position, Vec3(2, 0, 0)) < 0.1):
            self.attacked = True
            self.idle_sword()
    
    def defense(self):
        """Executa a animação de defesa com escudo e rotação da câmera."""
        self.is_defending = True
        camera.animate_rotation((-2, 2, 0), duration=0.4)
        self.shield.animate_rotation((-20, -20, -20), duration=0.2)
        self.shield.animate_position((-2, 0, 0), duration=0.2)
        
        # Verifica o fim da animação
        if (distance(self.shield.rotation, Vec3(-20, -20, -20)) < 1.0 and
            distance(self.shield.position, Vec3(-2, 0, 0)) < 0.1):
            self.defended = True
            self.idle_shield()
            
    def hurt(self, damage):
        """Executa a animação de dano e adiciona danos."""
        camera.shake(duration=0.5, magnitude=10)
        self.life -= damage
        self.was_hurt = False

    def die(self):
        camera.shake(duration=0.5, magnitude=10)
        camera.animate_rotation((0, 0, 90), duration=1.5, curve=curve.in_quad)
        camera.animate_position((-2, -3, 0), duration=1)
        
    def update(self):
        """Atualização do Player"""
        if self.life > 0:
            # Ataque
            if self.is_attacking:
                self.attack()
            # Defesa
            if self.is_defending:
                self.defense()
        else:
            self.die()