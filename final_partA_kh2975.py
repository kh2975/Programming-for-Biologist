#import all required modules

import numpy as np
import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib

'''

Krysten Harvey
Final Exam

'''

#read in table of data using pandas
cell_data = pd.read_table('tetrahymena.tsv', delim_whitespace=True)

#filter average cell diameters
d1 = cell_data['diameter']>= 19.2
cell_data = cell_data[d1]
d2 = cell_data['diameter']<= 26.0
cell_data = cell_data[d2]

#reset index of dataframe because of deleted values
cell_data = cell_data.reset_index()

#create a new column to be used as marker based on glucose value. all values are default as 1 (glucose)
cell_data['glucose_marker'] = 1

#search through df, and set glucose as 0 if no glucose was given
for i in range(0,len(cell_data['glucose'])):
    if cell_data['glucose'][i] == 'glucose_no':
        cell_data.set_value(i, 'glucose_marker', 0)

#group by culture number and average diameter and concentration. reset index again
cell_data = cell_data.groupby('culture').mean().reset_index()

#create new column to put back glucose values into table with default value as Glucose
cell_data['glucose'] = 'Glucose'

#if glucose marker is 0, set as No Glucose
for i in range(0,len(cell_data['glucose_marker'])):
    if cell_data['glucose_marker'][i] == 0:
        cell_data.set_value(i, 'glucose', 'No Glucose')


#create new columns for the logs of diameters and concentrations
cell_data['log_concentration'] = np.log(cell_data.conc)
cell_data['log_diameter'] = np.log(cell_data.diameter)

#create scatterplots using seaborn
nolog = sns.pairplot(x_vars=['conc'], y_vars=['diameter'], height=8, data=cell_data, hue= 'glucose',markers= ['o','+'])
log = sns.pairplot(x_vars=['log_concentration'], y_vars=['log_diameter'], height=8, data=cell_data, hue= 'glucose',markers= ['o','+'])

nolog.title = 'Average Cell Diameter vs. Concentration'
log.title = 'Average Cell Diameter vs. Concentration'

#save plots as pdfs
nolog.savefig("final_part_A_nonlog_kh2975.pdf")
log.savefig("final_part_A_log_kh2975.pdf")
