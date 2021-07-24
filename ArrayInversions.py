def merge_and_count_inversions(a, b):
    c = []
    size = len(a) + len(b)
    index_a = 0
    index_b = 0
    count = 0
    while index_a < len(a) and index_b < len(b):
        if a[index_a] < b[index_b]:
            c.append(a[index_a])
            index_a += 1
        else:
            c.append(b[index_b])
            index_b += 1
            count += (len(a) - index_a)
    while index_a < len(a):
        c.append(a[index_a])
        index_a += 1
    while index_b < len(b):
        c.append(b[index_b])
        index_b += 1

    inversions.append(count)
    return c


def sort(a):
    if len(a) == 0:
        return 0
    if len(a) == 1:
        return a
    inversions = 0
    split = int(len(a) / 2)
    x = sort(a[:split])
    y = sort(a[split:])
    # print(f'x : {x} y : {y}')
    z = merge_and_count_inversions(x, y)

    return z


inversions = []

test = [45, 23, 21, 75, 1, 32, 56, 121, 545, 665, 7571, 2, 3, 1]
test.sort(reverse=True)
sort(test)
print(sum(inversions))
