from ursina import Entity, camera, mouse

INITIAL_SWORD_POSITION = camera.position + (5, -1, 0)
INITIAL_SHIELD_POSITION = camera.position + (-5, -2, 0)

class Player:
    def __init__(self):
        self.life = 3
        self.scores = 0
        self.is_attacking = False
        self.is_defending = False
        self.attacked = False
        self.defended = False

        self.sword = Entity(model="quad",
                       texture="src/assets/images/sword.png",
                       position= INITIAL_SWORD_POSITION,
                       scale=(3, 7, 0))

        self.shield = Entity(model="quad",
                        texture="src/assets/images/shield.png",
                        position= INITIAL_SHIELD_POSITION,
                        scale=(6, 6, 0))
        
    def idle_sword(self):
        """Restaura a posição e rotação da espada."""
        self.sword.animate_rotation((0, 0, 0), duration=0.2)
        self.sword.animate_position(INITIAL_SWORD_POSITION, duration=0.2)
        camera.animate_rotation((0, 0, 0), duration=0.4)

    def idle_shield(self):
        """Restaura a posição e rotação do escudo."""
        self.shield.animate_rotation((0, 0, 0), duration=0.2)
        self.shield.animate_position(INITIAL_SHIELD_POSITION, duration=0.2)
        camera.animate_rotation((0, 0, 0), duration=0.4)

    def attack(self):
        """Executa a animação de ataque com espada e rotação da câmera."""
        self.is_attacking = True
        camera.animate_rotation((2, -2, 0), duration=0.4)
        self.sword.animate_rotation((-25, 35, -25), duration=0.2)
        self.sword.animate_position((2, 0, 0), duration=0.2)
        
        # Verifica o fim da animação
        if (self.sword.rotation == (-25, 35, -25) and
            self.sword.position == (2, 0, 0)):
            self.attacked = True
            self.is_attacking = False
    
    def defense(self):
        """Executa a animação de defesa com escudo e rotação da câmera."""
        self.is_defending = True
        camera.animate_rotation((-2, 2, 0), duration=0.4)
        self.shield.animate_rotation((-20, -20, -20), duration=0.2)
        self.shield.animate_position((-2, 0, 0), duration=0.2)
        
        # Verifica o fim da animação
        if (self.shield.rotation == (-20, -20, -20) and 
            self.shield.position == (-2, 0, 0)):
            self.defended = True
            self.is_defending = False
            
    def hurt(self):
        """Define a animação de esquiva do Mob, se existir."""
        camera.animate_rotation((-2, 2, 0), duration=0.4)
        self.life -= 1
        
        if (self.shield.rotation == (-20, -20, -20) and 
            self.shield.position == (-2, 0, 0)):
            camera.animate_rotation((0, 0, 0), duration=0.4)
        
    def update(self):
        """Atualização do Player"""
        if self.life > 0:
            if self.is_attacking:
                self.attack()
            else:
                self.idle_sword()

            if self.is_defending:
                self.defense()
            else:
                self.idle_shield()