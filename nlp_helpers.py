import nltk
from fuzzywuzzy import process


# Class to user query tokens and query related functions
class ProcessLanguageTokens:
	def __init__(self, query):
		self.tokens = nltk.word_tokenize(query)

	@property
	def token_category(self):
		return nltk.pos_tag(self.tokens)

	@property
	def useful_words(self):
		words = []
		for k, v in self.token_category:
			words.append(k) if v not in ['PRP', 'TO', 'CC', 'PRP$'] else None
		return words

	def get_matches(self, matcher_list, threshold):
		matched_list = []
		for word in self.useful_words:
			match_score = process.extractOne(word, matcher_list)
			if match_score[1] >= threshold:
				matched_list.append(match_score[0])
		return matched_list
