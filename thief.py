class Chromosome:
    def __init__(self, val, weight, capacity, profit) -> None:
        self.val: list[int] = val
        self.weight: list[int] = weight
        self.profit: list[int] = profit
        self.capacity: int = capacity
        self.fitness: int = self.calc_fitness()

    def __str__(self) -> str:
        s = ""
        for i in self.val:
            s += str(i)
        return s

    def calc_fitness(self) -> int:
        fitness = 0
        weight = 0
        for i in range(len(self.val)):
            if self.val[i] == 1:
                fitness += self.profit[i]
                weight += self.weight[i]
        if weight > self.capacity:
            fitness = self.capacity - weight

        return fitness
    
    def mutate_bit(self, i):
        self.val[i] = 1 if self.val[i] == 0 else 0
        self.fitness = self.calc_fitness()

def cross(a: Chromosome, b: Chromosome):
    x = a.val
    y = b.val
    x[0], x[1], y[0], y[1] = y[0], y[1], x[0], x[1]
    return Chromosome(x, a.weight, a.capacity, a.profit), Chromosome(y, a.weight, a.capacity, a.profit)

if __name__ == "__main__":
    weights = [2, 3, 4, 5]
    profits = [3, 5, 7, 9]

    pop = [Chromosome([1,1,1,1], weights, 9, profits), Chromosome([1,0,0,0], weights, 9, profits), Chromosome([1,0,1,0], weights, 9, profits), Chromosome([1,0,0,1], weights, 9, profits)]

    order = [3, 1, 4, 2]
    j = 0
    for i in range(4):
        pop.sort(key=lambda x: x.fitness, reverse=True)
        for i in pop:
            print(i.fitness, i.val)
        print("   ")
        a, b = cross(pop[2], pop[3])
        a.mutate_bit(j)
        j = (j+1)%4
        new_pop = [a, b, pop[0], pop[1]]
        pop = new_pop

    pop.sort(key=lambda x: x.fitness, reverse=True)
    print("====")
    for i in pop:
        print(i.fitness, i.val)