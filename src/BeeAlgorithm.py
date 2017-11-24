from src.Bee import Bee

class BeeAlgorithm:
    def __init__(self, num_of_bees, num_of_sites, num_of_elite_sites, patch_size, num_of_elite_bees):
        self.num_of_bees = num_of_bees
        self.num_of_sites = num_of_sites
        self.num_of_elite_sites = num_of_elite_sites
        self.patch_size = patch_size
        self.num_of_elite_sites = num_of_elite_bees
        self.population = []

