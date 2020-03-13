from gensim.models import word2vec
import logging
import os


def learn_word2vec(sentences):
    # num_features = 200  # 次元数
    # min_word_count = 20  # n回未満登場する単語を破棄
    # num_workers = 40  # 複数のスレッドで処理
    # context = 10  # 学習に使う前後の単語数
    # downsampling = 1e-3  # 単語を無視する頻度
    num_features = 200  # 次元数
    min_word_count = 10  # n回未満登場する単語を破棄
    num_workers = 40  # 複数のスレッドで処理
    context = 10  # 学習に使う前後の単語数
    downsampling = 1e-4  # 単語を無視する頻度

    logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

    # word2vecを学習
    model = word2vec.Word2Vec(sentences, workers=num_workers, hs=0, sg=1, negative=10, iter=25, size=num_features,
                              min_count=min_word_count, window=context, sample=downsampling, seed=1)
    model.init_sims(replace=True)

    # modelを保存
    if not os.path.exists("./data/model/"):
        os.mkdir("./data/model/")
    model.save("./data/model/word2vec.model")

    return model
