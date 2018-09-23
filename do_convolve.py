import subprocess
import os
import numpy

eccentricity_filenames = ['eccen0', 'eccen01a', 'eccen02a', 'eccen03a', 'eccen04a', 'eccen05a', 'eccen06a']

binary_ratio_filenames = ['br_0010']

for edir in eccentricity_filenames:
    for bdir in binary_ratio_filenames:
        cdir = os.path.join(edir, bdir, 'gas_only_hr/', 'mcfost', 'aph')
        os.chdir(cdir)
        subprocess.check_output('python convolve.py --filename ' + cdir + 'data_1/RT.fitz.gz' + ' --save ' +
                                edir+cdir + '_aph.png', stderr=subprocess.STDOUT,
                                         universal_newlines=True, shell=True)

        os.chdir('../../../../../')

        cdir = os.path.join(edir, bdir, 'gas_only_hr/', 'mcfost', 'per')
        os.chdir(cdir)
        subprocess.check_output('python convolve.py --filename ' + cdir + 'data_1/RT.fitz.gz' + ' --save ' +
                                edir+cdir + '_per.png', stderr=subprocess.STDOUT,
                                         universal_newlines=True, shell=True)

        os.chdir('../../../../../')
