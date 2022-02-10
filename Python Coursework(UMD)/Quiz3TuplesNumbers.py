# Julio Claros
# 114153234
# 2018-1-10


def number_list(l):
    lmin = min(l)
    lmax = max(l)
    lmean = sum(l) / len(l)
    lsort = sorted(l)
    mid_index = len(lsort) // 2
    lmedian = (l[mid_index] if len(lsort) % 2 == 1
               else (l[mid_index] + l[mid_index - 1]) / 2)

    print(6 // 2)
    print(l[mid_index])
    print(l[mid_index - 1])
    print(mid_index)
    a = lmin, lmax, lmean, lmedian
    print(a)


if __name__ == '__main__':
    get_numberlist([1, 2, 3, 4, 5, 6])



