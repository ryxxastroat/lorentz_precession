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

plt.rcParams['xtick.labelsize'] = 40
plt.rcParams['ytick.labelsize'] = 40
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



data1 = np.genfromtxt('mntp1.dat')
c0, c3, c4, c5, c6 = data1[:, 0], data1[:, 3], data1[:, 4], data1[:, 5], data1[:, 6]
Ntrim1 = 3333
c01=c0[:Ntrim1]
c31=c3[:Ntrim1]
c41=c4[:Ntrim1]
c51=c5[:Ntrim1]
c61=c6[:Ntrim1]

data11 = np.genfromtxt('mntp1_pset.dat')
cc0, cc1 = data11[:, 0], data11[:, 1]
data111 = np.genfromtxt('mntp1_widset.dat')
ccc0, ccc1, ccc2 = data111[:, 0], data111[:, 1], data111[:,2]


data2 = np.genfromtxt('mntp2.dat')
d0, d3, d4, d5, d6 = data2[:, 0], data2[:, 3], data2[:, 4], data2[:, 5], data2[:, 6]
Ntrim2 = 10000
d01=d0[:Ntrim2]
d31=d3[:Ntrim2]
d41=d4[:Ntrim2]
d51=d5[:Ntrim2]
d61=d6[:Ntrim2]

data22 = np.genfromtxt('mntp2_psetfil.dat')
dd0, dd1 = data22[:, 0], data22[:, 1]
data222 = np.genfromtxt('mntp2_widset.dat')
ddd0, ddd1, ddd2 = data222[:, 0], data222[:, 1], data222[:,2]

fig, ([[ax1,ax3],[ax2,ax4]]) = plt.subplots(2, 2,figsize=(12,10),sharex='col', sharey=False)
plt.subplots_adjust(hspace=0.0)

ax1.set_ylabel(r'$ P \,[t_c] $', fontsize=40)
ax2.set_ylabel(r'$ W/<\dot \Phi>\,[t_c] $', fontsize=40)
ax2.set_xlabel(r'$t \,[t_c]$', fontsize=40)
ax4.set_xlabel(r'$t \,[t_c]$', fontsize=40)
 
ax2.set_xlim([0,200])
ax4.set_xlim([0,600])
ax3.set_ylim([3.5,5])
ax4.set_ylim([0,4])
    
ax1.plot(cc0, cc1, 'bo')
ax1.plot(c01, c31)


ax2.plot(ccc0, ccc1, 'bo')
ax2.plot(c01, c41)


ax3.plot(dd0, dd1, 'bo')
ax3.plot(dd0, dd1)
#ax3.plot(d01, d51)


ax4.plot(ddd0, ddd1, 'bo')
ax4.plot(ddd0, ddd1)
#ax4.plot(d01, d61)


#ax1.legend(loc='best', fontsize=30)




plt.savefig("mnfig2.pdf", format='pdf', bbox_inches="tight")

plt.show()
