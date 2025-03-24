from ursina import Entity

class Player:
    def __init__(self):
        self.life = 3
        self.scores = 0
        self.is_attacking = False
        self.is_defending = False
    
        self.sword = Entity(model="quad",
                       texture="src/assets/sword.png",
                       position=(5, -1, 0),
                       scale=(3, 7, 0))

        self.shield = Entity(model="quad",
                        texture="src/assets/shield.png",
                        position=(-5, -2, 0),
                        scale=(6, 6, 0))
        
    def idle_sword(self):
        self.sword.animate_rotation((0, 0, 0), duration=0.2)
        self.sword.animate_position((5, -1, 0), duration=0.2)
        
    def idle_shield(self):
        self.shield.animate_rotation((0, 0, 0), duration=0.2)
        self.shield.animate_position((-5, -2, 0), duration=0.2)
    
    def attack(self):
        self.sword.animate_rotation((-25, 25, -25), duration=0.2)
        self.sword.animate_position((2, 0, 0), duration=0.2)
        
        if (self.sword.rotation == (-25, 25, -25) and 
            self.sword.position == (2, 0, 0)):
            self.is_attacking = False
    
    def defense(self):
        self.shield.animate_rotation((-20, -20, -20), duration=0.2)
        self.shield.animate_position((-2, 0, 0), duration=0.2)
        
        if (self.shield.rotation == (-20, -20, -20) and 
            self.shield.position == (-2, 0, 0)):
            self.is_defending = False
        
    def update(self):
        if self.is_attacking:
            self.attack()
        else:
            self.idle_sword()
            
        if self.is_defending:
            self.defense()
        else:
            self.idle_shield()