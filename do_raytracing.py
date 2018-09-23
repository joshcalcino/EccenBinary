import subprocess
import os
import numpy

eccentricity_filenames = ['eccen0', 'eccen01a', 'eccen02a', 'eccen03a', 'eccen04a', 'eccen05a', 'eccen06a']

binary_ratio_filenames = ['br_0010']

for edir in eccentricity_filenames:
    for bdir in binary_ratio_filenames:
        cdir = os.path.join(edir, bdir, 'gas_only_hr/')

        os.chdir(cdir)
        print('cd ' + cdir)

        if os.path.exists('mcfost'):
            pass
        else:
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

        if os.path.exists('aph'):
            pass
        else:
            os.mkdir('aph')

        if os.path.exists('per'):
            pass
        else:
            os.mkdir('per')

        if os.path.exists('data_th'):
            output = subprocess.check_output('rm -r data_*', stderr=subprocess.STDOUT,
                                             universal_newlines=True, shell=True)

        # print(output)

        subprocess.check_output('cp ../' + aph_file + ' aph/', stderr=subprocess.STDOUT,
                                         universal_newlines=True, shell=True)
        subprocess.check_output('cp ../' + per_file + ' per/', stderr=subprocess.STDOUT,
                                         universal_newlines=True, shell=True)

        subprocess.check_output('cp ../../../../ref3.0.para aph/', stderr=subprocess.STDOUT,
                                         universal_newlines=True, shell=True)
        subprocess.check_output('cp ../../../../ref3.0.para per/', stderr=subprocess.STDOUT,
                                         universal_newlines=True, shell=True)

        subprocess.check_output('cp ../../../../run.qscript aph/', stderr=subprocess.STDOUT,
                                         universal_newlines=True, shell=True)
        subprocess.check_output('cp ../../../../run.qscript per/', stderr=subprocess.STDOUT,
                                         universal_newlines=True, shell=True)

        os.chdir('aph')

        if os.path.exists('data_th'):
            subprocess.check_output('rm -r data_*', stderr=subprocess.STDOUT,
                                    universal_newlines=True, shell=True)

        output = subprocess.check_output('pwd', stderr=subprocess.STDOUT,
                                         universal_newlines=True, shell=True)
        file_lines = []
        with open('run.qscript', 'r') as rf:
            for i, line in enumerate(rf):
                #if i == 12:
                #    file_lines.append(''.join([line.strip(), ' ' + str(output)]))
                if i == 14:
                    file_lines.append(''.join([line.strip(), ' ' + aph_file, '\n']))
                elif i == 15:
                    file_lines.append(''.join([line.strip(), ' ' + aph_file, '\n']))
                else:
                    file_lines.append(line)
        # print(file_lines)
        with open('run2.qscript', 'w') as f:
            for line in file_lines:
                # print(line)
                f.write(line)

        # print(output)

        output = subprocess.check_output('sbatch run2.qscript', stderr=subprocess.STDOUT,
                                         universal_newlines=True, shell=True)
        print(output)

        os.chdir('../per')
        if os.path.exists('data_th'):
            subprocess.check_output('rm -r data_*', stderr=subprocess.STDOUT,
                                         universal_newlines=True, shell=True)
        # print(output)
        output = subprocess.check_output('pwd', stderr=subprocess.STDOUT,
                                         universal_newlines=True, shell=True)

        file_lines = []
        with open('run.qscript', 'r') as rf:
            for i, line in enumerate(rf):
                print(i)
                # print(file_lines)
                # if i == 12:
                #    file_lines.append(''.join([line.strip(), ' ' + str(output)]))
                if i == 14:
                    # print('i = 18')
                    file_lines.append(''.join([line.strip(), ' ' + per_file, '\n']))
                elif i == 15:
                    # print('i = 19')
                    file_lines.append(''.join([line.strip(), ' ' + per_file, '\n']))
                else:
                    # print('i don\'t care')
                    file_lines.append(line)

        # print(file_lines)
        with open('run2.qscript', 'w') as f:
            f.writelines(file_lines)

        subprocess.check_output('sbatch run2.qscript', stderr=subprocess.STDOUT,
                                         universal_newlines=True, shell=True)

        os.chdir('../../../../../')
        # exit()
