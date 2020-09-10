class MapTile:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def intro_text(self):
        raise NotImplementedError("Create a subclass instead!")

class StartTile(MapTile):
    def intro_text(self):
        return """
        You awake to find yourself in an apartment of an abandoned building. There's a light flickering in the hallway just outside the door.
        You poke your head out to see there are four directions you can try to go. All directions look dangerous but you can't stay here.
        You must venture out to gather supplies in order to survive and escape.
        """

class EmptyTile(MapTile):
    def intro_text(self):
        return """
        There is nothing of value here. Continue on.
        """

class VictoryTile(MapTile)
    def intro_text(self):
        return """
        There's a helicopter in the distance...
        you can hear its blades whirring as you get closer. It seems to be the only way out of here.
                
        VICTORY! You have escaped from DC.
        """

world_map = [
            [None, VictoryTile(1,0), [None]]
            [None, EmptyTile(1,1), None]
            [EmptyTile(0,2), StartTile(1,2), EmptyTile(2,2)]
            [None, EmptyTile(1,3), None]
            ]
def tile_at(x,y):
    if x < 0 or y < 0:
        return None

    try:
        return world_map[y][x]
    except IndexError:
        return None



