from libanalysis import PhantomAnalysis as pa
from glob import glob
import os


eccentricity_filenames = ['eccen0', 'eccen01a', 'eccen02a', 'eccen03a', 'eccen04a', 'eccen05a', 'eccen06a']

binary_ratio_filenames = ['br_0010', 'br_0050', 'br_0100']

for edir in eccentricity_filenames:
    for bdir in binary_ratio_filenames:
        cdir = os.path.join(edir, bdir, 'gas_only_hr')
        dumpfiles = glob(cdir)
        for dumpfile in dumpfiles:
            dump = pa(dumpfile)
            print(dump.ptmass_xyzmh)
