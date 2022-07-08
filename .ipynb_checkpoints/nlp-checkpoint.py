#pip3 install gensim==3.8.3
from gensim.summarization.summarizer import summarize
from gensim.summarization import keywords  # Import the library
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity 


class NLP():
    def __init__(self, text1, text2):
        self.text1 = text1
        self.text2 = text2
                
    def summarize(self, text, ratio=0.1):
        return summarize(text, ratio)
    
    def textlist(self):
        return [self.summarize(self.text1), self.summarize(self.text2)]
    
    def vectorize(self):
        cv = CountVectorizer()
        textlist = self.textlist()
        count_matrix = cv.fit_transform(textlist)
        return count_matrix
    
    def get_fit_score(self):
        count_matrix = self.vectorize()
        matchPercentage = cosine_similarity(count_matrix)[0][1] * 100
        matchPercentage = round(matchPercentage, 2)
        return matchPercentage
        
    def get_keywords(self, text, ratio=0.25):
        return keywords(text, ratio)