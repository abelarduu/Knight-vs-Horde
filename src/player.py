from ursina import Entity, camera

CAMERA_POSITION = camera.position
INITIAL_SWORD_POSITION = CAMERA_POSITION + (5, -1, 0)
INITIAL_SHIELD_POSITION = CAMERA_POSITION + (-5, -2, 0)

class Player:
    def __init__(self):
        self.life = 3
        self.scores = 0
        self.is_attacking = False
        self.is_defending = False

        self.sword = Entity(model="quad",
                       texture="src/assets/sword.png",
                       position= INITIAL_SWORD_POSITION,
                       scale=(3, 7, 0))

        self.shield = Entity(model="quad",
                        texture="src/assets/shield.png",
                        position= INITIAL_SHIELD_POSITION,
                        scale=(6, 6, 0))
        
    def idle_sword(self):
        """Restaura a posição e rotação da espada."""
        self.sword.animate_rotation((0, 0, 0), duration=0.2)
        self.sword.animate_position(INITIAL_SWORD_POSITION, duration=0.2)
        
    def idle_shield(self):
        """Restaura a posição e rotação da espada."""
        self.shield.animate_rotation((0, 0, 0), duration=0.2)
        self.shield.animate_position(INITIAL_SHIELD_POSITION, duration=0.2)
    
    def attack(self):
        """Executa a animação de ataque com espada e rotação da câmera."""
        camera.animate_rotation((2, -2, 0), duration=0.4)
        self.sword.animate_rotation((-25, 35, -25), duration=0.2)
        self.sword.animate_position((2, 0, 0), duration=0.2)
        
        if (self.sword.rotation == (-25, 35, -25) and 
            self.sword.position == (2, 0, 0)):
            camera.animate_rotation((0, 0, 0), duration=0.4)
            self.is_attacking = False
    
    def defense(self):
        """Executa a animação de defesa com escudo e rotação da câmera."""
        camera.animate_rotation((-2, 2, 0), duration=0.4)
        self.shield.animate_rotation((-20, -20, -20), duration=0.2)
        self.shield.animate_position((-2, 0, 0), duration=0.2)
        
        if (self.shield.rotation == (-20, -20, -20) and 
            self.shield.position == (-2, 0, 0)):
            camera.animate_rotation((0, 0, 0), duration=0.4)
            self.is_defending = False
        
    def update(self):
        """Atualização do Payer"""
        
        if self.is_attacking:
            self.attack()
        else:
            self.idle_sword()
            
        if self.is_defending:
            self.defense()
        else:
            self.idle_shield()
            