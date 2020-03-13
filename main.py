from scdv import dataFrame, word2vec, scdv, tsne_maker
import pickle
import numpy as np
import os


def main():
    # 文書のpathを指定してdocument_listの作成(pandas形式)
    # columns: "stock_name", "date", "document"
    document_list = dataFrame.make_dataFrame_new_data(data_path="./data/text_data/")

    # document_listの保存
    if not os.path.exists("./data/model/"):
        os.mkdir("./data/model/")
    with open("./data/model/doucment_list.pkl", "wb") as f:
        pickle.dump(document_list, f)

    # word2vecの学習
    word2vec_model = word2vec.learn_word2vec(document_list["document"])

    # scdvの作成
    prob_wordvecs = scdv.get_prob_wordvecs(word2vec_model, document_list)
    scdv_vector = scdv.get_scdv(prob_wordvecs, document_list)

    # scdvの保存
    np.save("./data/model/scdv", scdv_vector)

    tsne = tsne_maker.get_tsne(scdv, dimensions=2)

    # tsneの保存
    np.save("./data/model/tsne", tsne)


if __name__ == '__main__':
    main()
