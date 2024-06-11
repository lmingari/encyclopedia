import matplotlib.pyplot as plt
import numpy as np

AN     = 0.0123
rho    = 1.293
rho_p  = 2650.0 /rho
g      = 9.81
gammas = [ 1.65, 3, 5]
lss    = ['-','--',':']

fig, ax = plt.subplots()

# Data for plotting
x = np.logspace(0,4, num=100)
d = x*1E-6
for gamma, ls in zip(gammas,lss):
    y = np.sqrt(AN*(rho_p*g*d + 1E-4*gamma/rho/d))
    ax.plot(x, y, 
            label = r'$\gamma={0:.2f}\times 10^{{-4}}~kg~s^{{-2}}$'.format(gamma),
            ls = ls,
            color='k',
            lw=2.0)

ax.legend(title='Experimental parameter')
ax.set(
#    title = 'Theoretical expression for idealized soils',
    xlabel=r'Particle size ($\mu m$)', 
    ylabel=r'Threshold friction velocity ($m~s^{-1}$)',
    xscale='log',
    ylim  = [0,1.5],
    xlim  = [1,1E4],
    )
ax.grid(ls=':',alpha=0.6)

fig.savefig("ust_th.png",bbox_inches='tight')
