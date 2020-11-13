import numpy as np
import matplotlib.pyplot as plt

def simu(start,taux,nb_epochs,nb_last):
    """
    Make the simulation for the given parameters, and returns the given final value(s)
    """
    liste = [start]
    x = start
    for i in range (nb_epochs):
        x = taux*(x*(1-x))
        liste.append(x)
    return(list(set(np.round(liste[-nb_last:],4))))

#All the parameters that can be changed
start = 0.5
nb_epochs = 10000
nb_last = 100
number_of_steps = 10000
xmin = 3.568
xmax = 3.588
#y_limits should be either 'default' or a list of ymin and ymax like [0,1] 
y_limits = [0.3,0.6]
with_lines = True
save = True

for t in np.arange(xmin,xmax,(xmax-xmin)/number_of_steps):
    val = simu(start,t,nb_epochs,nb_last)
    plt.scatter([t]*len(val), val, s = 0.03, c = 'black', marker = '.')

plt.xlim([xmin, xmax])
if (len(y_limits)!='default'):
    plt.ylim(y_limits)

if with_lines:
    plt.axvline(x=1, ymin=0, ymax=1, c='r')
    plt.axvline(x=3, ymin=0, ymax=1, c='r')
    plt.axvline(x=3.57, ymin=0, ymax=1, c='r'   )

if save:
    name = str(nb_epochs) + '_' + str(nb_last) + '_' + str(number_of_steps) + '_' + str(xmin) + '_' + str(xmax) + '.png'
    plt.savefig(name)
    if with_lines:
        plt.axvline(x=1, ymin=0, ymax=1, c='r')
        plt.axvline(x=3, ymin=0, ymax=1, c='r')
        plt.axvline(x=3.57, ymin=0, ymax=1, c='r'   )
    name = str(nb_epochs) + '_' + str(nb_last) + '_' + str(number_of_steps) + '_' + str(xmin) + '_' + str(xmax) + '_withlines' '.png'
    plt.savefig(name)
    
if (with_lines and not save):
    plt.axvline(x=1, ymin=0, ymax=1, c='r')
    plt.axvline(x=3, ymin=0, ymax=1, c='r')
    plt.axvline(x=3.57, ymin=0, ymax=1, c='r'   )
    
plt.show()