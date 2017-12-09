import random
import src.configuration as conf
from src.Bee import Bee
from src.Classwork import Classwork
from src.Plotter import Plotter
from src.TimetablePlotter import *


class BeeAlgorithm:
    def __init__(self, num_of_bees, num_of_sites, num_of_elite_sites, patch_size, num_of_elite_bees, num_of_other_bees, max_gens):
        self.num_of_bees = num_of_bees
        self.num_of_sites = num_of_sites
        self.num_of_elite_sites = num_of_elite_sites
        self.patch_size = patch_size
        self.num_of_elite_bees = num_of_elite_bees
        self.num_of_other_bees = num_of_other_bees
        self.max_gens = max_gens
        self.population = []
        self.best = None
        self.fitness = []

    def search(self):
        best = None
        self.population = self.generate_population()
        for gen in range(self.max_gens):
            for bee in self.population:
                bee.calculate_bee_fitness()
            sorted(self.population, key=lambda x: x.fitness)
            if not best or self.population[0].fitness > best.fitness:
                best = self.population[0]
            next_gen = []

            for index, bee in enumerate(self.population[:self.num_of_sites]):
                neigh_size = self.num_of_elite_bees if index < self.num_of_elite_sites else self.num_of_other_bees
                next_gen.append(self.search_neigh(bee, neigh_size, self.patch_size))

            scouts = self.create_scout_bees(self.num_of_bees - self.num_of_sites)
            self.population = next_gen + scouts
            self.patch_size = self.patch_size * 0.95
            
            self.fitness.append(best.fitness)
        return best

    def generate_population(self):
        return [Bee(conf.NUM_OF_STUDENTS, conf.NAMES_OF_SUBJECTS) for _ in range(self.num_of_bees)]

    def search_neigh(self, parent, neigh_size, patch_size):
        neigh = []
        for _ in range(neigh_size):
            neigh.append(self.create_neigh_bee(parent, patch_size))
        
        for bee in neigh:
            bee.calculate_bee_fitness()

        return sorted(neigh, key=lambda x: x.fitness)[0]
        
    def create_neigh_bee(self, parent, patch_size):
        new_bee = parent
        for subject_index, subject in enumerate(parent.subjects):
            for term_index, term in enumerate(subject.terms):
                random_number = random.random()
                new_hour = term.hour + random_number * patch_size if random_number < 0.5 else term.hour - random_number * patch_size 
                if new_hour > conf.HOURS_SPACE[-1]:
                    new_hour = conf.HOURS_SPACE[-1]
                elif new_hour < conf.HOURS_SPACE[0]:
                    new_hour = conf.HOURS_SPACE[0]

                new_bee.subjects[subject_index].terms[term_index] = Classwork(term.classwork_name, term.day, new_hour, term.id)

                for student_index, student in enumerate(new_bee.students):
                    for classwork_index, classwork in enumerate(student.timetable):
                        if classwork.classwork_name == term.classwork_name and classwork.id == term.id:
                            classwork.hour = new_hour 

        return new_bee

    def create_scout_bees(self, num_of_scouts):
        scouts_population = []
        for _ in range(num_of_scouts):
            scouts_population.append(Bee(conf.NUM_OF_STUDENTS, conf.NAMES_OF_SUBJECTS))

        return scouts_population

    def get_fitness(self):
        return self.fitness

    def get_best_solution(self):
        return self.best


bee_algorithm = BeeAlgorithm(conf.NUM_OF_BEES, conf.NUM_OF_SITES, conf.NUM_OF_ELITE_SITES, conf.PATCH_SIZE, conf.NUM_OF_ELITE_BEES, conf.NUM_OF_OTHER_BEES, conf.MAX_GENS)
best = bee_algorithm.search()

plotter = Plotter()

plotter.plot_cost_function(bee_algorithm.fitness)


print('BEST')
for elem in best.students:
    for eleme in elem.timetable:
        print('Day ' + str(eleme.day) + '   hour : ' + str(eleme.hour))

#plot_timetable(best.get_random_student())