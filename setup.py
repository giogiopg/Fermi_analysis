import matplotlib.pyplot as plt 
import matplotlib
import numpy as np
from fermipy.gtanalysis import GTAnalysis
import yagmail
import time
from tkinter import messagebox
import getpass


print('Take into account that giving your email is completely optional. Just press enter when asked for it.')
entry_mail = str(input('Introduce tu email: '))
entry_password = getpass.getpass('Password: ')

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
	print('Done.')
else:
	try:
		yag.send(to=receiver, subject='FERMI NOTIFICATION', contents='Ha terminado el setup. Ha tardado '+elapsed+'mins.')
	except:
		messagebox.showerror('Error', 'Invalid email address')