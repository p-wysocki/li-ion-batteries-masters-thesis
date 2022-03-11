import pandas as pd
import numpy as np
import scipy.io
import os
import pyreadr
from collections import defaultdict

MAINFILE_PATH = os.path.abspath('')

def read_data():
	mat = scipy.io.loadmat(os.path.join(MAINFILE_PATH, 'data', 'RW9_clean.mat'))
	pqr=pd.Series(mat)

	pqr2 = pd.DataFrame(pqr)
	raw_data = pqr2.values[4][0]

	data_names = set()
	for data_array in raw_data[0]:
		data_names.add(data_array[0][0])



	data_dict = defaultdict(list)

	for data_array in raw_data[0]:
		data_dict[data_array[0][0]].append(data_array)

	return data_dict

