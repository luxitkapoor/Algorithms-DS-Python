def merge(a, b):
    size_of_merge = len(a) + len(b)
    index_a = 0
    index_b = 0
    c = []
    # for index_c in range(0, size_of_merge):
    #     if index_a >= len(a) and index_b <= len(b):
    #         # print(f"b : {len(b)} index : {index_b} list : {b[index_b]} c :{index_c}")
    #         c.append(b[index_b])
    #         index_b += 1

    #     elif index_b >= len(b) and index_a <= len(a):
    #         c.append(a[index_a])
    #         index_a += 1

    #     elif a[index_a] < b[index_b]:
    #         c.append(a[index_a])
    #         index_a += 1
    #     else:
    #         # print(f"b : {len(b)} index : {index_b} list : {b[0]}")
    #         c.append(b[index_b])
    #         index_b += 1
    while index_a < len(a) and index_b < len(b):
        if a[index_a] < b[index_b]:
            c.append(a[index_a])
            index_a += 1
        else:
            c.append(b[index_b])
            index_b += 1

    while index_a < len(a):
        c.append(a[index_a])
        index_a += 1
    while index_b < len(b):
        c.append(b[index_b])
        index_b += 1

    return c


def sort(a):
    if len(a) == 0:
        return "No elements in array"
    if len(a) == 1:
        return a
    split = int(len(a) / 2)
    x = a[:split]
    y = a[split:]

    sort_x = sort(x)
    sort_y = sort(y)
    # print(f'x : {sort_x} y: {sort_y}')
    z = merge(sort_x, sort_y)
    return z


test = [45, 23, 21, 75, 1, 32, 56, 121, 545, 665, 7571, 2, 3, 1]
test2 = [34, 21, 43, 1]
test3 = []
test4 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
test4.sort(reverse=True)
test5 = [1, 3, 5, 2, 4, 6]
print(test4)
print(sort(test5))
