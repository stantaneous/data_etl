import models
import nlp_helpers as helpers


# Class to contain a step and the transformation associated with that step
class TransformData:
	def __init__(self, query):
		language_token = helpers.ProcessLanguageTokens(query=query)
		table_list = models.table_lists
		transformation_list = models.data_transformations
		self.matched_table = language_token.get_matches(table_list, threshold=94)
		self.matched_transformation = language_token.get_matches(transformation_list, threshold=90)[0]
		if self.matched_transformation == ''