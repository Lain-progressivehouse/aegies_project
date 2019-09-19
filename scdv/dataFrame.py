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


def make_dataFrame_paragraph(files):
    document_list = pd.DataFrame(columns=["category1", "category2", "category3", "company", "document"])
    data_path = "/Users/main/Desktop/企業レポート"

    # files = list(find_all_files(data_path))
    for file in tqdm(files):
        # with open(file, "r") as f:
        #     word_list = preprocessing.document_to_wordlist(f.read())

        r = open(file, "r")
        word_list = preprocessing.document_to_paragraph(r.read())
        r.close()

        frame_list = file.replace("/Users/main/Desktop/企業レポート/", "").split("/")

        for p_word_list in word_list:
            if len(frame_list) < 4:
                t = pd.Series(
                    [frame_list[0], "_", "_", frame_list[1].replace("企業レポート_", "").replace(".txt", ""),
                     p_word_list], index=document_list.columns)
            else:
                t = pd.Series(
                    [frame_list[0], frame_list[1], frame_list[2],
                     frame_list[3].replace("企業レポート_", "").replace(".txt", ""),
                     p_word_list], index=document_list.columns)
            # ガテゴリ1 カテゴリ2 カテゴリ3 ファイル名

            document_list = document_list.append(t, ignore_index=True)

    with open("/Users/main/PycharmProjects/aegies/data/paragraph/document_list_.pkl", "wb") as f:
        pickle.dump(document_list, f)


def make_dataFrame_add_date():
    document_list = pd.DataFrame(columns=["category1", "category2", "category3", "company", "document", "date"])

    data_path = "/Users/main/Desktop/企業レポート"

    files = find_all_files(data_path)
    for file in tqdm(list(files)):
        # with open(file, "r") as f:
        #     word_list = preprocessing.document_to_wordlist(f.read())

        r = open(file, "r")
        s = r.read()
        word_list = preprocessing.document_to_wordlist(s)
        r.close()

        date = re.search(r"20[0-9]{2}/[0-9]{1,2}/[0-9]{1,2}", s).group(0)

        # ガテゴリ1 カテゴリ2 カテゴリ3 ファイル名
        frame_list = file.replace("/Users/main/Desktop/企業レポート/", "").split("/")

        if len(frame_list) < 4:
            t = pd.Series(
                [frame_list[0], "_", "_", frame_list[1].replace("企業レポート_", "").replace(".txt", ""),
                 word_list, date], index=document_list.columns)
        else:
            t = pd.Series(
                [frame_list[0], frame_list[1], frame_list[2], frame_list[3].replace("企業レポート_", "").replace(".txt", ""),
                 word_list, date], index=document_list.columns)

        document_list = document_list.append(t, ignore_index=True)

    # with open("/Users/main/PycharmProjects/aegies/data/document_list.pickle", "wb") as f:
    #     pickle.dump(document_list, f)

    return document_list


def make_dataFrame_new_data():
    document_list = pd.DataFrame(columns=["stock_name", "date", "document"])

    data_path = "/Users/lain./textdata/"

    files = find_all_files(data_path)
    for file in tqdm(list(files)):
        with open(file, "r") as f:
            word_list = preprocessing.document_to_wordlist(f.read())

        s = os.path.basename(file).replace(".txt", "").split("-")

        t = pd.Series([s[3], "{}-{}-{}".format(s[0], s[1], s[2]), word_list], index=document_list.columns)

        document_list = document_list.append(t, ignore_index=True)

    return document_list
