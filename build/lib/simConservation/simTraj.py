import random
import sys
import os
import numpy as np


class SimulateConservation():

    def __init__(self,popSize=100,numSims=100,initFreq=0.5):
   
        self.popSize = popSize
        self.numSims = numSims
        self.initFreq = initFreq
        self.alleleTraj = []


    def simDrift(self):  

        freq = self.initFreq
        while freq > 0 and freq < 1:
            freq = np.random.binomial(self.popSize, freq, 1)/self.popSize
            self.alleleTraj.append(freq)

        
   
    

