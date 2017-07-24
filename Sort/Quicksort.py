# ファイル読み込み
def read_file():
    opath = path + "target.txt"
    buff = []
    file = open(opath, "r", encoding="UTF-8")
    for line in file:
        buff += [int(line)]
    else:
        file.close()
    return buff


# クイックソート
def quick_sort(list, left, right):
    cursor_left = left
    cursor_right = right
    center = list[int((cursor_left + cursor_right) / 2)]

    while True:
        while list[cursor_left] < center: cursor_left += 1
        while list[cursor_right] > center: cursor_right -= 1
        if cursor_left <= cursor_right:
            list[cursor_left], list[cursor_right] = list[cursor_right], list[cursor_left]
            cursor_left += 1
            cursor_right -= 1
        if cursor_left > cursor_right:
            break

    if left < cursor_right: quick_sort(list, left, cursor_right)
    if cursor_left < right: quick_sort(list, cursor_left, right)


# 書き出し (追記まだ)
def write_file(list):
    wpath = path + "result.txt"
    file = open(wpath, 'w', encoding="UTF-8")
    for el in list:
        el = str(el) + "\n"
        file.write(el)
    else:
        file.close()


# ソート検査機
def isSorted(list):
    i = 0
    while list[i] <= list[i + 1]:
        i += 1
        if i == len(list) - 1:
            return print("ok! sorted")
            break
    else:
        return print("index [", i, "] and [", i + 1, "] are not sorted")


path = "/Users/Inhwa_rg1/IdeaProjects/PythonGround/Sort/"  # pathは適宜変えること
list = read_file()  # ソート前
print(list)
quick_sort(list, 0, len(list) - 1)  # ソート中
print(list)
print()
isSorted(list)
write_file(list)
