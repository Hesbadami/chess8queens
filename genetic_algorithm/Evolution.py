import random
from Chromosome import Board


class Genetics:
    def __init__(
        self,
        population=1000,  # population
        max_iter=800,  # max number of generations
        pb=0.80,  # breeding probability
        pm=0.005,  # mutation probability
        max_fittness=64
    ):
        self.generation = 1
        self.population_count = population
        self.max_iter = max_iter
        self.pb = pb
        self.pm = pm
        self.max_fittness = max_fittness

        self.avg_fittness = []  # stores average fittness value per generation
        self.best_fittness = []  # stores best fittness value per generation

        self.population = [Board() for c in range(self.population_count)]
        self.final_ans = self.population[0]

        self.save_stats()

    def save_stats(self):
        sigma = 0
        best = self.population[0]
        for b in self.population:
            sigma += b.fittness()
            if b.fittness() > best.fittness():
                best = b
        self.avg_fittness.append(sigma/self.population_count)
        self.best_fittness.append(best.fittness())

        if self.final_ans.fittness() < best.fittness():
            self.final_ans = best

    def select_parents(self):
        chances = []
        last = 0
        for b in self.population:
            last += b.fittness()
            chances.append((last, b))

        parents = []
        for i in range(self.population_count):
            r = random.randint(0, last)
            for key, value in chances:
                if r <= key:
                    break

            parents.append(value)
        return parents

    def reproduce(self, parents):
        childes = []
        a = 0
        while a + 1 < len(parents):
            r = random.randint(0, self.population_count)
            if r >= self.pb * self.population_count:
                childes.append(Board(parents[a].get_board()))
                childes.append(Board(parents[a+1].get_board()))
            else:
                childes.extend(parents[a].breed(parents[a+1]))
            a += 2
        return childes

    def next_gen(self):
        parents = self.select_parents()
        childes = self.reproduce(parents)

        for b in childes:
            b.mutate(possibility=self.pm)

        self.population = childes
        self.save_stats()
        self.generation += 1

    def terminate(self):
        if self.max_fittness <= self.best_fittness[-1]:
            return True

        return self.generation >= self.max_iter
