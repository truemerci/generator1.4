from itertools import permutations


def generator(num):
    for i in permutations(num):
        yield i


for j in generator([1, 2, 3]):
    print(j)
