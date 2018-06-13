from gensim import models
from gensim.models import word2vec
import logging


logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
model = models.Word2Vec.load('word2vec.model')
result = model.most_similar('足球')
for e in result:
    print(e)
