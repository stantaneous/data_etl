import models
import nlp_helpers as helpers
from transformation_functions import transformations_dict




# Class to contain a step and the transformation associated with that step
class TransformData:
	def __init__(self, query):
		language_token = helpers.ProcessLanguageTokens(query=query)
		table_list = models.loaded_table_dict.keys()
		transformation_list = transformations_dict.keys()
		self.matched_table = language_token.get_matches(table_list, threshold=94)
		self.matched_transformation = language_token.get_matches(transformation_list, threshold=90)[0]
		tx_fn = transformations_dict.get(self.matched_transformation)
		if not tx_fn:
			raise NotImplemented('This Transformation is not implemented yet!')
		self.transformation_function = tx_fn