# -*- coding: utf-8 -*-
"""
Created on Wed Aug  9 01:19:02 2017

@author: Harsha SlimShady
"""

import random
import operator
import matplotlib.pyplot as plt
import math

def fitness(vector):
    
    total = 0.0
    for i in range(len(vector)):
        total += math.sin(vector[i])
        #total += vector[i]**2
    return total

class particle:
    
    def __init__(self,dimension):
        
        self.position = []
        self.velocity = []
        
        pos = []
        vel = []
        for i in range(dimension):
            vel.append(random.uniform(-1,1))
            pos.append(random.uniform(0,20))
        
        self.position.append(pos)
        self.velocity.append(vel)
        self.best = pos
        
    def update_velocity(self,global_best):
        
        w = 0.5;c1 = 0.5;c2 = 1
        vel=[]
        for i in range(len(self.best)):
            r1 = random.random()
            r2 = random.random()
            dim_vel = w*self.velocity[-1][i]+c1*r1*(self.best[i]-self.position[-1][i])+c2*r2*(global_best[i]-self.position[-1][i])
            vel.append(dim_vel)
            
        self.velocity.append(vel)
        
    def update_position(self):
        
        pos = []
        for i in range(len(self.best)):
            pos.append(self.position[-1][i]+self.velocity[-1][i])
        
        self.position.append(pos)
        
        for i in range(len(self.best)):
            if self.position[-1][i]>20.0:
                self.position[-1][i]=20.0
        
        for i in range(len(self.best)):
            if self.position[-1][i]<0.0:
                self.position[-1][i]=0.0
    
    def evaluate(self):
        
        fitness_now = fitness(self.position[-1])
        
        if fitness_now < fitness(self.best):
            self.best = self.position[-1]
        

if __name__ == "__main__":
    
    swarm = []
    no_swarm = 10
    max_iter = 100000
    
    for i in range(no_swarm):
        swarm.append(particle(2))
    
    all_best = [fitness(swarm[i].best) for i in range(no_swarm)]
    index,value = min(enumerate(all_best),key=operator.itemgetter(1))
    global_best = swarm[index].best
    
    print(fitness(swarm[index].best),swarm[index].best)
    
    for i in range(no_swarm):
        print(fitness(swarm[i].best),swarm[i].best)
    print('----')
    
    
    for i in range(max_iter):
        
        for j in range(no_swarm):
            swarm[j].evaluate()
            swarm[j].update_velocity(global_best)
            swarm[j].update_position()
            
        all_best = [fitness(swarm[i].best) for i in range(no_swarm)]
        index,value = min(enumerate(all_best),key=operator.itemgetter(1))
        global_best = swarm[index].best
            
    print(fitness(swarm[index].best),swarm[index].best)
    
    for i in range(no_swarm):
        print(fitness(swarm[i].best),swarm[i].best)
    
    for i in range(no_swarm):
        x_co,y_co = [],[]
        
        for j in range(len(swarm[i].position)):
            x_co.append(swarm[i].position[j][0])
            y_co.append(swarm[i].position[j][1])
            
        plt.plot(x_co,y_co)
    
    print('Global best : %f'%fitness(global_best))
        
        
        
        
        
        
        
        
        
        
        
    
        