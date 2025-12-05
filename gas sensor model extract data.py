import glob,os,csv
import pandas as pd
import re

file_path = 'C:/Users/PARDAZESHGARAN/Documents/datfile'
outputpath = 'combind.csv'

pair_re = re.compile(r"(\d+):([-+]?[0-9]*\.?[0-9]+)")

num_features = 128

with open(outputpath,'w',newline='') as f:
    writer = csv.writer(f)


    #header
    header = ['label'] + [f'f{i}'for i in range(1 , num_features + 1)]
    writer.writerow(header)

    #rocess the every .dat file
    for filepath in glob.glob(os.path.join(file_path, '*.dat')):
        print(f'loading {filepath}')

        with open(filepath,'r',newline='') as d :
            for line in d:
                parts = line.strip().split()
                label = int(parts[0])
                
                row = [0,0] * num_features

                for p in parts[1:]:
                    m = pair_re.match(p)
                    if m:
                        idx,val = m.groups()
                    else:
                        pass
                    row[int(idx) - 1] = float(val)

                writer.writerow([label] + row)


print('combind is saved')