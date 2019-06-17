import numpy as np
import scipy as sp
import bhtsne
from gensim.models import KeyedVectors
import pickle


def plain_word2vec_document_vector(sentence, word2vec_model, num_features):
    bag_of_centroids = np.zeros(num_features, dtype="float32")

    for word in sentence:
        try:
            temp = word2vec_model[word]
        except:
            continue
        bag_of_centroids += temp

    bag_of_centroids = bag_of_centroids / len(sentence)

    return bag_of_centroids


def word_vec_average(document_list, word2vec_model):
    counter = 0
    num_features = 200
    plainDocVec_all = np.zeros((document_list["document"].size, num_features), dtype="float32")

    for sentence in document_list["document"]:
        plainDocVec_all[counter] = plain_word2vec_document_vector(sentence, word2vec_model, num_features)
        counter += 1

    tsne = bhtsne.tsne(plainDocVec_all.astype(sp.float64), dimensions=2, perplexity=30.0, theta=0.5, rand_seed=-1)

    return plainDocVec_all, tsne

def get_learned_word2vec_average():
    model = KeyedVectors.load_word2vec_format('/Users/main/PycharmProjects/aegies/data/entity_vector/entity_vector.model.bin', binary=True)
    document_list = pickle.load(open("/Users/main/PycharmProjects/aegies/data/document_list.pickle", "rb"))
    return  word_vec_average(document_list, model)