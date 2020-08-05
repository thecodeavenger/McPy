from classes import BasicClasses

class AbstractTerrainFeature:
    
    def generation_attempt(self, random: float, chunk, chunk_x: int, chunk_y: int, chunk_z: int, is_top_layer: bool):
        pass

class OreFeature(AbstractTerrainFeature):
    
    ore_name: str = "missing"
    chance: float = -1
    max_y: int = -1
    min_y: int = -1
    batch_min = 0
    batch_max = 0
    
    def __init__ (self, ore: str, weight: float, minimum_y: int, maximum_y: int, min_size: int, max_size: int):
        self.ore_name = ore
        self.chance = weight
        self.max_y = maximum_y
        self.min_y = minimum_y
        self.batch_min = min_size
        self.batch_max = max_size
    
    def generation_attempt(self, random: float, chunk, chunk_x: int, chunk_y: int, chunk_z, is_top_layer: bool):
        if is_top_layer:
            pass
        elif random < self.chance and chunk_y < self.max_y and chunk_y > self.min_y:
            chunk.addNewBlock(chunk_x, chunk_y, chunk_z, BasicClasses.Block(chunk_x, chunk_y, chunk_z, self.ore_name, None))
        else:
            pass
