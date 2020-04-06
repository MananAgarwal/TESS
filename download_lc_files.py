import numpy as np
import pandas as pd
import sys
import math
import lightkurve as lk

# download_list = "Resources/results_osborn.dat"
download_list = "results_osborn.dat"
download_dest = "./Data"

#Read TIC IDs
df = pd.read_table(download_list, delim_whitespace=True, skiprows=0, skip_blank_lines=True, comment='#', usecols=[7,8], names=('Sector','TICID'))

#Create a unique set of TIC IDs
arr_tic_id = df['TICID'].unique()
sector = [1,2,3,4]

for f in range(len(arr_tic_id)):
        tic_id = arr_tic_id[f]
        print("\nSearching for TIC ID %u" %tic_id)
        lk.search_lightcurvefile("TIC" + str(tic_id), sector=sector).download_all(download_dir=download_dest)