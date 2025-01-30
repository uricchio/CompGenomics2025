import random
import sys
import os
import numpy as np

class SimulateConservation():

    def __init__(self,popSize=100000,numSims=100,initFreq=0.999, s = 0.5, m = 0.2, h = 0.0):
   
        self.popSize = popSize
        self.numSims = numSims
        self.initFreq = initFreq
        self.s = s
        self.m = m
        self.h = h

        self.alleleTraj = []
        self.fitTraj = []

    def simDrift(self):  
        freq = self.initFreq
        self.alleleTraj.append(freq)
        while freq > 0 and freq < 1:
            freq = np.random.binomial(self.popSize, freq, 1)/self.popSize
            self.alleleTraj.append(freq)
        return
        
    def simSel(self):
       freq = self.initFreq
       while freq > 0 and freq < 1:
           # what should do in here? 
           freq = np.random.binomial(self.popSize, freq, 1)/self.popSize
           # do we want to use the same allele traj?
           self.alleleTraj.append(freq)
       return

    def simSelGeneFlow(self):
        freq = self.initFreq
        fitness = 1*(1-freq)**2 + (freq**2*(1-self.s) + 2*freq*(1-freq)*(1-self.s*self.h))
        self.alleleTraj.append(freq)
        self.fitTraj.append(fitness)
        for i in range(0,10):
        #while freq > 0 and freq < 1:
            # what should do in here? 
            delq = -self.m*freq - self.s*freq*(1-freq)*(self.h-(2*self.h-1)*freq)/(1-2*freq*(1-freq)*self.h*self.s+self.s*freq**2)  
            freq = np.random.binomial(self.popSize, freq+delq, 1)/self.popSize
            # do we want to use the same allele traj?
            self.alleleTraj.append(freq)
  
            fitness = 1*(1-freq)**2 + (freq**2*(1-self.s) + 2*freq*(1-freq)*(1-self.s*self.h))
            self.fitTraj.append(fitness)
            
            if i == 0:
                self.m = 0.025
        return      
 


