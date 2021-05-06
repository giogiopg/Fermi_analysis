import astropy.io.fits as pyfits
import matplotlib.pyplot as plt
import numpy as np 
from tkinter import messagebox
import os

SEDbins = str(input('Number of bins of your SED : '))
wd = os.getcwd()

SED_file = pyfits.open('%s/advdata/SED%s.fits' % (wd,SEDbins))
#SED_file.info()

Pd = SED_file[1].data 
Ed = SED_file[2].data 
SED_file.close()

E = Ed['energy']
dnde = Ed['dnde']
dnde_hi = Ed['dnde_hi']
dnde_lo = Ed['dnde_lo']
Ec_points = Pd['e_ref']
Ex_error = Pd['e_max'] - Pd['e_min']
E2_dnde = Pd['e2dnde']
E2_dnde_err = Pd['e2dnde_err']
E2_dnde_ul = Pd['e2dnde_ul']
ts = Pd['ts']

plt.loglog(E, (E**2)*dnde, 'k--')
plt.loglog(E, (E**2)*dnde_hi, 'k')
plt.loglog(E, (E**2)*dnde_lo, 'k')
plt.errorbar(Ec_points,
             E2_dnde, 
             yerr=E2_dnde_err, xerr=Ex_error , fmt ='o')
plt.xlabel('E [MeV]')
plt.ylabel(r'E$^{2}$ dN/dE [MeV cm$^{-2}$ s$^{-1}$]')
plt.show()

#print(POINTS_data[1])
vect_generico = np.arange(int(SEDbins))
aux = []

for i in vect_generico:
      plt.loglog(E, (E**2)*dnde, 'k--')
      plt.loglog(E, (E**2)*dnde_hi, 'k')
      plt.loglog(E, (E**2)*dnde_lo, 'k')
      plt.errorbar(Ec_points,E2_dnde, yerr=E2_dnde_err, xerr=Ex_error , fmt ='o')
      plt.errorbar(Ec_points[i],E2_dnde[i], yerr=E2_dnde_err[i], xerr=Ex_error[i] , fmt ='ro')
      plt.show()
      ans=messagebox.askyesno('Information','Is point %i an upper limit?' % (i))
      if ans == 0:
            j = int(i)
            aux.append(j)
      
vect_si = np.array(aux)

vect_no = np.delete(vect_generico, vect_si)

try:
      plt.loglog(E, (E**2)*dnde, 'k--')
      plt.loglog(E, (E**2)*dnde_hi, 'k')
      plt.loglog(E, (E**2)*dnde_lo, 'k')
      plt.errorbar(Ec_points[vect_si],
                  E2_dnde[vect_si], 
                  yerr=E2_dnde_err[vect_si],
                  xerr=Ex_error[vect_si] ,
                   fmt ='o')
      plt.errorbar(Ec_points[vect_no],
                  E2_dnde_ul[vect_no],
                  yerr=0.4*E2_dnde[vect_no],
                  xerr=Ex_error[vect_no],
                  fmt='o', uplims=True)

      plt.xlabel('E [MeV]')
      plt.ylabel(r'E$^{2}$ dN/dE [MeV cm$^{-2}$ s$^{-1}$]')
      plt.show()
except:
      messagebox.showerror('Error', 'No has elegido ningun upper limit o ningun valor bien calculado.')

plt.bar(Ec_points, ts, width=0.2*Ec_points, ec='k')
plt.hlines(y=9.0, xmax=max(Ec_points)+100, xmin=min(Ec_points)-100, linewidth=1, linestyle='dashed', color='black')
plt.xlim(min(Ec_points)-100, max(Ec_points)+100)
plt.xlabel('E [MeV]')
plt.ylabel('TS')
plt.xscale('log')
plt.show()
