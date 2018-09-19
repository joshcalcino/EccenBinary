import subprocess
import os
import numpy

eccentricity_filenames = ['eccen0', 'eccen01a', 'eccen02a', 'eccen03a', 'eccen04a', 'eccen05a', 'eccen06a']

binary_ratio_filenames = ['br_0010', 'br_0050', 'br_0100']

for edir in eccentricity_filenames:
    for bdir in binary_ratio_filenames:
        cdir = os.path.join(edir, bdir, 'gas_only_hr/')
        output=subprocess.check_output('cp phantomanalysis ' + cdir, stderr=subprocess.STDOUT,
                                universal_newlines=True, shell=True)
        print(output)
        os.chdir(cdir)
        print('cd ' + cdir)
        output = subprocess.check_output('ls', stderr=subprocess.STDOUT,
                                universal_newlines=True, shell=True)

        print(output)
        #output = subprocess.check_output('./phantomanalysis gas_only_hr_0*', stderr=subprocess.STDOUT,
        #                        universal_newlines=True, shell=True)
        print(output)
        sink1 = numpy.genfromtxt('sinkpositions_1.dat', dtype=None)
        sink2 = numpy.genfromtxt('sinkpositions_2.dat')
        print(sink1)
        dumpfile = []
        xs = []
        ys = []
        zs = []

        xc = []
        yc = []
        zc = []

        for i in range(0, len(sink1)):
            dumpfile.append(sink1[i][0])
            xs.append(sink1[i][1])
            ys.append(sink1[i][2])
            zs.append(sink1[i][3])

            xc.append(sink2[i][1])
            yc.append(sink2[i][2])
            zc.append(sink2[i][3])

        xyzs = numpy.array([xs, ys, zs])
        xyzc = numpy.array([xc, yc, zc])
        product = xyzc @ xyzs
        print(numpy.min(xyzc @ xyzs))
        print(numpy.max(xyzc @ xyzs))
        print(numpy.argmin(product))
        # print(sink1[:][2])
        os.chdir('../../../')
        exit()
