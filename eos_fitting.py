import sys
import pandas as pd
from ase.eos import EquationOfState

main_path = '/Users/kamyar/Box Sync/Projects/Silicon Copper Interaction/Na2SiO3/'
file_name = 'EOS_fitting_Na2SiO3.xlsx'
sys.path.append(main_path)

data = pd.read_excel(main_path+file_name)
eos = EquationOfState(data['volume'], data['energy'], eos='birchmurnaghan')
eos.fit()
eos.plot(filename='/Users/kamyar/Desktop/ata.eps')