try:
	import tkinter as tk 
	from tkinter import messagebox
	from make4FGLxml import *
	try:
		from gt_apps import evtbin
	except:
		messagebox.showwarning('Warning','Activate your enviroment!!! (conda activate fermi)')

	#-----------------------gui----------------------------------------

	ALTURA = 700
	ANCHO = 800
	
	root = tk.Tk()
	
	canvas = tk.Canvas(root, height=ALTURA, width=ANCHO)
	canvas.grid()
	
	fondo_image = tk.PhotoImage(file='fondo.png')
	fondo_label = tk.Label(root, image=fondo_image)
	fondo_label.place(relwidth=1, relheight=1)
	
	topframe = tk.Frame(root, bg='black', bd=10)
	topframe.place(relwidth=0.9, relheight=0.1, relx=0.5, rely=0.1, anchor='n')
	
	label_black = tk.Label(topframe, text='-----', bg='black', fg='black')
	label_black.grid(row = 0, column=0)
	
	label_black = tk.Label(topframe, text='-----', bg='black', fg='black')
	label_black.grid(row = 0, column=1)
	
	label_black = tk.Label(topframe, text='-----', bg='black', fg='black')
	label_black.grid(row = 0, column=2)
	
	label_configtitle = tk.Label(topframe, text='Config file', bg='purple', fg='white')
	label_configtitle.grid(row = 0, column=3)
	
	button_configinfo = tk.Button(topframe, text='i', bg='blue', fg='white',
		                     command=lambda: config_info())
	button_configinfo.grid(row=1, column=3)
	
	label_black = tk.Label(topframe, text='---', bg='black', fg='black')
	label_black.grid(row = 0, column=4)
	
	label_gtliketitle = tk.Label(topframe, text='Para el análisis', bg='purple', fg='white')
	label_gtliketitle.grid(row = 0, column=5)
	
	button_gtlikeinfo = tk.Button(topframe, text='i', bg='blue', fg='white',
		                     command=lambda: gtlike_info())
	button_gtlikeinfo.grid(row=1, column=5)
	
	label_black = tk.Label(topframe, text='---', bg='black', fg='black')
	label_black.grid(row = 0, column=6)
	
	label_cmaptitle = tk.Label(topframe, text='CMAP and roi .reg', bg='purple', fg='white')
	label_cmaptitle.grid(row = 0, column=7)
	
	button_cmapinfo = tk.Button(topframe, text='i', bg='blue', fg='white',
		                     command=lambda: cmap_info())
	button_cmapinfo.grid(row=1, column=7)
	
	label_black = tk.Label(topframe, text='---', bg='black', fg='black')
	label_black.grid(row = 0, column=8)
	
	label_residtitle = tk.Label(topframe, text='Resid, Ts maps', bg='purple', fg='white')
	label_residtitle.grid(row = 0, column=9)
	
	button_residinfo = tk.Button(topframe, text='i', bg='blue', fg='white',
		                     command=lambda: resid_info())
	button_residinfo.grid(row=1, column=9)
	
	label_black = tk.Label(topframe, text='---', bg='black', fg='black')
	label_black.grid(row = 0, column=10)
	
	label_SEDtitle = tk.Label(topframe, text='SED', bg='purple', fg='white')
	label_SEDtitle.grid(row = 0, column=11)
	
	button_SEDinfo = tk.Button(topframe, text='i', bg='blue', fg='white',
		                     command=lambda: SED_info())
	button_SEDinfo.grid(row=1, column=11)
	
	label_black = tk.Label(topframe, text='---', bg='black', fg='black')
	label_black.grid(row = 0, column=12)
	
	label_LCtitle = tk.Label(topframe, text='LC create', bg='purple', fg='white')
	label_LCtitle.grid(row = 0, column=13)
	
	button_LCinfo = tk.Button(topframe, text='i', bg='blue', fg='white',
		                     command=lambda: LCmake_info())
	button_LCinfo.grid(row=1, column=13)
	
	label_black = tk.Label(topframe, text='---', bg='black', fg='black')
	label_black.grid(row = 0, column=14)
	
	label_LCfiletitle = tk.Label(topframe, text='LC file', bg='purple', fg='white')
	label_LCfiletitle.grid(row = 0, column=15)
	
	button_LCfileinfo = tk.Button(topframe, text='i', bg='blue', fg='white',
		                     command=lambda: LCfile_info())
	button_LCfileinfo.grid(row=1, column=15)
	
	label_black = tk.Label(topframe, text='---', bg='black', fg='black')
	label_black.grid(row = 0, column=16)
	
	
	label_setuptitle = tk.Label(topframe, text='Setup', bg='purple', fg='white')
	label_setuptitle.grid(row = 0, column=17)
	
	button_setupinfo = tk.Button(topframe, text='i', bg='blue', fg='white',
		                     command=lambda: setup_info())
	button_setupinfo.grid(row=1, column=17)
	
	subframe = tk.Frame(root, bg='black', bd=10)
	subframe.place(relwidth=1.0, relheight=0.45, relx=0.5, rely=0.3, anchor='n')
	
	label_mail = tk.Label(subframe, text='Enter your email:', bg='black', fg='white')
	label_mail.grid(row = 0, column=0)
	
	entry_mail = tk.Entry(subframe, bg='gray')
	entry_mail.grid(row = 0, column=1)
	
	label_password = tk.Label(subframe, text='Password:', bg='black', fg='white')
	label_password.grid(row = 0, column=2)
	
	entry_password = tk.Entry(subframe, bg='gray', show='*')
	entry_password.grid(row = 0, column=3)
	
	label_target = tk.Label(subframe, text='Target:', bg='black', fg='white')
	label_target.grid(row = 1, column=0)
	
	entry_target = tk.Entry(subframe, bg='gray')
	entry_target.grid(row = 1, column=1)
	
	label_scfile = tk.Label(subframe, text='SC_file:', bg='black', fg='white')
	label_scfile.grid(row = 1, column=2)
	
	entry_scfile = tk.Entry(subframe, bg='gray')
	entry_scfile.grid(row = 1, column=3)
	
	label_tmin = tk.Label(subframe, text='tmin (MET):', bg='black', fg='white')
	label_tmin.grid(row = 2, column=0)
	
	entry_tmin = tk.Entry(subframe, bg='gray')
	entry_tmin.grid(row = 2, column=1)
	
	label_tmax = tk.Label(subframe, text='tmax (MET):', bg='black', fg='white')
	label_tmax.grid(row = 2, column=2)
	
	entry_tmax = tk.Entry(subframe, bg='gray')
	entry_tmax.grid(row = 2, column=3)
	
	label_Emin = tk.Label(subframe, text='Emin (MeV):', bg='black', fg='white')
	label_Emin.grid(row = 3, column=0)
	
	entry_Emin = tk.Entry(subframe, bg='gray')
	entry_Emin.grid(row = 3, column=1)
	
	label_Emax = tk.Label(subframe, text='Emax (MeV):', bg='black', fg='white')
	label_Emax.grid(row = 3, column=2)
	
	entry_Emax = tk.Entry(subframe, bg='gray')
	entry_Emax.grid(row = 3, column=3)
	
	label_evfile = tk.Label(subframe, text='Events file:', bg='black', fg='white')
	label_evfile.grid(row = 4, column=0)
	
	entry_evfile = tk.Entry(subframe, bg='gray')
	entry_evfile.grid(row = 4, column=1)
	
	label_freerad = tk.Label(subframe, text='Free rad (deg):', bg='black', fg='white')
	label_freerad.grid(row = 5, column=0)
	
	entry_freerad = tk.Entry(subframe, bg='gray')
	entry_freerad.grid(row = 5, column=1)
	
	label_tol = tk.Label(subframe, text='Tolerancia', bg='black', fg='white')
	label_tol.grid(row = 5, column=2)
	
	entry_tol = tk.Entry(subframe, bg='gray')
	entry_tol.grid(row = 5, column=3)
	
	label_ra = tk.Label(subframe, text='RA (deg):', bg='black', fg='white')
	label_ra.grid(row = 6, column=0)
	
	entry_ra = tk.Entry(subframe, bg='gray')
	entry_ra.grid(row = 6, column=1)
	
	label_dec = tk.Label(subframe, text='DEC (deg):', bg='black', fg='white')
	label_dec.grid(row = 6, column=2)
	
	entry_dec = tk.Entry(subframe, bg='gray')
	entry_dec.grid(row = 6, column=3)
	
	label_index = tk.Label(subframe, text='Index:', bg='black', fg='white')
	label_index.grid(row = 7, column=0)
	
	entry_index = tk.Entry(subframe, bg='gray')
	entry_index.grid(row = 7, column=1)
	
	label_SEDnbins = tk.Label(subframe, text='SED nbins:', bg='black', fg='white')
	label_SEDnbins.grid(row = 7, column=2)
	
	entry_SEDnbins = tk.Entry(subframe, bg='gray')
	entry_SEDnbins.grid(row = 7, column=3)
	
	label_author = tk.Label(subframe, text='Author: giogio', bg='black', fg='purple')
	label_author.grid(row = 8, column=0)
	
	label_black = tk.Label(subframe, text='', bg='black', fg='black')
	label_black.grid(row = 9, column=0)
	
	label_LCname = tk.Label(subframe, text='Exclusive for LC:', bg='black', fg='purple')
	label_LCname.grid(row = 0, column=5)
	
	label_LCname = tk.Label(subframe, text='LC name:', bg='black', fg='white')
	label_LCname.grid(row = 1, column=4)
	
	entry_LCname = tk.Entry(subframe, bg='gray')
	entry_LCname.grid(row = 1, column=5)
	
	label_LCnbins = tk.Label(subframe, text='LC nbins:', bg='black', fg='white')
	label_LCnbins.grid(row = 2, column=4)
	
	entry_LCnbins = tk.Entry(subframe, bg='gray')
	entry_LCnbins.grid(row = 2, column=5)
	
	label_LCemin = tk.Label(subframe, text='LC Emin:', bg='black', fg='white')
	label_LCemin.grid(row = 3, column=4)
	
	entry_LCemin = tk.Entry(subframe, bg='gray')
	entry_LCemin.grid(row = 3, column=5)
	
	label_LCemax = tk.Label(subframe, text='LC Emax:', bg='black', fg='white')
	label_LCemax.grid(row = 4, column=4)
	
	entry_LCemax = tk.Entry(subframe, bg='gray')
	entry_LCemax.grid(row = 4, column=5)
	
	
	
	
	button_config = tk.Button(subframe, text='Crate Config file', bg='gray', fg='black',
				              command=lambda: config_func(entry_target.get(), entry_tmin.get(),
				              	entry_tmax.get(), entry_scfile.get(), entry_Emin.get(),
				              	entry_Emax.get(), entry_evfile.get()))
	button_config.grid(row=11, column=0)
	
	button_analysis = tk.Button(subframe, text='  Analysis  ', bg='gray', fg='black',
		                        command=lambda: analysis_func(entry_target.get(), entry_freerad.get(),
		                        	entry_tol.get()))
	button_analysis.grid(row=11, column=1)
	
	button_cmap = tk.Button(subframe, text='CMAP and Roi.reg', bg='gray', fg='black',
		                    command=lambda: cmap_func(entry_mail.get(), entry_password.get(), entry_evfile.get(),
		                    	entry_ra.get(), entry_dec.get(), entry_tmin.get(), entry_tmax.get(),
		                    	entry_scfile.get(), entry_freerad.get()))
	button_cmap.grid(row=11, column=2)
	
	button_Residuals = tk.Button(subframe, text='Residuals plot', bg='gray', fg='black',
		                         command=lambda: residual_func(entry_target.get(), entry_index.get()))
	button_Residuals.grid(row=11, column=3)
	
	button_Ts = tk.Button(subframe, text='  Ts map  ', bg='gray', fg='black',
		                  command=lambda: ts_func(entry_target.get(), entry_index.get()))
	button_Ts.grid(row=12, column=0)
	
	button_Tsns = tk.Button(subframe, text='Ts map no source', bg='gray', fg='black',
		                   command=lambda: ts_func(entry_target.get(), entry_index.get()))
	button_Tsns.grid(row=12, column=1)
	
	button_SED = tk.Button(subframe, text=' SED analysis ', bg='gray', fg='black',
		                   command=lambda: SED_func(entry_target.get(), entry_SEDnbins.get()))
	button_SED.grid(row=12, column=2)
	
	button_setup = tk.Button(subframe, text='Setup files for analysis', bg='gray', fg='black',
		                     command=lambda: setup_func(entry_mail.get(), entry_password.get()))
	button_setup.grid(row=12, column=3)
	
	button_LCfile = tk.Button(subframe, text='Make LC file', bg='gray', fg='black',
		                     command=lambda: LCfile_func(entry_LCname.get(), entry_evfile.get(),entry_ra.get(), entry_dec.get(),
		                     	entry_LCemin.get(), entry_LCemax.get(), entry_tmin.get(), entry_tmax.get(),
		                     	entry_scfile.get(), entry_LCnbins.get()))
	button_LCfile.grid(row=11, column=4)
	
	button_LC = tk.Button(subframe, text='Make LC', bg='gray', fg='black',
		                     command=lambda: LC_func(entry_mail.get(), entry_password.get(), entry_LCname.get()))
	button_LC.grid(row=12, column=4)

	button_sourceinfo = tk.Button(subframe, text='Print target info', bg='purple', fg='white',
		                     	command=lambda: sourcegetinfo_func(entry_target.get()))
	button_sourceinfo.grid(row=12, column=5)

	button_sourceinfoinfo = tk.Button(subframe, text='i', bg='blue', fg='white',
		                     	command=lambda: sinfoinfo_info())
	button_sourceinfoinfo.grid(row=12, column=6, sticky='W')




	
	button_nbinsinfo = tk.Button(subframe, text='i', bg='blue', fg='white',
		                     command=lambda: sednbins_info())
	button_nbinsinfo.grid(row=7, column=4, sticky='W')
	
	button_emailinfo = tk.Button(subframe, text='i', bg='blue', fg='white',
		                     command=lambda: mail_info())
	button_emailinfo.grid(row=0, column=4, sticky='W')
	
	results_frame = tk.Frame(root, bg='purple', bd=10)
	results_frame.place(relx=0.5,rely=0.80, relwidth=0.9, relheight=0.1, anchor='n')
	
	label_results = tk.Label(results_frame, anchor='nw', justify='left', bd=4)
	label_results.place(relwidth=1, relheight=1)

	messagebox.showwarning('Warning', 'Remember that all the input should be written whith no blanks')
	
	def config_info():
		messagebox.showinfo('Information','Needed data to perform the Config file: target, tmin, tmax, emin, emax, scfile, evfile')
	def sednbins_info():
		messagebox.showinfo('Information','nbins must be an intenger. Allowed inputs are: 2, 3, 5, 6, 10, 15 and 30')
	def mail_info():
		messagebox.showinfo('Information','Performing setup takes several hours. Giving your email and pw is optional and only required to recieve a message when the proccess is done.')
	def gtlike_info():
		messagebox.showinfo('Information','Needed data to perform the Analysis: target, freerad, tolerance and having create the config and run the setup.')
	def cmap_info():
		messagebox.showinfo('Information','Needed data to perform the Cmap and Roi.reg: mail*,password*, evfile, ra,dec,tmin, tmax,scfile, freerad')
	def resid_info():
		messagebox.showinfo('Information','Needed data to perform the residual, Ts, and Tsns maps: target, index')
	def SED_info():
		messagebox.showinfo('Information','Needed data to perform the SED: target, SEDnbins')
	def LCfile_info():
		messagebox.showinfo('Information','Needed data to perform the LCfile: LCname, evfile, ra, dec, LCEmin, LCEmax, tmin, tmax, scfile, LCnbins')
	def LCmake_info():
		messagebox.showinfo('Information','Needed data to perform the LC: email*, password*, LCname and having created LC file.')
	def setup_info():
		messagebox.showinfo('Information','Needed data to setup all files for analysis: mail*, password*, having create config file.')
	def sinfoinfo_info():
		messagebox.showinfo('Information','This button prints information about a source from the catalog made in the fit. Be aware you need to have performed an analysis and provide your target.')
	def sourcegetinfo_func(entry_target):
		import astropy.io.fits as pyfits
		import matplotlib.pyplot as plt
		import numpy as np 
		import os

		messagebox.showwarning('Warning', 'If no source or incorrect name selected no results will be printed.')

		fuente = str(entry_target)
		J_all = fuente[4:]
		wd = os.getcwd()
		j = 0

		Model_file = pyfits.open('%s/advdata/fit_model.fits' % (wd))
		data = Model_file[4].data
		data_cat = Model_file[1].data
		Model_file.close()
		parametros = data['value']
		nombres = data['source_name']
		spect_type = data['type']
		source_type = data['group']
		param_nombres = data['name']
		param_err = data['error']
		param_scale = data['scale']
		
		nombres_cat = data_cat['name']
		spect_type_cat = data_cat['SpectrumType']
		GLAT = data_cat['GLAT']
		GLON = data_cat['GLON']
		RAJ2000 = data_cat['RAJ2000']
		DEJ2000 = data_cat['DEJ2000']
		ts = data_cat['ts']
		loglikelihood = data_cat['loglike']
		npred = data_cat['npred']
		offset = data_cat['offset']
		flux = data_cat['flux']
		fluxerr = data_cat['flux_err']
		print('-----------------------------Model params--------------------------------------')
		for i in range(len(nombres)):
			if nombres[i] ==  '4FGL '+J_all:
				if j < 2:
					print(nombres[i], source_type[i], spect_type[i], param_nombres[i], parametros[i]*param_scale[i], '+/-', param_err[i]*param_scale[i])
				if param_nombres[i] == 'Index' and spect_type[i] == 'PowerLaw':
					j = j + 1
				elif param_nombres[i] == 'Eb' and spect_type[i] == 'LogParabola':
					j = j + 1
				elif param_nombres[i] == 'Expfactor' and spect_type[i] == 'PLSuperExpCutoff2':
					j = j + 1

		for i in range(len(nombres_cat)):
			if nombres_cat[i] == '4FGL '+J_all:
				print('-----------------------------Catalog params--------------------------------------')
				print(nombres_cat[i], '\n', spect_type_cat[i])
				print('Equatorial coordinates (RAJ2000, DECJ2000: [', RAJ2000[i],',',DEJ2000[i],']')
				print('Galactic coordinates (GLON, GLAT): [', GLON[i],',',GLAT[i],']')
				print('TS: ', ts[i], '\nloglikelihood: ',loglikelihood[i], '\nnpred: ', npred[i], '\noffset: ', offset[i])
				print('Flux: ',flux[i], '+/-', fluxerr[i])

		label_results['text'] = 'Long output. It has been printed in the terminal.'



	def LC_func(entry_mail, entry_password, entry_LCname):
		ans=messagebox.askyesno('Warning','It will take a while. Is advisable to run in the terminal instead via ". (LCname)_LC_commands.txt" where LC_name is the name you have provided. Do you want to continue anyway?')
		if ans == 1:
			import subprocess
			import yagmail
	
			if entry_mail == '':
				messagebox.showwarning('Warning', 'No has dado ninguna direccion de correo.\n No se enviará un mensaje al terminar.')
			else:
				receiver = entry_mail
				yag = yagmail.SMTP(entry_mail, entry_password)
			command = '%s_LC_commands.txt' % (entry_LCname)
			subprocess.call(['sh',command])
			if entry_mail == '':
				label_results['text'] = 'Setup done.'
			else:
				try:
					yag.send(to=receiver, subject='FERMI NOTIFICATION', contents='Ha terminado la LC'+entry_LCname)
				except:
					messagebox.showerror('Error', 'Invalid email adress. It is also possible that you have to give your google account spetial conditions of privacy. You will have received a google alert in this case.')
		else:
			label_results['text'] = 'Proccess cancelled. Copy to run: . %s_LC_commands.txt' % (entry_LCname)
	
	
	def LCfile_func(entry_LCname, entry_evfile, entry_ra, entry_dec, entry_LCemin, entry_LCemax, entry_tmin, entry_tmax, entry_scfile, entry_LCnbins):
		import os
	
		name = str(entry_LCname)
		ra = str(entry_ra)
		dec = str(entry_dec)
		emin = str(entry_LCemin)
		emax = str(entry_LCemax)
		tmin = float(entry_tmin)
		tmax = float(entry_tmax)
		scfile=str(entry_scfile)
		nbins = float(entry_LCnbins)
		evfile = str(entry_evfile)
		wd = os.getcwd()
	
		tmin_corr = tmin + 1000
		tmax_corr = tmax - 1000
		binsz = str(round((tmax_corr - tmin_corr)/nbins,0))
		
	
	
		file1 = open(name+'_LC_commands.txt','w+')
	
		#first gtselect
		file1.write('gtselect zmax=90 emin='+emin+' emax='+emax+
			' infile=@'+evfile+' outfile='+name+'_'+ra+'_'+dec+'_LC_gtsel.fits'+
			' ra='+ra+' dec='+dec+' rad=1 tmin='+str(tmin_corr)+' tmax='+str(tmax_corr)+' evclass=128 evtype=3 \n')
	
		file1.write('gtmktime scfile='+scfile+' filter="(DATA_QUAL==1)'+ 
			' && ABS(ROCK_ANGLE)<90 && (LAT_CONFIG==1) && (angsep(RA_ZENITH,DEC_ZENITH,'+ra+','+dec+')+1<105)'+ 
			' && (angsep('+ra+','+dec+',RA_SUN,DEC_SUN)>5+1) &&(angsep('+ra+','+dec+',RA_SCZ,DEC_SCZ)<180)"'+ 
			' roicut=yes evfile='+name+'_'+ra+'_'+dec+'_LC_gtsel.fits'+
			' outfile='+name+'_'+ra+'_'+dec+'_LC_gtmktime.fits \n')
	
		file1.write('gtbin algorithm=LC evfile='+name+'_'+ra+'_'+dec+'_LC_gtmktime.fits'+
			' outfile='+name+'_'+ra+'_'+dec+'_LC_gtbin.fits scfile='+scfile+' tbinalg=LIN tstart='+str(tmin_corr)+
			' tstop='+str(tmax_corr)+' dtime='+binsz+' \n')
	
		file1.write('gtexposure infile='+name+'_'+ra+'_'+dec+'_LC_gtbin.fits'+
			' scfile='+scfile+' irfs=P8R3_SOURCE_V2 srcmdl="none" specin=-2.1 \n')
	
		file1.write('gtbary evfile='+name+'_'+ra+'_'+dec+'_LC_gtbin.fits outfile='+
			name+'_LC_gtbary.fits scfile='+scfile+' ra='+ra+' dec='+dec+' tcorrect=BARY \n')
	
		file1.write('mkdir folder'+name+'_LC \n')
	
		file1.write('scp -r '+wd+'/'+name+'_LC_gtbary.fits '+wd+'/folder'+name+'_LC/ \n')
	
		file1.write('scp -r '+wd+'/'+name+'_LC_commands.txt '+wd+'/folder'+name+'_LC/ \n')
	
		file1.write('rm '+name+'_'+ra+'_'+dec+'_LC_gtsel.fits '
			+name+'_'+ra+'_'+dec+'_LC_gtmktime.fits '
			+name+'_'+ra+'_'+dec+'_LC_gtbin.fits '
			+name+'_LC_gtbary.fits '+name+'_LC_commands.txt \n')
	
		file1.close()
	
		label_results['text'] = 'Done. Check terminal to see temporal bins.'
		print('Los bines elegidos son los siguientes:')
	
		t1 = tmin_corr
		bin_size = float(binsz)
		while t1 <= tmax_corr:
			t2 = t1
			t1 += bin_size
			print('[',t2,',',t1,']')
	
	
	
	
	
	def config_func(entry_target, entry_tmin, entry_tmax, entry_scfile, entry_Emin,entry_Emax,entry_evfile):
		try:
			congfile = open('config.yaml','w+')
	
			congfile.write('data:\n  evfile : %s \n  scfile : %s \n' % (entry_evfile, entry_scfile))
			congfile.write('\n')
			congfile.write('binning:\n  roiwidth   : 15.0\n  binsz      : 0.1\n  binsperdec : 8\n ')
			congfile.write('\n')
			congfile.write('selection :\n  emin : %s \n  emax : %s \n  zmax    : 90\n  evclass : 128\n  evtype  : 3\n  tmin    : %s \n  tmax    : %s \n  filter  : \'DATA_QUAL>0 && LAT_CONFIG==1\' \n  target : \'%s\' \n' % (entry_Emin,entry_Emax,entry_tmin, entry_tmax,entry_target))
			congfile.write('\n')
			congfile.write('gtlike:\n  edisp : True\n  irfs : \'P8R3_SOURCE_V3\'\n')
			congfile.write('\n')
			congfile.write('model:\n  src_roiwidth : 20.0\n  galdiff  : \'gll_iem_v07.fits\'\n  isodiff  : \'iso_P8R3_SOURCE_V3_v1.txt\'\n  catalogs : [\'gll_psc_v27.fit\']\n')
			congfile.write('\n')
			congfile.write('components:\n  - { selection : { evtype : 4  } } \n  - { selection : { evtype : 8  } } \n  - { selection : { evtype : 16 } } \n  - { selection : { evtype : 32 } }\n')
			congfile.write('\n')
			congfile.write('fileio:\n  outdir : advdata')
			congfile.close()
	
			label_results['text'] = 'Done.'
		except:
			label_results['Unable to proceed, check that the inputs are okay.']
	
	
	def analysis_func(entry_target, entry_freerad, entry_tol):
		import matplotlib.pyplot as plt 
		import matplotlib
		import numpy as np
		from fermipy.gtanalysis import GTAnalysis
	
		messagebox.showinfo('Information','Loading...')
	
		gta = GTAnalysis.create('advdata/prefit_model.npy')
	
		#Borramos las fuentes con TS<3
		deleted_sources = gta.delete_sources(minmax_ts=[-1,3])
	
		# Free Normalization of all Sources within 3 deg of ROI center
		gta.free_sources(distance=float(entry_freerad) ,pars='norm')
		# Free sources with TS > 10
		#gta.free_source('4FGL J0534.5+2201s')
		gta.free_sources(minmax_ts=[10,None],pars='norm')
		# Free all parameters of isotropic and galactic diffuse components
		gta.free_source('galdiff')
		gta.free_source('isodiff')
	
	
		gta.fit(min_fit_quality=2, optimizer='NEWMINUIT', tol=float(entry_tol), maxit=30)
	
		print('---------------TRAS EL AJUSTE---------------------')
		gta.print_roi()
		print(gta.roi[entry_target])
	
		label_results['text'] = 'Analysis done. \nCheck your ROI in terminal. \nMake sure Fit Quality=3 and Fit Statatus=0.'
		ans = messagebox.askyesno('Question', 'Save the results?')
	
		if ans == 1:
			gta.write_roi('fit_model')
			label_results['text'] = 'Results saved'
		else:
			label_results['text'] = 'No has guardado los resultados'
	
	def setup_func(entry_mail, entry_password):
		import matplotlib.pyplot as plt 
		import matplotlib
		import numpy as np
		from fermipy.gtanalysis import GTAnalysis
		import yagmail
		import time
	
		ans=messagebox.askyesno('Warning','It will take a while. Is advisable to run in the terminal instead via "python3 setup.py". Do you want to continue anyway?')
	
		if ans == 1:
			if entry_mail == '':
				messagebox.showwarning('Warning', 'No has dado ninguna direccion de correo.\n No se enviará un mensaje al terminar.')
			else:
				receiver = entry_mail
				yag = yagmail.SMTP(entry_mail, entry_password)
	
			start = time.time()
	
			gta = GTAnalysis('config.yaml',logging={'verbosity' : 3})
			gta.setup()
			gta.optimize()
	
			end = time.time()
			elapsed_min = round((end-start)/60.0,0)
			elapsed = str(elapsed_min)
	
			gta.write_roi('prefit_model')
			if entry_mail == '':
				label_results['text'] = 'Setup done.'
			else:
				try:
					yag.send(to=receiver, subject='FERMI NOTIFICATION', contents='Ha terminado el setup. Ha tardado '+elapsed+'mins.')
				except:
					messagebox.showerror('Error', 'Invalid email address')
		else: 
			label_results['text'] = 'Proccess canceled. Copy to run: python3 setup.py on the terminal'
	
	def cmap_func(entry_mail, entry_password, entry_evfile, entry_ra, entry_dec, entry_tmin, entry_tmax, entry_scfile, entry_freerad ):
		from gt_apps import filter
		from gt_apps import maketime
		from gt_apps import evtbin
		#from make4FGLxml import *
		import yagmail
	
		if entry_mail == '':
			messagebox.showerror('Error', 'Invalid email address. It is also possible that you have to give your google account spetial conditions of privacy. You will have received a google alert in this case.')
		else:
			receiver = entry_mail
			yag = yagmail.SMTP(entry_mail, entry_password)
	
		nombre = 'CMAPfile'
		ra = float(entry_ra)
		dec = float(entry_dec)
		tmin = int(entry_tmin)
		tmax = int(entry_tmax)
		scfile=str(entry_scfile)
	
		filter['infile'] = '@'+entry_evfile
		filter['outfile'] = nombre+'_gtselect.fits'
		filter['ra'] = ra
		filter['dec'] = dec
		filter['rad'] = 15
		filter['tmin'] = tmin
		filter['tmax'] = tmax
		filter['emin'] = 100
		filter['emax'] = 500000
		filter['zmax'] = 90
		filter['evclass'] = 128
		filter['evtype'] = 3
		filter.run()
	
		maketime['evfile'] = nombre+'_gtselect.fits'
		maketime['outfile'] = nombre+'_mktime.fits'
		maketime['scfile'] = scfile
		maketime['filter'] = 'DATA_QUAL>0 && LAT_CONFIG==1'
		maketime['apply_filter'] = 'yes'
		maketime['roicut'] = 'no'
	
		maketime.run()
	
		evtbin['algorithm'] = 'CMAP'
		evtbin['evfile'] = nombre+'_mktime.fits'
		evtbin['outfile'] = nombre+'_cmap.fits'
		evtbin['nxpix'] = 100
		evtbin['nypix'] = 100
		evtbin['binsz'] = 0.2
		evtbin['coordsys'] = 'CEL'
		evtbin['xref'] = ra
		evtbin['yref'] = dec
		evtbin['axisrot'] = 0.0
		evtbin['proj'] = 'AIT'
	
		evtbin.run()
	
	
		mymodel = srcList('gll_psc_v26.xml',nombre+'_mktime.fits','ROI.xml')
		mymodel.makeModel('gll_iem_v07.fits', 'gll_iem_v07', 'iso_P8R3_SOURCE_V3_v1.txt', 'iso_P8R3_SOURCE_V3_v1', radLim=float(entry_freerad))
	
		if entry_mail == '':
			label_results['text'] = 'CMAP done.'
		else:
			try:
				yag.send(to=receiver, subject='FERMI NOTIFICATION', contents='CMAP terminado')
			except:
				messagebox.showerror('Error', 'Invalid email adress. It is also possible that you have to give your google account spetial conditions of privacy. You will have received a google alert in this case.')
	
	
	def residual_func(entry_target, entry_index):
		import matplotlib.pyplot as plt 
		import matplotlib
		import numpy as np
		from fermipy.gtanalysis import GTAnalysis
	
		label_results['text'] = 'Loading...'
	
	
		gta = GTAnalysis.create('advdata/fit_model.npy')
	
		resid = gta.residmap(entry_target, model={'SpatialModel' : 'PointSource', 'Index' : float(entry_index)}, write_fits=True) 
	
		label_results['text'] = 'residual map done. (.fits file saved in advdata folder)'
	
	def ts_func(entry_target, entry_index):
		import matplotlib.pyplot as plt 
		import matplotlib
		import numpy as np
		from fermipy.gtanalysis import GTAnalysis
	
		label_results['text'] = 'Loading...'
	
	
		gta = GTAnalysis.create('advdata/fit_model.npy')
	
		tsmap = gta.tsmap('TS_MAP', model={'SpatialModel' : 'PointSource', 'Index' : float(entry_index)}, write_fits=True) 
	
		label_results['text'] = 'Ts map done. (.fits file saved in advdata folder)'
	
	def tsns_func(entry_target, entry_index):
		import matplotlib.pyplot as plt 
		import matplotlib
		import numpy as np
		from fermipy.gtanalysis import GTAnalysis
	
		label_results['text'] = 'Loading...'
	
	
		gta = GTAnalysis.create('advdata/fit_model.npy')
	
		tsmap = gta.tsmap('source_excludedTS', model={'SpatialModel' : 'PointSource', 'Index' : float(entry_index)}, exclude=[entry_target],write_fits=True) 
	
		label_results['text'] = 'Tsns done. (.fits file saved in advdata folder)'
	def SED_func(entry_target, entry_SEDnbins):
		import matplotlib.pyplot as plt 
		import matplotlib
		import numpy as np
		from fermipy.gtanalysis import GTAnalysis
	
		gta = GTAnalysis.create('advdata/fit_model.npy')
		if entry_SEDnbins == '30':
			sed = gta.sed(entry_target, outfile='SED%s.fits' % (str(entry_SEDnbins))) #loge_bins=gta.log_energies[::3], outfile='SED10.fits') 
		elif entry_SEDnbins == '15':
			sed = gta.sed(entry_target, outfile='SED%s.fits' % (str(entry_SEDnbins)), loge_bins=gta.log_energies[::2])
		elif entry_SEDnbins == '10':
			sed = gta.sed(entry_target, outfile='SED%s.fits' % (str(entry_SEDnbins)), loge_bins=gta.log_energies[::3])
		elif entry_SEDnbins == '6':
			sed = gta.sed(entry_target, outfile='SED%s.fits' % (str(entry_SEDnbins)), loge_bins=gta.log_energies[::5])
		elif entry_SEDnbins == '5':
			sed = gta.sed(entry_target, outfile='SED%s.fits' % (str(entry_SEDnbins)), loge_bins=gta.log_energies[::6])
		elif entry_SEDnbins == '3':
			sed = gta.sed(entry_target, outfile='SED%s.fits' % (str(entry_SEDnbins)), loge_bins=gta.log_energies[::10])
		elif entry_SEDnbins == '2':
			sed = gta.sed(entry_target, outfile='SED%s.fits' % (str(entry_SEDnbins)), loge_bins=gta.log_energies[::15])
		else:
			messagebox.showerror('Error', 'binsz must be integer and the values allowed are \n 2,3,5,6,10,15,30')
	
		label_results['text'] = 'SED done. (.fits file saved in advdata folder)'
	
	
	root.mainloop()


except:
	print('REMEMBER TO ACTIVATE YOUR ENVIROMENT!!! (conda activate fermi)\n If you have, please check fondo.png is in your folder.')