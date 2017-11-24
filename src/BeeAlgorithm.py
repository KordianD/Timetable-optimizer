from src.Bee import Bee


class BeeAlgorithm:
    def __init__(self, num_of_bees, num_of_sites, num_of_elite_sites, patch_size, num_of_elite_bees):
        self.num_of_bees = num_of_bees
        self.num_of_sites = num_of_sites
        self.num_of_elite_sites = num_of_elite_sites
        self.patch_size = patch_size
        self.num_of_elite_sites = num_of_elite_bees
        self.population = []
        self.best = None

    def generate_population(self):
        return [Bee for _ in range(self.num_of_bees)]

    def select_best_bees(self, num_of_best_bees):
        population = self.generate_population()
        sorted_population = sorted(population, key=lambda x: x.calculate_bee_fitness, reverse=True)
        self.best = sorted_population[0]
        return sorted_population[:num_of_best_bees]

    