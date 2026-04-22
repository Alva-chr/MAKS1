import numpy as np
import matplotlib.pyplot as plt
#Setting variables given from project description
r1 = 3.1
epsilon = 0.3
r_num = 30000
r2 = np.linspace(2.8,3.97,r_num)

x_plot = []
r_plot = []

x = np.ones((1,r_num))
x *= 0.5

y = np.ones((1,r_num))
y *= 0.5

x_current = 0
y_current = 0

x_next = 0
y_next = 0

plt.figure()
plt.xlabel('$r_2$',fontsize = 25)
plt.ylabel('x',fontsize = 25)
plt.title("Bifurcation diagram of the coupled system", fontsize = 25)

ax = plt.gca();

ax.text(
    0.02, 0.98,
    rf"{30000:d} parameter values" "\n"
    rf"{1000:d} transient iterates" "\n"
    rf"{600:d} recorded iterates" "\n"
    rf"set epsilon to {0.3:f} " "\n",
    transform = ax.transAxes,
    ha = 'left',
    va = 'top',
    bbox = dict(facecolor = 'white', alpha = 0.88, edgecolor = 'none')
  )

ax = plt.gca()
ax.set_xlim([2.7, 4])
ax.set_ylim([0.35, 0.85])

for j in range(len(r2)):
    print(str(round(100*j/len(r2), 1)) + "%")
    x_plot = []
    r_plot = []
    for i in range(1,1600):
        x_current = x[0][j]
        y_current = y[0][j]

        x_next = (1-epsilon)*r1*x_current*(1-x_current)+epsilon*r2[j]*y_current*(1-y_current)
        y_next = (1-epsilon)*r2[j]*y_current*(1-y_current)+epsilon*r1*x_current*(1-x_current)

        x[0][j] = x_next
        y[0][j] = y_next 
        
        if (i>1000):
            if (x_next not in x_plot):
                x_plot.append(x_next)
                r_plot.append(r2[j])
            else:
                break

    plt.scatter(r_plot, x_plot, color='black', marker = ',', lw=0, s=1)
    
plt.grid()
plt.show()