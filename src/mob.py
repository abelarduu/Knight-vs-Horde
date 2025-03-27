from ursina import Animation

class Mob(Animation):
    def __init__(self, animation_paths , *args):
        super().__init__(animation_paths[0], fps= 8,auto_destroy=False)
        self.life = 3
        self.is_attacking = False
        self.is_defending = False
        self.animation_paths = animation_paths
        self.anim = self.animation_paths[0]
        
    def idle(self):
        self.anim = self.animation_paths[0]
    
    def attack(self):
        self.anim = self.animation_paths[1]
        
    def dodge(self):
        self.anim = self.animation_paths[2]

    def update(self):
        self.idle()

