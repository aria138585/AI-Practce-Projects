Environment = {'A': 'Dirty', 'B': 'Dirty'}

class VacuumCleaner:
    perception_history = []
    recent_action = 'nothing'

    def __init__(self, env: dict, init_loc: str):
        self.world = env
        if not init_loc in ['A', 'B']:
            raise ValueError(f"Undefined Location {init_loc}")
        self.Location = init_loc
    
    def left(self):
        self.Location = 'A'
        self.recent_action = 'left'
    
    def right(self):
        self.Location = 'B'
        self.recent_action = 'right'
    
    def suck(self):
        self.world[self.Location] = 'Clean'
        self.recent_action = 'suck'
    
    def do_nothing(self):
        pass

    def move_away(self):
        if self.Location == 'A':
            self.right()
        else:
            self.left()
    
    def function(self):
        previous_loc = self.Location
        previous_state = self.world[self.Location]

        if self.world[self.Location] == 'Dirty':
            self.suck()
        else:
            self.move_away()
        self.perception_history.append((previous_loc, previous_state, self.recent_action))
        
    def peek_world(self):
        print(self.world)
        return self.world
    
    def peek_current_location(self):
        print(f"Currently in {self.Location}")
        return self.Location

vc = VacuumCleaner(Environment, 'A')
for i in range(10):
    vc.function()
print(vc.perception_history)
vc.peek_current_location()
