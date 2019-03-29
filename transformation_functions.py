import pandas as pd
from models import loaded_table_dict as table_dict, TableObj
import nlp_helpers

join_types = ['left', 'right', 'outer', 'inner']


def prompt_join_type():
	join_type_query = input('Which type of join left, right, outer, inner\n-->')
	join_type_query_tokens = nlp_helpers.ProcessLanguageTokens(query=join_type_query)

	# only take first join type found in user query
	join_type = join_type_query_tokens.get_matches(join_types, threshold=90)[0]

	# If join type not found then ask again
	if not join_type:
		print('Join type not found! Try again')
		return prompt_join_type()
	return join_type


def prompt_join_keys(left_or_right, table_column_list):
	join_keys_query = input('Join Key for the ' + left_or_right + ' Table?\n-->')
	join_keys_tokens = nlp_helpers.ProcessLanguageTokens(join_keys_query)

	# Get matched column with the user_query
	matched_key = join_keys_tokens.get_matches(table_column_list, threshold=91)
	return matched_key


def join(l_table, r_table, type=None, left_on=None, right_on=None):
	l_table = l_table
	r_table = r_table
	type = type
	if not type:
		type = prompt_join_type()
	left_on = left_on
	if not left_on:
		left_on = prompt_join_keys('Left', l_table.columns)
	right_on = right_on
	if not right_on:
		right_on = prompt_join_keys('Right', r_table.columns)

	# If left_on is empty then join on default columns
	if not left_on:
		print('Left Table keys not found! table will be joined on same columns')
		right_on = []
	joined_table = pd.merge(l_table.table, r_table.table, how=type, left_on=left_on, right_on=right_on)
	return TableObj(joined_table, 'tx_table')


def union(table_a, table_b):
	return pd.concat([table_a, table_b], ignore_index=True)

def filter(table):
	pass

transformations_dict = {
	'join': join,
	'union': union,
	'filter': filter
}

# --------------------- for debugging ----------------------------------

if __name__ == '__main__':
	tableA = table_dict.get('tableA')
	tableB = table_dict.get('tableB')
	print(join(tableA, tableB))
