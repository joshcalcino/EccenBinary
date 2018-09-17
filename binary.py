from libanalysis import PhantomAnalysis as pa
from glob import glob
import os


def get_dump_files(directory):
    dumpfiles = glob(directory)
    new_dumpfiles = []
    for dumpfile in dumpfiles:
        # print(dumpfile)
        if dumpfile[:-2:].isdigit():
            new_dumpfiles.append(dumpfile)
    return new_dumpfiles


eccentricity_filenames = ['eccen0', 'eccen01a', 'eccen02a', 'eccen03a', 'eccen04a', 'eccen05a', 'eccen06a']

binary_ratio_filenames = ['br_0010', 'br_0050', 'br_0100']

for edir in eccentricity_filenames:
    for bdir in binary_ratio_filenames:
        cdir = os.path.join(edir, bdir, 'gas_only_hr/*')
        dumpfiles = get_dump_files(cdir)
        for dumpfile in dumpfiles:
            dump = pa(dumpfile)
            print(dump.ptmass_xyzmh)
            print(dump.npart)
