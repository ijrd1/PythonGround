'''
テンプレートによる性成分

引数x, y, zを受け取り「x時のyはz」という文字列を返す関数を実装せよ
さらに，x=12, y="気温", z=22.4として，実行結果を確認せよ．
'''


# 方法1
def template(x, y, z):
    x = str(x)
    y = str(y)
    z = str(z)
    return x + "時の" + y + "は" + z


print(template(12, "気温", 22.4))


# Thinking Time
def make_str(i):
    return str(i)


# 方法2
def __template__(x, y, z):
    rst = list(map(lambda i: str(i), [x, y, z]))
    return "{0}時の{1}は{2}".format(rst[0], rst[1], rst[2])  # return rst[0] + "時の" + rst[1] + "は" + rst[2]


print(__template__(12, "気温", 22.4))
