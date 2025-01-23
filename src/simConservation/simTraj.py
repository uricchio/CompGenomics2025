import random
import sys
import os
import numpy as np

class SimulateConservation():

    def __init__(self,popSize=100,numSims=100,initFreq=0.7):
   
        self.popSize = popSize
        self.numSims = numSims
        self.initFreq = initFreq
        self.alleleTraj = []

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

   #def simInbreedDepression(self):
   #    freq = 
       
