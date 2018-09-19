import subprocess
import os
import numpy

eccentricity_filenames = ['eccen0', 'eccen01a', 'eccen02a', 'eccen03a', 'eccen04a', 'eccen05a', 'eccen06a']

binary_ratio_filenames = ['br_0010', 'br_0050', 'br_0100']

for edir in eccentricity_filenames:
    for bdir in binary_ratio_filenames:
        cdir = os.path.join(edir, bdir, 'gas_only_hr/*')
        subprocess.check_output('cp phantomanalysis ' + cdir, stderr=subprocess.STDOUT,
                                universal_newlines=True, shell=True)
        subprocess.check_output('cd ' + cdir, stderr=subprocess.STDOUT,
                                universal_newlines=True, shell=True)
        subprocess.check_output('./phantomanalysis gas_only_hr_0*' + cdir, stderr=subprocess.STDOUT,
                                universal_newlines=True, shell=True)
        sink1 = numpy.genfromtxt('sinkpositions_1.dat')
        sink2 = numpy.genfromtxt('sinkpositions_2.dat')
        print(sink1)
