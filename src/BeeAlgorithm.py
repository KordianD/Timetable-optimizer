from src.Bee import Bee


class BeeAlgorithm:
    def __init__(self, num_of_bees, num_of_sites, num_of_elite_sites, patch_size, num_of_elite_bees, num_of_other_bees, max_gens):
        self.num_of_bees = num_of_bees
        self.num_of_sites = num_of_sites
        self.num_of_elite_sites = num_of_elite_sites
        self.patch_size = patch_size
        self.num_of_elite_sites = num_of_elite_bees
        self.num_of_other_bees = num_of_other_bees
        self.max_gens = max_gens
        self.population = []
        self.best = None

    def search(self):
        best = None
        for _ in range(self.max_gens):
            for bee in self.population:
                bee.calculate_bee_fitness()
            sorted(self.population, key=lambda x: x.fitness)
            if not best or self.population[0].fitness > best.fitness:
                best = self.population[0]
            next_gen = []

            for index, bee in enumerate(self.population[:self.num_of_sites]):
                neigh_size = self.num_of_elite_bees if index < self.num_of_elite_sites else self.num_of_other_bees
                next_gen.append() #TODO


    def generate_population(self):
        return [Bee for _ in range(self.num_of_bees)]

    def select_best_bees(self, num_of_best_bees):
        population = self.generate_population()
        sorted_population = sorted(population, key=lambda x: x.calculate_bee_fitness, reverse=True)
        self.best = sorted_population[0]
        return sorted_population[:num_of_best_bees]

    def search_neigh(self, parent, neigh_size, patch_size):
        neigh = []
        for _ in range(neigh_size):
            neigh.append() #TODO
        
    def create_neigh_bee(self):
        pass #TODO
