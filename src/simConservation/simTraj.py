import random
import sys
import os
import numpy as np

class SimulateConservation():

    def __init__(self,popSize=1000,numSims=100,initFreq=0.5, s = 0.5, m = 0.2, h = 0.0, w11 = 1.2, w12 = 1, w22=1):
   
        self.popSize = popSize
        self.numSims = numSims
        self.initFreq = initFreq
        self.s = s
        self.m = m
        self.h = h
        self.w11 = w11
        self.w12 = w12
        self.w22 = w22

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
           expFreq = ((freq**2)*self.w11 + freq*(1-freq)*self.w12) / (freq**2*self.w11 + 2*freq*(1-freq)*self.w12 + (1-freq)**2*self.w22)

           freq = np.random.binomial(self.popSize, expFreq, 1)/self.popSize
           # do we want to use the same allele traj?
           self.alleleTraj.append(freq)
       return


