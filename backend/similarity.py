#/* Copyright (C) Florentina Petcu - All Rights Reserved
# * Unauthorized copying of this file, via any medium is strictly prohibited
# * Proprietary and confidential
# * Written by Florentina Petcu <florentina.ptc@gmail.com>, December 2018
# */

from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
from database import * 

def similarityDescription(position):
	ids = [d[0] for d in getDescriptions()]
	descriptions = [d[1] for d in getDescriptions()]

	tfidf_vectorizer = TfidfVectorizer()
	tfidf_matrix = tfidf_vectorizer.fit_transform(descriptions)

	similarity = cosine_similarity(tfidf_matrix[position: position + 1], tfidf_matrix)

	result = []
	for index, s in enumerate(similarity[0]):
		if s >= 0.35:
			result += [ids[index]]

	return result

def getSimilarBooksList(idBook):
	similarIds = similarityDescription(idBook - 2)
	return getBooksListById(similarIds)