import numpy as np
from pylab import *

fs = "svd_eigenvalues.txt"

data = {}
data[r"HS$_1$ $\Delta \phi$"] = np.loadtxt("HS_N12/%s"%fs)
data[r"HS$^*_1$ $\Delta \phi$"] = np.loadtxt("HS_N13/%s"%fs)
data[r"SW$_1$ $\Delta \epsilon$"] = np.loadtxt("SW_epsilon/%s"%fs)
data[r"SW$_2$ $\Delta \phi$"] = np.loadtxt("SW_phi_2well/%s"%fs)
data[r"SW$_1$ $\Delta \phi, \epsilon$"] = np.loadtxt("SW_phiep/%s"%fs)
data[r"SW$_1$ $\Delta \phi$"] = np.loadtxt("SW_phi_1well/%s"%fs)

from itertools import cycle
marker_list = 'oDv^<>s1234sp*h+xD'
marker_iter = cycle(marker_list)

KEYS = sorted(data.keys())

fig = figure()
ax = subplot(111)
colors_list = cycle(['b','g','r','c','m','DarkOrange','k'])

for key in KEYS:
    S = data[key]

    SX = np.array(range(1,len(S)+1))
    S /= S[0]

    label = r"$\textrm{%s}$"%key
    semilogy(SX,S, marker=marker_iter.next(), 
             markersize=7,
             label=label, 
             markeredgewidth=0,
             color = colors_list.next())

xlabel(r"$n$")
ylabel(r"$\log \lambda_n / \lambda_1$")
xlim(xmin=.8,xmax=7)
ylim(10**-4,4)

ax.legend(ncol=2)

ax.xaxis.set_minor_locator(MultipleLocator(0.5))
ax.xaxis.set_major_locator(MultipleLocator(1.0))

fig.tight_layout()
show()
#savefig("render/SVD_singular_values.pdf")


