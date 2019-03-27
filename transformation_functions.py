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

	join_keys_left = input('Join Key for the Left Table?\n-->')
	nlp_join_keys_left = nlp_helpers.ProcessLanguageTokens(join_keys_left)
	matched_keys_left = nlp_join_keys_left.get_matches(tabla_a_columns, threshold=90)

	join_keys_right = input('Join Key for the Right Table?\n-->')
	nlp_join_keys_right = nlp_helpers.ProcessLanguageTokens(join_keys_right)
	matched_keys_right = nlp_join_keys_right.get_matches(table_b_columns, threshold=90)


	joined_table = pd.merge(table_a.table, table_b.table, how=TypeofJoin, left_on=matched_keys_left, right_on=matched_keys_right)
	return joined_table


def union(table_a, table_b):
	pass

transformations_dict = {
	'join' : join,
	'union': union
}

# --------------------- for debugging ----------------------------------

if __name__ == '__main__':
	tableA = table_dict.get('tableA')
	tableB = table_dict.get('tableB')
	print(join(tableA, tableB))