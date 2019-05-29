#!/usr/bin/python
#-*- coding:UTF-8 -*-
#-----------------------------------------------------------------------#
# File Name: main.py
# Author: Junyi Li
# Personal Page: DukeEnglish.github.io
# Mail: 4ljy@163.com
# Created Time: 2019-05-19
# Description: 
#-----------------------------------------------------------------------#

import sys
from hanziconv import HanziConv

# from goose import Goose
# from goose.text import StopWordsChinese


import sys
from utils.extractor import Extractor


def main(argv):
    # url = 'https://www.dbs.com/hongkong-zh/about-us/our-management/piyush-gupta/default.page'
    # g = Goose({'stopwords_class': StopWordsChinese})
    # article = g.extract(url=url)
    # data = HanziConv.toSimplified(u''.join(article.cleaned_text[:]))
    # data = data.replace('\n', ' ').replace('\r', '')
    data = '汤姆是林肯的哥哥'
    print(data)

    extractor = Extractor()
    extractor.load()
    extractor.chunk_str(data)
    extractor.resolve_all_conference()
    print("Triple: ")
    print('\n'.join(str(p) for p in extractor.triple_list))

    extractor.release()


if __name__ == "__main__":
    main(sys.argv)