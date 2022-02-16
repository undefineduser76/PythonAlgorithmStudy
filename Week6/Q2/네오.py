"""
부모를 타고 올라가면서 10% 씩 떼주는 것을 구현하는 문제입니다.
"""

from collections import defaultdict


def solution(enroll, referral, seller, amount):
    parent = {}
    total = defaultdict(lambda: 0)

    for enroller, referrer in zip(enroll, referral):
        parent[enroller] = referrer

    for who, amt in zip(seller, amount):
        sell(who, amt * 100, parent, total)

    answer = [total[name] for name in enroll]

    return answer


def sell(who, price, parent, total):
    while who != '-':
        to_give = int(price * 0.1)
        total[who] += price - to_give
        if to_give == 0:
            break
        who = parent[who]
        price = to_give
