import numpy as np
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt
from numpy import log10 as lg
from numpy import pi as pi
from scipy.interpolate import interp1d
from scipy.interpolate import splrep,splev
from scipy.integrate import odeint
from scipy.integrate import ode
import warnings
import timeit
import scipy.optimize as opt
from matplotlib import cm
from astropy import constants as const
from astropy import units as u
from mpl_toolkits.axes_grid1.inset_locator import zoomed_inset_axes
from mpl_toolkits.axes_grid1.inset_locator import mark_inset


import matplotlib.font_manager as font_manager

plt.rcParams['xtick.labelsize'] = 30
plt.rcParams['ytick.labelsize'] = 30
plt.rcParams['xtick.direction'] = 'in'
plt.rcParams['ytick.direction'] = 'in'
plt.rcParams['xtick.major.size'] = 8
plt.rcParams['ytick.major.size'] = 8
plt.rcParams['xtick.minor.size'] = 4
plt.rcParams['ytick.minor.size'] = 4
plt.rcParams['xtick.top'] = True
plt.rcParams['ytick.right'] = True
plt.rcParams['axes.labelpad'] = 8.0
plt.rcParams['figure.constrained_layout.h_pad'] = 0
plt.rcParams['text.usetex'] = True
plt.rc('text', usetex=True)
plt.tick_params(axis='both', which='minor', labelsize=18)
import matplotlib.ticker
from matplotlib.ticker import (MultipleLocator, FormatStrFormatter,
                               AutoMinorLocator)



data1 = np.genfromtxt('data3/mntp1.dat')
c0, c2, c3 = data1[:, 0], data1[:, 2], data1[:, 3]
Ntrim1 = 10000
c01=c0[:Ntrim1]
c21=c2[:Ntrim1]
c31=c3[:Ntrim1]


data11 = np.genfromtxt('data3/mntp1_pset.dat')
cc0, cc1 = data11[:, 0], data11[:, 1]
data111 = np.genfromtxt('data3/mntp1_widset.dat')
ccc0, ccc1 = data111[:, 0], data111[:, 1]


data2 = np.genfromtxt('data3/mntp2.dat')
d0, d2, d3 = data2[:, 0], data2[:, 2], data2[:, 3]
Ntrim2 = 10000
d01=d0[:Ntrim2]
d21=d2[:Ntrim2]
d31=d3[:Ntrim2]

data22 = np.genfromtxt('data3/mntp2_pset.dat')
dd0, dd1 = data22[:, 0], data22[:, 1]
data222 = np.genfromtxt('data3/mntp2_widset.dat')
ddd0, ddd1 = data222[:, 0], data222[:, 1]
spl1=splrep(dd0,dd1)
x1 = np.linspace(data22[0,0],  data22[len(data22)-1,0], 1000)
y1 = splev(x1,spl1)
spl2=splrep(ddd0,ddd1)
x2 = np.linspace(data222[0,0],  data222[len(data222)-1,0], 1000)
y2 = splev(x2,spl2)

fig, ([[ax1,ax3],[ax2,ax4]]) = plt.subplots(2, 2,figsize=(24,12),sharex='col', sharey=False)
plt.subplots_adjust(hspace=0.0)

ax1.set_ylabel(r'$ P \,[t_c] $', fontsize=30)
ax2.set_ylabel(r'$ W/\dot \Phi\,[t_c] $', fontsize=30)
ax2.set_xlabel(r'$t \,[t_c]$', fontsize=30)
ax4.set_xlabel(r'$t \,[t_c]$', fontsize=30)
 
ax2.set_xlim([0,200])
ax4.set_xlim([0,800])
ax1.set_ylim([3.1,4.7])
ax2.set_ylim([-0.1,1.3])
ax3.set_ylim([3.4,5.2])
ax4.set_ylim([-0.6,6.4])
    
ax1.plot(cc0, cc1, 'bo')
ax1.plot(c01, c21)


ax2.plot(ccc0, ccc1, 'bo')
ax2.plot(c01, c31)


ax3.plot(dd0, dd1, 'bo')
ax3.plot(x1,y1)
#ax3.plot(d01, d21)


ax4.plot(ddd0, ddd1, 'bo')
ax4.plot(x2,y2)
#ax4.plot(d01, d31)



#ax1.legend(loc='best', fontsize=30)
ax2.xaxis.set_minor_locator(MultipleLocator(10))
ax4.xaxis.set_major_locator(MultipleLocator(100))
ax4.xaxis.set_minor_locator(MultipleLocator(20))
ax1.yaxis.set_minor_locator(MultipleLocator(0.1))
ax2.yaxis.set_minor_locator(MultipleLocator(0.1))
ax3.yaxis.set_minor_locator(MultipleLocator(0.1))
ax4.yaxis.set_major_locator(MultipleLocator(2))
ax4.yaxis.set_minor_locator(MultipleLocator(0.4))

ax1.text(10, 4.5, 'solution tp-I', fontsize=30)
ax3.text(50, 4.95, 'solution tp-II', fontsize=30)

plt.savefig("mnfig2.pdf", format='pdf', bbox_inches="tight")

plt.show()
