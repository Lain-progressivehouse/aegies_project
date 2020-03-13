import scipy as sp
import bhtsne


def get_tsne(matrix, dimensions=2):
    tsne = bhtsne.tsne(matrix.astype(sp.float64), dimensions=dimensions, perplexity=30.0, theta=0.5, rand_seed=-1)
    return tsne
