import subprocess
import os
import numpy

eccentricity_filenames = ['eccen0', 'eccen01a', 'eccen02a', 'eccen03a', 'eccen04a', 'eccen05a', 'eccen06a']

binary_ratio_filenames = ['br_0010', 'br_0050', 'br_0100']

for edir in eccentricity_filenames:
    for bdir in binary_ratio_filenames:
        cdir = os.path.join(edir, bdir, 'gas_only_hr/')

        os.chdir(cdir)
        print('cd ' + cdir)

        os.mkdir('mcfost')

        skip_aph = len('aphelion in file b\'')
        skip_per = len('perihelion in file b\'')
        aph_file = ''
        per_file = ''

        with open('aphelion_perihelion.txt', 'r') as f:
            for i, line in enumerate(f):
                if i == 0:
                    aph_file = line[skip_aph:-2]
                elif i == 1:
                    per_file = line[skip_per:-2]

        os.chdir('mcfost')
        os.mkdir('aph')
        os.mkdir('per')

        subprocess.call('cp ../' + aph_file + ' aph/')
        subprocess.call('cp ../' + per_file + ' per/')

        subprocess.call('cp ../../../../ref3.0.para aph/')
        subprocess.call('cp ../../../../ref3.0.para per/')

        subprocess.call('cp ../../../../run.pbs aph/')
        subprocess.call('cp ../../../../run.pbs per/')

        os.chdir('aph')
        file_lines = []
        with open('run.pbs', 'r') as rf:
            for i, line in enumerate(rf):
                if i == 16:
                    file_lines.append(''.join([line.strip(), ' ' + aph_file, '\n']))
                if i == 17:
                    file_lines.append(''.join([line.strip(), ' ' + aph_file, '\n']))
                else:
                    file_lines.append(line)

        with open('run.pbs', 'w') as f:
            f.writelines(file_lines)

        subprocess.call('qsub run.pbs')

        os.chdir('../per')
        file_lines = []
        with open('run.pbs', 'r') as rf:
            for i, line in enumerate(rf):
                if i == 16:
                    file_lines.append(''.join([line.strip(), ' ' + per_file, '\n']))
                if i == 17:
                    file_lines.append(''.join([line.strip(), ' ' + per_file, '\n']))
                else:
                    file_lines.append(line)

        with open('run.pbs', 'w') as f:
            f.writelines(file_lines)

        subprocess.call('qsub run.pbs')

        os.chdir('../../../../../')
        # exit()
