import numpy as np
import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib



exp = pd.read_table('tetrahymena.tsv', delim_whitespace=True)

x = exp['diameter']>= 19.2
exp = exp[x]
y = exp['diameter']<= 26.0
exp = exp[y]
exp = exp.reset_index()

exp['glucose_marker'] = 1

for i in range(0,len(exp['glucose'])):
    if exp['glucose'][i] == 'glucose_no':
        exp.set_value(i, 'glucose_marker', 0)
         
exp = exp.groupby('culture').mean().reset_index()
print(exp)

exp['log_concentration'] = np.log(exp.conc)
exp['log_diameter'] = np.log(exp.diameter)

nolog = sns.pairplot(x_vars=['conc'], y_vars=['diameter'], height=7, data=exp, hue= 'glucose_marker',markers= ['o','+'])
log = sns.pairplot(x_vars=['log_concentration'], y_vars=['log_diameter'], height=7, data=exp, hue= 'glucose_marker',markers= ['o','+'])

nolog.title = 'Average Cell Diameter vs. Concentration'
log.title = 'Average Cell Diameter vs. Concentration'
nolog.savefig("final_part_A_nonlog_kh2975.pdf")
log.savefig("final_part_A_log_kh2975.pdf")
