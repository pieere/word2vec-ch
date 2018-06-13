import logging

from gensim.models import word2vec

def main():

    logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
    sentences = word2vec.LineSentence("wiki_result.csv")
    model = word2vec.Word2Vec(sentences, size=250)

    model.save("word2vec.model")


if __name__ == "__main__":
    main()
