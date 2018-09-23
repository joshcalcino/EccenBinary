import subprocess
import os


eccentricity_filenames = ['eccen0', 'eccen02a', 'eccen03a', 'eccen04a', 'eccen05a', 'eccen06a'] # 'eccen01a',

binary_ratio_filenames = ['br_0010']

for edir in eccentricity_filenames:
    for bdir in binary_ratio_filenames:
        cdir = os.path.join(edir, bdir, 'gas_only_hr/', 'mcfost', 'aph')

        subprocess.check_output('python convolve.py --filename ' + cdir + '/data_1/RT.fits.gz' + ' --save ' +
                                edir+'_'+bdir + '_aph.png', stderr=subprocess.STDOUT,
                                         universal_newlines=True, shell=True)

        cdir = os.path.join(edir, bdir, 'gas_only_hr/', 'mcfost', 'per')

        subprocess.check_output('python convolve.py --filename ' + cdir + '/data_1/RT.fits.gz' + ' --save ' +
                                edir+'_'+bdir + '_per.png', stderr=subprocess.STDOUT,
                                         universal_newlines=True, shell=True)

