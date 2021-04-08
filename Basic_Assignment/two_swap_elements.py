def change_pos(my_lst):
    even = []
    odd = []
    size = len(my_lst)
    for i in range(0, size):
        if i % 2 == 0:
            even.append(my_lst[i])
        else:
            odd.append(my_lst[i])

    new_lst = []
    i = 0
    j = 0

    if size % 2 == 0:
        for k in range(0, size):
            if k % 2 == 0:
                new_lst.append(odd[i])
                i = i + 1
            else:
                new_lst.append(even[j])
                j = j + 1
    else:
        for k in range(0, size):
            if k == size - 1:
                new_lst.append(even[len(even) - 1])
            else:
                if k % 2 == 0:
                    new_lst.append(odd[i])
                    i = i + 1
                else:
                    new_lst.append(even[j])
                    j = j + 1

    return new_lst


def test_change_pos():
    assert change_pos([0, 1, 2, 3, 4, 5]) == [1, 0, 3, 2, 5, 4]


print(change_pos([10, 2, 7, 9, 11, 24]))
print(change_pos([0, 1, 2, 3, 4, 5]))
print(change_pos([1, 2, 3, 4, 5]))
