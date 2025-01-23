
import matplotlib.pyplot as plt
from  simConservation import simTraj
import numpy as np 
     
newConsObj = simTraj.SimulateConservation()
newConsObj.simDrift()

plt.plot(np.arange(0,len(newConsObj.alleleTraj)), newConsObj.alleleTraj)
plt.show()

