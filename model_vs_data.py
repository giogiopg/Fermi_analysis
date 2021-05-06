import astropy.io.fits as pyfits
import matplotlib.pyplot as plt
import numpy as np 
import os

print('Currently only implemented for PowerLaw-kind spectra. Be aware you must have precomputed a SED first using this file.')
SEDname = str(input('Number of bins of your SED : '))
wd = os.getcwd()
try:
	SED_file = pyfits.open('%s/advdata/SED%s.fits' % (wd,SEDname))

	Pd = SED_file[1].data
	Ed = SED_file[2].data 
	SED_file.close()

	E = Ed['energy']
	#dnde = Ed['dnde']
	Ec_points = Pd['e_ref']
	Ex_error = Pd['e_max'] - Pd['e_min']
	dnde = Pd['dnde']
	dnde_err = Pd['dnde_err']

	Model_file = pyfits.open('%s/advdata/fit_model.fits' % (wd))
	data = Model_file[4].data
	Model_file.close()

	parametros = data['value']
	nombres = data['source_name']
	param_nombres = data['name']
	param_err = data['error']
	param_scale = data['scale']

	Prefactor = parametros[1]*param_scale[1]
	Prefactor_err = param_scale[1]*param_err[1]
	index = parametros[0]*param_scale[0]
	scale = parametros[2]*param_scale[2]

	print('Comprobación de que los parámetros del modelo estén bien:')
	print('(Prefactor)', nombres[1], param_nombres[1], Prefactor)
	print('(Prefactor_err)', nombres[1], param_nombres[1], Prefactor_err)
	print('(Index)', nombres[0], param_nombres[0], index)
	print('(Scale)', nombres[2], param_nombres[2], scale)


	PL = Prefactor*(E/scale)**index



	plt.plot(E, PL)
	plt.errorbar(Ec_points, dnde, yerr=dnde_err, fmt ='o')
	plt.xscale('log')
	plt.show()

	#error
	resids = dnde - Prefactor*(Ec_points/scale)**index
	resids_err = (dnde_err**2 + (Prefactor_err*(Ec_points/scale)**index)**2)**0.5 #+ (Prefactor*Ex_error*(Ec_points/scale)**(index-1))**2)**0.5

	plt.errorbar(Ec_points, resids, yerr=resids_err, fmt ='o')
	plt.hlines(y=0.0, xmax=max(Ec_points), xmin=min(Ec_points), linewidth=1, linestyle='dashed', color='green')
	plt.xscale('log')
	plt.show()
except:
	print('Error:  Sorry, maybe it is my fault, but I was unable to find the SEDs file. Make sure you have precomputed a SED with %s bins.' % (SEDname))

