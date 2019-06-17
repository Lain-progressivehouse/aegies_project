import os
import re
from scdv import preprocessing
import pandas as pd
import pickle
from tqdm import tqdm


def find_all_files(directory):
    """
	引数のディレクトリ下のファイルのパスの一覧を取得する
	:param directory: ディレクトリ
	:return: ファイルのパスの一覧を取得
	"""
    for root, dirs, files in os.walk(directory):
        for file in files:
            if re.search(r"[\s\S]*?.txt", file):
                yield os.path.join(root, file)


def make_dataFrame():
    document_list = pd.DataFrame(columns=["category1", "category2", "category3", "company", "document"])

    data_path = "/Users/main/Desktop/企業レポート"

    files = find_all_files(data_path)
    for file in tqdm(list(files)):
        # with open(file, "r") as f:
        #     word_list = preprocessing.document_to_wordlist(f.read())

        r = open(file, "r")
        word_list = preprocessing.document_to_wordlist(r.read())
        r.close()

        # ガテゴリ1 カテゴリ2 カテゴリ3 ファイル名
        frame_list = file.replace("/Users/main/Desktop/企業レポート/", "").split("/")

        if len(frame_list) < 4:
            t = pd.Series(
                [frame_list[0], "_", "_", frame_list[1].replace("企業レポート_", "").replace(".txt", ""),
                 word_list], index=document_list.columns)
        else:
            t = pd.Series(
                [frame_list[0], frame_list[1], frame_list[2], frame_list[3].replace("企業レポート_", "").replace(".txt", ""),
                 word_list], index=document_list.columns)

        document_list = document_list.append(t, ignore_index=True)

    with open("/Users/main/PycharmProjects/aegies/data/document_list.pickle", "wb") as f:
        pickle.dump(document_list, f)
