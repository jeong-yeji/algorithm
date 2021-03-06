# https://programmers.co.kr/learn/courses/30/lessons/42862


def solution(n, lost, reserve):
    set_reserve = set(reserve) - set(lost)
    set_lost = set(lost) - set(reserve)

    for l in set_reserve:
        if l - 1 in set_lost:
            set_lost.remove(l - 1)
        elif l + 1 in set_lost:
            set_lost.remove(l + 1)

    return n - len(set_lost)