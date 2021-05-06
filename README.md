# Fermi_analysis

This repository has been created with the aim of attaching the source code used in my Bachelor's Thesis. Therefore, it has been created to fullfil personal neccesities.
The code has been implemented using the Fermi Tools as well as fermipy. (Poner enlaces).

With this repository you should be able to:

- Perform your own binned analysis.
- Get a counts Map of the región as well as a ROI .reg file.
- Make TS maps, with the chance to exclude your source of interest.
- Make residual maps.
- SED plots as well as TS per energy bin plots.
- Check of how well your dNdE fits your model after de analysis (Implemented only for 'Powerlaw')
- Light curves.

The code is entirely written in python3.7. Make sure you have the following dependencies installed:

-Conda (ENLACE)
-FERMITOOLS (ENLACE)
-FERMIPY (ENLACE)
-yagmail (INSTRUCCIONES)
-Numpy
-astropy.io
-matplotlib
-os
-time
(creo que estás últimas tres dependencias vienen incluidas dentro de la instalación de las fermitools)

Some steps of the analysis take hours to finish. Yagmail is used to send messages to your gmail account when a proccess is finished. Consequently, you will be asked to provide your password (of course it is optional).

# Setup the enviroment to start your analysis

First of all you will need to create the repository in which you will perform all your analysis.

Second, you will need to launch a data query via fermi servers and download your photon and Spacecraft files into your repository. You will also need to create your event file. The instructions to do so are and the data query web page can be found here: ENLACE

To use the GIOFERMI tools, the easiest way is to git clone the tools into your analysis repository were your photon and spacecraft data files are placed. (Go to that folder and run):

_holi_
