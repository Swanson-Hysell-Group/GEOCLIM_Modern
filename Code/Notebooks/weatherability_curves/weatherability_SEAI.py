import netCDF4 as nc
import numpy as np
from matplotlib import pyplot as plt
from cycler import cycler

####################################
##########   PARAMETERS   ##########
RECORD = True

# COLOR CYCLE - 5 colors
COLOR = ['royalblue','purple','firebrick','coral','gold']
plt.rc( 'axes', prop_cycle=cycler('color',COLOR) )

# FILES
f = list()
f.append( nc.Dataset('GDSS_GFDL_3lvl_ctrl.nc') )
f.append( nc.Dataset('GDSS_GFDL_3lvl_redIA5.nc') )
f.append( nc.Dataset('GDSS_GFDL_3lvl_redIA10.nc') )
f.append( nc.Dataset('GDSS_GFDL_3lvl_redIA.nc') )
f.append( nc.Dataset('GDSS_GFDL_3lvl_noIA.nc') )
####################################
####################################

####################################################

##  Plotting

fig, ax = plt.subplots(figsize=(9,6))
fig.delaxes(ax)
ax = fig.add_axes([0.11,0.13,0.87,0.85])

#--------------------------------------------------#

for fk in f:
    ax.plot( fk['atm_CO2_level'][:], 1e-12*fk['volcanic_degassing'][:], linestyle='-', marker='o', linewidth=3 )

ylim = [3.25, 5]
ax.set_ylim(ylim)

for k in range(len(f)):
    Slopemean = 1e-12 * (f[k]['volcanic_degassing'][-1]-f[k]['volcanic_degassing'][0])/2
    ax.text(900, ylim[0]+(0.4-(0.35/len(f))*k)*(ylim[1]-ylim[0]),
            '~{0:.2f} Tmol per 2xCO$_2$'.format(Slopemean), color=COLOR[k], fontsize=14)

ax.legend(['PD ctrl','5 Myr','10 Myr','15 Myr','no SEAI'], fontsize=15)
ax.set_xlabel('Atm. CO$_2$ (ppm)', fontsize=18)
ax.set_ylabel('Sil. weathering flux (Tmol of CO$_2$ / yr)', fontsize=18)
ax.tick_params(axis='both', labelsize=14)

####################################################

##  Drawing

if RECORD:
    fig.savefig('weatherability_SEAI.pdf', format='pdf', transparent=True)
else:
    plt.show()
