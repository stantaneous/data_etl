import pandas as pd

# Lists of Possible entities

join_types = ['left', 'right', 'outer', 'inner']


class TableObj:
	def __init__(self, table, type='user_table'):
		self.table = table
		self.columns = table.columns.to_list()
		self.type = type


loaded_table_dict = {
	'tableA': TableObj(pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3', 'K4', 'K5'],
									 'A': ['A0', 'A1', 'A2', 'A3', 'A4', 'A5'],
									 'id': ['K0', 'K1', 'K2', 'K3', 'K4', 'K5']
									 })),
	'tableB': TableObj(pd.DataFrame({'key': ['K0', 'K1', 'K2'],
									 'B': ['B0', 'B1', 'B2'],
									 'id': ['K0', 'K1', 'K3']
									 }))
}

