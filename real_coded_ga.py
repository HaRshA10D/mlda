# -*- coding: utf-8 -*-
"""
Created on Tue Aug  1 17:26:43 2017

@author: Harsha SlimShady
"""

import math
import random
import matplotlib.pyplot as plt
import numpy as np

class ga(object):
    
    def __init__(self,chromosomes):
        self.chromosomes = chromosomes
        self.length = len(self.chromosomes)
        self.fitness = self.evaluate(self.chromosomes)
    
    def evaluate(self,chromosomes):
        fitness = []
        for x in chromosomes:
            fitness.append(math.sin(x))
        return fitness
    
    def getValues(self):
        self.fitness = self.evaluate(self.chromosomes)
        return self.chromosomes,self.fitness
    
    def tournamentSelection(self):
        parents = []
        for i in range(0,self.length):
            rand = np.random.choice(range(0,self.length),2,replace=False)
            if(self.fitness[rand[0]]>self.fitness[rand[1]]):
                parents.append(self.chromosomes[rand[0]])
            else:
                parents.append(self.chromosomes[rand[1]])
        self.parents = parents
        
    def crossover(self,pc):
        nu = 20
        children = []
        for i in range(0,int(pc*self.length)):
            rand = np.random.choice(range(0,self.length),2,replace=False)
            r = random.random()
            if(r>0.5):
                b = (1/(2*(1-r)))**(1/(nu+1))
            else:
                b = (2*r)**(1/(nu+1))
            c1 = 1/2*((1+b)*self.parents[rand[0]]+(1-b)*self.parents[rand[1]])
            c2 = 1/2*((1-b)*self.parents[rand[0]]+(1+b)*self.parents[rand[1]])
            children.append(c1)
            children.append(c2)
        self.children = children

    def mutation(self,pm):
        nu = 20
        mutants = []
        for i in range(0,int(pm*0.8*len(self.children)*2)+1):
            r = random.random()
            if(r>0.5):
                d = 1-(2*(1-r))**(1/(nu+1))
            else:
                d = (2*r)**(1/(nu+1))-1
            mutants.append(self.children[random.randint(0,len(self.children)-1)]+d)
        self.mutants = mutants
        
    def selectforNextgen(self):
        total = []
        total.extend(self.chromosomes)
        total.extend(self.children)
        total.extend(self.mutants)
        totalfitness = np.sin(np.array(total))
        totalfitness = totalfitness.tolist()
        
        self.chromosomes = [x for (y,x) in sorted(zip(totalfitness,total))][:self.length]

if __name__ == "__main__":
    
    points = np.linspace(0,2*math.pi,100)
    sinvals = np.sin(points)
    
    initialch = []
    for i in range(0,10):
        initialch.append(random.random()*2*math.pi)
    for i in range(0,100):
        chset = ga(initialch)
        chset.tournamentSelection()
        chset.crossover(0.8)
        chset.mutation(0.2)
        chset.selectforNextgen()
        initialch, fitness = chset.getValues()
    chromosomes, fitness = chset.getValues()
    #chset = ga(initialch)
    #chromosomes, fitness = chset.getValues()
    print(fitness)
    plt.plot(points,sinvals)
    plt.scatter(chromosomes,fitness)
    plt.show()
    