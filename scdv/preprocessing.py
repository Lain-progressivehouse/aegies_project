import re
import MeCab


def document_to_wordlist(document):
    document = re.sub(r"\s[\s]+", " ", re.sub("[\n\t]", " ", document))
    document = document.replace(" 市場動向 ", "").replace(" 競合状況 ", "")
    document = re.sub(r"(20[0-9]{2}/[0-9]{1,2}/[0-9]{1,2}調査)", "", document)

    tokenizer = MeCab.Tagger("-Ochasen -d /usr/local/lib/mecab/dic/mecab-ipadic-neologd")
    tokenizer.parse("")
    node = tokenizer.parseToNode(document)
    keywords = []
    while node:
        if node.feature.split(",")[0] == u"名詞":
            keywords.append(node.surface)
        elif node.feature.split(",")[0] == u"形容詞":
            keywords.append(node.feature.split(",")[6])
        elif node.feature.split(",")[0] == u"動詞":
            keywords.append(node.feature.split(",")[6])
        node = node.next

    wordlist = []
    for word in keywords:
        wordlist.append(re.sub(
            r'[．◆©～－｜‘’0123456789０１２３４５６７８９・〔〕▼！＠＃＄％＾＆\-|\\＊\“（）＿■×※⇒—●(：〜＋=)／*&^%$#@!~`){}…\[\]\"\'\”:;<>?＜＞？､、。・･,./『』【】「」→←○]+',
            "", word))

    wordlist = filter(("").__ne__, wordlist)

    return list(wordlist)