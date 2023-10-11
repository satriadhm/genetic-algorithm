import random
from math import sin,cos,sqrt,exp

#Genetic Algorithm Steps

#make array for data limit x and y

x_limit = [-1,2]
y_limit = [-1,1]


#Create the population and the cromosome
def generate_population(jumlah_individu, panjang_individu):
    return [[random.randint(0,9) for i in range(panjang_individu)] for j in range(jumlah_individu)]

#Split cromosome into two part
def split_cromosome(cromosome):
    return cromosome[:len(cromosome)//2], cromosome[len(cromosome)//2:]


#rumus yang akan dicari nilai minimumnya
def function(x,y):
    return -(abs(sin(x)*cos(y)*exp(abs(1-(sqrt(x**2+y**2))))))

#decode cromosome
def decode(cromosome, limit):
    multiplier, divider = 0, 0
    for i in range(len(cromosome)):
        multiplier += cromosome[i]*(10**(i+1))
        divider += 9*(10**(i+1))

    return limit[0] + ((limit[1]-limit[0])/divider * multiplier)
    

#Calculate fitness 
    def calculate_fitness():
        return 0


# Determine fitness and evaluate the fitness of each individual in the population
# Select the best fit individuals for reproduction

# crossover and breed new individuals
def crossover(orangtua1, orangtua2):
    anak1, anak2, anakan = [], [], []
    probability_of_crossover = random.randint(0,9)
    if probability_of_crossover < 0.9:
       anak1[:1], anak1[1:] = orangtua1[:1], orangtua2[1:]
       anak2[:1], anak2[1:] = orangtua2[:1], orangtua1[1:]
       anakan.append(anak1)
       anakan.append(anak2)
    else:
        anakan.append(orangtua1)
        anakan.append(orangtua2)

        

# Mutation and add new individuals to the population
def mutation(anak1, anak2):
    for i in range(len(anak1)):
        probability_of_mutation_for_anak1 = random.randit(0,9)
        if probability_of_mutation_for_anak1 < 0.1:
            anak1[i] = random.randint(0,9)
        
        probability_of_mutation_for_anak2 = random.randit(0,9)
        if probability_of_mutation_for_anak2 < 0.1:
            anak2[i] = random.randint(0,9)
    
    return anak1, anak2

# Looping for population selection process
