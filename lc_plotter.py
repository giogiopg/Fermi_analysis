from astropy.io import fits
import matplotlib.pyplot as plt
import numpy as np 
import os 

fuente = str(input('Your LC name: '))

wd = os.getcwd()

try:
	hdul = fits.open(wd+'/folder'+fuente+'_LC/'+fuente+'_LC_gtbary.fits')
	data = hdul[1].data

	tiempo = data['TIME']
	cuentas = data['COUNTS']
	exposition = data['EXPOSURE']
	error = data['ERROR']
	flux = cuentas/exposition
	flux_error = error/exposition

	hdul.close()
	#flux = flux[np.logical_not(np.isnan(flux))]
	i = np.argwhere(np.isnan(flux))
	flux = np.delete(flux, i)
	flux_error = np.delete(flux_error, i)
	tiempo = np.delete(tiempo, i)



	#limits
	maxtime = max(tiempo)
	mintime = min(tiempo)
	flux_median = np.median(flux[:-1])
	flux_dev = np.std(flux[:-1])

	plt.plot(tiempo[:-1], flux[:-1], color='navy', marker='o', markersize=6, linestyle='dashed', linewidth=2 )
	plt.errorbar(tiempo[:-1], flux[:-1], yerr=flux_error[:-1], color='blue', linestyle='dashed', linewidth=2 )
	plt.hlines(y=flux_median, xmax=maxtime, xmin=mintime, linewidth=2, linestyle='solid', color='black')
	plt.hlines(y=flux_median + 2*flux_dev, xmax=maxtime, xmin=mintime, linewidth=2, linestyle='dashed', color='silver')
	plt.hlines(y=flux_median - 2*flux_dev, xmax=maxtime, xmin=mintime, linewidth=2, linestyle='dashed', color='silver')

	plt.show()
except:
	print('Error:  Sorry, maybe it is my fault, but I was unable to find your file. Make sure you have precomputed a LC named %s.' % (fuente))