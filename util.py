import random


def arg_max_random(Q):
    l = list(zip(Q, range(len(Q))))
    l.sort(reverse=True, key=lambda x: x[0][0])
    max_list = [e[1] for e in l if e[0][0] == l[0][0][0]]
    return random.choice(max_list)
