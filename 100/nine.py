'''
Typoglycemia

スペースで区切られた
単語列に対して，
各単語の先頭と末尾の文字は残し，
それ以外の文字の順序をランダムに並び替える

プログラムを作成せよ．

ただし，長さが４以下の単語は並び替えないこととする．

適当な英語の文
（例えば "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."）
を与え，その実行結果を確認せよ．
'''

import random


def rdm_sort(stc):
    split_list = stc.split(" ")
    str_list = []

    for i in split_list:

        if len(i) > 4:
            str_list.append(i[1:len(i) - 1])  # 先頭と末尾の文字を覗く

            for j in str_list:
                lst = []

                for r in j:
                    lst.append(r)

                random.shuffle(lst)


    return split_list


target_stc = "I couldn't believe that I could actually understand what I was reading" \
             " : the phenomenal power of the human mind ."

print(rdm_sort(target_stc))