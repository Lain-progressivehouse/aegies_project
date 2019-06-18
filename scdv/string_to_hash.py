import hashlib
import pickle
import collections
import pandas as pd


def get_hash_list(document_list, category="category1"):
    """
    document_listの文書からHashを求めて重複する文書を排除
    :param document_list: 文書リスト
    :param category: どのcategoryでの重複を排除するか
    :return: [category1, category2, category3, hash, document]
    """
    all_hash_list = list(map(lambda x: hashlib.sha512("".join(x).encode()).hexdigest(), document_list["document"]))

    opt_document_list = pd.DataFrame(columns=["category1", "category2", "category3", "hash", "document"])

    hash_dict = collections.defaultdict(list)

    # dict kry: category value: list(hash)

    for category1, category2, category3, document, hash, ctgry in zip(document_list["category1"],
                                                                      document_list["category2"],
                                                                      document_list["category3"],
                                                                      document_list["document"],
                                                                      all_hash_list, document_list[category]):
        if hash_dict.get(ctgry) == None or hash not in hash_dict.get(ctgry):
            hash_dict[ctgry].append(hash)
            t = pd.Series([category1, category2, category3, hash, document], index=opt_document_list.columns)
            opt_document_list = opt_document_list.append(t, ignore_index=True)

    # with open("/Users/main/PycharmProjects/aegies/data/opt/opt_documents.pkl", "wb") as f:
    #     pickle.dump(opt_document_list, f)

    return opt_document_list
