#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def LISBottomUp(a):
    n = len(a)
    D = []
    for i in range(n):
        D.append(1)
        for j in range(1, i-1):
            if a[j] < a[i] and D[j] + 1 > D[i]:
                D[i] = D[j] + 1

    ans = 0
    for i in range(n):
        ans = max(ans, D[i])

    return ans


def LISBottomUp2(a):
    n = len(a)
    D = []
    prev = []
    for i in range(n):
        D.append(1)
        prev.append(-1)
        for j in range(1, i-1):
            if a[j] < a[i] and D[j] + 1 > D[i]:
                D[i] = D[j] + 1
                prev[i] = j

    ans = 0
    maxi = 0
    for i in range(n):
        if ans < D[i]:
            ans = D[i]
            maxi = i
    print("reconstructed sequence without prev: ")
    print(replyANS(D, ans, maxi))
    print("reconstructed sequence: ")
    print(replyANSwith(maxi, prev))

    return ans


def replyANSwith(maxi, prev):
    L = []
    while True:
        L.append(maxi)
        if prev[maxi] == -1:
            break
        maxi = prev[maxi]

    L.reverse()
    return L


def replyANS(d, ans, maxi):
    L = []
    while True:
        L.append(maxi)
        if ans == 1:
            break
        ans -= 1
        while True:
            maxi -= 1
            if d[maxi] == ans and a[maxi] < a[L[-1]]:
                break
    L.reverse()
    return L


if __name__ == '__main__':
    a = [7, 2, 1, 3, 8, 4, 9, 1, 2, 6, 5, 9, 3, 8, 1]
    print("Maximum sequence length is ", LISBottomUp(a))
    print("Maximum sequence length is ", LISBottomUp2(a))
