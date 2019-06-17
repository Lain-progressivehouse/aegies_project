import hashlib
import pickle
import collections
import pandas as pd


def get_hash_list(document_list):
    all_hash_list = list(map(lambda x: hashlib.sha512("".join(x).encode()).hexdigest(), document_list["document"]))

    opt_document_list = pd.DataFrame(columns=["category1", "category2", "category3", "hash", "document"])

    hash_dict = collections.defaultdict(list)

    # dict kry: category value: list(hash)

    for category1, category2, category3, document, hash in zip(document_list["category1"], document_list["category2"],
                                                               document_list["category3"], document_list["document"],
                                                               all_hash_list):
        if hash_dict.get(category1) == None or hash not in hash_dict.get(category1):
            hash_dict[category1].append(hash)
            t = pd.Series([category1, category2, category3, hash, document], index=opt_document_list.columns)
            opt_document_list = opt_document_list.append(t, ignore_index=True)

    # with open("/Users/main/PycharmProjects/aegies/data/opt/opt_documents.pkl", "wb") as f:
    #     pickle.dump(opt_document_list, f)

    return opt_document_list
