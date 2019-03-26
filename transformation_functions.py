import pandas as pd
from models import table_dict
import nlp_helpers
from models import join_types


def join(table_a, table_b):
	tabla_a_columns = table_a.columns
	table_b_columns = table_b.columns
	TypeofJoin = input('Which type of join left, right, outer, inner\n-->')
	join_type_nlp_obj = nlp_helpers.ProcessLanguageTokens(query=TypeofJoin)
	TypeofJoin = join_type_nlp_obj.get_matches(join_types, threshold=60)[0]

	if not TypeofJoin:
		print('Join Type is Invalid Try again!')
		return join(table_a, table_b)

	JoinKeyLeftTable = input('Join Key for the Left Table?\n-->')
	JoinKeyLeftTable = JoinKeyLeftTable[0].split(',')
	matched_left_key = []
	for key in JoinKeyLeftTable:
		matched_left_key += nlp_helpers.ProcessLanguageTokens(key)

	JoinKeyRightTable = input('Join Key for the Right Table?\n-->')
	JoinKeyRightTable = JoinKeyRightTable[0].split(',')
	joined_table = pd.merge(table_a, table_b, how=TypeofJoin, left_on=JoinKeyLeftTable, right_on=JoinKeyRightTable)
	return joined_table


# --------------------- for debugging ----------------------------------

if __name__ == '__main__':
	tableA = table_dict.get('tableA')
	tableB = table_dict.get('tableB')
	print(join(tableA, tableB))