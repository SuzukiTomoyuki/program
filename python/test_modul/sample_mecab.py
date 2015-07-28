# -*- coding: utf-8 -*-

import MeCab

def extractKeyword(text):

    tagger = MeCab.Tagger('-Ochasen')
    node = tagger.parseToNode(text.encode('utf-8'))
    keywords = []
    while node:
        if node.feature.split(",")[0] == r"名詞":
            keywords.append(node.surface)
        node = node.next
    return keywords

if __name__ == "__main__":
    keywords = extractKeyword(u"ケンシロウ「お前は既に死んでいる」アミバ「うわらば！！」")
    for w in keywords:
        print w,
    print
    keywords2 = extractKeyword(u"death victer enemy ships")
    for w in keywords2:
        print w,