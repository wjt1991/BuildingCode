import pandas as pd

# read
dat_file_path = 'Level1_0.2pu_for_80s.dat'
data = pd.read_csv(dat_file_path, sep="\s+", header=None)
data = data.T
headers = ['t', 'v(t)', 'i(t)', 'Vrms', 'Irms', 'P', 'Q', 'f']
data.columns = headers

# save
excel_file_path = 'Level1_0.2pu_for_80s.xlsx'
data.to_excel(excel_file_path, index=False, header=headers)

print("saved to", excel_file_path)
