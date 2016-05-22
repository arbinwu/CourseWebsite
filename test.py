# !/usr/bin/env python
# -*- coding: UTF-8 -*-
from whoosh.index import create_in
from whoosh.fields import *
from whoosh.analysis import RegexAnalyzer
from whoosh.analysis import Tokenizer, Token
import jieba


class ChineseTokenizer(Tokenizer):
    def __call__(self, value, positions=False, chars=False,
                 keeporiginal=False, removestops=True,
                 start_pos=0, start_char=0, mode='', **kwargs):
        assert isinstance(value, text_type), "%r is not unicode" % value
        t = Token(positions, chars, removestops=removestops, mode=mode,
                  **kwargs)
        seglist = jieba.cut(value, cut_all=False)  # 使用结巴分词库进行分词
        for w in seglist:
            t.original = t.text = w
            t.boost = 1.0
            if positions:
                t.pos = start_pos + value.find(w)
            if chars:
                t.startchar = start_char + value.find(w)
                t.endchar = start_char + value.find(w) + len(w)
            yield t  # 通过生成器返回每个分词的结果token


def ChineseAnalyzer():
    return ChineseTokenizer()


analyzer = ChineseAnalyzer()
schema = Schema(title=TEXT(stored=True), path=ID(stored=True), content=TEXT(stored=True, analyzer=analyzer))
ix = create_in('D:\Graduation Project\CourseWebsite\indexdir', schema)
writer = ix.writer()
writer.add_document(title=u'First document', path=u'/a',
                    content=u'考试通知')
writer.add_document(title=u'Second document”, path=u”/b',
                    content=u'The second one 你 中文测试中文 is even more interesting!')
writer.commit()
searcher = ix.searcher()
results = searcher.find('content', u'考试通知')
print(len(results))

for hit in results:
    print(hit.highlights("content"))




# !/user/bin/env python
# -*- coding: utf-8 -*-
# """
# Created on 2015/7/7  10:08
# 使用动态规划算法实现编辑距离的计算
# @author: Wang Xu
# # """
# import numpy as np
#
#
# class LevenshteinDistance:
#     def leDistance(self, input_x, input_y):
#         xlen = len(input_x) + 1  # 此处需要多开辟一个元素存储最后一轮的计算结果
#         ylen = len(input_y) + 1
#
#         dp = np.zeros(shape=(xlen, ylen), dtype=int)
#         for i in range(0, xlen):
#             dp[i][0] = i
#         for j in range(0, ylen):
#             dp[0][j] = j
#
#         for i in range(1, xlen):
#             for j in range(1, ylen):
#                 if input_x[i - 1] == input_y[j - 1]:
#                     dp[i][j] = dp[i - 1][j - 1]
#                 else:
#                     dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])
#         return dp[xlen - 1][ylen - 1]
#
#
# if __name__ == '__main__':
#     ld = LevenshteinDistance()
#     print(ld.leDistance('瓦罐蹄膀饭', '瓦罐焖蹄饭'))  # Prints 2
#     print(ld.leDistance('abc', 'ad') / 5)  # Prints 1
#     print(ld.leDistance('b', ''))  # Prints 1
#     print(ld.leDistance('', ''))  # Prints 0
#     print(ld.leDistance('杭椒小炒肉面', '外婆小肉面'))  # Prints 3
#     print(ld.leDistance('外婆小肉面', '杭椒小炒肉面'))  # Prints 3
# import string
# s1 = 'abc  defg'
# s2 = ' '
# r = s1.replace(s2, '',)
# print(r)
