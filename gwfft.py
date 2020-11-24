import numpy as np
import matplotlib.pyplot as plt
from numpy import log10 as lg
import numpy as np
import matplotlib.pyplot as plt
import math
import matplotlib
from scipy.fftpack import fft,ifft

matplotlib.rcParams['xtick.labelsize'] = 30
matplotlib.rcParams['ytick.labelsize'] = 30
matplotlib.rcParams['xtick.direction'] = 'in'
matplotlib.rcParams['ytick.direction'] = 'in'
matplotlib.rcParams['xtick.major.size'] = 10
matplotlib.rcParams['ytick.major.size'] = 10
matplotlib.rcParams['xtick.minor.size'] = 6
matplotlib.rcParams['ytick.minor.size'] = 6
matplotlib.rcParams['xtick.top'] = True
matplotlib.rcParams['ytick.right'] = True
matplotlib.rcParams['axes.labelpad'] = 8.0
matplotlib.rcParams['figure.constrained_layout.h_pad'] = 0
plt.rcParams['text.usetex'] = True
plt.rc('text', usetex=True)
plt.tick_params(axis='both', which='major', labelsize=18)
plt.rcParams['font.sans-serif'] = ['Times New Roman']
plt.close()

from matplotlib.ticker import (MultipleLocator, FormatStrFormatter,
                               AutoMinorLocator)
from matplotlib.backends.backend_pdf import PdfPages

fig, (ax2, ax3) = plt.subplots(2, figsize=(14,14),sharex=True)
matplotlib.rcParams['xtick.labelsize'] = 30
matplotlib.rcParams['ytick.labelsize'] = 30
import matplotlib.font_manager as font_manager
from mpl_toolkits.axes_grid1.inset_locator import zoomed_inset_axes
from mpl_toolkits.axes_grid1.inset_locator import mark_inset

plt.subplots_adjust(hspace=0.0)

ax2.semilogx(2*np.pi*xf1, ps1, linewidth=2,color='b',linestyle='dotted',label='solution tp-I')
ax2.semilogx(2*np.pi*xf3, ps3, linewidth=1.5,color='tab:blue',label='solution tp-II')
# ax2.set_xlabel(r'$\rm{f_{GW}\,[{Hz}]}$',fontsize=25)

# ax2.set_ylim(1*1e-30,7*1e-23)



# ax2.set_xlabel(r'$\rm{f_{GW}\,[{Hz}]}$',fontsize=25)
ax2.set_ylabel(r'$\mathcal{F}\,(r\,h_{+})\,[t_{c}]$',fontsize=30)
# ax2.set_ylim(1*1e-30,7*1e-23)
# ax2.set_yticks([1e-29,1e-27,1e-25,1e-23])
# ax2.set_yticks([1e-6,1e-5,1e-4,1e-3, 1e-2,1e-1])
# locmin = matplotlib.ticker.LogLocator(base=10,subs=(0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9),numticks=12)
# ax2.yaxis.set_minor_locator(locmin)
# ax2.yaxis.set_minor_formatter(matplotlib.ticker.NullFormatter())
ax2.axvline(x=1.438,color='r',linestyle='dashed')
ax2.axvline(x=2*1.438,color='r',linestyle='dashed')
ax2.set_ylim(-0.02,0.29)
ax2.yaxis.set_minor_locator(MultipleLocator(0.05/5))
ax2.set_yticks([0,0.05,0.1,0.15,0.2,0.25])


ax3.semilogx(2*np.pi*xf4, ps4,linewidth=1.5,color='tab:blue')
ax3.semilogx(2*np.pi*xf2, ps2,linewidth=2,color='b',linestyle='dotted')

ax3.set_xlabel(r'$\rm Angular \ Frequency$\,$[1/t_c]$',fontsize=30)
ax3.set_ylabel(r'$\mathcal{F}\,(r\,h_{\times})\,[t_{c}]$',fontsize=30)
ax3.set_xlim(0.08*2*np.pi,1.2*2*np.pi)
# ax3.set_ylim(8.1e-6,7*1e-23)
# ax3.set_yticks([1e-29,1e-27,1e-25,1e-23])
ax3.axvline(x=1.438,color='r',linestyle='dashed')
ax3.axvline(x=2*1.438,color='r',linestyle='dashed')

plt.minorticks_on()
ax2.legend(fontsize=30, frameon=False,loc='upper left')
# fig.tight_layout() 
# plt.subplots_adjust(hspace=0)
sub_axes = plt.axes([0.70, .65, .18, .2]) 
sub_axes.plot(2*np.pi*xf3, ps3,linewidth=2) 
sub_axes.set_ylim(0,0.0036)
sub_axes.set_xlim(3.96,4.23)

sub_axes.tick_params(axis='both', which='major', labelsize=23)
sub_axes.set_xticks([4.0,4.1,4.2])
# sub_axes.grid(alpha=0.6)
# sub_axes.yaxis.set_minor_locator(MultipleLocator(0.05/2))
# sub_axes.xaxis.set_minor_locator(MultipleLocator(0.05/5))
mark_inset(ax2, sub_axes, loc1=3, loc2=4)
        
sub_axes = plt.axes([0.70, .28, .18, .2]) 
sub_axes.plot(2*np.pi*xf4, ps4,linewidth=2) 
sub_axes.set_ylim(0,0.0036)
sub_axes.set_xlim(3.96,4.23)

sub_axes.tick_params(axis='both', which='major', labelsize=23)
sub_axes.set_xticks([4.0,4.1,4.2])
# sub_axes.grid(alpha=0.6)
# sub_axes.yaxis.set_minor_locator(MultipleLocator(0.05/2))
# sub_axes.xaxis.set_minor_locator(MultipleLocator(0.05/5))
mark_inset(ax3, sub_axes, loc1=3, loc2=4)
        
plt.savefig("gwfft.pdf", format='pdf', bbox_inches="tight")
# with PdfPages('fft_gw.pdf') as pdf:
#     pdf.savefig(fig)