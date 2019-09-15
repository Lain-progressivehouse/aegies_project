import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import scipy as sp
import bhtsne


def get_tsne(matrix, dimensions=2):
    tsne = bhtsne.tsne(matrix.astype(sp.float64), dimensions=dimensions, perplexity=30.0, theta=0.5, rand_seed=-1)
    return tsne


def scatter(tsne, document_list):
    doc_tsne = pd.DataFrame(tsne[:, 0], columns=["x"])
    doc_tsne["y"] = pd.DataFrame(tsne[:, 1])
    doc_tsne["category"] = list(document_list["category1"])
    sns.set_style("darkgrid")

    # sns.color_palette(sns.color_palette(n_colors=16))

    sns.set(font="IPAexGothic")
    g = sns.lmplot(data=doc_tsne, x="x", y="y", hue="category", fit_reg=False, legend=False, size=8, legend_out=False)
    box = g.ax.get_position()
    g.ax.set_position([box.x0, box.y0, box.width * 0.85, box.height])
    g.ax.legend(loc='center right', bbox_to_anchor=(1.25, 0.5), ncol=1)
    plt.show()


def create_docvec_scatter(matrix, document_list):
    """
    文書ベクトルの散布図を作成する
    :param matrix: 行列
    :return:
    """
    tsne = bhtsne.tsne(matrix.astype(sp.float64), dimensions=2, perplexity=30.0, theta=0.5, rand_seed=-1)
    doc_tsne = pd.DataFrame(tsne[:, 0], columns=["x"])
    doc_tsne["y"] = pd.DataFrame(tsne[:, 1])
    doc_tsne["category"] = list(document_list["category1"])
    sns.set_style("darkgrid")
    sns.set(font="IPAexGothic")
    sns.lmplot(data=doc_tsne, x="x", y="y", hue="category", fit_reg=False, size=10)
    # 図を表示
    plt.show()
    return tsne


def create_wordvec_scatter(matrix, vocab):
    """
    単語ベクトルの散布図を作成する
    :param matrix: 単語ベクトルの行列
    :param vocab: 単語リスト
    :return:
    """
    tsne = bhtsne.tsne(matrix.astype(sp.float64), dimensions=2, perplexity=30.0, theta=0.5, rand_seed=-1)
    plt.figure(figsize=(16, 12))  # 図のサイズ
    plt.scatter(tsne[0:500, 0], tsne[0:500, 1])

    count = 0
    for label, x, y in zip(vocab, tsne[0:500, 0], tsne[0:500, 1]):
        count += 1
        if count < 0:
            continue

        plt.annotate(label, xy=(x, y), xytext=(0, 0), textcoords='offset points')

        if count == 500:
            break

    plt.show()

    return tsne
