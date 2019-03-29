import models
import nlp_helpers as helpers
from transformation_functions import transformations_dict

join_types = ['left', 'right', 'outer', 'inner']
# Class to contain a step and the transformation associated with that step
class TransformData:
	def __init__(self, query):
		language_token = helpers.ProcessLanguageTokens(query=query)
		self.language_token = language_token
		table_list = list(models.loaded_table_dict.keys())
		transformation_list = list(transformations_dict.keys())
		# Get tables, transformations, join_type, left and right keys from the user_query
		self.matched_table = language_token.get_matches(table_list, threshold=94)
		self.matched_transformation = language_token.get_matches(transformation_list, threshold=90)[0]
		tx_fn = transformations_dict.get(self.matched_transformation)
		if not tx_fn:
			raise NotImplemented('This Transformation is not implemented yet!')
		self.transformation_function = tx_fn

	def load_table(self, table_name):
		table_a = models.loaded_table_dict.get(self.matched_table[0])
		table_b = models.loaded_table_dict.get(self.matched_table[1])
		if not table_a or not table_b:
			raise ValueError('Could Not Find Tables in loaded table list')
		models.loaded_table_dict[table_name] = self.transformation_function(table_a, table_b)


# ----------------------- DEBUGGING -----------------------------------------

if __name__ == '__main__':
	i = 0
	query = ""
	list_of_transformations = []
	while query != 'end!':
		i += 1
		query = input('Enter Query. end! to stop\n-->')
		transformation = TransformData(query)
		transformation.load_table('step' + str(i))
		list_of_transformations.append(transformation)
		print('step'+str(i)+' table generated successfully!')
		print('Loaded Table List:')
		print(list(models.loaded_table_dict.keys()))
