import random
from math import sin,cos,sqrt

#Genetic Algorithm Steps
#Create the population and the cromosome
def generate_population(jumlah_individu, panjang_individu):
    return [[random.randint(0,9) for i in range(panjang_individu)] for j in range(jumlah_individu)]

#Split cromosome into two part
def split_cromosome(cromosome):
    return cromosome[:len(cromosome)//2], cromosome[len(cromosome)//2:]

#Calculate fitness
def calculate_fitness(x,y):
    return (sin(sqrt(x**2 + y**2))**2 - 0.5) / (1 + 0.001 * (x**2 + y**2))**2

# Determine fitness and evaluate the fitness of each individual in the population
# Select the best fit individuals for reproduction

# crossover and breed new individuals
def crossover(orangtua1, orangtua2):
    anak1, anak2, anakan = [], [], []
    probability_of_crossover = random.random()
    if probability_of_crossover < 0.9:
       anak1[:1], anak1[1:] = orangtua1[:1], orangtua2[1:]
       anak2[:1], anak2[1:] = orangtua2[:1], orangtua1[1:]
       anakan.append(anak1)
       anakan.append(anak2)
    else:
        anakan.append(orangtua1)
        anakan.append(orangtua2)

        

# Mutation and add new individuals to the population
# Repeat
