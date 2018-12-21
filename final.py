import numpy as np
import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib



cell_data = pd.read_table('tetrahymena.tsv', delim_whitespace=True)

d1 = cell_data['diameter']>= 19.2
cell_data = cell_data[d1]
d2 = cell_data['diameter']<= 26.0
cell_data = cell_data[d2]
cell_data = cell_data.reset_index()

cell_data['glucose_marker'] = 1

for i in range(0,len(cell_data['glucose'])):
    if cell_data['glucose'][i] == 'glucose_no':
        cell_data.set_value(i, 'glucose_marker', 0)
         
cell_data = cell_data.groupby('culture').mean().reset_index()


cell_data['glucose'] = 'Glucose'
for i in range(0,len(cell_data['glucose_marker'])):
    if cell_data['glucose_marker'][i] == 0:
        cell_data.set_value(i, 'glucose', 'No Glucose')


cell_data['log_concentration'] = np.log(cell_data.conc)
cell_data['log_diameter'] = np.log(cell_data.diameter)

nolog = sns.pairplot(x_vars=['conc'], y_vars=['diameter'], height=8, data=cell_data, hue= 'glucose',markers= ['o','+'])
log = sns.pairplot(x_vars=['log_concentration'], y_vars=['log_diameter'], height=8, data=cell_data, hue= 'glucose',markers= ['o','+'])


nolog.set_title = 'Average Cell Diameter vs. Concentration'
log.set_title = 'Average Cell Diameter vs. Concentration'
nolog.savefig("final_part_A_nonlog_kh2975.pdf")
log.savefig("final_part_A_log_kh2975.pdf")
