#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def FibTD(n):
    if f[n] == -1:
        if n <= 1:
            f[n] = n
        else:
            f[n] = FibTD(n-1) + FibTD(n-2)
    return f[n]


def FibBU(n):
    f[0] = 0
    f[1] = 1
    for i in range(2, n+1):
        f[i] = f[i - 1] + f[i - 2]
    return f[n]


def FibBUImproved(n):
    if n <= 1:
        return n

    prev = 0
    curr = 1

    for _ in range(n-1):
        next = prev + curr
        prev = curr
        curr = next

    return curr


if __name__ == '__main__':
    n = int(input("Enter n... "))
    f = [-1] * (n+1)

    print(FibTD(n))
    print(FibBU(n))
    print(FibBUImproved(n))
