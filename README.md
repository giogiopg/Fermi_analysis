# Fermi_analysis

The GIO analysis tools have been developed to fulfill my Bachelor's Thesis necessities.
The code has been implemented using the Fermi Tools(https://github.com/fermi-lat/Fermitools-conda) as well as fermipy (https://github.com/fermiPy/fermipy).


With the GIO tools you should be able to:

- Perform your own binned analysis.
- Get a counts Map of the región as well as a ROI .reg file.
- Make TS maps, with the chance to exclude your source of interest.
- Make residual maps.
- SED plots as well as TS per energy bin plots.
- Check of how well your dNdE fits your model after de analysis (Implemented only for 'Powerlaw')
- Light curves.

The code is entirely written in python3.7. Make sure you have the following dependencies installed:

- Conda (ENLACE)
- FERMITOOLS (ENLACE)
- FERMIPY (ENLACE)
- yagmail (INSTRUCCIONES)
- Numpy
- astropy.io
- matplotlib
- os
- time
- tkinter
(creo que estás últimas tres dependencias vienen incluidas dentro de la instalación de las fermitools)

Running the installing dependencies file via

_$ . install_all.txt_

will install all the dependencies needed for the analysis, included miniconda3.

Some steps of the analysis take hours to finish. Yagmail is used to send messages to your gmail account when a proccess is finished. Consequently, you will be asked to provide your password (of course it is optional).

# Setup the enviroment to start your analysis

First of all you will need to create the repository in which you will perform all your analysis.

Second, you will need to launch a data query via fermi servers and download your photon and Spacecraft files into your repository. You will also need to create your event file. The instructions to do so are and the data query web page can be found here: https://fermi.gsfc.nasa.gov/cgi-bin/ssc/LAT/LATDataQuery.cgi

To use the GIOFERMI tools, the easiest way is to git clone the tools into your analysis repository were your photon and spacecraft data files are placed. Then unzip the fermifiles.zip file. You can also remove the zip file after unzipping it. Last but not least, download the fermi difusse model catalog. To put it briefly, go to the folder where you have put your photon a spacecraft files and run:

_$https://github.com/giogiopg/Fermi_analysis.git_

_$unzip fermifiles.zip_

_Srm fermifiles.zip_

_Swget https://fermi.gsfc.nasa.gov/ssc/data/analysis/software/aux/4fgl/gll_iem_v07.fits_
 
Do not forget to activate your fermi enviroment before using the GIO tools:

_$conda activate fermi_

You a ready forr your analysis!
