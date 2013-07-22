import itertools
import numpy as np
from pylab import *

phi = 0.40

data = {}
data[r"HS$_1$ $\Delta \phi$"]     = "HS_N12/%s"
data[r"HS$^*_1$ $\Delta \phi$"]   = "HS_N13/%s"
data[r"SW$_1$ $\Delta \epsilon$"] = "SW_epsilon/%s"
data[r"SW$_2$ $\Delta \phi$"]     = "SW_phi_2well/%s"
data[r"SW$_1$ $\Delta \phi, \epsilon$"] = "SW_phiep/%s"
data[r"SW$_1$ $\Delta \phi$"] = "SW_phi_1well/%s"

phi_keys = [r"HS$_1$ $\Delta \phi$", 
            r"HS$^*_1$ $\Delta \phi$", 
            r"SW$_1$ $\Delta \phi$",
            r"SW$_2$ $\Delta \phi$"]

epsilon_keys = [r"SW$_1$ $\Delta \epsilon$"]

phi_ep_keys = [r"SW$_1$ $\Delta \phi, \epsilon$"]

def polyval2d(x, y, m):
    order = int(np.sqrt(len(m))) - 1
    ij = itertools.product(range(order+1), range(order+1))
    z = np.zeros_like(x)
    for a, (i,j) in zip(m, ij):
        z += a * x**i * y**j
    return z

for key in data:
    target_param = None

    loc = data[key]
    S  = np.loadtxt(loc%"svd_eigenvalues.txt")
    R  = np.loadtxt(loc%"svd_radial_points.txt")
    V  = np.loadtxt(loc%"svd_v_eigenvectors.txt")
    U_POLYS = np.loadtxt(loc%"svd_u_polynomials.txt")

    if key in phi_keys:
        target_param = 0.40
    if key in epsilon_keys:
        target_param = -1.0


    if key not in phi_ep_keys:
        U  = np.array([polyval(p,target_param)  for p in U_POLYS])
        label = "%s [%.4f]"%(key,target_param)
        #print U.shape, V.shape
    else:
        t1, t2 = 0.40, -1.0
        U = np.array([polyval2d(t1,t2,p) for p in U_POLYS])
        label = "%s [%.4f, %.4f]"%(key,t1,t2)
        #print U.shape, V.shape


    GR = np.dot(U.T,np.dot(np.diag(S),V))
    print R.shape, GR.shape
    plot(R,GR,label=label)

legend()
show()

