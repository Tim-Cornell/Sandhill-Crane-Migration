import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
birddata = pd.read_csv("bird_tracking.csv") #make sure,you are in the right directory , check (>>>pwd)
Cranes = pd.unique(birddata.Crane) #look at the unique names of the cranes in the csv_file
''' To look at all the cranes trajectories, we plot each crane in the same plot '''
plt.figure(figsize = (7,7))
for Crane in Cranes:
    ix = birddata.Crane == Crane 
    x,y = birddata.X[ix], birddata.Y[ix]
    plt.plot(x,y,".", label=Crane)
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.legend(loc="lower left")
plt.show()