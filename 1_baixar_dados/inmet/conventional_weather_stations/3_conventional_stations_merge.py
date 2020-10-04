import glob
import os

import pandas as pd

os.chdir("data/conventional_stations_csv")

all_filenames = [i for i in glob.glob('*.csv')]

# combine all files in the list
combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames])
# export to csv
combined_csv.to_csv("merged.csv", index=False, encoding='utf-8')
