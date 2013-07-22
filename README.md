#  Supplementary Information

## Title
Singular Value Decomposition of the Radial Distribution Function for Hard Sphere and Square Well Potentials

## Journal
PLOS ONE

##  Author 
Travis Hoppe
National Institutes of Health, National Institute of Diabetes and Digestive and Kidney Diseases

## Copyright
All data is released under the Creative Commons 3.0 Attribution license
http://creativecommons.org/licenses/by/3.0/us/

# File formats
The reduced vectors for g(r) are stored in name/, see text
for a detailed description of the parameters used. Example Python programs
are provided that plot the extreme parameters of g(r) in `plot_extreme_gr.py` 
and the singular values in `plot_singular_values.py`. Programs require the 
libraries `numpy` and `matplotlib` to run.

## Number singular values used, k

    6 HS_N12
    6 HS_N13
    4 SW_epsilon
    5 SW_phi_1well
    5 SW_phi_2well
    6 SW_Phipps

### "svd_eigenvalues.txt"
List of the k singular values

    s_1
    s_2
    ...
	s_k

### "svd_u_polynomials.txt"
List of the polynomials to recreate the coefficient vectors `u(param)`

    p11 p12 p13 ... p1k
    p21 p22 p23 ... p2k
    ... ... ... ... ...
    pk1 pk2 pk3 ... pkk

Where each row represents the polynomial

    p11*x^(k+1) + p12*x^(k+0) + p13*x^(k-1) ... + p1k*x^(0)
	
The entries are zero-padded so they have equal columns.

For the two parameter system `SW_phiep`, the polynomials 
are stored differently to accommodate the higher dimensions.
Here row is the expansion of the coefficients to 

    \sum_i^(k+1) \sum_j^(k+1) a_(i,j)*x^i*y*^j
	
Where `x` represents the parameter `\phi` and `y` the parameter `epsilon` and
the matrix of coefficients `a(i,j)` is stored as a row flattened array

### "svd_radial_points.txt"
List of the `m` radial points for the basis vectors `v(r)`,
`r_1 = \sigma` and `r_m = 6\sigma`.

    r_1
	r_2
	...
	r_m

### "svd_v_eigenvectors.txt"
List of the `k` eigenvectors `v(r)`, each has length `m`

    v11 v12 ... v1m
	v21 v22 ... v2m
	... ... ... ...
	vk1 vk2 ... vkm
