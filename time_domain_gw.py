import numpy as np
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt
from numpy import log10 as lg
from numpy import pi as pi
from scipy.interpolate import interp1d as sp_interp1d
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

plt.close()

import matplotlib.gridspec as gridspec
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(24,16))
gs = gridspec.GridSpec(2, 1, hspace=0.3)

names=['gwtp1','gwtp2']
labels=['solution tp-I','solution tp-II']
N=np.array([10000,10000])
lim=np.array([100,200])
ylim1=np.array([-0.45,-0.35])
ylim2=np.array([0.7,0.55])
ylim3=np.array([-0.45,-0.35])
ylim4=np.array([0.45,0.45])
yposition=np.array([0.5,0.4])
xminor=np.array([4,10])
color=['tab:blue','tab:green']

for i in range(2):
    gss = gridspec.GridSpecFromSubplotSpec(2, 1, subplot_spec=gs[i],
                                           hspace=0.0)
    
    data=np.genfromtxt('data3/'+names[i]+'.dat')
    c0, c1, c2= data[:, 0], data[:, 1], data[:, 2]
   
    c01=c0[:N[i]]
    c11=c1[:N[i]]
    c21=c2[:N[i]]
    
    ax0 = fig.add_subplot(gss[0])
    ax1 = fig.add_subplot(gss[1], sharex=ax0)
    ax0.plot(c01,c11, color = color[i])
    ax0.set_ylim(ylim1[i],ylim2[i])
    ax0.set_ylabel(r'$rh_+\,[t_{c}]$', fontsize=30)
    ax1.plot(c01,c21, color = color[i])
    ax1.set_xlabel(r'$t\,[t_{c}]$', fontsize=30)
    ax1.set_xlim(0,lim[i])
    ax1.set_ylim(ylim3[i],ylim4[i])
    ax1.set_ylabel(r'$rh_\times\,[t_{c}]$', fontsize=30)
    ax0.tick_params(axis="x", labelbottom=0)
    ax0.text(0.05*lim[i], yposition[i], labels[i], fontsize=30)
    ax0.yaxis.set_major_locator(MultipleLocator(0.5))
    ax0.yaxis.set_minor_locator(MultipleLocator(0.1))
    ax1.yaxis.set_major_locator(MultipleLocator(0.5))
    ax1.yaxis.set_minor_locator(MultipleLocator(0.1))
    ax1.xaxis.set_minor_locator(MultipleLocator(xminor[i]))
  
plt.savefig("gw.pdf", format='pdf', bbox_inches="tight")


